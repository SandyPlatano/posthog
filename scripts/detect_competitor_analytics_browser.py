#!/usr/bin/env python3
"""
Analytics Competitor Detection Script (Browser Version)

Uses Playwright to render pages in a real browser, bypassing bot protection.
Reads a CSV with company names/URLs and detects which PostHog competitor
analytics tools they're using by inspecting their HTML.

Installation:
    pip install playwright
    playwright install chromium

Usage:
    python detect_competitor_analytics_browser.py input.csv output.csv
"""

import csv
import sys
import re
import time
import asyncio
from typing import List, Dict, Set, Optional
from urllib.parse import urlparse
from playwright.async_api import async_playwright, Browser, Page, TimeoutError as PlaywrightTimeout

# Timeout for page loads (milliseconds)
PAGE_TIMEOUT = 15000

# PostHog competitors and their detection patterns
COMPETITORS = {
    'Mixpanel': [
        r'mixpanel\.com/libs/mixpanel',
        r'cdn\.mxpnl\.com',
        r'mixpanel\.init',
    ],
    'Amplitude': [
        r'cdn\.amplitude\.com',
        r'amplitude\.getInstance',
        r'amplitude\.init',
    ],
    'Heap': [
        r'heap-analytics\.com',
        r'heapanalytics\.com',
        r'heap\.load',
    ],
    'Hotjar': [
        r'static\.hotjar\.com',
        r'hotjar\.com/c/hotjar',
        r'_hjSettings',
    ],
    'FullStory': [
        r'fullstory\.com/s/fs\.js',
        r'fullstory\.com/rec',
        r'window\[\'_fs_',
    ],
    'LogRocket': [
        r'cdn\.logrocket\.com',
        r'cdn\.lr-ingest\.com',
        r'LogRocket\.init',
    ],
    'Segment': [
        r'cdn\.segment\.com',
        r'analytics\.load',
        r'analytics\.js',
    ],
    'Google Analytics': [
        r'google-analytics\.com/analytics\.js',
        r'googletagmanager\.com/gtag/js',
        r'gtag\(',
        r'ga\(',
        r'UA-\d+-\d+',
        r'G-[A-Z0-9]+',
    ],
    'Pendo': [
        r'cdn\.pendo\.io',
        r'pendo\.initialize',
    ],
    'Intercom': [
        r'widget\.intercom\.io',
        r'Intercom\(',
    ],
    'PostHog': [
        r'app\.posthog\.com',
        r'posthog\.init',
        r'posthog\.js',
    ],
    'Clarity': [
        r'clarity\.ms',
        r'clarity\(',
    ],
    'Matomo': [
        r'matomo\.js',
        r'piwik\.js',
        r'_paq\.push',
    ],
    'Plausible': [
        r'plausible\.io/js/plausible',
    ],
}


def normalize_url(company_input: str) -> str:
    """Convert company name or URL to a full URL."""
    company_input = company_input.strip()

    # If it already looks like a URL
    if company_input.startswith(('http://', 'https://')):
        return company_input

    # If it has a domain extension but no protocol
    if '.' in company_input and not ' ' in company_input:
        return f'https://{company_input}'

    # Otherwise assume it's a company name, make it .com
    company_name = company_input.lower().replace(' ', '')
    return f'https://{company_name}.com'


def detect_analytics_tools(html: str) -> Set[str]:
    """Detect which analytics tools are present in the HTML."""
    detected = set()

    for tool_name, patterns in COMPETITORS.items():
        for pattern in patterns:
            if re.search(pattern, html, re.IGNORECASE):
                detected.add(tool_name)
                break  # Found this tool, move to next

    return detected


async def fetch_page_content(page: Page, url: str) -> str:
    """Fetch page content using Playwright."""
    try:
        # Navigate to the page
        response = await page.goto(url, wait_until='networkidle', timeout=PAGE_TIMEOUT)

        if not response:
            raise Exception("NO_RESPONSE")

        if response.status >= 400:
            raise Exception(f"HTTP_{response.status}")

        # Wait a bit for any lazy-loaded scripts
        await page.wait_for_timeout(2000)

        # Get the full page content
        html = await page.content()

        return html

    except PlaywrightTimeout:
        raise Exception("TIMEOUT")
    except Exception as e:
        error_str = str(e)
        if "net::ERR_NAME_NOT_RESOLVED" in error_str:
            raise Exception("DNS_ERROR")
        elif "net::ERR_CONNECTION_REFUSED" in error_str:
            raise Exception("CONNECTION_REFUSED")
        elif error_str.startswith("HTTP_"):
            raise
        else:
            raise Exception("ERROR")


async def process_companies(input_csv: str, output_csv: str):
    """Process the input CSV and write results to output CSV."""
    results = []

    # Read input CSV
    try:
        with open(input_csv, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            companies = list(reader)

            # Check for required column
            if not companies:
                print("Error: Input CSV is empty")
                return

            # Accept either 'company' or 'url' or 'name' as column header
            column_name = None
            for possible_name in ['company', 'url', 'name', 'Company', 'URL', 'Name']:
                if possible_name in companies[0]:
                    column_name = possible_name
                    break

            if not column_name:
                print(f"Error: CSV must have a 'company', 'url', or 'name' column. Found: {list(companies[0].keys())}")
                return
    except FileNotFoundError:
        print(f"Error: Input file '{input_csv}' not found")
        return
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return

    # Process each company with Playwright
    total = len(companies)
    print(f"Processing {total} companies...\n")
    print("Starting browser (this may take a moment)...\n")

    async with async_playwright() as p:
        # Launch browser in headless mode
        browser = await p.chromium.launch(headless=True)

        # Create a context with realistic browser settings
        context = await browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            ignore_https_errors=True  # Ignore SSL certificate errors
        )

        page = await context.new_page()

        for idx, row in enumerate(companies, 1):
            company_input = row[column_name]
            url = normalize_url(company_input)

            print(f"[{idx}/{total}] Checking {company_input} ({url})...")

            try:
                html = await fetch_page_content(page, url)
                detected = detect_analytics_tools(html)

                # Remove PostHog from competitors list for cleaner output
                detected.discard('PostHog')

                if detected:
                    tools_str = ', '.join(sorted(detected))
                    print(f"  ✓ Found: {tools_str}")
                else:
                    tools_str = 'None detected'
                    print(f"  - No known analytics tools detected")

                results.append({
                    'company': company_input,
                    'url': url,
                    'analytics_tools': tools_str
                })

            except Exception as e:
                error_msg = str(e)
                import traceback
                # Print full error for debugging (uncomment for troubleshooting)
                # traceback.print_exc()

                # Simplify error messages for CSV
                if error_msg == "TIMEOUT":
                    csv_error = "TIMEOUT"
                    print(f"  ✗ Timeout (page took too long to load)")
                elif error_msg == "DNS_ERROR":
                    csv_error = "DNS_ERROR"
                    print(f"  ✗ DNS error (domain not found)")
                elif error_msg == "CONNECTION_REFUSED":
                    csv_error = "CONNECTION_REFUSED"
                    print(f"  ✗ Connection refused")
                elif error_msg.startswith("HTTP_"):
                    csv_error = error_msg
                    status_code = error_msg.replace("HTTP_", "")
                    print(f"  ✗ HTTP {status_code} error")
                else:
                    csv_error = "ERROR"
                    print(f"  ✗ Error")

                results.append({
                    'company': company_input,
                    'url': url,
                    'analytics_tools': csv_error
                })

            # Small delay between requests to be respectful
            await asyncio.sleep(0.5)

        await browser.close()

    # Write results to CSV
    try:
        with open(output_csv, 'w', newline='', encoding='utf-8') as f:
            fieldnames = ['company', 'url', 'analytics_tools']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)

        print(f"\n✓ Results written to {output_csv}")

        # Summary statistics
        tools_count = {}
        error_count = {'BLOCKED': 0, 'TIMEOUT': 0, 'DNS_ERROR': 0, 'CONNECTION_REFUSED': 0, 'OTHER': 0}
        success_count = 0

        for result in results:
            tools = result['analytics_tools']

            # Track errors
            if tools in ['BLOCKED', 'TIMEOUT', 'DNS_ERROR', 'CONNECTION_REFUSED']:
                error_count[tools] += 1
            elif tools.startswith('HTTP_') or tools == 'ERROR':
                error_count['OTHER'] += 1
            elif tools != 'None detected':
                # Count detected tools
                success_count += 1
                for tool in tools.split(', '):
                    tools_count[tool] = tools_count.get(tool, 0) + 1

        print("\n" + "="*50)
        print("SUMMARY")
        print("="*50)

        if tools_count:
            print("\nDetected Analytics Tools:")
            for tool, count in sorted(tools_count.items(), key=lambda x: x[1], reverse=True):
                print(f"  {tool}: {count} companies")

        # Show error summary
        total_errors = sum(error_count.values())
        if total_errors > 0:
            print(f"\nErrors:")
            if error_count['TIMEOUT'] > 0:
                print(f"  Timeouts: {error_count['TIMEOUT']} sites")
            if error_count['DNS_ERROR'] > 0:
                print(f"  DNS errors: {error_count['DNS_ERROR']} sites")
            if error_count['CONNECTION_REFUSED'] > 0:
                print(f"  Connection refused: {error_count['CONNECTION_REFUSED']} sites")
            if error_count['OTHER'] > 0:
                print(f"  Other errors: {error_count['OTHER']} sites")

        print(f"\nTotal: {success_count} successful, {total_errors} errors out of {len(results)} sites")

    except Exception as e:
        print(f"Error writing output CSV: {e}")


def main():
    if len(sys.argv) != 3:
        print("Analytics Competitor Detection Script (Browser Version)")
        print("=" * 60)
        print("\nUsage: python detect_competitor_analytics_browser.py input.csv output.csv")
        print("\nRequirements:")
        print("  pip install playwright")
        print("  playwright install chromium")
        print("\nInput CSV should have a 'company', 'url', or 'name' column with company names or URLs")
        print("Output CSV will contain: company, url, analytics_tools")
        sys.exit(1)

    input_csv = sys.argv[1]
    output_csv = sys.argv[2]

    # Run the async function
    asyncio.run(process_companies(input_csv, output_csv))


if __name__ == '__main__':
    main()
