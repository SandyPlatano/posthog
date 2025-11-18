# Competitive Landscape Guide

Understanding PostHog's competitors and how to position against them is critical for sales conversations. This guide covers the main competitors and how to handle objections.

## Market Overview

PostHog competes in several categories:
1. **Product Analytics** - Amplitude, Mixpanel, Heap
2. **Session Replay** - Hotjar, FullStory, LogRocket
3. **Feature Flags** - LaunchDarkly, Split
4. **Experimentation** - Optimizely, VWO

PostHog's unique position: **All-in-one platform for engineers**.

---

## Primary Competitors

### Amplitude

**What they do:** Product analytics with strong visualization and collaboration features.

**Their strengths:**
- Enterprise scale and maturity
- User-friendly for non-technical users
- Powerful visualizations
- Strong marketing team analytics

**Their weaknesses:**
- No autocapture
- No session replay
- No feature flags/experiments (native)
- Not engineer-focused
- "Talk to sales" pricing opacity

**PostHog wins when:**
- Buyer is an engineer or engineering-led team
- They want all-in-one (reduce tool sprawl)
- They want autocapture
- They value transparent pricing
- They need session replay

**PostHog loses when:**
- Non-technical marketing teams are buying
- They need deep enterprise integrations
- They have existing Amplitude investment

**Key talking points:**
- "Amplitude is built for marketing teams; PostHog is built for engineers"
- "PostHog has autocapture; Amplitude requires manual instrumentation"
- "PostHog includes session replay and feature flags; Amplitude is just analytics"
- "PostHog pricing is transparent; Amplitude requires sales calls"

---

### Mixpanel

**What they do:** Event-based product analytics with easy-to-use interface.

**Their strengths:**
- Easy to use for non-technical users
- Good mobile analytics
- Strong segmentation
- Lower price point than Amplitude

**Their weaknesses:**
- No autocapture
- No session replay
- No feature flags (native)
- Limited for technical users
- Marketing-focused

**PostHog wins when:**
- Technical team is making the decision
- They need more than just analytics
- They want to move fast with autocapture
- They want self-serve and transparency

**PostHog loses when:**
- Marketing team is buying
- They want maximum simplicity
- Mobile-first with no web component

**Key talking points:**
- "Mixpanel focuses on ease of use; PostHog focuses on depth for engineers"
- "PostHog has autocapture and session replay; Mixpanel has neither"
- "PostHog is all-in-one; Mixpanel is just analytics"
- "Both are usage-based, but PostHog includes more products"

---

### Heap

**What they do:** Product analytics with autocapture, now owned by Contentsquare.

**Their strengths:**
- Autocapture (like PostHog)
- Visual labeling
- Good for non-technical users
- Session replay included

**Their weaknesses:**
- Acquired by Contentsquare (marketing analytics)
- No feature flags/experiments
- Less developer-focused
- Limited session replay features
- Closed source

**PostHog wins when:**
- They want open source
- They need feature flags and experiments
- They want engineer-focused tooling
- They're concerned about the Contentsquare acquisition

**PostHog loses when:**
- They're heavily invested in Heap already
- They need Contentsquare ecosystem

**Key talking points:**
- "PostHog is the most direct alternative to Heap"
- "Both have autocapture, but PostHog adds feature flags and experiments"
- "PostHog is open source; Heap is closed and now owned by a marketing company"
- "PostHog's session replay has more developer features (DOM explorer, network events)"

---

### Hotjar

**What they do:** Session replay, heatmaps, and surveys.

**Their strengths:**
- Very easy to set up
- Good heatmaps
- Simple surveys
- Low cost entry point

**Their weaknesses:**
- No real analytics
- No feature flags
- Limited technical depth
- Not for serious product teams

**PostHog wins when:**
- They need analytics + replay together
- They want to consolidate tools
- They're a technical team
- They need more than basic surveys

**PostHog loses when:**
- They just need simple heatmaps
- Very small team with minimal needs
- Budget is extremely constrained

**Key talking points:**
- "Hotjar is great for marketers; PostHog is for product engineers"
- "PostHog is all-in-one; Hotjar still needs you to buy Amplitude or Mixpanel"
- "PostHog's session replay connects to analytics; Hotjar's is standalone"
- "PostHog has feature flags and experiments; Hotjar doesn't"

---

### LaunchDarkly

**What they do:** Feature flag management and experimentation.

**Their strengths:**
- Deep feature flag capabilities
- Enterprise-grade
- Good SDK support
- Strong in regulated industries

**Their weaknesses:**
- Expensive
- No analytics
- No session replay
- Requires separate analytics tool

**PostHog wins when:**
- They want flags + analytics together
- They're price-sensitive
- They want all-in-one
- They value open source

**PostHog loses when:**
- Deep feature flag needs (tons of flags, complex targeting)
- Heavily regulated industry with specific requirements
- Already invested in LaunchDarkly

**Key talking points:**
- "PostHog feature flags are integrated with analytics and session replay"
- "LaunchDarkly is just flags; you still need analytics elsewhere"
- "PostHog is more cost-effective for most teams"
- "PostHog is open source; LaunchDarkly is closed"

---

### FullStory

**What they do:** Digital experience intelligence (session replay + analytics).

**Their strengths:**
- Very good session replay
- DX analytics
- Good for UX teams
- Frustration detection

**Their weaknesses:**
- Expensive
- Not engineer-focused
- No feature flags
- More UX than product

**PostHog wins when:**
- Engineering team is buying
- They need feature flags
- They want open source
- Price sensitivity

**PostHog loses when:**
- UX team is the primary buyer
- They need deep UX-specific features

---

### LogRocket

**What they do:** Frontend monitoring and session replay.

**Their strengths:**
- Error tracking + replay
- Good for debugging
- Performance monitoring

**Their weaknesses:**
- Limited analytics
- No feature flags
- More monitoring than product analytics

**PostHog wins when:**
- They need full product analytics
- They want all-in-one
- Feature flags are important

---

## Quick Comparison Matrix

| Feature | PostHog | Amplitude | Mixpanel | Heap | Hotjar | LaunchDarkly |
|---------|---------|-----------|----------|------|--------|--------------|
| Product Analytics | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| Autocapture | ✅ | ❌ | ❌ | ✅ | ❌ | ❌ |
| Session Replay | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ |
| Feature Flags | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Experiments | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ |
| Surveys | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ |
| Open Source | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Self-Host | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Engineer-First | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Transparent Pricing | ✅ | ❌ | ✅ | ❌ | ✅ | ❌ |

---

## Tools PostHog Replaces

According to G2 reviews, PostHog can replace:

1. **Heap** - Product analytics
2. **LaunchDarkly** - Feature flags and A/B testing
3. **Hotjar** - Session replay and surveys

This consolidation means:
- Less tool sprawl
- Lower total cost
- Integrated data
- Simpler stack

---

## Positioning by Buyer Type

### Engineering-Led Teams

**Lead with:**
- Technical depth
- Open source
- API-first
- Self-serve everything

**Avoid:**
- Comparisons to "marketing tools"
- Over-simplified features

### Product-Led Teams

**Lead with:**
- All-in-one platform
- Autocapture for speed
- Session replay + analytics together
- Feature flags for experimentation

**Avoid:**
- Over-technical positioning
- Assuming deep technical knowledge

### Enterprise Buyers

**Lead with:**
- Self-serve Enterprise (unique!)
- RBAC and security
- Self-host option for compliance
- Transparent pricing

**Avoid:**
- Dismissing enterprise needs
- Over-promising customization

---

## Common Objections and Responses

### "We already use Amplitude/Mixpanel"

**Response:**
- "What PostHog adds: autocapture, session replay, feature flags—all integrated"
- "See how users actually behave, not just metrics"
- "Run experiments without another tool"
- "You can migrate incrementally"

### "LaunchDarkly has better feature flags"

**Response:**
- "For deep flag needs, possibly true"
- "But PostHog integrates flags with analytics and replay"
- "See exactly how flags affect metrics"
- "Watch sessions by flag variant"
- "Significantly more cost-effective"

### "We need something easier for non-technical users"

**Response:**
- "PostHog is built for engineers because they're your decision makers"
- "Non-technical tools mean engineers still need to instrument everything"
- "Autocapture means fast time-to-value"
- "UI is improving constantly"

### "Is PostHog mature enough?"

**Response:**
- "$450M+ valuation, backed by top investors"
- "Used by thousands of companies"
- "Open source means community validation"
- "Handbook is public—see how they operate"

### "We need enterprise support"

**Response:**
- "Enterprise add-on is $2k/month, self-serve"
- "Dedicated support included"
- "Training and onboarding"
- "RBAC and advanced security"

### "What about GDPR/privacy?"

**Response:**
- "EU hosting available"
- "Self-host for complete control"
- "Cookieless tracking option"
- "Granular privacy controls"
- "We use PostHog ourselves—we care about privacy"

---

## When to Qualify Out

Be honest when PostHog might not be the right fit:

### Pure Marketing Analytics
If they need attribution, campaign tracking, and marketing-specific features, Amplitude might be better.

### Deep UX Focus
If they're primarily UX researchers wanting heatmaps and frustration detection, FullStory might fit better.

### Non-Technical Buyers
If the entire team is non-technical and needs maximum simplicity, Mixpanel might be easier.

### Massive Flag Volume
If they have thousands of complex flags with sophisticated targeting, LaunchDarkly's depth might matter.

**Being honest builds trust.** PostHog values this explicitly.

---

## Competitive Research Resources

### PostHog Comparison Pages
- [Mixpanel Alternatives](https://posthog.com/blog/best-mixpanel-alternatives)
- [Amplitude Alternatives](https://posthog.com/blog/best-amplitude-alternatives)
- [Heap Alternatives](https://posthog.com/blog/best-heap-alternatives)
- [PostHog vs Heap](https://posthog.com/blog/posthog-vs-heap)

### External
- G2 reviews for all products
- Competitor pricing pages
- Industry analyst reports

---

## Talking Points Summary

### Universal Differentiators

1. **All-in-one** - Replaces 3+ tools
2. **Open source** - Transparency and trust
3. **Autocapture** - Instant value
4. **Engineer-first** - Built for your ICP
5. **Native integration** - Chart → session → flag
6. **Transparent pricing** - No sales wall

### Against Analytics Tools (Amplitude/Mixpanel/Heap)

- PostHog includes session replay and feature flags
- PostHog is built for engineers, not marketers
- PostHog has autocapture (vs Amplitude/Mixpanel)
- PostHog is open source (vs all)

### Against Replay Tools (Hotjar/FullStory)

- PostHog has full analytics (they don't)
- PostHog has feature flags (they don't)
- PostHog is for engineers (they're for UX/marketing)
- PostHog connects replay to analytics natively

### Against Flag Tools (LaunchDarkly)

- PostHog is all-in-one (flags + analytics + replay)
- PostHog is more cost-effective
- PostHog is open source
- PostHog connects flags to metrics natively

---

## Key Takeaways

1. **Know the landscape** - Understand each competitor's strengths and weaknesses
2. **Lead with differentiation** - All-in-one, open source, engineer-first
3. **Be honest** - Qualify out when PostHog isn't the best fit
4. **Connect to value** - Always tie features to customer outcomes
5. **Use their words** - Let G2 reviews and customers speak for you
