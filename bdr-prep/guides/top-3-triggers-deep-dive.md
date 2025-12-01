# Top 3 Triggers for PostHog BDR Outreach
## What I'd Research and Why (From a BDR's Perspective)

> **Context**: You have 8 hours in a workday. You can reach out to 40-50 people. These are the 3 triggers that would make me prioritize one company over another.

---

## Trigger #1: Recently Funded (Series B+) + Actively Hiring Product Engineers

### The Signal
**What I'm looking for**:
- Funding announcement in **last 3-6 months** (not older, momentum fades)
- Series B, C, or D round (not Seed/Series A - they're too early)
- Funding amount: **$20M+** (shows they have budget for a $50k+ tool)
- **Simultaneously**: 3+ open "Product Engineer" or "Full-Stack Engineer" roles posted

### Why This is #1

#### 1. **Budget is Proven and Fresh**
They literally just deposited millions into their bank account. The #1 objection in sales is "we don't have budget." This trigger eliminates that objection.

**Specifically**:
- CFO hasn't locked down next year's budget yet (still in allocation mode)
- Engineering leaders are being asked "what do you need to scale?"
- There's a window of 3-6 months post-funding where spending on tooling is expected
- After 6+ months, budget gets more locked down

#### 2. **The Pain is Acute RIGHT NOW**
Hiring 3+ engineers simultaneously isn't normal operations - it's a scaling event. This means:

**Current State**:
- Small eng team (maybe 20-30 engineers) where everyone knows everyone
- Informal processes work
- Can get by with basic analytics (GA4, manual SQL queries, etc.)
- One person can manage feature flags and experiments

**Near Future** (3-6 months):
- Team will be 40-60+ engineers
- Can't rely on tribal knowledge anymore
- Need real infrastructure for experiments, analytics, feature management
- **Coordination tax skyrockets** - this is the pain PostHog solves

**The Gap**: They're about to experience massive pain, but haven't felt it yet. Perfect time to get in.

#### 3. **Engineers = Decision Makers**
PostHog's ICP is engineering-led companies where **engineers make buying decisions**.

When you're hiring product engineers, those engineers will:
- Ask "what tools do we use?" during interviews
- Complain about bad tools during onboarding
- Demand better analytics/flags/experimentation tools
- Drive internal conversations about tooling

**The new hires become your internal champions without you even knowing it.**

#### 4. **Urgency + Priority**
Post-funding companies have clear mandates from their board:
- "Use this capital to accelerate growth"
- "Scale the team and ship faster"
- "Improve product velocity"

This makes tooling a **priority**, not a "nice to have." The VP of Engineering has explicit goals to improve team efficiency.

### How to Research This

**Step 1: Find the Funding Announcement (2-3 minutes)**

**Sources**:
- Crunchbase (filter: Series B+, last 6 months, $20M+)
- LinkedIn company posts (they always announce funding)
- TechCrunch, VentureBeat, The Information
- Twitter/X searches: "[company name] funding"

**What to capture**:
- Funding amount: "$30M Series B"
- Lead investor: "led by Sequoia Capital"
- Quote from CEO about how they'll use the money
- Date of announcement

**Why this matters**: You'll reference this specifically in your outreach.

**Step 2: Check Job Postings (1-2 minutes)**

**Sources**:
- Company careers page (direct)
- LinkedIn Jobs (search by company)
- Greenhouse/Lever public boards
- Wellfound (AngelList)

**What to look for**:
- **Quantity**: How many engineering roles? (3+ = significant scaling)
- **Titles**: "Product Engineer", "Full-Stack Engineer", "Software Engineer"
- **NOT**: "Senior Staff Principal Architect" (too senior, slow hire)
- **Bonus**: If job description mentions "data-driven" or "experimentation"

**Why this matters**: Shows they're actively scaling, not just thinking about it.

**Step 3: Understand What They'll Use the Money For (2 minutes)**

**Sources**:
- Read the funding announcement press release
- Check CEO's LinkedIn post about the funding
- Look for quotes like "we'll use this to [X]"

**Common themes**:
- "Expand the product team" ✅ (great signal)
- "Scale go-to-market" (okay signal, means GTM hire priorities)
- "Enter new markets" ✅ (need better analytics for new segments)
- "Accelerate product development" ✅ (perfect - PostHog enables this)

**Why this matters**: You can tie PostHog's value to their stated goals.

### The Outreach Message

**Subject**: Re: Series B + scaling to [X] engineers

**Body**:
```
Hey [Name],

Congrats on the $30M Series B from Sequoia! Saw the announcement
about using it to accelerate product development - that's exciting.

Also noticed you're scaling the eng team pretty aggressively
(8 product engineer roles open right now).

Quick question: As you grow from ~30 to 60+ engineers over the
next few months, what's your plan for maintaining experimentation
velocity and data-driven decision making?

Most teams we work with hit a coordination wall around 50 engineers
where the informal processes break down. Managing feature flags,
experiments, and analytics across multiple tools becomes a real
drag on velocity.

[Similar Company] (also Sequoia-backed) consolidated all of that
into PostHog right after their Series B and it became a key part
of their scaling infrastructure.

Worth a 15-min conversation about what they did? Happy to share
specifics on how they maintained velocity through hypergrowth.

Best,
[Your name]
```

**Why this works**:
- ✅ References specific, recent event (funding)
- ✅ Shows you did research (job count, investor name)
- ✅ Identifies pain they're about to experience
- ✅ Positions PostHog as scaling infrastructure, not just a tool
- ✅ Uses relevant social proof (same investor)
- ✅ Low-friction CTA (just a conversation)

### Time Investment vs. Return

**Research time per company**: 5-7 minutes
**Outreach time**: 3-5 minutes (semi-custom)
**Total time**: 10-12 minutes per company

**Expected return**:
- Reply rate: **30-40%** (very high because it's timely and relevant)
- Meeting rate: **15-20%** (of those who reply)
- Opportunity rate: **10-15%** (strong intent, clear budget)

**Math**:
- 5 hours of research = 30 companies
- 30 companies × 35% reply rate = 10-11 replies
- 10 replies × 17% meeting rate = ~5 meetings booked
- 5 meetings × 12% opp rate = ~2 opportunities created

**That's 2 opportunities from 1 day of work.** At PostHog's ACV ($20k-100k+), that's massive.

---

## Trigger #2: Using Mixpanel + LaunchDarkly + Session Replay Tool (Tool Sprawl)

### The Signal
**What I'm looking for**:
- Using **Mixpanel OR Amplitude** (product analytics)
- **AND** using **LaunchDarkly OR Split.io** (feature flags)
- **AND** using **FullStory, LogRocket, OR Hotjar** (session replay)
- Bonus: Also using separate A/B testing tool (Optimizely, VWO)

### Why This is #2

#### 1. **Budget is Already Allocated**
This is the most important point: **They're already paying for this category.**

**Typical costs**:
- Mixpanel: $24k-60k/year (depends on volume)
- LaunchDarkly: $20k-50k/year
- FullStory: $15k-40k/year
- **Total**: $60k-150k/year on tools PostHog replaces

**What this means**:
- Not a new budget request - it's a **reallocation**
- CFO already approved spending in this category
- Just need to prove PostHog is better/cheaper than current stack
- Way easier conversation than "find new budget"

#### 2. **The Pain is Active and Experienced**
They're not imagining pain - **they're living it every day**:

**Daily Experience**:
- Product manager sees a funnel drop-off in Mixpanel
- "Why are users dropping off?"
- Need to jump to FullStory to watch session replays
- FullStory doesn't connect to Mixpanel data
- Manual work: Filter by same user cohort, find sessions, watch 10+ sessions
- **15-30 minutes wasted** to get context

**Weekly Experience**:
- Engineering wants to test a new feature with a flag
- Toggle flag in LaunchDarkly
- Check impact in Mixpanel
- **No automatic connection** between flag variants and metrics
- Manual analysis: Export data, join in SQL, analyze
- **Hours wasted** per experiment

**Monthly Experience**:
- Finance asks: "What are we spending on analytics tools?"
- VP Eng realizes: "We're paying $120k/year across 4 different tools"
- "And we still can't get fast answers to product questions"
- **Frustration builds**

#### 3. **Clear, Quantifiable ROI**
This is the easiest ROI story to tell:

**Current State**:
- $120k/year across multiple tools
- 10 hours/week of context switching (@ $75/hr loaded cost = $39k/year)
- **Total cost**: $159k/year

**PostHog State**:
- $60k/year (one platform, all features)
- 2 hours/week of context switching (@ $75/hr = $7.8k/year)
- **Total cost**: $67.8k/year

**Savings**: $91k/year + faster insights + better decisions

**CFO loves this math.**

#### 4. **High Switching Propensity**
Companies using multiple tools are already frustrated:

**Common complaints** (from G2 reviews, Reddit, etc.):
- "Too many tools to manage"
- "Data doesn't connect between tools"
- "Expensive and getting worse every year"
- "Support is slow across multiple vendors"

**They're already looking for a better solution**, they just haven't found PostHog yet.

### How to Research This

**Step 1: Detect Tech Stack (2-3 minutes)**

**Sources**:
- **BuiltWith** (most reliable, shows JS libraries on site)
- **Clearbit Reveal** (shows firmographic + some tech data)
- **Wappalyzer** browser extension (manual check)
- **LinkedIn job posts** (sometimes mention tools: "Experience with Mixpanel preferred")
- **Engineering blog** (often mentions tools they use)

**What to capture**:
- Which analytics tool: "Mixpanel"
- Which feature flag tool: "LaunchDarkly"
- Which session replay tool: "FullStory"
- Date last detected: (recent = still using it)

**Pro tip**: If BuiltWith shows Segment, they're probably sending data to multiple downstream tools. Check what Segment destinations they have.

**Step 2: Estimate Their Costs (1-2 minutes)**

**Use public pricing + company size**:

Company with **100 employees, 500k monthly users**:
- Mixpanel Growth plan: ~$40k/year (based on event volume)
- LaunchDarkly Pro: ~$35k/year (based on seats)
- FullStory Business: ~$30k/year (based on sessions)
- **Total**: ~$105k/year

**Why this matters**: You can lead with "you're probably spending $100k+/year on analytics tools..."

**Step 3: Find Evidence of Pain (3-5 minutes)**

**Sources**:
- **LinkedIn posts** from their team: Search "from:[company] (data OR analytics OR experiments)"
- **Engineering blog**: Search blog for "how we experiment" or "analytics infrastructure"
- **G2 reviews**: Check if they left reviews of current tools (complaints = pain)
- **Job descriptions**: "Manage our analytics stack" in job posts = complex stack to maintain

**What to look for**:
- Complaints about "context switching" or "tool sprawl"
- Hiring "Analytics Engineer" (means they need someone to manage integrations)
- Blog posts about "building our data infrastructure" (pain!)

**Why this matters**: Lets you reference specific pain in your outreach.

### The Outreach Message

**Subject**: Quick q re: Mixpanel + LaunchDarkly + FullStory

**Body**:
```
Hey [Name],

Noticed you're using Mixpanel for analytics, LaunchDarkly for
feature flags, and FullStory for session replay.

Quick question: When you see something interesting in Mixpanel
(like a funnel drop-off), what's your current process for
understanding *why* it happened?

I ask because most teams we talk to at your scale (~100 engineers)
say the context-switching between tools is one of their biggest
velocity killers. Hypothesis → experiment → analyze takes days
instead of hours because data lives in 3 different places.

[Similar Company] was in the same spot - Mixpanel + LD + FullStory.
They consolidated everything into PostHog and cut their tool costs
by 40% while getting faster insights.

Worth a quick look at what they did? I can show you exactly how
they set it up and the ROI math.

Best,
[Your name]
```

**Why this works**:
- ✅ Shows you know their exact stack (research!)
- ✅ Asks about specific pain point they definitely experience
- ✅ Quantifies the pain (velocity killer)
- ✅ Clear value prop (consolidation + cost savings)
- ✅ Social proof with similar company
- ✅ Low-friction CTA

### Time Investment vs. Return

**Research time per company**: 6-8 minutes
**Outreach time**: 4-5 minutes
**Total time**: 10-13 minutes per company

**Expected return**:
- Reply rate: **25-35%** (high because pain is real and current)
- Meeting rate: **15-20%**
- Opportunity rate: **12-15%** (high because budget exists)

---

## Trigger #3: Engineering Leader Posted on LinkedIn About Product Velocity/Data Challenges (Last 30 Days)

### The Signal
**What I'm looking for**:
- **CTO, VP Engineering, or Head of Product** posted on LinkedIn
- **Within last 30 days** (not older - momentum matters)
- Post mentions **one of these topics**:
  - "Product velocity", "shipping faster", "iteration speed"
  - "Data-driven decisions", "analytics", "experimentation"
  - "Team scaling challenges", "maintaining quality at scale"
  - "Engineering productivity", "developer experience"

### Why This is #3

#### 1. **Top of Mind = Perfect Timing**
If someone publicly posts about a problem, **that problem is occupying significant mental space.**

**Psychology**:
- They've been thinking about this issue for weeks/months
- Frustrated enough to post about it publicly
- Probably discussed internally multiple times
- Looking for solutions (consciously or subconsciously)

**When someone posts "We need to ship faster but not break things," they're literally telling you their pain point.**

#### 2. **Social Proof of Caring**
By posting on LinkedIn, they're signaling:
- This topic matters to their professional identity
- They think about product/engineering excellence
- They're engaged with their craft (not coasting)
- They value thought leadership in this area

**These are exactly the kind of buyers PostHog wants** - people who care about craft, quality, and shipping great products.

#### 3. **Built-In Conversation Starter**
The post gives you a natural, non-salesy way to start a conversation:

**BAD**: "Hi, I saw you're a VP of Engineering, want to see a demo?"

**GOOD**: "Loved your post on maintaining velocity as you scale - we see this exact challenge with a lot of engineering leaders. How are you approaching [specific thing from post]?"

**It's not cold outreach, it's engaging with their content.** Different vibe entirely.

#### 4. **Direct Line to Decision Maker**
You're reaching out to the **actual decision maker** (CTO, VP Eng), not a product manager or engineer who has to convince others.

**Decision-making power**:
- CTOs/VPs can say "yes, let's buy this" or "yes, let's start a trial"
- They control budget for engineering tools
- They set the vision for engineering infrastructure

**One conversation = access to the decision maker.** No need to multi-thread (initially).

#### 5. **Low Competition**
Most BDRs don't do this because:
- Takes effort to monitor LinkedIn
- Requires reading and understanding the post
- Needs custom messaging (can't template easily)

**This means less inbox noise.** They might get 10 sales emails/day, but only 1-2 thoughtful replies to their LinkedIn posts.

### How to Research This

**Step 1: Find the Posts (5-10 minutes per day)**

**Method A: LinkedIn Search**

Use LinkedIn search operators:
```
from:CTO OR from:"VP Engineering" OR from:"Head of Product"
(velocity OR analytics OR experimentation OR shipping OR data-driven)
```

**Filters**:
- Posted: Past Week (check daily) or Past Month (check weekly)
- Industry: Computer Software, Internet, B2B
- Location: Your target regions

**Method B: LinkedIn Sales Navigator**

If you have Sales Navigator:
- Lead search → filters by title
- Save search: "CTOs posting about product"
- Get alerts when new posts match

**Method C: Manual Monitoring**

- Build a list of 50-100 target CTOs/VPs
- Check their LinkedIn profiles weekly
- Set up alerts for their activity

**What to capture**:
- Exact text of the post
- Engagement (comments, likes - higher = more important to them)
- Comments from their team (shows it's an organizational issue, not just personal)
- Date posted

**Step 2: Understand the Context (5-7 minutes)**

Read the post carefully:

**Ask yourself**:
- What **specific problem** are they describing?
- What **solution** are they currently trying (if mentioned)?
- What **outcome** do they want?
- What's the **underlying pain**?

**Example Post**:
> "We've 2x'd our eng team in the last 6 months. The good: we're shipping more features. The challenge: experiments that used to take 2 days now take 2 weeks. Too much coordination overhead between product, eng, and data. Need to figure this out."

**Your analysis**:
- Problem: Experiment velocity has slowed down
- Current solution: Unclear (maybe manual coordination)
- Desired outcome: Fast experiments despite team growth
- Underlying pain: Coordination overhead, tool friction

**Step 3: Research the Company (3-5 minutes)**

Now that you know the person is interested, research their company:

- Company size and growth
- Recent funding (if any)
- Current tech stack (use BuiltWith)
- Job postings (confirming they're scaling)
- Engineering blog (to understand culture)

**Step 4: Find the Connection to PostHog (2 minutes)**

How does PostHog solve their specific problem?

**Their Pain** → **PostHog Solution**:
- "Experiments take too long" → Feature flags + built-in experimentation
- "Too many tools" → All-in-one platform
- "Data access too slow" → Self-serve analytics for engineers
- "Can't see why users behave X way" → Integrated session replay

**Step 5: Craft Custom Response (5-10 minutes)**

This needs to be genuinely custom, not a template.

### The Outreach Message

**IMPORTANT**: First, engage on LinkedIn itself (not email).

**Step 1: Comment on the Post**

```
This resonates! We've heard this exact challenge from a lot of
engineering leaders around the 50-100 engineer mark. What we've
seen work well: giving engineers self-serve access to experimentation
+ analytics in one tool, so they don't need to coordinate with data
teams for every question. Curious - is the slowdown more on the
setup side or the analysis side?
```

**Why**: Public engagement first shows you're genuine, not just selling.

**Step 2: Send LinkedIn DM (Next Day)**

```
Hey [Name],

Loved your post on experiment velocity slowing down as you scale -
that's such a common challenge and most teams don't talk about it
openly.

I commented yesterday, but wanted to reach out directly because
this is literally the exact problem PostHog was built to solve.
We work with a lot of engineering-led teams at your scale (~100 engineers)
who hit the same wall.

The core issue is usually that experimentation workflows are spread
across too many tools (feature flags in LD, analytics in Mixpanel,
qualitative feedback somewhere else). Every experiment requires
coordination across 3+ tools and 2+ teams.

[Similar Company's CTO] had the same challenge. They consolidated
everything into PostHog and cut experiment time from 2 weeks to
2 days. Happy to show you exactly what they did.

15-min call to walk through it? I can share the before/after of
their workflow.

Best,
[Your name]
```

**Why this works**:
- ✅ References their specific post (shows it's custom)
- ✅ Validates their thinking (not dismissive)
- ✅ Directly addresses their stated problem
- ✅ Offers specific solution + proof
- ✅ Low-friction CTA

### Time Investment vs. Return

**Research time per company**: 15-20 minutes (higher than other triggers)
**Outreach time**: 7-10 minutes (highly custom)
**Total time**: 22-30 minutes per company

**Expected return**:
- Reply rate: **40-50%** (very high - you're engaging with their content)
- Meeting rate: **20-25%** (they want to talk about the problem)
- Opportunity rate: **10-15%** (high intent)

**Math**:
- 8 companies researched per day (30 min each)
- 8 × 45% reply rate = 3-4 replies/day
- 3-4 × 22% meeting rate = ~1 meeting/day
- 1 meeting × 12% opp rate = 1-2 opps/week from this approach

**This is the highest-quality pipeline** but requires the most effort.

---

## Why These 3 Triggers (and Not Others)?

### What Makes a Great Trigger?

**The Trigger Evaluation Framework**:

| Criteria | Trigger #1 (Funding + Hiring) | Trigger #2 (Tool Sprawl) | Trigger #3 (LinkedIn Post) |
|----------|-------------------------------|--------------------------|----------------------------|
| **Budget Proven** | ✅ Just raised millions | ✅ Already paying $100k+/yr | ⚠️ Unknown |
| **Pain is Current** | ⚠️ About to feel it | ✅ Feeling it daily | ✅ Top of mind |
| **Timing is Right** | ✅ 3-6 month window | ✅ Anytime (pain is constant) | ✅ Posted in last 30 days |
| **Decision Maker Access** | ⚠️ May need to multi-thread | ⚠️ May need to multi-thread | ✅ Direct to DM |
| **Research Difficulty** | ⚠️ Medium (5-7 min) | ⚠️ Medium (6-8 min) | 🔴 High (15-20 min) |
| **Volume Available** | ⚠️ ~50/month | ✅ ~500/month | 🔴 ~20-30/month |
| **Reply Rate** | 🎯 35% | 🎯 30% | 🎯 45% |

**Key Insights**:
- **Trigger #1** = Best balance of timing + budget
- **Trigger #2** = Highest volume + proven budget
- **Trigger #3** = Highest intent + quality, lowest volume

### Triggers I Considered But Rejected

**❌ Recently left a bad review of a competitor**
- **Why I didn't choose it**: Low volume (not many people leave public reviews), hard to find consistently

**❌ Visited PostHog website multiple times (intent signal)**
- **Why I didn't choose it**: Requires marketing automation + website tracking already set up. Also, warm leads should be handled differently (faster response, different messaging).

**❌ Hired a new CTO/VP Engineering in last 90 days**
- **Why I didn't choose it**: New execs spend first 90 days learning, not buying. Better to wait until 90-180 days in when they want to make their mark.

**❌ Company hit 100 employees (milestone)**
- **Why I didn't choose it**: Not painful enough yet. 100 → 200 is the real pain point, hard to time.

**❌ Using free tier of competitor (Amplitude free, Mixpanel free)**
- **Why I didn't choose it**: Usually means low budget, not ready to pay $20k+. Better for self-serve motion.

---

## Practical Daily Workflow Using These 3 Triggers

### Monday Morning (2 hours)
**Goal**: Build this week's target list

1. **Run Trigger #1 searches** (30 min)
   - Crunchbase: Companies that raised Series B+ in last 3 months
   - Cross-reference: Which ones are hiring 3+ engineers?
   - Output: ~10 companies

2. **Run Trigger #2 searches** (45 min)
   - BuiltWith: Companies using Mixpanel + LaunchDarkly + session replay
   - Filter: ICP companies (50-500 employees, B2B SaaS)
   - Output: ~30 companies

3. **Check Trigger #3** (45 min)
   - LinkedIn: Search for posts from CTOs/VPs in last week
   - Filter for relevant topics
   - Output: ~5-10 posts

**Total targets for the week**: 45-50 companies

### Monday Afternoon - Thursday (6 hours/day outreach)
**Goal**: Research + reach out

**Priority order**:
1. **Trigger #3 first** (highest reply rate, time-sensitive)
   - 2 hours/day = 4-5 companies deeply researched + custom outreach

2. **Trigger #1 second** (high intent, good timing)
   - 2 hours/day = 10-12 companies researched + outreach

3. **Trigger #2 third** (volume play)
   - 2 hours/day = 10-12 companies researched + outreach

### Friday (Measurement & Learning)
**Goal**: Analyze results, refine approach

- Review reply rates by trigger
- Read all replies and objections
- Refine messaging based on what's working
- Plan next week's searches

---

## The Bottom Line

If I were a PostHog BDR and could only focus on 3 triggers, these are the ones I'd choose because:

1. **Trigger #1 (Funding + Hiring)**: Perfect timing + proven budget = high conversion
2. **Trigger #2 (Tool Sprawl)**: Current pain + budget allocated = easy ROI story
3. **Trigger #3 (LinkedIn Posts)**: Top of mind + direct to DM + low competition = highest quality

**Combined expected results**:
- 45-50 new companies researched per week
- 15-18 replies per week (30-35% avg reply rate)
- 3-5 meetings booked per week
- 2-3 opportunities created per week

**That's 8-12 opportunities per month, just from these 3 triggers.**

At PostHog's ACV, that's $160k-1.2M in pipeline per month from one BDR. 🚀
