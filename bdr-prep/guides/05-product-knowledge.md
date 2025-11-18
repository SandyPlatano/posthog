# PostHog Product Knowledge Guide

This guide covers everything you need to know about PostHog's products to have confident technical conversations with engineers and product teams.

## What is PostHog?

PostHog is the **single platform for engineers to analyze, test, observe, and deploy new features**.

Key positioning:
- Built for **product engineers** (full-stack, frontend-skewed)
- All-in-one platform (replaces multiple tools)
- Open source (open-core model)
- Self-serve everything, including Enterprise

---

## The Product Suite

PostHog offers 8 integrated products:

| Product | Purpose | Free Tier |
|---------|---------|-----------|
| Product Analytics | Understand user behavior | 1M events/month |
| Session Replay | Watch real sessions | 5K recordings/month |
| Feature Flags | Safe feature rollouts | 1M requests/month |
| Experiments | A/B testing | 1M requests/month |
| Surveys | In-app feedback | 250 responses/month |
| CDP | Customer data platform | 1M events/month |
| Data Warehouse | SQL access to data | 1M rows synced/month |
| Error Tracking | Exception monitoring | 100K exceptions/month |

### Why All-in-One Matters

Traditional stack might include:
- Amplitude (analytics)
- LaunchDarkly (feature flags)
- Hotjar (session replay + surveys)

PostHog replaces all of these with one integrated platform where:
- All products share the same data
- Jump from a chart to a session replay
- See how feature flags affect metrics
- No data integration complexity

---

## Product Analytics

### What It Does

Analyzes user behavior to answer questions like:
- How many users signed up this week?
- What's our conversion rate?
- Where do users drop off?
- Which features are used most?

### Key Features

**Trends**
- Track metrics over time
- Compare periods
- Break down by properties

**Funnels**
- Visualize conversion paths
- See where users drop off
- Identify improvement opportunities

**Retention**
- Track user return rates
- Understand stickiness
- Measure product-market fit signals

**Paths**
- See user journeys
- Find unexpected flows
- Identify navigation issues

**Lifecycle**
- Track new, returning, resurrecting, dormant users
- Understand growth dynamics

### Autocapture

Unlike competitors (Amplitude, Mixpanel), PostHog has **autocapture**:
- Starts collecting data immediately
- No engineering required for basic tracking
- Captures pageviews, clicks, form submissions
- Works on `<a>`, `<button>`, `<input>`, `<form>`, etc.

This is a major differentiator for quick time-to-value.

### Custom Events

Beyond autocapture, teams capture business-specific events:
```javascript
posthog.capture('purchase_completed', {
    product_id: '12345',
    price: 99.99,
    currency: 'USD'
})
```

---

## Session Replay

### What It Does

Records real user sessions to replay later, showing exactly what users experienced.

### What It Captures

- DOM changes
- Mouse movements
- Clicks and scrolls
- Console logs
- Network requests
- Performance data

### Use Cases

1. **Debug issues** - See exactly what went wrong
2. **Understand behavior** - Watch how users navigate
3. **Validate assumptions** - See if users behave as expected
4. **Support customers** - Understand their specific issues

### Privacy Controls

- Mask all inputs by default (recommended)
- Mask specific elements with CSS class
- Respect Do Not Track
- Configurable data retention

### Platform Support

- Web: Full support
- Android: Beta
- iOS: Alpha

### Pricing

5,000 recordings/month free, then usage-based.

---

## Feature Flags

### What It Does

Safely roll out features to specific users or percentages.

### Key Capabilities

**Percentage Rollouts**
- Start at 5%, scale to 100%
- Catch issues early
- Easy rollback

**User Targeting**
- By user properties
- By device/browser
- By cohort membership

**Multivariate Flags**
- Multiple variants
- Different payloads per variant

**Payloads**
- Attach JSON configuration
- Change behavior without deploy

### Code Example

```javascript
if (posthog.isFeatureEnabled('new_checkout')) {
    showNewCheckout()
} else {
    showOldCheckout()
}

// With payload
const config = posthog.getFeatureFlagPayload('new_checkout')
```

### Use Cases

1. **Safe releases** - Roll out gradually
2. **Kill switches** - Turn off broken features instantly
3. **Beta programs** - Give early access to specific users
4. **Entitlements** - Control feature access by plan

---

## Experiments (A/B Testing)

### What It Does

Test hypotheses with statistical rigor to make data-driven decisions.

### How It Works

1. Create experiment with hypothesis
2. Define control and test variants
3. Set goal metric (conversion, retention, etc.)
4. Let it run to statistical significance
5. Make decision based on results

### Features

- **Statistical engine** - Bayesian or frequentist
- **Goal metrics** - Conversion, retention, custom
- **Targeting** - Who enters the experiment
- **Session replay integration** - Watch sessions by variant

### Connection to Feature Flags

Experiments are built on feature flags:
- Creating an experiment creates a flag
- Flag controls which variant users see
- Experiment tracks metrics per variant

### Example Questions

- Do users convert more with blue or green button?
- Does a simplified onboarding improve retention?
- Which pricing page layout drives more upgrades?

---

## Surveys

### What It Does

Collect user feedback directly in your product.

### Survey Types

- **Open-ended** - Text responses
- **Multiple choice** - Select options
- **Rating scales** - NPS, satisfaction
- **Yes/No** - Binary choices

### Targeting

- Show to specific users/cohorts
- Trigger on specific pages/events
- Control frequency

### Use Cases

1. **NPS surveys** - Measure satisfaction
2. **Feature feedback** - After using new features
3. **Churn surveys** - Why users leave
4. **Research** - Understand user needs

---

## CDP (Customer Data Platform)

### What It Does

Collect, transform, and sync customer data.

### Capabilities

- **Sources** - Import from external tools
- **Destinations** - Export to external tools
- **Transformations** - Clean and enrich data

### Use Cases

1. Sync PostHog data to data warehouse
2. Import data from other sources
3. Create unified customer profiles

---

## Data Warehouse

### What It Does

Query all your data with SQL.

### Features

- SQL interface
- Bring your own data
- Join with PostHog data
- Build custom reports

### Use Cases

1. Complex analysis beyond UI capabilities
2. Join with external data (CRM, billing, etc.)
3. Power BI tools and dashboards

---

## Error Tracking

### What It Does

Capture and monitor application errors.

### Features

- Automatic error capture
- Stack traces
- User context
- Connected to session replay

### Use Cases

1. Monitor production errors
2. Prioritize fixes by impact
3. Debug with full context

---

## Key Differentiators

### 1. Native Integration

All products share the same data foundation:
- Jump from a trend to a session replay
- See feature flag impact on metrics
- Connect errors to user sessions

> "Every product we build is natively integrated. This means you can jump from a graph to a session recording to visually see why something happened."

### 2. Autocapture

Unlike Amplitude/Mixpanel:
- Starts collecting immediately
- No engineering required
- Retroactive analysis possible

> "PostHog supports event autocapture, which means it starts capturing data from the moment you deploy PostHog's code."

### 3. Open Source

Full transparency and trust:
- Code is available
- Can self-host
- Community contributions
- No vendor lock-in

> "One of PostHog's most significant differentiators is its open-source (open-core) model."

### 4. Engineer-First

Built for product engineers, not marketers:
- Technical depth
- API-first
- No dumbed-down features
- Respects technical users

### 5. Transparent Pricing

No "talk to sales" wall:
- All pricing public
- Self-serve for everything
- Enterprise is self-serve too

### 6. Privacy by Design

- Self-hosting option
- EU hosting (GDPR)
- Cookieless tracking possible
- Granular privacy controls

---

## Pricing Model

### Philosophy

PostHog believes in transparent, usage-based pricing with generous free tiers.

### Free Tier

| Product | Free Allowance |
|---------|----------------|
| Product Analytics | 1M events/month |
| Session Replay | 5K recordings/month |
| Feature Flags | 1M requests/month |
| Surveys | 250 responses/month |
| Data Warehouse | 1M rows synced/month |
| Error Tracking | 100K exceptions/month |

This resets monthly—not a trial.

### Usage-Based Pricing

After free tier, pay for what you use:
- No long-term commitments required
- Pay as you grow
- Volume discounts at scale

### Enterprise Add-on

$2,000/month includes:
- RBAC (role-based access control)
- Dedicated support
- Training
- Advanced security
- Extended retention (60 months for replay)

### Discounts

| Annual Commit | Discount |
|---------------|----------|
| >$20k prepaid | 20% |
| >$60k | Additional 5% |
| >$100k | Additional 15% |
| Multi-year | 5% per additional year |

---

## Common Use Cases by Company Stage

### Early Stage / Pre-PMF

Focus on:
- Product Analytics (understand users)
- Session Replay (see user struggles)
- Surveys (collect feedback)

Questions to answer:
- Are users getting value?
- Where do they struggle?
- What do they actually want?

### Growth Stage / Post-PMF

Focus on:
- Feature Flags (ship safely)
- Experiments (optimize)
- Full analytics depth

Questions to answer:
- What drives conversion?
- Which features matter?
- How to optimize funnels?

### Scale / Enterprise

Focus on:
- All products integrated
- Data Warehouse (custom analysis)
- Enterprise features (RBAC, etc.)

Questions to answer:
- How to maintain velocity safely?
- How to democratize data access?
- How to comply with regulations?

---

## Demo Scenarios

### Scenario 1: "We need to understand our users"

Show:
1. Sign up and implement (quick)
2. Autocapture in action
3. Create first insight (trend)
4. Build a funnel
5. Jump to session replay

### Scenario 2: "We're afraid to ship features"

Show:
1. Create a feature flag
2. Roll out to 10%
3. Monitor impact on metrics
4. Show how to roll back

### Scenario 3: "We want to run experiments"

Show:
1. Create experiment
2. Define variants
3. Set goal metric
4. Show results (use sample data)
5. Watch sessions by variant

### Scenario 4: "We use multiple tools"

Show:
1. List tools PostHog replaces
2. Demonstrate integration (chart → replay)
3. Calculate potential savings
4. Highlight reduced complexity

---

## Technical Details for Conversations

### SDKs Available

- JavaScript (web)
- React, Next.js, Vue, Angular
- React Native
- iOS, Android, Flutter
- Python, Node.js, Ruby, Go, PHP
- Rust, Elixir, Java

### Data Storage

- Cloud (US or EU)
- Self-hosted option
- Single-tenant option for Enterprise

### API

Full REST API for everything:
- Export data
- Create insights programmatically
- Manage feature flags
- Query events

### Integrations

- Segment
- Rudderstack
- Slack
- Webhooks
- Many more

---

## Objection Handling

### "Amplitude/Mixpanel is industry standard"

- PostHog has autocapture (they don't)
- PostHog is all-in-one (they're just analytics)
- PostHog is built for engineers (they're for marketers)
- PostHog is transparent (no "talk to sales")

### "We need enterprise features"

- Enterprise is self-serve ($2k/month)
- RBAC, dedicated support included
- Can still customize at scale

### "We're worried about privacy/GDPR"

- EU hosting available
- Self-host option
- Cookieless tracking possible
- Full data control

### "It seems complex"

- Autocapture for instant value
- Use what you need
- Add products as you grow
- Native integration reduces complexity

---

## Resources

### Documentation
- [Product Analytics](https://posthog.com/docs/product-analytics)
- [Session Replay](https://posthog.com/docs/session-replay)
- [Feature Flags](https://posthog.com/docs/feature-flags)
- [Experiments](https://posthog.com/docs/experiments)
- [Surveys](https://posthog.com/docs/surveys)

### Pricing
- [Pricing Page](https://posthog.com/pricing)

### Tutorials
- [All Tutorials](https://posthog.com/tutorials)
