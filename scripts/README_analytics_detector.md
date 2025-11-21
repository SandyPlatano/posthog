# Analytics Competitor Detection Tool

This Python script analyzes company websites to detect which analytics tools they're using, specifically focusing on PostHog competitors.

## What It Does

The script:
1. Takes a CSV with company names or URLs as input
2. Fetches each company's homepage HTML
3. Scans for analytics tracking scripts (Mixpanel, Amplitude, Heap, etc.)
4. Outputs a CSV with the detected tools

## Detected Tools

- **Mixpanel** - Product analytics
- **Amplitude** - Product analytics
- **Heap** - Digital insights
- **Hotjar** - Heatmaps & session recording
- **FullStory** - Session replay
- **LogRocket** - Session replay & monitoring
- **Segment** - Customer data platform
- **Google Analytics** - Web analytics
- **Pendo** - Product experience
- **Intercom** - Customer messaging
- **Clarity** - Microsoft's behavior analytics
- **Matomo** - Open-source analytics
- **Plausible** - Privacy-friendly analytics
- **PostHog** - Also detected (for reference)

## Installation

### Requirements

```bash
pip install requests
```

That's it! The script only needs the `requests` library.

## Usage

### Basic Usage

```bash
python detect_competitor_analytics.py input.csv output.csv
```

### Input CSV Format

Your input CSV should have a column named `company`, `url`, or `name`:

**Option 1: Company names**
```csv
company
Stripe
Airbnb
Shopify
```

**Option 2: Full URLs**
```csv
url
https://stripe.com
https://www.airbnb.com
https://shopify.com
```

**Option 3: Domain names**
```csv
company
stripe.com
airbnb.com
shopify.com
```

The script will automatically:
- Add `https://` if missing
- Add `.com` if it's just a company name
- Handle redirects

### Output CSV Format

The output CSV contains:
- `company` - Original input
- `url` - Normalized URL that was checked
- `analytics_tools` - Comma-separated list of detected tools (or ERROR if failed)

**Example output:**
```csv
company,url,analytics_tools
Stripe,https://stripe.com,"Segment, Google Analytics"
Airbnb,https://airbnb.com,"Mixpanel, Google Analytics"
Shopify,https://shopify.com,"Google Analytics, Hotjar"
```

## Examples

### Example 1: Check Tech Companies

**input.csv:**
```csv
company
GitHub
Linear
Notion
```

**Run:**
```bash
python detect_competitor_analytics.py input.csv results.csv
```

**Output:**
```
Processing 3 companies...

[1/3] Checking GitHub (https://github.com)...
  - No known analytics tools detected
[2/3] Checking Linear (https://linear.app)...
  ✓ Found: Amplitude, Google Analytics
[3/3] Checking Notion (https://notion.so)...
  ✓ Found: Segment

✓ Results written to results.csv

Summary:
  Amplitude: 1 company
  Google Analytics: 1 company
  Segment: 1 company
```

### Example 2: Check E-commerce Sites

You can also provide full URLs:

```csv
url
https://www.shopify.com
https://www.bigcommerce.com
https://www.wix.com
```

## Limitations & Troubleshooting

### Bot Protection (403 Errors)

Many large websites use bot protection (Cloudflare, etc.) that blocks automated requests:

```
ERROR: Failed to fetch https://example.com: 403 Client Error: Forbidden
```

**Workarounds:**
1. **Try smaller/tech-forward companies** - They're less likely to have aggressive bot protection
2. **Manual checking** - For blocked sites, you can:
   - Open the website in your browser
   - View page source (Ctrl+U / Cmd+U)
   - Search for analytics script patterns (mixpanel, amplitude, etc.)
3. **Use browser automation** - For advanced users, consider Selenium or Playwright (not included in this script)

### Timeout Errors

If a site is slow or unresponsive:
```
ERROR: Failed to fetch https://example.com: Read timed out
```

The script uses a 10-second timeout by default. You can modify `REQUEST_TIMEOUT` in the script if needed.

### False Negatives

The script might miss analytics tools if:
- They're loaded asynchronously after page load
- They use custom domains
- They're loaded through tag managers in complex ways
- The site uses server-side analytics

### False Positives

Rare, but possible if:
- A site mentions a tool in their docs/blog but doesn't actually use it
- Code comments reference analytics tools

## Advanced Usage

### Customize Detection Patterns

Edit the `COMPETITORS` dictionary in the script to add new tools or patterns:

```python
COMPETITORS = {
    'MyAnalyticsTool': [
        r'myanalytics\.com/script\.js',
        r'myAnalyticsObject\.init',
    ],
    # ... existing tools
}
```

### Change Timeout

Modify the timeout (in seconds):

```python
REQUEST_TIMEOUT = 20  # Increase for slow sites
```

### Add Rate Limiting

The script includes a 0.5-second delay between requests. Increase if needed:

```python
time.sleep(1.0)  # Wait 1 second between requests
```

## Tips for Best Results

1. **Start with tech companies** - They usually have fewer bot protections
2. **Use exact domains** - If you know the domain, provide it directly
3. **Batch processing** - Process 10-20 companies at a time
4. **Check during off-peak hours** - Less likely to be rate-limited
5. **Verify important results manually** - Spot-check a few results

## Real-World Use Cases

### Market Research
```bash
# Check what analytics tools your competitors' customers use
python detect_competitor_analytics.py target_customers.csv results.csv
```

### Sales Intelligence
```bash
# Identify companies using competitor tools for sales outreach
python detect_competitor_analytics.py leads.csv analytics_stack.csv
```

### Competitive Analysis
```bash
# See what tools similar companies in your space use
python detect_competitor_analytics.py similar_companies.csv tech_stack.csv
```

## Privacy & Ethics

**Important:** This tool only accesses publicly available information (website HTML). However:

- ✅ Use for legitimate business research
- ✅ Use for competitive analysis
- ✅ Use to understand market trends
- ❌ Don't use for malicious purposes
- ❌ Respect robots.txt and rate limits
- ❌ Don't overwhelm small sites with requests

## Troubleshooting

### Script won't run
```bash
# Make sure Python 3 is installed
python3 --version

# Install dependencies
pip3 install requests
```

### Permission denied
```bash
# Make script executable
chmod +x detect_competitor_analytics.py
```

### Import errors
```bash
# Install in correct Python environment
python3 -m pip install requests
```

## Contributing

Found a bug or want to add a new analytics tool pattern? Contributions welcome!

## License

This script is provided as-is for business intelligence and research purposes.
