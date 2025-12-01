# PostHog Lead Qualification Checklist
## Hard Disqualifiers & Priority Order for Fast Filtering

> **Purpose**: Save time by identifying poor fits in 60 seconds or less. Check these criteria in order before investing research time.

---

## The Philosophy: Disqualify Fast, Research Deep

**The Problem**: Most BDRs waste hours researching companies that never had a chance.

**The Solution**: A **3-tier qualification filter** that takes 60 seconds to eliminate 70% of poor fits.

```
100 Raw Leads
    ↓
Tier 1: Hard Disqualifiers (10 seconds)
    ↓ 60 leads pass
Tier 2: ICP Fit Check (30 seconds)
    ↓ 35 leads pass
Tier 3: Budget & Authority (20 seconds)
    ↓ 25 qualified leads
    ↓
THEN: Deep research & personalization
```

---

## TIER 1: Hard Disqualifiers (10 seconds)
### Check These FIRST - Instant "No"

These are non-negotiable. If they fail ANY of these, **stop immediately and move to next lead**.

---

### ❌ DISQUALIFIER #1: Company Size Outside Range

**The Rule**: Must be **15-500 employees**

**Why this matters**:
- **<15 employees**: Too small, likely <$20k budget, self-serve motion
- **>500 employees**: Too big, slow enterprise sales cycle, different sales motion

**How to check** (5 seconds):
- LinkedIn company page: Shows employee count
- Clearbit: Shows employee range
- Company website "About" page

**Immediate action**:
- <15 employees → Skip (unless extremely high-value use case)
- 15-500 employees → Continue to next check ✅
- >500 employees → Tag for enterprise motion (different team)

**Example**:
- ❌ 8-person startup → Skip
- ✅ 120-person company → Continue
- ⚠️ 800-person company → Pass to enterprise team

---

### ❌ DISQUALIFIER #2: Wrong Buyer Persona (Marketing-Led)

**The Rule**: **Engineering or Product** must be primary buyer, NOT marketing

**Why this matters**:
- PostHog is built for engineers/product teams
- Marketing-led buyers want different features (attribution, campaign tracking)
- If marketing is driving the decision, you'll lose to Amplitude/Mixpanel

**How to check** (3 seconds):
- Look at their LinkedIn: Is your contact in Marketing?
- Check job postings: All marketing analysts, no product engineers?
- Website positioning: Pure B2C/marketing analytics focus?

**Red flags**:
- Contact title: "Head of Marketing Analytics", "Marketing Operations"
- Company type: E-commerce, pure consumer apps (not B2B)
- Use case: "We want to track our ad campaigns"

**Immediate action**:
- Marketing is primary buyer → Skip ❌
- Engineering/Product is buyer → Continue ✅
- Mixed (both involved) → Continue but note risk ⚠️

**Example**:
- ❌ E-commerce brand wanting to track Facebook ads → Skip
- ✅ B2B SaaS with product engineers → Continue
- ⚠️ B2C app but engineers make tool decisions → Continue with caution

---

### ❌ DISQUALIFIER #3: Industry Misfit

**The Rule**: Must be **tech/software company or tech-enabled business**

**Why this matters**:
- PostHog's value prop resonates with technical, product-focused teams
- Traditional industries (retail, manufacturing, etc.) don't have product engineers
- Different buying motion, different pain points

**How to check** (2 seconds):
- LinkedIn industry tag
- Company description
- What do they build/sell?

**Green light industries**:
- ✅ B2B SaaS
- ✅ Developer tools
- ✅ Fintech
- ✅ Digital health
- ✅ Marketplace/platform
- ✅ Tech-enabled services

**Red light industries**:
- ❌ Traditional retail (not e-commerce)
- ❌ Manufacturing
- ❌ Consulting/services (no product)
- ❌ Traditional finance/insurance
- ❌ Hospitality

**Immediate action**:
- Wrong industry → Skip ❌
- Tech/tech-enabled → Continue ✅

---

## TIER 2: ICP Fit Check (30 seconds)
### If They Passed Tier 1, Check These Next

---

### 🟡 CHECKPOINT #4: Funding Stage

**The Ideal**: **Series A to Pre-IPO** (Series B+ is sweet spot)

**Why this matters**:
- Pre-seed/Seed: Usually too early, no budget for $20k+ tool
- Series A: Starting to be viable
- Series B-D: Perfect (have PMF, scaling, have budget)
- Post-IPO/Public: Different motion, move to enterprise team

**How to check** (10 seconds):
- Crunchbase (free info): Last funding round
- LinkedIn company page: Sometimes shows funding
- Company website footer: Often shows "Series B-backed by X"

**Scoring**:
- Pre-seed/Seed → ❌ Skip (too early)
- Series A → ⚠️ Marginal (need strong signals elsewhere)
- Series B-D → ✅ Perfect
- Post-IPO → ⚠️ Pass to enterprise team
- Bootstrapped/Profitable → ✅ Continue (check revenue signals)

**Exception**: Bootstrapped companies CAN work if they show other strong signals (500+ employees, clear revenue, hiring aggressively).

---

### 🟡 CHECKPOINT #5: Engineering Team Size

**The Ideal**: **10+ engineers** (more engineers = higher value)

**Why this matters**:
- <10 engineers: Can probably get by with basic tools
- 10-30 engineers: Starting to feel pain
- 30-100 engineers: Sweet spot, high pain
- 100+ engineers: Complex needs, high value

**How to check** (10 seconds):
- LinkedIn: Search "[Company Name] software engineer" → see how many results
- Job postings: How many engineering roles open?
- Company website: Team page or engineering blog

**Quick estimate formula**:
- Total employees × 0.3 = rough engineering headcount for B2B SaaS
- 100 total employees → ~30 engineers

**Scoring**:
- <10 engineers → ❌ Skip (too small)
- 10-30 engineers → ⚠️ Marginal
- 30-100 engineers → ✅ Sweet spot
- 100+ engineers → ✅ Continue but may need enterprise approach

---

### 🟡 CHECKPOINT #6: Product Complexity

**The Question**: Do they have a **digital product** that requires analytics/experiments?

**Why this matters**:
- No product = no need for product analytics
- Simple product = basic needs (can use free tools)
- Complex product = high need for sophisticated analytics

**How to check** (10 seconds):
- What does the company actually build?
- Is it a web app? Mobile app? Platform?
- Or is it services/consulting?

**Green flags**:
- ✅ SaaS application
- ✅ Mobile app
- ✅ Developer tools/API
- ✅ Marketplace/platform
- ✅ Consumer app with product features

**Red flags**:
- ❌ Pure services business (no product)
- ❌ Static website/content business
- ❌ E-commerce only (just selling products, not building product features)

**Immediate action**:
- No digital product → ❌ Skip
- Simple product + small team → ❌ Skip
- Complex product → ✅ Continue

---

## TIER 3: Budget & Authority (20 seconds)
### Final Checks Before Deep Research

If they've passed Tier 1 and Tier 2, now check if there's a path to $20k+/year and if you can reach decision makers.

---

### 💰 CHECKPOINT #7: Budget Signals ($20k+/year Minimum)

**The Rule**: Must be able to afford **$20k+/year** (PostHog's sales threshold)

**Why this matters**:
- Below $20k → Self-serve handles them (not worth sales time)
- $20k-60k → Good fit for sales
- $60k+ → Great fit, higher priority

**How to check** (10 seconds):

**Proxy #1: Revenue Estimation**
- Need $100k+/month revenue (~$1.2M/year) to afford $20k/year tool
- VC-backed Series B+ usually qualifies
- Bootstrapped: Check for "We're hiring" + 50+ employees

**Proxy #2: Current Tool Spend**
- If using Mixpanel/Amplitude/LaunchDarkly → already spending $20k+
- If using Google Analytics free → probably not ready

**Proxy #3: Funding Amount**
- Raised $10M+ total → probably have budget
- Raised <$3M total → probably too early

**Quick decision tree**:
```
Series B+ with 50+ employees → ✅ Has budget
Using paid competitors → ✅ Has budget
Hiring aggressively (10+ open roles) → ✅ Has budget
Series A with <30 employees → ❌ Probably too small
Using only free tools + small team → ❌ No budget
```

---

### 👤 CHECKPOINT #8: Access to Decision Maker

**The Question**: Can you reach someone with **buying authority** (or close to it)?

**Why this matters**:
- If you can't reach the decision maker, the deal stalls
- PostHog's buyers: CTO, VP Eng, Head of Product, sometimes CEO

**How to check** (10 seconds):
- LinkedIn: Can you find CTO/VP Engineering profile?
- Can you find their email? (Apollo, RocketReach, etc.)
- Are they active on LinkedIn? (If yes, easier to reach)

**Decision maker hierarchy** (from best to worst):

**Tier A (Can sign $20k-100k+ deal)**:
1. CTO
2. VP Engineering
3. VP Product
4. CEO/Founder (at smaller companies)

**Tier B (Strong influence, might need approval)**:
5. Head of Engineering
6. Engineering Manager (at 50+ person companies)
7. Head of Product

**Tier C (User/Champion, can't sign)**:
8. Product Manager
9. Product Engineer
10. Data Analyst

**Immediate action**:
- Can reach Tier A decision maker → ✅ Continue
- Only found Tier C contacts → ⚠️ Note: Will need to multi-thread up
- Can't find any relevant contacts → ❌ Skip (or add to long-term nurture)

---

## The 60-Second Qualification Workflow

**Time per lead**: 60 seconds max

### Step 1: Tier 1 Hard Disqualifiers (10 sec)
1. Check LinkedIn company page
2. Employee count: 15-500? ✅/❌
3. Industry: Tech/tech-enabled? ✅/❌
4. Your contact: Engineering/Product? ✅/❌

**If ANY are ❌ → Skip immediately**

### Step 2: Tier 2 ICP Fit (30 sec)
5. Quick Crunchbase check: Series A+? ✅/⚠️/❌
6. Estimate eng team: 10+ engineers? ✅/⚠️/❌
7. Digital product exists? ✅/❌

**If mostly ❌ → Skip. If mostly ✅ → Continue**

### Step 3: Tier 3 Budget & Authority (20 sec)
8. Budget signals: Revenue/funding/current tools? ✅/⚠️/❌
9. Can you find CTO/VP Eng on LinkedIn? ✅/❌

**If both ✅ → QUALIFIED. Proceed to deep research.**

---

## Real Examples: Fast Qualification in Action

### Example 1: Quick Disqualify (10 seconds)

**Company**: Jane's Marketing Agency
- Check LinkedIn: 8 employees ❌ (too small)
- **STOP** → Skip

**Time spent**: 10 seconds

---

### Example 2: Marginal Fit (45 seconds)

**Company**: Acme E-commerce
- Employees: 120 ✅
- Industry: E-commerce ⚠️ (consumer-focused)
- Contact: Head of Growth Marketing ❌ (marketing-led)
- **STOP** → Wrong buyer persona

**Time spent**: 45 seconds

---

### Example 3: Strong Qualification (60 seconds)

**Company**: Vercel (example)
- Employees: 150 ✅
- Industry: B2B SaaS, developer tools ✅
- Your contact: VP Engineering ✅
- Funding: Series B, $100M ✅
- Eng team: ~50 engineers ✅
- Product: Complex developer platform ✅
- Budget: Currently using Amplitude + LaunchDarkly ✅
- Decision maker: Can find CTO on LinkedIn ✅

**QUALIFIED** → Proceed to deep research (triggers, personalization, etc.)

**Time spent**: 60 seconds

---

## Qualification Scoring Shortcut

If you want a **simple points-based system** for quick qualification:

| Criteria | Points | Your Check |
|----------|--------|------------|
| **15-500 employees** | 3 pts | ___/3 |
| **Engineering/Product buyer** | 3 pts | ___/3 |
| **Tech industry** | 2 pts | ___/2 |
| **Series A+ funding** | 2 pts | ___/2 |
| **10+ engineers** | 2 pts | ___/2 |
| **Complex digital product** | 2 pts | ___/2 |
| **$20k+ budget signals** | 3 pts | ___/3 |
| **Can reach decision maker** | 3 pts | ___/3 |
| **TOTAL** | **20 pts** | **___/20** |

**Scoring**:
- **15-20 points**: ✅ Qualified - proceed to research
- **10-14 points**: ⚠️ Marginal - need strong trigger to pursue
- **<10 points**: ❌ Not qualified - skip

---

## Common Objections & How to Handle Them

### "But they're a big brand name, shouldn't we try anyway?"

**Answer**: Brand name ≠ good fit.

**Example**: Nike has 75,000 employees but:
- ❌ >500 employees (enterprise motion)
- ❌ Not a tech company (traditional retail)
- ❌ Marketing-led buyers (not product engineers)

**Better to spend time** on a 150-person B2B SaaS company with engineers making decisions.

---

### "What if they're at 14 employees but just raised a Series B?"

**Answer**: Series B at 14 employees is unusual but signals high value per employee.

**Decision**: Make an exception - the funding signal is strong enough. But verify:
- Check if they're **hiring aggressively** (signal of growth)
- Check **recent revenue news** (are they growing fast?)
- If yes → Proceed to qualify

---

### "They're using Google Analytics free tier - does that mean no budget?"

**Answer**: Not necessarily, but it's a yellow flag.

**Decision tree**:
- GA free + Series B+ + hiring → ⚠️ Might be ready to upgrade (proceed)
- GA free + Series A + small team → ❌ Probably too early
- GA free + bootstrapped + large team → ⚠️ Might have budget (check other signals)

---

## Integration with Trigger Research

**Important**: Only research triggers (funding, hiring, tech stack, LinkedIn posts) AFTER a lead passes all 3 qualification tiers.

**The efficient workflow**:
```
1. Raw lead comes in (60 sec)
   ↓
2. Run through 3-tier qualification (60 sec)
   ↓
3. If qualified → Research triggers (10-20 min)
   ↓
4. If triggers present → Craft personalized outreach (5-10 min)
   ↓
5. Send message
```

**Don't waste 20 minutes researching a 10-person company** that fails Tier 1.

---

## Qualification Checklist Template (Copy This)

Use this for each new lead:

```
COMPANY: _________________________
CONTACT: _________________________

TIER 1: HARD DISQUALIFIERS (10 sec)
□ Employee count: 15-500? Y/N
□ Tech/tech-enabled industry? Y/N
□ Engineering/Product buyer? Y/N
→ ALL must be YES to continue

TIER 2: ICP FIT (30 sec)
□ Funding: Series A+? Y/N/Bootstrap
□ Engineering team: 10+? Y/N
□ Complex digital product? Y/N
→ Mostly YES to continue

TIER 3: BUDGET & AUTHORITY (20 sec)
□ Budget signals present? Y/N
□ Can reach decision maker? Y/N
→ Both YES to continue

QUALIFICATION DECISION:
□ ✅ QUALIFIED → Proceed to trigger research
□ ⚠️ MARGINAL → Need very strong trigger
□ ❌ NOT QUALIFIED → Skip

NOTES:
_________________________________
_________________________________
```

---

## Key Takeaways

### The 3 Most Important Disqualifiers (Check First):

1. **Company size outside 15-500 employees** → Instant skip
2. **Marketing-led buyer** (not engineering/product) → Instant skip
3. **No $20k+ budget signals** → Instant skip

### The Efficiency Rule:

**Spend 60 seconds to qualify, 20 minutes to research.**

NOT: 20 minutes to research, then realize they're not qualified.

### The Mindset Shift:

❌ Old way: "This company looks interesting, let me research them"
✅ New way: "Does this company pass my filters? No? Next."

**You're not looking for reasons to pursue. You're looking for reasons to disqualify.**

The faster you disqualify poor fits, the more time you have for high-quality leads.

---

## What To Do With Disqualified Leads

Don't just delete them - categorize:

**Bucket 1: Too Small (Now)**
- <15 employees but good fit otherwise
- Add to 6-month follow-up list
- Check back when they grow

**Bucket 2: Wrong Buyer**
- Marketing-led, but company is otherwise good
- Try to find engineering contacts
- Multi-thread into product/eng team

**Bucket 3: No Budget (Yet)**
- Good ICP but too early stage
- Add to nurture campaign
- Check back after next funding round

**Bucket 4: Truly Not a Fit**
- Wrong industry, no product, etc.
- Remove from list entirely
- Don't waste future time

---

## Bottom Line

**Before investing ANY research time, ask**:

1. Are they 15-500 employees?
2. Is engineering/product the buyer?
3. Can they afford $20k+/year?

If all three are YES → Proceed.

If ANY are NO → Skip.

**It's not about finding reasons to reach out. It's about finding reasons NOT to waste time.**

Qualify fast. Research deep. Win deals.
