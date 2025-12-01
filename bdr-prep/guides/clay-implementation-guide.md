# Clay Implementation Guide: PostHog Qualification Funnel
## Step-by-Step Setup for the 60-Point Scoring System

> **Goal**: Build a Clay workflow that automatically scores leads, enriches them with web data, and generates personalized messaging hooks.

---

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Table 1: Lead Enrichment & Scoring](#table-1-lead-enrichment--scoring)
3. [Table 2: Contact Discovery](#table-2-contact-discovery)
4. [Table 3: Personalization Engine](#table-3-personalization-engine)
5. [Integration & Automation](#integration--automation)

---

## Prerequisites

### Required Clay Credits/Integrations
- **Clearbit** (primary enrichment)
- **Crunchbase** (funding data)
- **BuiltWith** (tech stack)
- **LinkedIn** (people & jobs data)
- **Apollo** or **RocketReach** (contact finding)
- **OpenAI/Anthropic** (AI personalization)
- **HubSpot/Salesforce** (CRM integration)

### Data Sources You'll Need
- List of target companies (domains or LinkedIn URLs)
- Or: Import from existing CRM
- Or: Build from LinkedIn Sales Navigator export

---

## Table 1: Lead Enrichment & Scoring

### Purpose
Take raw company data and output scored, qualified leads with messaging hooks.

### Table Structure

#### Column 1: Company Input
**Type**: Import or Manual Entry
- **Data**: Company domain (e.g., `stripe.com`)
- **Or**: LinkedIn company URL

#### Column 2: Clearbit Company Enrichment
**Integration**: Clearbit Company API
**Settings**:
- Input: `{{Company Domain}}`
- Waterfall: Yes (if Clearbit fails, use People Data Labs)

**Key Fields to Extract**:
- Company name
- Domain
- Industry
- Employee count (range)
- Estimated revenue
- Founded year
- Location (HQ city, country)
- Company type (private/public)
- Tech stack (if available)
- Description

**Formula Column - Company Size Score**:
```javascript
// Score for 15-500 employees
if (clearbit.employees >= 15 && clearbit.employees <= 500) {
  return 3;
} else {
  return 0;
}
```

**Formula Column - Founded Date Score**:
```javascript
// Score for 2015-2022 founding
const year = new Date(clearbit.foundedYear).getFullYear();
if (year >= 2015 && year <= 2022) {
  return 3;
} else {
  return 0;
}
```

**Formula Column - Company Type Score**:
```javascript
// Score for private company
if (clearbit.type === "private") {
  return 3;
} else {
  return 0;
}
```

**Formula Column - Geography Score**:
```javascript
// Score for favorable geography
const goodCountries = ["United States", "United Kingdom", "Germany", "France", "Canada", "Netherlands"];
if (goodCountries.includes(clearbit.country)) {
  return 3;
} else {
  return 0;
}
```

#### Column 3: Crunchbase Funding Data
**Integration**: Crunchbase
**Settings**:
- Input: `{{Company Domain}}` or `{{Company Name}}`
- Waterfall: Yes (try domain first, then name)

**Key Fields to Extract**:
- Total funding amount
- Last funding date
- Last funding round (Seed, Series A, B, C, etc.)
- Last funding amount
- Investor names (array)
- Number of funding rounds

**Formula Column - Recent Funding Score**:
```javascript
// Score for funding in last 6-12 months
const lastFundingDate = new Date(crunchbase.lastFundingDate);
const monthsSinceFunding = (Date.now() - lastFundingDate) / (1000 * 60 * 60 * 24 * 30);

if (monthsSinceFunding <= 12 && ["Series B", "Series C", "Series D"].includes(crunchbase.lastFundingRound)) {
  return 5;
} else {
  return 0;
}
```

**Formula Column - Top Investor Score**:
```javascript
// Score for top-tier investors
const topInvestors = [
  "Sequoia Capital", "Andreessen Horowitz", "Y Combinator",
  "Accel", "Benchmark", "Greylock Partners", "Kleiner Perkins",
  "Founders Fund", "Index Ventures", "Bessemer Venture Partners"
];

const hasTopInvestor = crunchbase.investors.some(inv =>
  topInvestors.some(top => inv.includes(top))
);

return hasTopInvestor ? 2 : 0;
```

**Formula Column - Revenue Growth Score**:
```javascript
// If revenue data available and showing growth
// This requires historical data - may need manual research or alternative source
// For now, use funding velocity as proxy

const fundingRounds = crunchbase.numberOfRounds;
if (fundingRounds >= 3 && lastFundingScore === 5) {
  return 3; // Growing fast enough to raise multiple rounds
} else {
  return 0;
}
```

**Formula Column - Runway Score**:
```javascript
// Estimate runway based on funding amount and company size
// Very rough heuristic
const lastRaise = crunchbase.lastFundingAmount;
const employees = clearbit.employees || 50;
const estimatedMonthlyBurn = employees * 10000; // $10k per employee rough estimate
const estimatedRunwayMonths = lastRaise / estimatedMonthlyBurn;

if (estimatedRunwayMonths >= 18) {
  return 2;
} else {
  return 0;
}
```

#### Column 4: LinkedIn Company Data
**Integration**: LinkedIn Company Scraper (via Apify or Phantombuster)
**Settings**:
- Input: `{{LinkedIn Company URL}}` (find first if needed)

**Key Fields to Extract**:
- Company LinkedIn URL
- Employee count (updated)
- Recent posts (last 10)
- Jobs posted (if accessible via scraper)

#### Column 5: Job Postings Scraper
**Integration**: Custom HTTP API or Greenhouse/Lever API
**Method**: Use Apify "LinkedIn Jobs Scraper" or custom scraper

**Settings**:
- Input: `{{Company Name}}` or `{{Company Domain}}`
- Search for: All active jobs

**Key Fields to Extract**:
- Total number of open roles
- Roles by department (Engineering, Product, Data, Growth)
- Specific role titles
- Date posted

**Formula Column - Hiring Engineers Score**:
```javascript
// Score for hiring product engineers
const engineeringRoles = jobPostings.filter(job =>
  job.title.match(/product engineer|software engineer|full stack|frontend|backend/i)
);

if (engineeringRoles.length >= 3) {
  return 5;
} else if (engineeringRoles.length >= 1) {
  return 3;
} else {
  return 0;
}
```

**Formula Column - Hiring Data/Analytics Score**:
```javascript
// Score for hiring data roles
const dataRoles = jobPostings.filter(job =>
  job.title.match(/data engineer|analytics engineer|data analyst|data scientist/i)
);

if (dataRoles.length >= 2) {
  return 3;
} else if (dataRoles.length >= 1) {
  return 2;
} else {
  return 0;
}
```

**Formula Column - Hiring Growth/Product Score**:
```javascript
// Score for hiring growth/product roles
const growthRoles = jobPostings.filter(job =>
  job.title.match(/product manager|growth|product lead/i)
);

if (growthRoles.length >= 2) {
  return 2;
} else if (growthRoles.length >= 1) {
  return 1;
} else {
  return 0;
}
```

#### Column 6: BuiltWith Tech Stack
**Integration**: BuiltWith API
**Settings**:
- Input: `{{Company Domain}}`

**Key Fields to Extract**:
- Detected technologies (array)
- Analytics tools
- Marketing tools
- Infrastructure

**Formula Column - Competitor Detection Score**:
```javascript
// Score for using PostHog competitors
const competitors = [
  "Mixpanel", "Amplitude", "Heap", "Google Analytics",
  "LaunchDarkly", "Split.io", "Optimizely", "VWO",
  "FullStory", "LogRocket", "Hotjar", "Crazy Egg"
];

const detectedCompetitors = builtwith.technologies.filter(tech =>
  competitors.some(comp => tech.name.includes(comp))
);

if (detectedCompetitors.length >= 1) {
  return 5;
} else {
  return 0;
}
```

**Formula Column - Multiple Tools Score**:
```javascript
// Score for using multiple point solutions PostHog replaces
if (detectedCompetitors.length >= 3) {
  return 2;
} else {
  return 0;
}
```

#### Column 7: Company Blog/Content Check
**Integration**: HTTP API or Web Scraper
**Settings**:
- Check for: `/blog` or `/engineering` on domain

**Formula Column - Engineering Blog Score**:
```javascript
// Check if engineering blog exists
const blogUrls = [
  `https://${domain}/blog`,
  `https://${domain}/engineering`,
  `https://blog.${domain}`,
  `https://engineering.${domain}`
];

// Would need to check HTTP status
// For Clay, use "Find URLs" or "HTTP Request" enrichment
if (engineeringBlogExists) {
  return 1;
} else {
  return 0;
}
```

#### Column 8: Recent Company News
**Integration**: Google Search API or News API
**Settings**:
- Query: `{{Company Name}} product launch OR funding OR update`
- Time range: Last 6 months

**Formula Column - Product Launch Score**:
```javascript
// Check for product launch mentions
const newsArticles = newsAPI.articles || [];
const hasProductLaunch = newsArticles.some(article =>
  article.title.match(/launch|release|announce|introduces/i)
);

if (hasProductLaunch) {
  return 2;
} else {
  return 0;
}
```

#### Column 9: LinkedIn Activity Check
**Integration**: Apify LinkedIn Post Scraper
**Settings**:
- Input: `{{LinkedIn Company URL}}`
- Limit: Last 10 posts

**Formula Column - Data/Analytics Posts Score**:
```javascript
// Check if company posts about data challenges
const recentPosts = linkedinPosts || [];
const dataRelatedPosts = recentPosts.filter(post =>
  post.text.match(/analytics|data|metrics|insights|experimentation|a\/b test/i)
);

if (dataRelatedPosts.length >= 1) {
  return 2;
} else {
  return 0;
}
```

#### Column 10: TOTAL SCORE CALCULATION
**Type**: Formula Column
**Name**: `Total Score`

```javascript
// Core ICP (24 points max)
const icpScore =
  companySizeScore +          // 3
  foundedDateScore +          // 3
  companyTypeScore +          // 3
  geographyScore;             // 3
  // Role score added in Table 2 (6 points)

// Financial (12 points max)
const financialScore =
  recentFundingScore +        // 5
  revenueGrowthScore +        // 3
  topInvestorScore +          // 2
  runwayScore;                // 2

// Pain (12 points max)
const painScore =
  hiringEngineersScore +      // 5
  hiringDataScore +           // 3
  hiringGrowthScore +         // 2
  productLaunchScore;         // 2

// Tech Stack (8 points max)
const techScore =
  competitorScore +           // 5
  multipleToolsScore +        // 2
  engineeringBlogScore;       // 1

// Behavioral (4 points max)
const behavioralScore =
  dataPostsScore +            // 2
  // communityActivityScore added in Table 3
  // reviewScore added in Table 3

const totalScore =
  icpScore +
  financialScore +
  painScore +
  techScore +
  behavioralScore;

return totalScore;
```

#### Column 11: Priority Tier
**Type**: Formula Column
**Name**: `Priority`

```javascript
if (totalScore >= 45) {
  return "🔥 Hot Lead";
} else if (totalScore >= 35) {
  return "⭐ Warm Lead";
} else if (totalScore >= 25) {
  return "💡 Qualified Lead";
} else if (totalScore >= 15) {
  return "❄️ Cold Lead";
} else {
  return "🚫 Poor Fit";
}
```

#### Column 12: Filter Row
**Type**: Filter
**Condition**: `{{Total Score}} >= 25`

This ensures only qualified leads pass to the next table.

#### Column 13: Generate Messaging Hooks
**Type**: AI Formula (GPT-4 or Claude)
**Prompt**:

```
You are a BDR writing personalized outreach for PostHog, an all-in-one product analytics platform.

Company: {{Company Name}}
Industry: {{clearbit.industry}}
Employees: {{clearbit.employees}}
Recent Funding: {{crunchbase.lastFundingRound}} - ${{crunchbase.lastFundingAmount}} ({{crunchbase.lastFundingDate}})
Investors: {{crunchbase.investors}}
Hiring For: {{jobPostings.titles}}
Tech Stack: {{builtwith.technologies}}
Recent News: {{newsAPI.headlines}}

Generate 3 personalized messaging hooks (1-2 sentences each) that:
1. Reference a specific signal from their company
2. Connect it to a pain point PostHog solves
3. Feel natural and conversational

Format as JSON:
{
  "hook1": "...",
  "hook2": "...",
  "hook3": "..."
}
```

---

## Table 2: Contact Discovery

### Purpose
Find decision-makers at qualified companies and enrich with role-specific scoring.

### Input
Qualified companies from Table 1 (score >= 25)

### Table Structure

#### Column 1: Import from Table 1
**Type**: Import Table
- Select Table 1
- Import all rows with score >= 25

#### Column 2: Find People - Apollo
**Integration**: Apollo.io People Search
**Settings**:
- Company domain: `{{Company Domain}}`
- Job titles:
  - "Engineering" OR "CTO" OR "VP Engineering" OR "Engineering Manager"
  - "Product" OR "Product Manager" OR "Head of Product"
  - "CEO" OR "Founder" OR "VP"
- Seniority: Manager, Director, VP, C-Level
- Limit: 10 per company

**Waterfall**: Apollo → RocketReach → Lusha

#### Column 3: Role Scoring
**Type**: Formula Column
**Name**: `Role Score`

```javascript
const title = contact.title.toLowerCase();

// Engineering roles (6 points)
if (title.match(/cto|vp engineering|head of engineering|engineering manager|director of engineering/i)) {
  return 6;
}

// Leadership roles (3 points)
if (title.match(/ceo|founder|coo|vp(?!.*engineering)/i)) {
  return 3;
}

// Product roles (3 points)
if (title.match(/product manager|head of product|vp product|cpo/i)) {
  return 3;
}

return 0;
```

#### Column 4: LinkedIn Profile Enrichment
**Integration**: Phantombuster or Apify LinkedIn Profile Scraper
**Settings**:
- Input: `{{LinkedIn URL}}`

**Extract**:
- Recent posts (last 5)
- Recent activity
- Skills
- Headline

#### Column 5: Email Verification
**Integration**: ZeroBounce or Bouncer
**Settings**:
- Input: `{{Email}}`

**Filter**: Only keep valid emails

#### Column 6: Final Contact Score
**Type**: Formula Column

```javascript
// Add role score to company score from Table 1
return companyScore + roleScore;
```

#### Column 7: Filter High-Priority Contacts
**Type**: Filter
**Condition**: `{{Final Contact Score}} >= 30`

---

## Table 3: Personalization Engine

### Purpose
Deep research on high-priority contacts to generate highly personalized outreach.

### Input
High-priority contacts from Table 2 (score >= 35)

### Table Structure

#### Column 1: Import High-Priority Contacts
**Type**: Import Table
- Select Table 2
- Import rows with score >= 35

#### Column 2: Recent LinkedIn Posts
**Integration**: Apify LinkedIn Post Scraper
**Settings**:
- Profile: `{{LinkedIn URL}}`
- Limit: 5 most recent posts

#### Column 3: Company Blog Articles
**Integration**: Web Scraper or RSS Feed
**Settings**:
- URL: `{{Company Domain}}/blog` or engineering blog
- Limit: 5 most recent

**Check for**: Articles written by the contact

#### Column 4: Community Presence
**Integration**: Google Search or Manual Research
**Search**: `{{Contact Name}} {{Company Name}} site:news.ycombinator.com OR site:producthunt.com`

**Formula Column - Community Score**:
```javascript
if (communityResults.length >= 1) {
  return 1;
} else {
  return 0;
}
```

#### Column 5: Competitor Reviews
**Integration**: G2 or Capterra API
**Search**: Reviews by company domain on competitor tools

**Formula Column - Review Score**:
```javascript
if (hasRecentReview) {
  return 1;
} else {
  return 0;
}
```

#### Column 6: Final Total Score
**Type**: Formula Column

```javascript
return contactScore + communityScore + reviewScore;
```

#### Column 7: AI-Generated Personalized Message
**Integration**: OpenAI GPT-4 or Anthropic Claude
**Type**: AI Formula

**Prompt**:
```
You are a BDR at PostHog writing a highly personalized cold outreach email.

CONTACT INFO:
- Name: {{Contact Name}}
- Title: {{Contact Title}}
- Company: {{Company Name}}
- Industry: {{Industry}}

COMPANY SIGNALS:
- Employees: {{Employees}}
- Recent Funding: {{Funding Round}} - ${{Funding Amount}} ({{Funding Date}})
- Top Investors: {{Investors}}
- Hiring: {{Job Titles}}
- Tech Stack: {{Detected Tools}}
- Recent News: {{News Headlines}}

CONTACT SIGNALS:
- Recent LinkedIn Posts: {{LinkedIn Posts}}
- Recent Blog Articles: {{Blog Articles}}
- Community Activity: {{Community Results}}

POSTHOG VALUE PROPS:
- All-in-one product analytics (replaces Mixpanel, LaunchDarkly, FullStory, etc.)
- Built for engineers by engineers
- Self-hostable for compliance
- Transparent pricing
- Ships fast, built for high-velocity teams

Write a 4-6 sentence personalized email that:
1. Opens with a specific, genuine observation about them or their company
2. Asks a thoughtful question related to a real pain point
3. Mentions PostHog naturally as a solution
4. Includes relevant social proof (similar company or their investor's portfolio)
5. Ends with a low-friction CTA
6. Feels conversational, not salesy

DO NOT:
- Use generic praise ("I love your content")
- Be overly formal
- Mention you "came across their profile"
- Use marketing jargon

Output only the email body, no subject line.
```

#### Column 8: Subject Line Generator
**Type**: AI Formula

**Prompt**:
```
Based on this email body and company context, write 3 subject line options that are:
- Specific and relevant
- 4-7 words
- Not clickbaity
- Reference something concrete

Email: {{Generated Email}}
Company: {{Company Name}}
Key Signal: {{Top Signal}}

Format as JSON:
{
  "subject1": "...",
  "subject2": "...",
  "subject3": "..."
}
```

---

## Integration & Automation

### Export to CRM (HubSpot)

#### Table 1 → HubSpot Companies
**Mapping**:
- Company Domain → Company Domain (unique ID)
- Company Name → Company Name
- Total Score → Custom Property: `posthog_lead_score`
- Priority Tier → Custom Property: `posthog_priority`
- All enrichment data → Custom properties

**Automation**: Update on new row + daily sync

#### Table 2 → HubSpot Contacts
**Mapping**:
- Email → Email (unique ID)
- Name → First Name + Last Name
- Title → Job Title
- Company → Associated Company
- Final Score → Custom Property: `posthog_contact_score`
- Role Score → Custom Property: `role_score`

**Automation**: Create contact + associate with company

#### Table 3 → HubSpot Sequences/Tasks
**Mapping**:
- High-priority contacts → Enroll in sequence
- Generated email → Sequence email 1
- Subject lines → Store in custom property for reference

**Automation**: Trigger sequence enrollment when row added

---

### Automated Daily Workflow

**Morning (9 AM)**:
1. Clay runs all tables for new leads
2. Scores calculated automatically
3. High-priority leads (45+) → Slack notification
4. All qualified leads (25+) → Sync to HubSpot

**Afternoon (2 PM)**:
1. Re-check job postings for updates (things change fast)
2. Re-check LinkedIn for new posts
3. Update scores if significant changes

**Weekly (Monday 9 AM)**:
1. Refresh all enrichment data
2. Re-score existing leads
3. Identify score increases (new funding, new jobs posted)
4. Alert on "hot leads" that just became high-priority

---

## Testing & Validation

### Phase 1: Test with 10 Known Good Leads
1. Input 10 companies you know fit PostHog's ICP
2. Verify enrichment data accuracy
3. Check score alignment (should be 35+)
4. Review generated messaging

### Phase 2: Test with 10 Known Bad Leads
1. Input 10 companies that are NOT a fit
2. Verify they score low (<25)
3. Ensure scoring is working as expected

### Phase 3: Production with 100 Leads
1. Run 100 new leads through full funnel
2. Track reply rates by score bracket
3. Identify false positives/negatives
4. Adjust scoring weights

### Phase 4: Continuous Improvement
1. Weekly review of lead quality
2. Track score → opportunity conversion
3. Adjust point allocations based on closed-won data
4. Refine messaging based on reply rates

---

## Troubleshooting

### Issue: Enrichment Not Finding Data
**Solution**: Add more waterfall providers
- Try 3-4 sources for each data point
- Use People Data Labs as Clearbit backup
- Manual research for high-value leads (45+)

### Issue: Scores Too High or Too Low
**Solution**: Adjust point allocations
- Review 20 closed-won deals
- Identify common signals
- Weight those signals higher

### Issue: AI Messages Too Generic
**Solution**: Improve prompt with examples
- Add 3-5 example messages
- Be more specific about signals to reference
- Explicitly ban generic phrases

### Issue: Too Many Leads
**Solution**: Raise threshold
- Move to 30+ instead of 25+
- Focus only on Hot/Warm (35+)
- Add additional filtering criteria

### Issue: Not Enough Leads
**Solution**: Broaden input sources
- Add more lead sources (LinkedIn SalesNav, etc.)
- Lower score threshold temporarily
- Expand ICP criteria slightly

---

## Cost Optimization

### Credit Usage Estimates
- **Clearbit**: ~50 credits per company
- **Crunchbase**: ~30 credits per company
- **BuiltWith**: ~20 credits per company
- **LinkedIn Scraper**: ~10 credits per profile
- **Apollo/RocketReach**: ~1 credit per contact
- **AI Generation**: ~100 credits per message

**Per Lead (Company + 2 Contacts + Personalization)**:
~350 credits = ~$3.50

### Optimization Tips
1. **Filter early**: Only enrich companies that meet basic criteria first
2. **Waterfall wisely**: Start with cheapest sources
3. **Batch processing**: Run daily instead of real-time
4. **Cache results**: Don't re-enrich same company daily
5. **Prioritize AI spend**: Only generate messages for 35+ scored leads

---

## Quick Start Checklist

- [ ] Set up Clay account with required integrations
- [ ] Create Table 1: Lead Enrichment & Scoring
- [ ] Configure Clearbit, Crunchbase, BuiltWith enrichments
- [ ] Build scoring formulas for all 5 categories
- [ ] Create Table 2: Contact Discovery
- [ ] Configure Apollo/RocketReach waterfall
- [ ] Add role scoring and email verification
- [ ] Create Table 3: Personalization Engine
- [ ] Set up AI message generation with refined prompts
- [ ] Connect to HubSpot/Salesforce
- [ ] Test with 10 known good/bad leads
- [ ] Launch production with 100 leads
- [ ] Set up daily automation
- [ ] Track metrics and iterate weekly

---

**Pro Tip**: Start simple with just Table 1 and basic scoring. Get that working and validated before building out the full personalization engine. You can manually personalize messages for the first 50 leads while you refine the AI prompts.

The scoring gets you priority. The research gets you the meeting. Focus on accuracy before automation.
