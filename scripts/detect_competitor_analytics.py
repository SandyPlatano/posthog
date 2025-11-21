#!/usr/bin/env python3
"""
Analytics Competitor Detection Script

Reads a CSV with company names/URLs and detects which PostHog competitor
analytics tools they're using by inspecting their HTML.

Usage:
    python detect_competitor_analytics.py input.csv output.csv
"""

import csv
import sys
import re
import time
import random
from typing import List, Dict, Set, Optional
from urllib.parse import urlparse
import requests
from requests.exceptions import RequestException, Timeout

# Timeout for HTTP requests (seconds)
REQUEST_TIMEOUT = 15
MAX_RETRIES = 3

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

# Rotate through different user agents to avoid detection
USER_AGENTS = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
]


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


def get_alternative_urls(url: str) -> List[str]:
    """Generate alternative URLs to try (with and without www)."""
    urls = [url]

    # Try with/without www
    if '://www.' in url:
        urls.append(url.replace('://www.', '://'))
    elif '://' in url:
        urls.append(url.replace('://', '://www.'))

    return urls


def fetch_html(url: str) -> str:
    """Fetch HTML content from a URL with retry logic."""
    session = requests.Session()

    # Try alternative URLs (with/without www)
    urls_to_try = get_alternative_urls(url)

    for attempt_url in urls_to_try:
        for retry in range(MAX_RETRIES):
            try:
                # Rotate user agent
                user_agent = random.choice(USER_AGENTS)

                headers = {
                    'User-Agent': user_agent,
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Connection': 'keep-alive',
                    'Upgrade-Insecure-Requests': '1',
                    'Cache-Control': 'no-cache',
                }

                response = session.get(
                    attempt_url,
                    headers=headers,
                    timeout=REQUEST_TIMEOUT,
                    allow_redirects=True,
                    verify=True
                )
                response.raise_for_status()
                return response.text

            except requests.exceptions.HTTPError as e:
                # If 403/401, don't retry - likely bot protection
                if response.status_code in [403, 401]:
                    if attempt_url == urls_to_try[-1]:  # Last URL to try
                        raise Exception("BLOCKED")
                    else:
                        break  # Try next URL variant
                # For other HTTP errors, retry
                if retry == MAX_RETRIES - 1:
                    raise Exception(f"HTTP {response.status_code}")
                time.sleep(1 * (retry + 1))  # Exponential backoff

            except requests.exceptions.Timeout:
                if retry == MAX_RETRIES - 1:
                    raise Exception("TIMEOUT")
                time.sleep(1 * (retry + 1))

            except RequestException as e:
                if retry == MAX_RETRIES - 1:
                    raise Exception(f"CONNECTION_ERROR")
                time.sleep(1 * (retry + 1))

    raise Exception("BLOCKED")


def detect_analytics_tools(html: str) -> Set[str]:
    """Detect which analytics tools are present in the HTML."""
    detected = set()

    for tool_name, patterns in COMPETITORS.items():
        for pattern in patterns:
            if re.search(pattern, html, re.IGNORECASE):
                detected.add(tool_name)
                break  # Found this tool, move to next

    return detected


def process_companies(input_csv: str, output_csv: str):
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

    # Process each company
    total = len(companies)
    print(f"Processing {total} companies...\n")

    for idx, row in enumerate(companies, 1):
        company_input = row[column_name]
        url = normalize_url(company_input)

        print(f"[{idx}/{total}] Checking {company_input} ({url})...")

        try:
            html = fetch_html(url)
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

            # Simplify error messages for CSV
            if error_msg == "BLOCKED":
                csv_error = "BLOCKED"
                print(f"  ✗ Blocked (403 - bot protection)")
            elif error_msg == "TIMEOUT":
                csv_error = "TIMEOUT"
                print(f"  ✗ Timeout")
            elif error_msg == "CONNECTION_ERROR":
                csv_error = "CONNECTION_ERROR"
                print(f"  ✗ Connection error")
            elif error_msg.startswith("HTTP"):
                csv_error = error_msg
                print(f"  ✗ {error_msg}")
            else:
                csv_error = "ERROR"
                print(f"  ✗ Error: {error_msg}")

            results.append({
                'company': company_input,
                'url': url,
                'analytics_tools': csv_error
            })

        # Be nice to servers - random delay
        time.sleep(random.uniform(0.5, 1.5))

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
        error_count = {'BLOCKED': 0, 'TIMEOUT': 0, 'CONNECTION_ERROR': 0, 'OTHER': 0}
        success_count = 0

        for result in results:
            tools = result['analytics_tools']

            # Track errors
            if tools in ['BLOCKED', 'TIMEOUT', 'CONNECTION_ERROR']:
                error_count[tools] += 1
            elif tools.startswith('HTTP') or tools == 'ERROR':
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
            if error_count['BLOCKED'] > 0:
                print(f"  Bot protection (403): {error_count['BLOCKED']} sites")
            if error_count['TIMEOUT'] > 0:
                print(f"  Timeouts: {error_count['TIMEOUT']} sites")
            if error_count['CONNECTION_ERROR'] > 0:
                print(f"  Connection errors: {error_count['CONNECTION_ERROR']} sites")
            if error_count['OTHER'] > 0:
                print(f"  Other errors: {error_count['OTHER']} sites")

        print(f"\nTotal: {success_count} successful, {total_errors} errors out of {len(results)} sites")

    except Exception as e:
        print(f"Error writing output CSV: {e}")


def main():
    if len(sys.argv) != 3:
        print("Usage: python detect_competitor_analytics.py input.csv output.csv")
        print("\nInput CSV should have a 'company', 'url', or 'name' column with company names or URLs")
        print("Output CSV will contain: company, url, analytics_tools")
        sys.exit(1)

    input_csv = sys.argv[1]
    output_csv = sys.argv[2]

    process_companies(input_csv, output_csv)


if __name__ == '__main__':
    main()
