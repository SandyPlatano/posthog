# PostHog Lingo & Terminology Glossary

A comprehensive guide to the terminology you'll need for PostHog conversations. Terms marked with 🦔 are PostHog-specific.

---

## Core PostHog Products

**Product Analytics** 🦔
- PostHog's analytics platform that helps teams understand user behavior through trends, funnels, retention, paths, and lifecycle insights
- Example: "With Product Analytics, you can see exactly where users drop off in your signup funnel"

**Session Replay** 🦔
- Records real user sessions showing mouse movements, clicks, console logs, and network requests so you can watch exactly what users experienced
- Example: "Session Replay lets you see the bug exactly as the user experienced it"

**Feature Flags** 🦔
- Tool for safely rolling out features to specific users or percentages, with instant rollback capability
- Example: "Use Feature Flags to roll out to 5% of users first, then scale up if metrics look good"

**Experiments** 🦔
- A/B testing platform built on feature flags with statistical analysis to validate hypotheses
- Example: "Run an Experiment to test if the blue or green button drives more conversions"

**Surveys** 🦔
- In-app feedback collection tool for NPS, user research, and feature feedback
- Example: "Use Surveys to ask churning users why they're leaving"

**CDP (Customer Data Platform)** 🦔
- Collects, transforms, and syncs customer data across tools
- Example: "The CDP syncs PostHog data to your data warehouse automatically"

**Data Warehouse** 🦔
- SQL interface to query all your data and join with external sources
- Example: "Use the Data Warehouse to join PostHog events with Stripe revenue data"

**Error Tracking** 🦔
- Captures application errors with stack traces, connected to session replays
- Example: "Error Tracking shows you the session replay of when the error occurred"

---

## Product Analytics Terminology

**Autocapture** 🦔
- PostHog's ability to automatically capture frontend events (clicks, pageviews, form submissions) without manual instrumentation
- Example: "Unlike Amplitude, PostHog has autocapture so you start collecting data immediately"
- **Why it matters:** Major differentiator that provides instant value and enables retroactive analysis

**Events**
- User interactions or occurrences tracked in your product (e.g., "button_clicked", "purchase_completed")
- Example: "Track custom events like 'checkout_started' to measure conversion"

**Actions** 🦔
- A PostHog concept that groups one or more events into a new named format for easier analysis
- Example: "Create an Action called 'Successful Signup' that combines email_verified and profile_completed events"

**Properties**
- Additional data attached to events (e.g., user_id, device_type, price)
- Example: "Filter your funnel by the 'plan_type' property to see enterprise vs. free user behavior"

**Trends**
- Visualization showing how metrics change over time
- Example: "The Trends chart shows our daily active users are growing 15% month-over-month"

**Funnels**
- Tracks users through a series of sequential steps to measure conversion and drop-off
- Example: "Our signup funnel shows 60% of users complete step 1, but only 30% finish step 2"

**Retention**
- Measures how many users return to your product over time
- Example: "Our 7-day retention is 40%, meaning 40% of new users come back within a week"

**Cohorts**
- Groups of users who share common characteristics or behaviors
- Example: "Create a cohort of 'Power Users' who used the product 10+ times this month"

**Paths**
- Visualization showing the actual routes users take through your product
- Example: "The Paths insight revealed users are clicking through Settings to reach Billing instead of the direct link"

**Lifecycle**
- Analysis showing user states: new, returning, resurrecting (came back), or dormant
- Example: "Our Lifecycle chart shows we're getting more resurrecting users, which is good for retention"

---

## Technical & Implementation Terms

**SDK (Software Development Kit)**
- Library that integrates PostHog into your application
- Example: "We support SDKs for JavaScript, React, Python, iOS, Android, and 10+ more languages"

**Instrumentation**
- The process of adding code to track events in your application
- Traditional tools require heavy instrumentation; PostHog's autocapture reduces this burden

**Retroactive Analysis** 🦔
- Ability to query data that was collected before you defined the event (enabled by autocapture)
- Example: "With retroactive analysis, you can define an event today and see historical data immediately"
- **Why it matters:** Huge advantage over Amplitude/Mixpanel which can't analyze events you didn't predefine

**Self-Hosting** 🦔
- Running PostHog on your own infrastructure instead of PostHog's cloud
- Example: "If you need full data control for compliance, you can self-host PostHog"

**Open Source** 🦔
- PostHog's core is MIT-licensed and publicly available
- Example: "Because PostHog is open source, you can inspect the code and even contribute features"

---

## Feature Flag & Experimentation Terms

**Rollout**
- Gradually releasing a feature to increasing percentages of users
- Example: "Start with a 10% rollout, monitor metrics, then scale to 50% and finally 100%"

**Rollback**
- Instantly turning off a feature flag without redeploying code
- Example: "When we saw the bug, we did an instant rollback by toggling the flag off"

**Targeting**
- Showing features to specific user segments based on properties
- Example: "Target the beta feature only to users with email domains from @company.com"

**Multivariate Flag**
- Feature flag with more than two variants (beyond just on/off)
- Example: "Use a multivariate flag to test 3 different pricing page layouts"

**Payload**
- JSON configuration attached to a feature flag to change behavior without redeploying
- Example: "The payload contains the new API endpoint URL, so we can switch it without a deploy"

**Variants**
- Different versions in an A/B test (e.g., control, test variant A, test variant B)
- Example: "We're testing 3 variants: current flow, simplified flow, and gamified flow"

**Statistical Significance**
- Confidence level that results aren't due to random chance (typically 95%+)
- Example: "The experiment reached statistical significance after 2 weeks with 5,000 users"

**Goal Metric**
- The key metric you're trying to improve in an experiment
- Example: "Our goal metric is conversion rate from trial to paid"

---

## Session Replay Terms

**DOM (Document Object Model)**
- The structure of a web page that session replay captures
- Example: "Session Replay captures DOM changes to show exactly what the user saw"

**Console Logs**
- Error messages and debug information displayed in the browser console, captured in replays
- Example: "The console logs in the replay show a 404 error right before the user gave up"

**Network Requests**
- API calls and data fetches that session replay can capture
- Example: "The network tab shows the checkout API took 8 seconds, explaining the user frustration"

**Masking**
- Hiding sensitive information (like passwords, credit cards) in session replays
- Example: "All form inputs are masked by default to protect user privacy"

---

## Business & Market Terms

**Product Engineer**
- PostHog's primary ICP: full-stack engineers who build products with a user-obsessed mindset
- Example: "Product engineers want tools they can implement themselves without waiting for PMs"
- **Why it matters:** This is who you're selling to - not marketers or traditional PMs

**ICP (Ideal Customer Profile)**
- Target customer: Series B to IPO, 15-500 employees, $100k+/month revenue, engineering-led
- Example: "This Series C SaaS company with 200 employees fits our ICP perfectly"

**Tool Sprawl**
- Using too many separate tools that create data silos and integration complexity
- Example: "They're using Mixpanel, LaunchDarkly, Hotjar, and Optimizely - classic tool sprawl"

**Data Silos**
- When data is trapped in separate tools and can't be connected
- Example: "Their analytics and session replay are siloed, so they can't connect metrics to actual user behavior"

**Product-Market Fit (PMF)**
- When a product successfully satisfies strong market demand
- Example: "Series B companies have already found product-market fit and need analytics to scale"

**Engineering-Led**
- Companies where engineers make buying decisions and drive product direction
- Example: "As an engineering-led company, their VP of Engineering will make the final call on tools"

---

## Competitive Intelligence Terms

**Amplitude**
- Traditional product analytics competitor (requires manual instrumentation, no autocapture)
- Example: "Unlike Amplitude, PostHog has autocapture and includes session replay"

**Mixpanel**
- Product analytics competitor (similar to Amplitude, no autocapture)
- Example: "Mixpanel requires weeks of engineering setup; PostHog starts collecting data immediately"

**LaunchDarkly**
- Feature flag competitor (single-product tool, not integrated with analytics)
- Example: "LaunchDarkly only does feature flags, but PostHog shows how flags impact your metrics"

**Hotjar**
- Session replay and survey competitor (not integrated with analytics)
- Example: "Hotjar can't jump from a conversion funnel to a session replay like PostHog can"

**FullStory**
- Session replay competitor (expensive, marketed to product managers)
- Example: "FullStory is 3-4x more expensive and doesn't include analytics or feature flags"

**Segment**
- Customer data platform competitor
- Example: "PostHog's CDP can replace Segment for many use cases at lower cost"

---

## PostHog-Specific Features & Differentiators

**Native Integration** 🦔
- All PostHog products share the same data foundation and can seamlessly connect
- Example: "Click on any data point in a trend chart and jump directly to session replays of those users"
- **Why it matters:** This is PostHog's killer feature - competitors can't do this

**All-in-One Platform** 🦔
- Single platform replacing 4-5 separate tools (analytics, flags, replay, experiments, surveys)
- Example: "PostHog replaces Amplitude, LaunchDarkly, Hotjar, and Optimizely with one integrated platform"

**Transparent Pricing** 🦔
- All pricing publicly available, no "Contact Sales" gatekeeping
- Example: "Engineers love that they can see exact pricing and start using PostHog without talking to sales"

**Self-Serve Everything** 🦔
- Even Enterprise plan ($2,000/month) is self-serve without sales calls
- Example: "You can upgrade to Enterprise right from the dashboard - no sales process needed"

**Groups** 🦔
- Aggregate events by companies, teams, or any entity beyond individual users
- Example: "Use Groups to analyze behavior by company instead of just individual users"

---

## Analytics & Growth Metrics

**DAU/MAU (Daily/Monthly Active Users)**
- Count of unique users active in a given period
- Example: "Our DAU is 10,000 and MAU is 50,000, giving us a DAU/MAU ratio of 20%"

**Conversion Rate**
- Percentage of users who complete a desired action
- Example: "Our trial-to-paid conversion rate is 15%"

**Churn**
- When users stop using your product
- Example: "Our monthly churn is 5%, meaning we lose 5% of customers each month"

**Retention Rate**
- Percentage of users who return to your product
- Example: "Day 7 retention is 40% - nearly half of new users come back within a week"

**Drop-off**
- Where users leave a funnel or stop progressing
- Example: "We see 60% drop-off between adding to cart and starting checkout"

**Activation**
- When a user experiences core product value for the first time
- Example: "Our activation event is when users complete their first analysis"

**LTV (Lifetime Value)**
- Total revenue expected from a customer over their lifetime
- Example: "Our average LTV is $2,400 for enterprise customers"

**CAC (Customer Acquisition Cost)**
- Cost to acquire a new customer (marketing + sales expenses)
- Example: "If our CAC is $800 and LTV is $2,400, we have a healthy 3:1 ratio"

---

## Sales & Conversation Terms

**Discovery**
- Initial conversation to understand prospect's needs and pain points
- Example: "In discovery, ask about their current analytics stack and integration pain"

**Qualification**
- Determining if a prospect fits PostHog's ICP
- Example: "They're Series A with 8 employees - not quite qualified yet, but good to nurture"

**Pain Points**
- Problems or frustrations the prospect is experiencing
- Example: "Their main pain points are tool sprawl and lack of integration between analytics and replays"

**Use Case**
- Specific way a customer will use PostHog
- Example: "Their primary use case is understanding why users drop off during onboarding"

**Champions**
- People inside the prospect's company who advocate for PostHog
- Example: "The senior frontend engineer is our champion - they're pushing for PostHog internally"

**Objection**
- Concern or hesitation from a prospect
- Example: "The objection was 'we already use Amplitude' - I explained autocapture and native integration"

**POC (Proof of Concept)**
- Trial implementation to validate PostHog solves their problem
- Example: "They're running a 2-week POC with their production traffic to test session replay"

---

## Common Acronyms

**BDR** - Business Development Representative (you!)
**SDK** - Software Development Kit
**API** - Application Programming Interface
**CDP** - Customer Data Platform
**ICP** - Ideal Customer Profile
**PMF** - Product-Market Fit
**NPS** - Net Promoter Score
**DAU** - Daily Active Users
**MAU** - Monthly Active Users
**LTV** - Lifetime Value
**CAC** - Customer Acquisition Cost
**UI** - User Interface
**UX** - User Experience
**GDPR** - General Data Protection Regulation (EU privacy law)
**RBAC** - Role-Based Access Control
**MTTR** - Mean Time To Repair
**SaaS** - Software as a Service
**B2B** - Business to Business
**ARR** - Annual Recurring Revenue
**MRR** - Monthly Recurring Revenue

---

## Key Phrases & Messaging

**"Built for Product Engineers"**
- Core positioning: technical depth for engineers who own the product
- Example: "PostHog is built for product engineers who want to ship fast and understand their users"

**"All-in-one platform"**
- Replace multiple tools with one integrated solution
- Example: "You can replace Amplitude, LaunchDarkly, and Hotjar with PostHog's all-in-one platform"

**"Jump from chart to replay"**
- Demonstrates native integration advantage
- Example: "When you see a drop in conversion, just click the data point and watch session replays to see why"

**"Start collecting data immediately"**
- Autocapture value proposition
- Example: "Unlike Mixpanel, PostHog's autocapture means you start collecting data the moment you deploy"

**"No talk to sales required"**
- Self-serve, transparent pricing advantage
- Example: "Engineers love that they can try PostHog and see pricing without talking to sales"

**"Open source and transparent"**
- Trust and control positioning
- Example: "PostHog is open source, so you can inspect the code and even self-host if needed"

---

## Quick Reference: Top 20 Terms to Master

1. **Product Engineer** - Your buyer persona
2. **Autocapture** - PostHog's biggest technical differentiator
3. **Native Integration** - Why all-in-one matters
4. **Session Replay** - Visual debugging superpower
5. **Feature Flags** - Safe shipping mechanism
6. **Experiments** - A/B testing platform
7. **Funnel** - Conversion tracking
8. **Retention** - User stickiness measurement
9. **Cohorts** - User segmentation
10. **Retroactive Analysis** - Query historical data
11. **Self-Hosting** - Data control option
12. **Transparent Pricing** - No sales gatekeeping
13. **Tool Sprawl** - Key pain point
14. **Data Silos** - Integration problem
15. **ICP** - Ideal customer profile
16. **Engineering-Led** - Decision-making structure
17. **Rollout** - Gradual feature release
18. **Churn** - User loss metric
19. **Activation** - First value moment
20. **Open Source** - Trust and transparency

---

## Resources

- PostHog Official Glossary: https://posthog.com/docs/glossary
- Product Knowledge Guide: `05-product-knowledge.md`
- ICP Deep Dive: `08-product-engineer-icp-deep-dive.md`
- Sales Playbook: `02-sales-playbook.md`

---

**Pro Tip:** When talking to product engineers, use technical terms confidently but avoid sales jargon. Engineers respect technical precision and can tell immediately if you understand what you're talking about.
