# PostHog Qualification Funnel Scoring Framework
## Enhanced with Clay Web Enrichment

> **Purpose**: A comprehensive scoring system that combines PostHog's existing ICP model with web-enriched data points to identify high-quality leads and enable personalized outreach.

---

## Table of Contents
1. [Overview](#overview)
2. [Scoring Framework (60-Point Scale)](#scoring-framework)
3. [Data Sources & Clay Implementation](#data-sources--clay-implementation)
4. [Custom Messaging Framework](#custom-messaging-framework)
5. [Prioritization Matrix](#prioritization-matrix)

---

## Overview

### Current State
PostHog uses a **24-point Clearbit-based scoring model** focused on firmographics and role data. While effective, it lacks:
- Technographic signals (tech stack, competitor usage)
- Behavioral signals (hiring, funding, growth indicators)
- Pain indicators (problems PostHog solves)

### Enhanced State
This framework expands to a **60-point system** that layers on web-enriched data to identify:
- **Who** they are (existing ICP scoring)
- **What problems** they're experiencing (pain signals)
- **When** to reach out (timing signals)
- **Why** PostHog matters to them (messaging hooks)

---

## Scoring Framework (60-Point Scale)

### Category 1: Core ICP Fit (24 points)
*Current PostHog scoring - automated via Clearbit*

| Criteria | Points | Details |
|----------|--------|---------|
| **Engineering Role** | 6 | Software Engineer, Engineering Manager, CTO, VP Engineering |
| **Leadership Role** | 3 | C-suite, VP-level (non-engineering) |
| **Product Role** | 3 | Product Manager, Head of Product, CPO |
| **Private Company** | 3 | Private companies are preferred over public |
| **Founded 2015-2022** | 3 | Sweet spot for PMF + growth phase |
| **15-500 Employees** | 3 | Ideal size range (not too small, not too enterprise) |
| **Favorable Geography** | 3 | US, UK, EU primary markets |

**Threshold**: 18+ points = Strong ICP fit

---

### Category 2: Financial & Growth Signals (12 points)
*Clay enrichment from Crunchbase, PitchBook, press releases*

| Criteria | Points | Details |
|----------|--------|---------|
| **Recent Funding (6-12 months)** | 5 | Series B+ funding = budget + growth mandate |
| **Revenue Growth** | 3 | 2x+ YoY growth = scaling pain points |
| **Top-Tier Investors** | 2 | a16z, Sequoia, YC, etc. = quality signal |
| **Runway & Health** | 2 | 18+ months runway = stable buying power |

**Data Points to Collect**:
- Last funding date & amount
- Total funding to date
- Lead investors
- Revenue range (if public)
- Growth trajectory indicators

**Messaging Hooks**:
- "Congrats on the Series B - as you scale..."
- "With your recent funding, now's the time to..."
- "Other [Investor] portfolio companies use PostHog to..."

---

### Category 3: Pain Indicators (12 points)
*Clay enrichment from job boards, LinkedIn, company updates*

| Criteria | Points | Details |
|----------|--------|---------|
| **Hiring Product Engineers** | 5 | Active job posts = scaling engineering team |
| **Hiring Data/Analytics Roles** | 3 | Need for data infrastructure/insights |
| **Hiring Growth/Product** | 2 | Scaling product organization |
| **Product Launch/Update** | 2 | Mentioned new features, redesigns = iteration needs |

**Where to Find**:
- LinkedIn jobs section
- Company careers page
- Ashby/Greenhouse job boards
- Recent blog posts/announcements

**Messaging Hooks**:
- "Saw you're hiring 5 product engineers - here's how PostHog helps teams like yours ship faster..."
- "As you scale your product team to [X] people, here's how we help maintain velocity..."
- "Just launched [feature]? Here's how to measure impact without slowing down..."

---

### Category 4: Tech Stack & Competitor Signals (8 points)
*Clay enrichment from BuiltWith, Clearbit Reveal, LinkedIn tech mentions*

| Criteria | Points | Details |
|----------|--------|---------|
| **Using Competing Tools** | 5 | Mixpanel, Amplitude, LaunchDarkly, Optimizely, FullStory, Heap |
| **Multiple Point Solutions** | 2 | Using 3+ separate tools PostHog replaces |
| **Engineering Blog** | 1 | Active eng blog = technical culture |

**Tools to Detect**:
- **Analytics**: Mixpanel, Amplitude, Heap, Google Analytics 4
- **Feature Flags**: LaunchDarkly, Split.io, Unleash
- **A/B Testing**: Optimizely, VWO, AB Tasty
- **Session Replay**: FullStory, LogRocket, Hotjar
- **Surveys**: Qualtrics, SurveyMonkey, Typeform

**Messaging Hooks**:
- "Noticed you're using [Mixpanel + LaunchDarkly + FullStory] - here's how PostHog consolidates that into one platform..."
- "Saw [tool] on your tech stack - here's what [similar company] saved by switching..."
- "Love your recent blog post on [topic] - here's how PostHog supports that workflow..."

---

### Category 5: Behavioral & Timing Signals (4 points)
*Clay enrichment from news, LinkedIn, G2/Capterra reviews*

| Criteria | Points | Details |
|----------|--------|---------|
| **Posted About Data/Analytics** | 2 | LinkedIn posts, blog mentions about data challenges |
| **Active on Product Communities** | 1 | Product Hunt, Hacker News, dev communities |
| **Left Review of Competitor** | 1 | Recent reviews = active evaluation mode |

**Messaging Hooks**:
- "Saw your post about [data challenge] - here's how we approach that..."
- "Noticed you're active on [community] - thought you'd appreciate PostHog's approach to..."
- "Saw your [competitor] review mentioning [pain point] - here's how PostHog addresses that..."

---

## Score Interpretation

| Total Score | Priority | Action |
|-------------|----------|--------|
| **45-60** | 🔥 Hot Lead | Immediate personalized outreach, multi-threaded approach |
| **35-44** | ⭐ Warm Lead | Personalized outreach, single-threaded initially |
| **25-34** | 💡 Qualified Lead | Templatized outreach with 1-2 personalizations |
| **15-24** | ❄️ Cold Lead | Nurture sequence, content sharing |
| **<15** | 🚫 Poor Fit | Skip or long-term nurture |

---

## Data Sources & Clay Implementation

### Clay Waterfall Enrichment Strategy

#### Step 1: Core Firmographic Data
**Providers**: Clearbit → People Data Labs → Hunter
- Company size, industry, location
- Employee count, revenue range
- Founding date
- Contact email patterns

#### Step 2: Funding & Financial Data
**Providers**: Crunchbase → PitchBook → Diffbot
- Funding rounds, amounts, dates
- Investor information
- Revenue estimates
- Growth signals

#### Step 3: Technology Stack
**Providers**: BuiltWith → Clearbit Reveal → 6sense
- Detected technologies
- Competing tools in use
- Infrastructure signals
- Engineering blog presence

#### Step 4: Hiring & Job Postings
**Providers**: Greenhouse/Ashby APIs → LinkedIn Jobs Scraper → Custom Web Scraper
- Open roles by department
- Job post dates and urgency indicators
- Team growth trajectory

#### Step 5: Behavioral Signals
**Providers**: Apify (LinkedIn scraper) → SimilarWeb → News APIs
- Recent LinkedIn posts about data/analytics
- Product launches and updates
- Community presence
- Competitor reviews

#### Step 6: Contact Finding & Validation
**Providers**: Apollo → RocketReach → Prospeo
- Decision-maker identification
- Email verification
- LinkedIn profile enrichment
- Direct dial discovery

---

## Custom Messaging Framework

### Message Structure Template

```
[Opening Hook - based on specific signal]
↓
[Company/Role Relevance - ICP fit point]
↓
[Problem/Pain Point - pain indicator signal]
↓
[PostHog Solution - relevant product capability]
↓
[Social Proof - similar company/investor]
↓
[Soft CTA]
```

---

### Messaging Examples by Score Profile

#### Profile A: High ICP + Recent Funding + Hiring Engineers (Score: 48)

**Data Points**:
- Engineering Manager at 150-person Series B company
- Raised $30M 3 months ago (Sequoia-backed)
- Hiring 8 product engineers
- Using Mixpanel + LaunchDarkly

**Message**:
```
Hey [Name],

Congrats on the Sequoia-led Series B! Saw you're scaling the eng
team to [X] engineers - that's exciting growth.

Quick question: As you scale, how are you handling the coordination
tax between Mixpanel for analytics, LaunchDarkly for flags, and
whatever you're using for session replay?

We work with a lot of Sequoia companies (including [Similar Company])
who consolidated all of that into PostHog as they hit this scale.
Teams love having everything in one platform as they grow past 100 engineers.

Worth a quick chat? I can show you what [Similar Company] set up.

[Signature]
```

---

#### Profile B: Strong ICP + Tech Stack + Product Launch (Score: 38)

**Data Points**:
- Product Engineer at 200-person company
- Using Amplitude + FullStory
- Recently launched new onboarding flow (from blog)
- Active on Hacker News

**Message**:
```
Hey [Name],

Loved reading about your new onboarding redesign on the blog -
the approach to [specific detail] was really clever.

Quick question: I noticed you're using Amplitude + FullStory to
measure impact. How are you connecting the quantitative data
(Amplitude) with the qualitative sessions (FullStory) to
understand *why* users behave the way they do?

We built PostHog specifically for high-craft product teams like
yours who ship frequently and need that full picture. Everything
lives in one tool, so you can jump from a funnel drop-off directly
to session replays showing what happened.

Relevant enough for a quick 15-min demo? Happy to show you
exactly what [Similar Company] set up.

[Signature]
```

---

#### Profile C: Good ICP + Competitor Pain + Active Hiring (Score: 42)

**Data Points**:
- VP Engineering at 300-person company
- Left 3-star review of Mixpanel citing "complexity" and "cost"
- Hiring data analysts and analytics engineers
- Series C funded

**Message**:
```
Hey [Name],

Saw your Mixpanel review mentioning the complexity as the team
grew - we hear that a lot from teams at your scale.

The fact that you're now hiring dedicated analytics engineers
tells me you're feeling that pain acutely. Most teams at 300
people are spending way too much time maintaining their data
infrastructure vs. actually using it.

PostHog was built specifically for engineering-led companies
who want product analytics that engineers actually enjoy using.
No separate data engineering team needed - our CEO [Posthog value]
makes this one of our core principles.

Worth exploring? Happy to show you what [Similar Company] did
when they made the switch at around your scale.

[Signature]
```

---

#### Profile D: Mid ICP + Strong Timing Signal (Score: 32)

**Data Points**:
- Product Manager at 100-person company
- Posted on LinkedIn about "struggling with data silos"
- Founded 2018, likely Series A/B stage
- Using Google Analytics + Hotjar

**Message**:
```
Hey [Name],

Your LinkedIn post about data silos really resonated - I work
with a lot of product teams dealing with exactly that problem
as they grow.

Saw you're using GA + Hotjar. The classic issue: analytics in
one place, session replays in another, and never the two shall
meet, right?

Quick question: When you see a funnel drop-off in GA, what's
your process for figuring out *why* it's happening? How many
tools do you have to jump between?

PostHog puts everything in one place - analytics, session replay,
feature flags, A/B tests, surveys. Built specifically to solve
the data silo problem you mentioned.

Worth a 15-min look? I can show you exactly what I mean.

[Signature]
```

---

## Prioritization Matrix

### Daily Workflow

**Morning (High-Value Activities)**:
1. Review new leads scored 45+ → Immediate personalized outreach
2. Review leads scored 35-44 → Personalized outreach
3. Research top 10 leads for deep personalization

**Afternoon (Medium-Value Activities)**:
4. Review leads scored 25-34 → Semi-personalized outreach
5. Follow up on previous outreach (35+ scored leads)
6. Update CRM with research findings

**End of Day (Nurture)**:
7. Add 15-24 scored leads to nurture sequences
8. Share relevant content with warm leads

---

### Weekly Lead Volume Targets

| Score Range | Target Outreach Volume | Expected Reply Rate | Expected Opportunity Rate |
|-------------|----------------------|-------------------|------------------------|
| 45-60 | 10-15 leads | 30-40% | 15-20% |
| 35-44 | 20-30 leads | 20-30% | 8-12% |
| 25-34 | 50-75 leads | 10-15% | 3-5% |
| 15-24 | Automated nurture | 5-8% | 1-2% |

---

## Clay Workflow Overview

### Recommended Clay Table Structure

**Table 1: Lead Enrichment & Scoring**
1. Input: Company domain or LinkedIn URL
2. Enrich: Clearbit → Crunchbase → BuiltWith → LinkedIn
3. Score: Formula columns for each category
4. Filter: Only pass leads with 25+ score
5. Output: To outreach table

**Table 2: Contact Finding**
1. Input: High-scoring companies from Table 1
2. Find contacts: Apollo → RocketReach → Hunter waterfall
3. Filter: Engineering, Product, Leadership roles only
4. Verify: Email verification
5. Output: To CRM (HubSpot/Salesforce)

**Table 3: Personalization Research**
1. Input: High-priority leads (35+ score)
2. Enrich: Recent LinkedIn posts, blog articles, job postings
3. Generate: AI-powered personalization snippets
4. Output: Feed into outreach sequences

---

## Continuous Improvement

### Metrics to Track

**Lead Quality Metrics**:
- Reply rate by score bracket
- Opportunity conversion by score bracket
- Score calibration (are high scores actually better leads?)

**Scoring Refinement**:
- Which signals correlate most with closed-won deals?
- Which signals have false positive/negative rates?
- Adjust point allocations quarterly based on data

**Messaging Effectiveness**:
- Reply rates by messaging type
- Which hooks get the most engagement?
- A/B test different message structures

---

## Appendix: Pain Point Deep Dive

### Common Pain Points PostHog Solves

1. **Tool Sprawl** → "Using 3+ separate tools for analytics, feature flags, session replay"
2. **Data Silos** → "Can't connect quantitative data to qualitative insights"
3. **Engineering Overhead** → "Need dedicated data engineering team to maintain analytics"
4. **Slow Iteration** → "Too much friction to run experiments and ship features"
5. **Privacy/Compliance** → "Need self-hosted solution for compliance"
6. **Cost Scaling** → "Current tool costs scaling faster than value"
7. **Adoption Issues** → "Current tool too complex, engineers won't use it"

### Signal-to-Pain Mapping

| Signal | Likely Pain Point | PostHog Solution Angle |
|--------|------------------|----------------------|
| Using Mixpanel + LaunchDarkly + FullStory | Tool sprawl, data silos | All-in-one platform |
| Hiring analytics engineers | Engineering overhead | Self-serve analytics |
| Recent funding + growth | Cost scaling, tool sprawl | Transparent pricing, consolidation |
| Posting about "data access" | Data democratization | Built for engineers |
| Using expensive enterprise tool | Cost scaling | Transparent pricing |
| Public company or 500+ employees | Compliance needs | Self-hosted option |
| Active eng blog | Technical culture | Built by engineers for engineers |

---

## Quick Reference: Scoring Cheat Sheet

```
CORE ICP (24 pts)
□ Engineering role (6) or Leadership (3) or Product (3)
□ Private company (3)
□ Founded 2015-2022 (3)
□ 15-500 employees (3)
□ Good geography (3)

FINANCIAL (12 pts)
□ Recent funding (5)
□ Revenue growth (3)
□ Top investors (2)
□ Good runway (2)

PAIN (12 pts)
□ Hiring product engineers (5)
□ Hiring data/analytics (3)
□ Hiring growth/product (2)
□ Product launches (2)

TECH STACK (8 pts)
□ Using competitors (5)
□ Multiple point solutions (2)
□ Engineering blog (1)

BEHAVIORAL (4 pts)
□ Posts about data (2)
□ Active in communities (1)
□ Competitor reviews (1)

TOTAL: /60 points
```

---

## Next Steps

1. **Set up Clay tables** using the waterfall enrichment strategy
2. **Configure scoring formulas** in Clay for automatic calculation
3. **Create message templates** for each score bracket
4. **Set up CRM integration** to sync scored leads
5. **Track metrics** and refine scoring weights quarterly
6. **Build feedback loop** from AE to BDR on lead quality

---

**Remember**: The score gets you in the door. The research and personalization get you the meeting. Use the score to prioritize, use the signals to personalize.
