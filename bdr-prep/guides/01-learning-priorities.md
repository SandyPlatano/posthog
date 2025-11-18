# Learning Priorities for PostHog Founding BDR

This guide outlines what to prioritize in your preparation, organized by importance and sequence.

## Priority 1: Understand PostHog's Philosophy (Critical)

Before anything else, internalize WHY PostHog does things differently:

### The Core Philosophy
- **No BS sales talk** - Be direct, open, and honest
- **Share information publicly** - Don't hide behind mandatory demo calls
- **Admit when you don't know** - Or when PostHog isn't the right solution
- **Product-led growth** - Engineers try before they buy, self-serve is primary

### Why This Matters
PostHog explicitly warns new hires: "Don't execute your previous company's playbook." They're trying to do things differently from 90% of the industry. If you come in with traditional BDR tactics, you'll fail.

### Action Items
- [ ] Read the [Sales Overview](https://posthog.com/handbook/growth/sales/overview) completely
- [ ] Read [How We Work](https://posthog.com/handbook/growth/sales/how-we-work)
- [ ] Read [Company Values](https://posthog.com/handbook/values)
- [ ] Understand why they hate "MEDPICC from your car phone"

---

## Priority 2: Technical Competency (High)

As a Founding BDR, you need to be technical enough to not need an engineer. This is non-negotiable.

### What "Technical" Means at PostHog
- Can implement PostHog in a web or mobile app
- Understand what autocapture does vs custom events
- Can explain feature flags and experiments to an engineer
- Know when to use server-side vs client-side SDKs
- Understand the data pipeline and how events flow

### Skills to Develop

#### Must Have (Week 1-2)
1. **JavaScript/Web implementation**
   - Install posthog-js
   - Configure autocapture
   - Capture custom events
   - Identify users

2. **Feature Flags basics**
   - Create a flag
   - Evaluate it in code
   - Understand rollout percentages

3. **Product Analytics**
   - Create insights (trends, funnels, retention)
   - Understand event properties and user properties
   - Create cohorts

#### Should Have (Week 2-3)
4. **Session Replay**
   - Understand privacy controls
   - Know what gets recorded
   - Use replay to debug issues

5. **Experiments/A/B Testing**
   - Set up an experiment
   - Understand statistical significance
   - Connect experiments to feature flags

6. **Multi-platform implementation**
   - React/Next.js setup
   - Python backend setup
   - Know when to use which SDK

### Action Items
- [ ] Sign up for [PostHog Cloud](https://app.posthog.com/signup) (free tier is generous)
- [ ] Implement on a personal project or test site
- [ ] Complete at least 3 tutorials from [PostHog Tutorials](https://posthog.com/tutorials)
- [ ] Build a demo environment you can use in calls

---

## Priority 3: ICP and Qualification (High)

Know exactly who PostHog sells to and how to qualify them.

### The ICP: High-Performing Product Engineers

**Target Companies:**
- Series B to IPO stage
- 15-500 employees
- Revenue over $100K/month
- Top-tier investor backing
- B2B startups with product-market fit
- Engineering-led decision making

**Target Personas:**
- Product engineers (full-stack, frontend-skewed)
- Engineering leadership (bonus if they code)
- Technical product managers

### ICP Scoring Criteria (24-point scale)

PostHog uses Clearbit to score leads:

| Factor | Points |
|--------|--------|
| Engineering role | 6 |
| Leadership/Product role | 3 each |
| Private company | 3 |
| Founded 2015-2022 | 3 |
| 15-500 employees | Highest weight |
| Country/region | Varies |

### Qualification Questions

Before scheduling a call, consider:
1. How large is the company? Revenue?
2. Have they raised funding? (Will they pay >$20k?)
3. What is the role of the form-filler?
4. Are engineers already involved?

### Converting Lead to Opportunity (BANT-adjacent)

Must have:
- At least one call to establish relationship
- Clearly identified problem PostHog can solve

### Action Items
- [ ] Memorize the ICP criteria
- [ ] Practice qualifying sample companies
- [ ] Understand the 24-point scoring system
- [ ] Read [ICP Scoring](https://posthog.com/handbook/growth/marketing/icp)

---

## Priority 4: Product Knowledge (High)

Know every product PostHog offers and when to recommend each.

### Core Products

1. **Product Analytics** - User behavior analysis
2. **Session Replay** - Watch real user sessions
3. **Feature Flags** - Safe feature rollouts
4. **Experiments** - A/B testing with stats
5. **Surveys** - In-app user feedback
6. **CDP** - Customer data platform
7. **Data Warehouse** - SQL access to data
8. **Error Tracking** - Exception monitoring

### Key Differentiators

- **Autocapture**: Unlike Mixpanel/Amplitude, starts capturing immediately
- **Native Integration**: All products talk to each other
- **Open Source**: Full transparency, self-host option
- **Engineer-First**: Built for builders, not marketers

### Common Use Cases

1. **Understanding user behavior** → Product Analytics
2. **Debugging conversion drops** → Funnels + Session Replay
3. **Safe feature releases** → Feature Flags
4. **Testing hypotheses** → Experiments
5. **Collecting feedback** → Surveys
6. **Privacy/compliance** → Self-hosting

### Action Items
- [ ] Use each product at least once
- [ ] Know pricing for each product
- [ ] Understand the free tier limits
- [ ] Build demo scenarios for common use cases

---

## Priority 5: Competitive Intelligence (Medium-High)

Know how PostHog compares to every competitor.

### Primary Competitors

| Competitor | Strength | PostHog Advantage |
|------------|----------|-------------------|
| **Amplitude** | Enterprise scale, non-technical users | All-in-one, open source, engineer-focused |
| **Mixpanel** | Ease of use, marketing teams | Autocapture, feature flags, session replay |
| **Heap** | Autocapture | More developer features, open source |
| **LaunchDarkly** | Feature flags | Integrated with analytics |
| **Hotjar** | Session replay | Full analytics platform |

### Tools PostHog Replaces
- Heap (product analytics)
- LaunchDarkly (feature flags)
- Hotjar (session replay + surveys)

### When PostHog Might NOT Be Right
- Pure marketing analytics (use Amplitude)
- Non-technical teams (use Mixpanel)
- Enterprise needing heavy customization (maybe)

### Action Items
- [ ] Read PostHog's competitor comparison pages
- [ ] Try competitor free tiers to understand them
- [ ] Prepare battle cards for common objections
- [ ] Know when to honestly recommend against PostHog

---

## Priority 6: Company Culture (Medium)

Understand how PostHog operates to fit in.

### Core Culture Elements

1. **All-Remote**: 100% distributed, 20+ countries
2. **Transparency**: Public handbook, roadmap, investor info
3. **Async-First**: Written communication, GitHub-centric
4. **Small Teams**: Max 6 people, full autonomy
5. **PRs over Issues**: Do it yourself, don't just open tickets
6. **Bias for Action**: "Why not now?"

### What They Look For

- Culture fit is MORE important than skills (skills can be taught)
- Self-starters who don't need management
- People comfortable with ambiguity
- Written communicators

### Action Items
- [ ] Read [Culture](https://posthog.com/handbook/company/culture)
- [ ] Read [Communication](https://posthog.com/handbook/company/communication)
- [ ] Understand async-first workflows
- [ ] Be prepared to discuss how you work independently

---

## Priority 7: Sales Operations (Medium)

Understand the mechanics of PostHog sales.

### CRM Lead Statuses
- **New**: Just entered, not contacted
- **Working**: Actively engaging

### Key Processes
- Ben (sales lead) does onboarding with new hires
- First week: Go through sales process, shadow calls
- Use Buildbetter for call recordings
- Internal playbook covers company style and communication

### Contract Thresholds
- $20k: Minimum for customization
- 20% discount for prepaid >$20k
- Additional discounts at $60k and $100k

### Action Items
- [ ] Understand the CRM workflow
- [ ] Read [Managing our CRM](https://posthog.com/handbook/growth/sales/crm)
- [ ] Read [Sales Operations](https://posthog.com/handbook/growth/sales/sales-operations)
- [ ] Understand contract rules and discount structures

---

## Weekly Learning Schedule

### Week 1: Foundation
- Day 1-2: Philosophy and culture (Priority 1, 6)
- Day 3-4: ICP and qualification (Priority 3)
- Day 5: Product overview (Priority 4)

### Week 2: Technical Deep Dive
- Day 1-2: Basic implementation (Priority 2)
- Day 3-4: Feature flags and experiments
- Day 5: Session replay and surveys

### Week 3: Sales Preparation
- Day 1-2: Competitive intelligence (Priority 5)
- Day 3-4: Sales operations (Priority 7)
- Day 5: Practice demos and qualifying

### Week 4: Interview Prep
- Mock outbound campaigns
- Technical implementation challenges
- Culture fit scenarios
- Prepare questions about the role

---

## Self-Assessment Checkpoints

### After Week 1
- [ ] Can I explain PostHog's sales philosophy in my own words?
- [ ] Do I understand why they reject traditional sales tactics?
- [ ] Can I score a lead using ICP criteria?

### After Week 2
- [ ] Can I implement PostHog without looking at docs?
- [ ] Can I set up a feature flag and experiment?
- [ ] Do I know when to use which SDK?

### After Week 3
- [ ] Can I handle objections about competitors?
- [ ] Do I understand the pricing and discount structure?
- [ ] Can I demo any PostHog product convincingly?

### After Week 4
- [ ] Can I run a mock outbound campaign to ICP targets?
- [ ] Am I prepared for technical interview questions?
- [ ] Can I articulate why I'm a culture fit?
