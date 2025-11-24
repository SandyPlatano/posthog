# Campaign Creation Framework - PostHog Style

## Naming Convention

Create campaigns using: **[ICP/Vertical] - [Purpose] - [Version]**

Example: `B2B-SaaS - Cold - Q1-2025`

---

## [ICP/Vertical]: Who is this for?

Define your target vertical or ideal customer segment.

### PostHog Primary Verticals

**B2B-SaaS** = B2B SaaS companies (Series B+)
- Primary ICP: Product-focused B2B companies
- 15-500 employees, $100k+/month revenue
- Engineering-led decision making
- Examples: Notion, Linear, Vercel

**DevTools** = Developer Tools & Infrastructure
- Companies building for engineers
- High technical complexity
- Strong engineering culture
- Examples: Supabase, Prisma, Railway

**FinTech** = Financial Technology
- Payment processors, banking apps, crypto
- High data sensitivity needs
- Compliance requirements (self-hosting interest)
- Examples: Stripe-like companies, neobanks

**AI/ML** = AI & Machine Learning Products
- LLM applications, ML platforms
- Need to track AI feature performance
- High usage/cost monitoring needs
- Examples: AI copilots, ML-powered apps

**Marketplace** = Marketplace Platforms
- Two-sided marketplace businesses
- Complex user journey tracking
- Conversion optimization focus
- Examples: Airbnb-style, B2B marketplaces

**HealthTech** = Healthcare & Wellness Tech
- Digital health products
- Telemedicine platforms
- Often need self-hosting for HIPAA
- Examples: Health tracking apps, telehealth

**PropTech** = Property & Real Estate Tech
- Real estate platforms
- Property management software
- Examples: Zillow-style, rental platforms

---

## [Purpose]: Why are you reaching out?

Define the play or campaign goal.

### PostHog Campaign Types

**Cold** = General cold outreach for that vertical
- First-touch outreach to ICP companies
- No prior relationship or product usage
- Lead with value, not pitch
- Focus: Build awareness + book qualified calls

**Warm** = Following up on product-engaged leads
- Signed up but not actively using ("tire-kickers")
- Was a customer, moved to new company
- Engaged with content but not signed up
- Focus: Remove friction, offer help

**Expansion** = Existing customer growth plays
- Current customers under $20k spend
- Using only 1-2 products (cross-sell opportunity)
- Heavy usage approaching limits
- Focus: Help them get more value

**Consolidation** = Tool consolidation messaging
- Target companies using 3+ tools PostHog replaces
- Emphasize cost savings + unified data
- Examples: "Using Amplitude + LaunchDarkly + Hotjar?"
- Focus: Simplification benefits

**Comp-Amp** = Competitive play against Amplitude
- Target Amplitude customers
- Emphasize: Better pricing, autocapture, all-in-one
- Technical comparison focused

**Comp-Mix** = Competitive play against Mixpanel
- Target Mixpanel customers
- Emphasize: Session replay, feature flags, better UX

**Comp-LD** = Competitive play against LaunchDarkly
- Target LaunchDarkly customers
- Emphasize: Analytics + experiments + flags unified

**Comp-Heap** = Competitive play against Heap
- Target Heap customers
- Emphasize: Modern UI, better data warehouse, flags

**Ent-Play** = Enterprise target account play
- Large prospect requiring custom approach
- Multi-threaded outreach strategy
- ABM-style campaign for 1-5 accounts
- Focus: High-touch, personalized

**Trigger** = Event-based outreach
- Funding announcement (Series B+)
- Engineering leadership hire (VP Eng, CTO)
- Product launch or major feature release
- Competitor migration signals
- Focus: Timely, relevant context

**Re-Engage** = Churned or dormant users
- Former customers who left
- Inactive users (90+ days no activity)
- Trial expirations without conversion
- Focus: "What changed?" + product improvements

---

## [Version]: When did you create this?

Essential for A/B testing, iteration tracking, and performance measurement.

### Format Options

**Time-based:**
- `Q1-2025`, `Q2-2025`, `Q3-2025`, `Q4-2025`
- Good for: Quarterly campaign refreshes

**Version-based:**
- `v1.0`, `v1.1`, `v2.0`
- Good for: Rapid iteration and A/B tests

**Date-based (for high-velocity testing):**
- `Jan2025`, `2025-01`, `25-01`
- Good for: Weekly/monthly tests

### When to Increment Versions

- **Messaging change**: Updated value prop or copy
- **Target change**: Different segment within vertical
- **Channel change**: LinkedIn vs Email vs Multi-touch
- **Offer change**: Demo vs. Resource vs. Direct ask
- **Quarterly refresh**: New quarter = new version

---

## Example Campaigns

### Example 1: General Cold Outreach
**Campaign:** `B2B-SaaS - Cold - Q1-2025`

**Who:** B2B SaaS companies, Series B+, 50-200 employees
**Why:** First-touch cold outreach
**When:** Q1 2025 campaign

**Messaging angle:** Tool consolidation (replacing Amplitude + LaunchDarkly)

---

### Example 2: Competitive Displacement
**Campaign:** `DevTools - Comp-Amp - v1.0`

**Who:** Developer tools companies
**Why:** Competitive play against Amplitude
**When:** First version

**Messaging angle:** "Engineers deserve better analytics tools built by engineers"

---

### Example 3: Event-Based Outreach
**Campaign:** `FinTech - Trigger - Q1-2025`

**Who:** FinTech companies
**Why:** Outreach triggered by Series B+ funding
**When:** Q1 2025

**Messaging angle:** "Congrats on the raise - here's how to instrument product analytics from day one"

---

### Example 4: Warm Follow-up
**Campaign:** `AI/ML - Warm - v2.0`

**Who:** AI/ML product companies
**Why:** Following up with signups not actively using
**When:** Second iteration (improved messaging)

**Messaging angle:** "Track LLM costs + user experience in one place"

---

### Example 5: Multi-threaded Enterprise
**Campaign:** `Marketplace - Ent-Play - Shopify`

**Who:** Specific target: Shopify
**Why:** Custom enterprise play for major account
**When:** Named account (not time-based)

**Messaging angle:** Highly personalized, multi-persona outreach

---

## Campaign Tracking Sheet Template

| Campaign Name | Vertical | Purpose | Version | Start Date | Emails Sent | Replies | Calls Booked | Opps Created | Notes |
|---------------|----------|---------|---------|------------|-------------|---------|--------------|--------------|-------|
| B2B-SaaS - Cold - Q1-2025 | B2B-SaaS | Cold | Q1-2025 | 2025-01-06 | 150 | 12 | 5 | 2 | Testing consolidation angle |
| DevTools - Comp-Amp - v1.0 | DevTools | Comp-Amp | v1.0 | 2025-01-10 | 80 | 8 | 3 | 1 | Strong technical response |
| AI/ML - Warm - v2.0 | AI/ML | Warm | v2.0 | 2025-01-15 | 200 | 25 | 10 | 4 | v2 improved by 40% |

---

## Best Practices

### Do's ✅
- **Be specific:** Don't use generic verticals - pick precise ICP segments
- **Test variations:** Always run v1.0, v1.1, v2.0 to optimize
- **Track rigorously:** Can't improve what you don't measure
- **Align with PostHog values:** No BS, helpful, technically credible
- **Personalize at scale:** Use Clay/tools for relevant personalization

### Don'ts ❌
- **Don't spam:** Quality > quantity (PostHog brand protection)
- **Don't pitch immediately:** Lead with value, not product
- **Don't ignore ICP fit:** Better to send 50 great emails than 500 mediocre
- **Don't copy competitors:** This is PostHog's way, not typical BDR plays
- **Don't forget to version:** Always track iterations

---

## Campaign Development Checklist

Before launching a campaign, ensure:

- [ ] **ICP validated:** Confirmed this vertical fits PostHog's scoring criteria
- [ ] **Messaging drafted:** 2-3 email sequences + LinkedIn messages written
- [ ] **Value-first approach:** Leading with help/insights, not product pitch
- [ ] **Personalization plan:** Clay workflow or manual research process defined
- [ ] **Success metrics:** Clear KPIs set (reply rate, call book rate, opp creation)
- [ ] **Version baseline:** Starting with v1.0 to enable iteration tracking
- [ ] **Brand-aligned:** Reviewed against PostHog's "no BS" values
- [ ] **Technical credibility:** Can back up claims with product knowledge

---

## Notes on PostHog-Specific Considerations

### Engineering-Led Sales
Remember: Your campaigns must appeal to **product engineers**, not traditional buyers.

- Use technical language naturally
- Show, don't tell (link to docs, not just claims)
- Respect their time (no unnecessary calls)
- Prove technical credibility early

### Brand Protection
PostHog has incredible brand reputation. Don't ruin it with:

- Aggressive sales tactics
- False personalization ("I saw you work at {company}")
- Volume over quality plays
- Overpromising or gatekeeping info

### The Outbound Experiment
PostHog is new to outbound. Your campaigns are **experiments**:

- Document what works and what doesn't
- Be willing to kill underperforming campaigns fast
- Share learnings with the team
- Build the playbook as you go

---

## Resources

- [PostHog Sales Playbook](guides/02-sales-playbook.md)
- [ICP Scoring](https://posthog.com/handbook/growth/marketing/icp)
- [Outbound Sales Handbook](https://posthog.com/handbook/growth/sales/outbound-sales)
- [Product Engineer Deep-Dive](guides/08-product-engineer-icp-deep-dive.md)
