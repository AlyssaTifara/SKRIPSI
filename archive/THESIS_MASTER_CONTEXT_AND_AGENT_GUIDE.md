# THESIS_MASTER_CONTEXT_AND_AGENT_GUIDE

> **Purpose:** Master context and operating guide for Antigravity /
> agentic development workflow.
>
> **Project:** D4 Sarjana Terapan Sistem Informasi Bisnis --- Politeknik
> Negeri Malang
>
> **Research domain:** Smart Farming --- Maize --- Poultry Feed ---
> Business/Information Analysis
>
> **Current status:** Research direction is being validated with the
> partner/supervisor. A web-based system is the eventual implementation
> target, but the exact system form, requirements, architecture,
> technology stack, and features are **NOT YET LOCKED**.
>
> **Critical rule:** Do not turn assumptions into facts. Do not lock the
> research problem, gap, RQ, method, title, or system architecture
> before the unresolved partner context and data requirements have been
> validated.

------------------------------------------------------------------------

# 0. HOW TO USE THIS DOCUMENT

This document is the current master context for an agentic workflow
supporting the thesis.

The intended workflow is:

**Research context validation** → **business/information need** → **data
requirement** → **research problem** → **research gap** → **research
question** → **research objective** → **method mapping** → **solution
requirements** → **system design** → **implementation** →
**testing/evaluation** → **thesis + journal manuscript**

The final implementation target is a **web-based system**, but this does
NOT mean the system type has already been decided.

The agent must therefore work in two layers:

1.  **Research layer**
    -   Understand the real partner problem.
    -   Establish evidence and research logic.
    -   Determine what information must be produced.
    -   Determine what analytical method is appropriate.
2.  **System layer**
    -   Translate validated information requirements into a web-based
        system.
    -   Determine architecture, modules, UI, database, calculations,
        visualization, and testing only after the research requirements
        justify them.

The agent must never reverse this order simply because coding is
possible.

------------------------------------------------------------------------

# 1. PROJECT IDENTITY

## 1.1 Academic Program

-   Institution: Politeknik Negeri Malang
-   Program: D4 / Sarjana Terapan Sistem Informasi Bisnis
-   Field orientation:
    -   Business Information Systems
    -   Data Analysis
    -   Business Analysis
    -   System Analysis
    -   Information management
    -   Decision support / information support where justified

The thesis must remain recognizably **Sistem Informasi Bisnis**, not
become a pure agronomy, animal nutrition, or machine learning thesis.

The technical implementation should support the business/information
analysis rather than become the research objective by itself.

------------------------------------------------------------------------

# 2. CURRENT RESEARCH DOMAIN

## 2.1 Domain

Smart Farming.

## 2.2 Commodity

Maize / corn / jagung.

## 2.3 Partner Context

The research partner is in **Sumenep**.

Based on the latest clarification from the supervisor, the partner is a
**bank-sampah entity that synergizes with smart farming**.

The smart farming activity includes maize cultivation on the available
land.

Important: - The partner profile exists and was identified by the
supervisor as the correct profile. - The exact contents of the Google
Drive profile have NOT been independently extracted into this context. -
Do not invent details from that profile. - Only use facts explicitly
provided by the supervisor/user or later validated from the actual
partner.

------------------------------------------------------------------------

# 3. LATEST PARTNER CONTEXT --- VALIDATED SO FAR

The following information has been communicated by the supervisor and is
the current working context.

## 3.1 Land

There are:

-   3 maize plots.
-   Each plot = 5 × 6 meters.
-   Each plot = 30 m².
-   Total maize area = 90 m².

Conceptually:

``` text
Plot 1 = 5 × 6 m = 30 m²
Plot 2 = 5 × 6 m = 30 m²
Plot 3 = 5 × 6 m = 30 m²

Total = 90 m²
```

## 3.2 Planting Age / Harvest Pattern

The three plots are understood to differ in age by approximately one
month.

The intended idea appears to be that the plots are staggered so that a
plot can be harvested approximately every month.

However:

> **The exact operational interpretation is still OPEN and must be
> confirmed.**

Do NOT state as a validated operational fact that every plot is
definitely harvested once every month until the supervisor/partner
confirms it.

## 3.3 Maize Utilization

The supervisor explained that maize will be:

-   chopped using a machine;
-   used as part of feed;
-   potentially used for chickens and catfish.

The feed may also be mixed with:

-   bran / dedak;
-   other organic materials.

The broader goal is to utilize the smart-farming production and organic
resources to reduce purchased feed / operational feed costs.

Do NOT state that feed cost will become literally zero unless actual
cost data and the partner's operational model support that claim.

Safer wording:

> "potential to reduce purchased feed requirements / operational feed
> costs."

## 3.4 Poultry Feed Requirement

The supervisor mentioned an estimated:

> approximately 200 grams per chicken per day.

This number is **NOT YET DEFINED ENOUGH TO USE IN A FINAL MODEL**.

We do not yet know whether:

-   200 g = total feed intake per chicken per day; OR
-   200 g = maize requirement per chicken per day; OR
-   another interpretation applies.

Therefore:

> **200 g/chicken/day = OPEN PARAMETER.**

Do not silently convert it into maize consumption.

## 3.5 Initial Information Need

The supervisor's specific initial question was essentially:

> How many chickens can be supplied per month if the available
> land/production is considered?

This suggests a potential analytical direction:

**maize production capacity → feed availability → poultry support
capacity**

But this is still a **working direction**, not yet the final research
problem.

------------------------------------------------------------------------

# 4. TEN OPEN QUESTIONS TO THE SUPERVISOR

These questions have been sent / are being asked and have **NOT YET BEEN
ANSWERED**.

They are especially important for the next supervision session.

## OPEN-Q1 --- Form of Maize

For maize that will be chopped by machine:

> Is the intended material the whole maize plant (e.g., stem, leaves,
> cob), or mainly the grain/kernel/maize grain?

Why it matters: - determines the relevant yield unit; - determines feed
formulation; - determines literature needed; - affects nutritional
assumptions; - affects system data model.

Status:

`OPEN — DO NOT ASSUME`

------------------------------------------------------------------------

## OPEN-Q2 --- Exact Harvest Pattern

For the three 5 × 6 m plots:

> Is the intended operation that each plot is harvested once per month
> in rotation, resulting in one plot being harvested each month?

Why it matters: - determines monthly production; - determines
time-series logic; - affects the production calculation; - affects
whether the system needs a crop-cycle/planting schedule module.

Status:

`OPEN — DO NOT ASSUME`

------------------------------------------------------------------------

## OPEN-Q3 --- Yield per Plot

> Is there already an estimated/actual harvest yield per plot
> (e.g. kg/plot), or may production initially be estimated from
> secondary literature?

Why it matters: - yield is the core production input; - determines
whether the model can be partner-specific; - determines whether
literature-based estimation is acceptable.

Status:

`OPEN — DO NOT ASSUME`

------------------------------------------------------------------------

## OPEN-Q4 --- Meaning of 200 g/chicken/day

> Is approximately 200 g/chicken/day total feed requirement, rather than
> maize-specific requirement?

Why it matters: - if it is total feed, maize proportion is required; -
if it is maize-specific, the calculation is substantially simpler.

Status:

`OPEN — DO NOT ASSUME`

------------------------------------------------------------------------

## OPEN-Q5 --- Feed Composition

If 200 g is total feed:

> What percentage/proportion of the feed mixture is maize compared with
> bran and other organic materials?

Why it matters: - required to convert total feed requirement into maize
requirement; - affects capacity calculation; - affects scenario
analysis.

Status:

`OPEN — DO NOT ASSUME`

------------------------------------------------------------------------

## OPEN-Q6 --- Allocation Between Chicken and Catfish

> Is all maize production prioritized for chicken feed, or is part of it
> allocated to catfish feed?

Why it matters: - determines the available maize fraction for
chickens; - introduces an allocation constraint; - affects the
calculated poultry capacity.

Status:

`OPEN — DO NOT ASSUME`

------------------------------------------------------------------------

## OPEN-Q7 --- Main Desired Output

> Is the main goal to estimate the maximum/expected number of chickens
> that can be supplied by the maize production from the three plots in
> one month?

Why it matters: - determines the primary output; - helps distinguish
capacity analysis from other possible research directions.

Status:

`OPEN — DO NOT ASSUME`

------------------------------------------------------------------------

## OPEN-Q8 --- Chicken Quantity: Input or Output?

> Is the number of chickens already determined by the partner, or is the
> number of chickens the research should calculate from available maize
> production?

Why it matters: - if chicken count is fixed → sufficiency/adequacy
analysis; - if chicken count is unknown → capacity estimation; - if both
are needed → system may support both modes.

Status:

`OPEN — DO NOT ASSUME`

------------------------------------------------------------------------

## OPEN-Q9 --- Cost Analysis Scope

> Should the research also consider potential feed-cost reduction, or
> should the initial scope stop at chicken supply capacity?

Why it matters: - determines whether economic analysis is part of the
thesis; - determines additional data requirements; - prevents
uncontrolled scope expansion.

Status:

`OPEN — DO NOT ASSUME`

------------------------------------------------------------------------

## OPEN-Q10 --- Data Source

> Can actual production/feed/chicken data be obtained from the partner,
> or should the research initially use secondary literature/data?

Why it matters: - determines feasibility; - determines validity of the
model; - determines system input design; - affects research method and
evaluation.

Status:

`OPEN — DO NOT ASSUME`

------------------------------------------------------------------------

# 5. WHAT IS ALREADY COMPLETED

## 5.1 Notebook 1 --- Data Understanding

Completed.

Purpose: - understand the exploratory dataset; - identify variables; -
understand structure and data types; - establish an initial analytical
landscape.

## 5.2 Notebook 2 --- Data Quality & EDA

Completed.

The exploratory dataset contained approximately:

-   111 observations
-   22 columns

Relevant examples included: - total_days - yield - soil moisture -
irrigation type - NDVI - disease status - planting/harvest-related
information

The notebook was exploratory and helped understand data quality and
patterns.

## 5.3 Notebook 3 --- Candidate Research Problems

Completed and considered sufficient.

Earlier candidate areas included: 1. planting/harvest cycle; 2.
irrigation; 3. crop condition / disease / NDVI.

Important:

> These are NOT the current final research problems.

The partner context later changed the direction substantially.

Do not automatically return to these old candidates.

------------------------------------------------------------------------

# 6. IMPORTANT STATUS OF THE EXPLORATORY DATASET

The previous maize dataset is a **proxy/exploratory dataset**.

It is NOT evidence of the actual Sumenep partner's conditions.

Never write statements such as:

-   "the partner has irrigation problems because the dataset shows...";
-   "the Sumenep farm has disease issues...";
-   "the partner's maize yield is X based on the Kaggle data."

Correct interpretation:

> The exploratory dataset was used to understand relevant agricultural
> variables and analytical possibilities before the actual partner
> context was validated.

The partner-specific research must use: - actual partner data, if
available; - appropriately selected secondary data/literature; - or
clearly declared assumptions/scenarios.

------------------------------------------------------------------------

# 7. WHAT HAS BEEN EXPLICITLY DEPRIORITIZED / REJECTED

The following directions should NOT be reintroduced unless new evidence
from the partner makes them relevant.

## 7.1 Machine Learning

Current direction:

> **NO MACHINE LEARNING**

Do not automatically propose: - Random Forest - XGBoost - neural
networks - yield prediction ML - classification models - deep learning

ML is not currently justified.

## 7.2 Big Data

Do not introduce: - Hadoop - Spark - distributed processing - big-data
architecture

The dataset and problem do not justify this.

## 7.3 Old Crop-Condition Focus

Do not assume the thesis is about: - disease detection; - NDVI; -
irrigation optimization; - soil moisture prediction.

These came from the earlier exploratory phase and are not the current
partner-driven direction.

## 7.4 Generic Fodder Research

Do not shift the project into a generic: - forage crop thesis; -
ruminant feed thesis; - dairy feed thesis.

The relevant current context is specifically **maize utilization as part
of poultry feed**, with possible catfish allocation.

## 7.5 Unverified Operational Problems

Do not invent: - feed shortage; - feed stockout; - excess production; -
storage shortage; - information-system failure; - overproduction; -
underproduction; - inefficient scheduling; - farmer resistance; - data
unavailability at the partner.

These require evidence.

------------------------------------------------------------------------

# 8. LITERATURE MAPPING STATUS

Broad literature mapping has been completed.

Research Opportunity Mapping has also been completed.

A focused core literature set was developed instead of continuously
expanding the source count.

The literature themes are:

## A. Maize → Poultry Feed

Core examples: 1. Assessment of Maize (Zea mays) as Feed Resource for
Poultry 2. The Importance of Maize for Poultry --- Grain SA

Purpose: - establish maize's role in poultry feed; - understand relevant
feed context.

## B. Maize Production / Staggered Planting

Core examples: 3. Sequential maize planting: A cropping strategy for the
small farmer 4. Effect of Different Planting Dates on Yield and Some
Agronomic Characters of Twelve Maize Hybrids 5. Corn planting and
harvest scheduling under storage capacity and growing degree units
uncertainty 6. Determining an Optimal Corn Planting Schedule by Using
the Integration of Supply Chain Risk Evaluation Model 7. Optimizing Crop
Planting Schedule Considering Planting Window and Storage Capacity ---
Frontiers

Purpose: - understand staggered/sequential planting; - understand
planting/harvest timing; - support production-period reasoning if the
partner context requires it.

Important: The existence of this literature does NOT prove that
scheduling is the research problem.

The partner already appears to have a staggered-plot concept. Scheduling
is currently supporting context unless new evidence makes it a research
problem.

## C. Supply / Procurement / Planning

Core examples: 8. A System Dynamics Model for Resilient and Sustainable
Corn Procurement System Design in the Feed Industry 9. Production
planning decisions in the broiler chicken supply chain with growth
uncertainty

Purpose: - understand supply-demand relationships; - production
planning; - feed supply context.

## D. SIB / FMIS

Core examples: 10. Obstacles and features of Farm Management Information
Systems: A systematic literature review 11. Reference architecture
design for farm management information systems

Purpose: - connect the agricultural problem to an information-system
perspective; - understand information requirements and system
architecture; - establish why a digital information solution can be
relevant.

------------------------------------------------------------------------

# 9. LITERATURE THAT WAS DROPPED OR IS BACKUP ONLY

Do not unnecessarily reload all previous sources.

Examples of backup/dropped areas: - Cornell feed inventory - FAO poultry
feed availability - generic optimization of raw material supply
scheduling - generic cloud FMIS papers - planting sweet corn GDD -
optimal green fodder harvest - round-the-year green fodder - Indian
forage crops/grasses

The Indian forage crops/grasses source was specifically assessed as weak
for the current direction because it is more focused on forage/ruminants
and is not direct evidence for maize grain/chicken feed/SIB.

------------------------------------------------------------------------

# 10. RESEARCH OPPORTUNITY STATUS

Earlier literature mapping identified opportunities such as: -
feed-driven crop scheduling; - simplified staggered planting; -
harvest/storage alignment; - small-scale FMIS integration; -
supply-demand advisory.

These should now be treated as **background opportunities**, not final
research problems.

The current partner-specific direction points more directly toward:

> **Assessing/communicating the capacity of maize production to support
> poultry feed requirements.**

Potential conceptual chain:

``` text
3 maize plots
      ↓
maize production
      ↓
monthly maize availability
      ↓
maize available for poultry feed
      ↓
feed requirement
      ↓
chicken support capacity
      ↓
decision-support information
```

This is a working research direction.

------------------------------------------------------------------------

# 11. PRELIMINARY RESEARCH FRAMEWORK

## 11.1 Input

### Land & Production

-   number of plots;
-   plot dimensions;
-   total area;
-   planting dates;
-   harvest dates;
-   yield per plot;
-   production period;
-   form of maize used as feed.

### Feed

-   feed requirement per chicken per day;
-   feed composition;
-   maize proportion;
-   bran proportion;
-   other organic feed materials.

### Allocation

-   maize allocation to chickens;
-   maize allocation to catfish;
-   losses/waste if relevant.

### Supporting Data

-   literature-based yield parameters if necessary;
-   literature-based poultry feed parameters if necessary.

## 11.2 Processing

### Production Analysis

-   calculate production per plot;
-   estimate production per month;
-   determine maize available for feed.

### Feed Requirement Analysis

-   calculate feed requirement;
-   convert total feed requirement to maize requirement when
    appropriate.

### Capacity Analysis

-   compare available maize against maize requirement;
-   estimate chicken capacity;
-   identify adequacy / surplus / deficit if appropriate.

### Scenario Analysis --- Optional

Only include if uncertainty justifies it.

Potential scenarios: - low/base/high yield; - different maize feed
proportions; - different chicken populations; - different allocation to
catfish.

Do not force scenario analysis if the final research design does not
require it.

------------------------------------------------------------------------

# 12. PRELIMINARY FORMULAS

These are conceptual only.

## 12.1 Monthly Maize Production

``` text
Monthly Maize Production
=
Yield per Plot × Number of Plots Harvested in the Period
```

The final formula depends on: - actual harvest schedule; - yield
definition; - whether yield is fresh weight/dry weight/whole
plant/grain; - whether all plots produce equivalent yields.

## 12.2 Total Feed Requirement

If 200 g is total feed:

``` text
Monthly Feed Requirement per Chicken
=
Daily Feed Requirement × Number of Days
```

## 12.3 Maize Requirement

If maize is a proportion of total feed:

``` text
Monthly Maize Requirement per Chicken
=
Monthly Feed Requirement per Chicken
×
Maize Proportion in Feed
```

## 12.4 Chicken Capacity

Conceptually:

``` text
Chicken Capacity
=
Maize Available for Chicken Feed per Month
÷
Monthly Maize Requirement per Chicken
```

This formula must NOT be implemented as a final business rule until the
unresolved parameters are validated.

------------------------------------------------------------------------

# 13. CURRENT DATA REQUIREMENT MATRIX

  ----------------------------------------------------------------------------------
  Parameter                 Why Needed        Current Status    Possible Source
  ------------------------- ----------------- ----------------- --------------------
  Number of plots           Production        VALIDATED         Partner/supervisor
                            structure                           

  Plot size                 Production        VALIDATED         Partner/supervisor
                            structure                           

  Total area                Production        DERIVED           Calculation
                            structure                           

  Planting interval         Monthly           OPEN              Partner/supervisor
                            production logic                    

  Harvest interval          Monthly           OPEN              Partner/supervisor
                            production logic                    

  Yield per plot            Production        OPEN              Partner or
                            capacity                            literature

  Yield unit                Valid calculation OPEN              Partner/literature

  Maize form                Feed model        OPEN              Partner/supervisor

  Feed                      Feed demand       OPEN              Partner + literature
  requirement/chicken/day                                       

  Maize proportion          Convert feed to   OPEN              Partner/literature
                            maize                               

  Feed ingredients          Feed context      Partially known   Partner

  Chicken count             Capacity vs       OPEN              Partner
                            target                              

  Catfish allocation        Resource          OPEN              Partner
                            allocation                          

  Feed cost                 Economic scope    OPEN              Partner

  Actual production data    Validation        OPEN              Partner

  Actual feed formulation   Validation        OPEN              Partner
  ----------------------------------------------------------------------------------

------------------------------------------------------------------------

# 14. DATA STATUS TAXONOMY

Every important fact should be tagged.

Use these statuses:

### `[VALIDATED]`

Directly confirmed by partner/supervisor or verified source.

### `[OPEN]`

Question has been raised but not answered.

### `[ASSUMPTION]`

Temporary assumption used only for exploration.

### `[LITERATURE-BASED]`

Parameter comes from an external scientific source.

### `[PARTNER-DATA]`

Actual data supplied by partner.

### `[DERIVED]`

Calculated from validated inputs.

### `[PROXY]`

Exploratory dataset or non-partner data.

### `[DECISION-PENDING]`

A research/scope decision still requires supervisor/researcher judgment.

### `[REJECTED]`

Previously considered but intentionally removed from the current
direction.

Agents MUST preserve these distinctions.

------------------------------------------------------------------------

# 15. CURRENT RESEARCH PROBLEM STATUS

The final research problem is **NOT LOCKED**.

Potential working statement:

> There is a need to determine the production capacity of maize from the
> available smart-farming land and relate that capacity to poultry feed
> requirements so that the partner can obtain information about the
> number of chickens that can potentially be supported by the available
> production.

This is only a **working problem hypothesis**.

Do not present it as the final research problem until: 1. partner
context is validated; 2. actual information need is confirmed; 3. data
availability is assessed; 4. literature gap is established.

------------------------------------------------------------------------

# 16. CURRENT RESEARCH GAP STATUS

The research gap is **NOT LOCKED**.

Do not manufacture a gap such as: - "no research has done this"; - "no
system exists"; - "previous studies only focus on..."; - "there is no
digital system for small farms..."

unless supported by the literature review.

A valid gap must be derived from the actual mapped literature.

Potential direction to investigate:

> Existing research may address maize production, feed utilization,
> production planning, or farm information systems separately, while the
> current context may require an integrated information model connecting
> small-scale maize production capacity with poultry feed support
> capacity.

This is a **hypothesis to test**, not a final claim.

------------------------------------------------------------------------

# 17. CURRENT RQ STATUS

Research Questions are **NOT LOCKED**.

Possible conceptual question:

> How can maize production capacity from the partner's smart-farming
> plots be assessed against poultry feed requirements to estimate the
> number of chickens that can be supported?

But do not finalize this until Q1--Q10 and literature evidence are
resolved.

------------------------------------------------------------------------

# 18. CURRENT METHOD STATUS

Working methodological direction:

> **Quantitative capacity analysis**

Potential supporting methods: - descriptive quantitative analysis; -
production calculation; - requirement calculation; - capacity/adequacy
analysis; - scenario analysis if justified; - system requirements
analysis; - web-based information-system design and implementation.

This is tentative.

Do NOT automatically introduce: - machine learning; - complex
optimization; - simulation; - advanced AI; - mathematical
optimization; - big-data processing.

Use complexity only if the validated problem requires it.

------------------------------------------------------------------------

# 19. WEB-BASED SYSTEM TARGET

## 19.1 Final Implementation Direction

The eventual thesis implementation target is:

> **A web-based information system.**

However, the exact system type is not yet known.

It could potentially become: - a calculation/information system; -
dashboard; - decision-support interface; - planning tool; - capacity
assessment system; - or another form justified by the validated
requirements.

The agent must NOT choose one prematurely.

## 19.2 System Design Principle

The system should emerge from:

``` text
Partner Problem
      ↓
Information Need
      ↓
Data Requirement
      ↓
Analysis / Method
      ↓
Information Output
      ↓
System Requirement
      ↓
Web-Based System
```

Not:

``` text
"I want to build a dashboard"
      ↓
find a problem to fit it
```

------------------------------------------------------------------------

# 20. PRELIMINARY CONCEPTUAL SYSTEM ARCHITECTURE

Current conceptual architecture only:

``` text
┌──────────────────────────────────────────────┐
│                  INPUT / DATA                │
│                                              │
│ • Land & plot data                           │
│ • Planting / harvest data                    │
│ • Maize yield                                │
│ • Feed requirement                           │
│ • Feed composition                           │
│ • Maize proportion                           │
│ • Chicken population                         │
│ • Resource allocation                        │
│ • Literature parameters where necessary      │
└───────────────────────┬──────────────────────┘
                        │
                        ▼
┌──────────────────────────────────────────────┐
│             DATA PROCESSING / ANALYSIS       │
│                                              │
│ • Production calculation                     │
│ • Monthly availability calculation           │
│ • Feed requirement calculation               │
│ • Maize requirement calculation              │
│ • Capacity analysis                          │
│ • Optional scenario analysis                 │
└───────────────────────┬──────────────────────┘
                        │
                        ▼
┌──────────────────────────────────────────────┐
│               INFORMATION OUTPUT             │
│                                              │
│ • Production/month                           │
│ • Available maize                            │
│ • Feed requirement                           │
│ • Chicken capacity                            │
│ • Adequacy / surplus / deficit               │
│ • Scenario comparison if justified           │
└───────────────────────┬──────────────────────┘
                        │
                        ▼
┌──────────────────────────────────────────────┐
│                DECISION SUPPORT              │
│                                              │
│ • Evaluate feed-support capacity             │
│ • Plan utilization of maize production       │
│ • Identify additional feed requirements      │
│ • Support operational decisions               │
└──────────────────────────────────────────────┘
```

This is a conceptual model, NOT a final software architecture.

------------------------------------------------------------------------

# 21. SYSTEM SCOPE --- CURRENTLY UNKNOWN

Do not assume the final system needs all of these.

Potential future modules:

1.  Authentication / user management
2.  Partner/farm profile
3.  Plot management
4.  Planting management
5.  Harvest management
6.  Production recording
7.  Feed composition management
8.  Poultry requirement management
9.  Production-to-feed calculation
10. Chicken capacity calculation
11. Scenario analysis
12. Dashboard
13. Reports
14. Historical data
15. Recommendation/decision support

These are candidate modules only.

Each module must be justified by validated requirements.

------------------------------------------------------------------------

# 22. TECHNOLOGY STACK STATUS

Technology stack is **NOT FIXED**.

Current rule:

> Antigravity may recommend a stack only after understanding the
> validated system requirements.

Do not assume: - React; - Next.js; - Vue; - Laravel; - Django; -
FastAPI; - Node; - PostgreSQL; - MySQL; - Firebase; - Supabase; - etc.

The stack should be selected based on: - thesis feasibility; - student's
skill level; - maintainability; - development speed; - deployment
simplicity; - data requirements; - system complexity; - evaluation
requirements.

The thesis does not benefit from unnecessary technical complexity.

------------------------------------------------------------------------

# 23. DEVELOPMENT PRINCIPLES

## Principle 1 --- Research First

No coding before requirements are sufficiently validated.

## Principle 2 --- No Assumption Leakage

An assumption used during brainstorming must never silently become: - a
database constraint; - a business rule; - a formula; - a UI label; - a
thesis claim.

## Principle 3 --- Traceability

Every important system feature should trace back to: - a partner need; -
a research objective; - a data requirement; - or an explicitly justified
supporting function.

## Principle 4 --- Minimal Sufficient System

Build the smallest system that can validly answer the research question.

Do not build a giant farm-management platform unless the research
actually requires it.

## Principle 5 --- SIB Identity

The system must demonstrate: - information flow; - data processing; -
information output; - decision support; - usability for an
operational/business context.

## Principle 6 --- Evidence Before Claims

Do not claim: - cost savings; - zero feed cost; - production
sufficiency; - sustainability; - efficiency improvement; - adoption; -
usability success;

unless they are supported by data/evaluation.

## Principle 7 --- Separate Research Model and Software Implementation

A mathematical formula can exist before the software.

A software feature must not determine the research question.

------------------------------------------------------------------------

# 24. AGENTIC WORKFLOW

The project is intended to use a **subagent-driven workflow**.

Recommended agent roles:

## Agent 1 --- Research Context Analyst

Responsibilities: - maintain validated context; - classify facts vs
assumptions; - identify unresolved questions; - prevent scope drift.

Output: - context updates; - validation matrix; - open questions.

## Agent 2 --- Literature / Research Gap Analyst

Responsibilities: - analyze existing literature; - map variables,
methods, contexts, outputs; - identify evidence-supported gap; -
challenge weak novelty claims.

Output: - literature matrix; - gap candidates; - evidence-backed
research opportunity.

## Agent 3 --- Business / Requirements Analyst

Responsibilities: - translate partner context into: - actors; - business
process; - information needs; - decisions; - functional requirements; -
non-functional requirements.

Output: - AS-IS/TO-BE where justified; - requirements; - use cases; -
information flow.

## Agent 4 --- Data Analyst

Responsibilities: - define required data; - validate data types; -
calculate analytical parameters; - identify missing data; - distinguish
actual, secondary, proxy, and assumed data.

Output: - data dictionary; - calculation model; - validation rules; -
analytical model.

## Agent 5 --- System Architect

Responsibilities: - design web-system architecture only after
requirements are stable; - recommend stack; - define modules; - define
data flow; - define database architecture.

Output: - architecture; - component diagram; - ERD; - API structure
where needed.

## Agent 6 --- UX/UI Analyst

Responsibilities: - translate validated user needs into interface; -
prioritize clarity over visual complexity; - design input forms,
results, dashboard/report views.

Output: - information architecture; - wireframes; - UI specifications.

## Agent 7 --- Implementation Agent

Responsibilities: - implement only approved requirements; - maintain
code quality; - avoid adding unapproved features.

Output: - working web application.

## Agent 8 --- QA / Testing Agent

Responsibilities: - test formulas; - test validation; - test user
flows; - test edge cases; - test calculations against manual reference
values.

Output: - test plan; - test cases; - test results; - defect list.

## Agent 9 --- Academic Reviewer

Responsibilities: - review whether implementation aligns with: -
research problem; - RQ; - objective; - method; - SIB discipline; -
evidence.

Output: - academic consistency review; - thesis-risk flags.

------------------------------------------------------------------------

# 25. SUBAGENT RULES

Every subagent must state:

1.  What it knows.
2.  What is validated.
3.  What is assumed.
4.  What remains unknown.
5.  What evidence it used.
6.  What decision it recommends.
7.  What dependencies remain.
8.  What it will NOT decide yet.

Subagents must not silently resolve unresolved supervisor questions.

If an answer depends on Q1--Q10:

> mark it `BLOCKED BY PARTNER VALIDATION`.

If work can proceed without the answer:

> proceed using an explicit placeholder or scenario.

------------------------------------------------------------------------

# 26. PLANNING RULES

When creating a development/research plan:

Each task should have:

-   Task ID
-   Objective
-   Inputs
-   Dependencies
-   Expected output
-   Acceptance criteria
-   Validation method
-   Status
-   Blocking questions

Example:

``` text
TASK: DATA-001
Objective:
Define minimum production dataset required for monthly capacity calculation.

Depends on:
Q1, Q2, Q3, Q6, Q10.

Status:
BLOCKED/PARTIAL

Acceptance:
Every required parameter has:
- definition
- unit
- source
- validation status
- fallback source if appropriate
```

------------------------------------------------------------------------

# 27. STOP CONDITIONS

An agent must stop and ask for validation rather than making assumptions
when:

1.  A formula depends on an unresolved parameter.
2.  A system feature would imply an unvalidated business process.
3.  A database field would encode an unconfirmed rule.
4.  A research claim would require evidence not yet available.
5.  The system direction conflicts with the latest supervisor guidance.
6.  The task would reintroduce an explicitly rejected direction.
7.  The agent cannot distinguish partner data from proxy/literature
    data.

------------------------------------------------------------------------

# 28. CURRENT KNOWN DECISIONS

These are the current decisions/constraints:

-   Program = D4 Sarjana Terapan Sistem Informasi Bisnis.
-   Domain = Smart Farming.
-   Commodity = Maize.
-   Partner context = Sumenep.
-   No ML.
-   No Big Data/Hadoop/Spark.
-   Exploratory Kaggle/proxy data is not partner evidence.
-   Notebook 1 completed.
-   Notebook 2 completed.
-   Notebook 3 completed.
-   Literature Mapping completed.
-   Research Opportunity Mapping completed.
-   Current partner direction involves maize production and poultry feed
    capacity.
-   Final implementation target = web-based system.
-   System type = NOT YET DECIDED.
-   Technology stack = NOT YET DECIDED.
-   Final title = NOT DECIDED.
-   Final research problem = NOT DECIDED.
-   Final gap = NOT DECIDED.
-   Final RQ = NOT DECIDED.
-   Final method = NOT DECIDED.
-   Q1--Q10 = OPEN.

------------------------------------------------------------------------

# 29. CURRENTLY UNKNOWN / HIGH-RISK ITEMS

The following are the biggest research risks:

## Risk 1 --- Yield data

If actual yield is unavailable, determine whether literature-based yield
can validly represent the partner context.

## Risk 2 --- Maize form

Whole-plant maize vs grain/pipilan changes the analytical model
substantially.

## Risk 3 --- Feed composition

If 200 g is total feed, maize proportion becomes essential.

## Risk 4 --- Resource allocation

Chicken vs catfish allocation must be clarified.

## Risk 5 --- Target chicken count

Need to distinguish: - capacity estimation; - adequacy against a known
chicken population; - planning target.

## Risk 6 --- Scope expansion into cost analysis

Cost analysis should only be included if the partner's information need
and data support it.

## Risk 7 --- System premature design

Do not build features before research requirements are stable.

------------------------------------------------------------------------

# 30. CURRENT RECOMMENDED ROADMAP

## PHASE 1 --- Partner Validation

Status: IN PROGRESS

-   Ask Q1--Q10.
-   Conduct supervisor discussion.
-   Validate actual partner process.
-   Identify accessible data.

## PHASE 2 --- Data Requirement

-   Build validated data dictionary.
-   Classify source of each parameter.
-   Determine missing data.
-   Determine which parameters require literature.

## PHASE 3 --- Analytical Model

-   Define production calculation.
-   Define feed requirement calculation.
-   Define allocation.
-   Define capacity calculation.
-   Test with manual calculations.
-   Determine whether scenario analysis is justified.

## PHASE 4 --- Research Formulation

-   Business/information need.
-   Research problem.
-   Literature-supported gap.
-   RQ.
-   Objective.
-   Method.

## PHASE 5 --- System Requirements

-   Actors.
-   Processes.
-   Information flow.
-   Functional requirements.
-   Non-functional requirements.
-   Data model.
-   Acceptance criteria.

## PHASE 6 --- System Design

-   Architecture.
-   Database/ERD.
-   UI/UX.
-   API/backend if needed.
-   Calculation engine.
-   Visualization.

## PHASE 7 --- Implementation

-   Build MVP.
-   Validate formulas.
-   Implement required modules.
-   Add only justified features.

## PHASE 8 --- Testing & Evaluation

Potential testing areas: - calculation accuracy; - functional testing; -
usability; - requirement fulfillment; - consistency with partner needs.

The exact evaluation method must be selected based on the final research
design.

## PHASE 9 --- Thesis + Journal

Align: - research narrative; - methodology; - results; - system
implementation; - evaluation; - discussion; - conclusion.

------------------------------------------------------------------------

# 31. JOURNAL STRATEGY

The researcher wants to start the journal manuscript early because
publication/review processes can take a long time.

This should be done in parallel with thesis preparation.

## Safe-to-write sections now

-   Background/general context.
-   Literature review.
-   Research opportunity narrative.
-   Conceptual framework.
-   Preliminary methodology structure.

## Sections that should wait for validated data

-   partner-specific results;
-   final numerical findings;
-   final discussion;
-   final system evaluation;
-   final conclusions.

Do not fabricate partner results to accelerate manuscript writing.

The journal should eventually be aligned with the validated thesis
contribution.

------------------------------------------------------------------------

# 32. POTENTIAL RESEARCH CONTRIBUTION --- NOT YET FINAL

One possible contribution direction is:

> translating small-scale maize production information into actionable
> poultry-support capacity information through a web-based information
> system.

Potentially, the system could bridge:

``` text
Agricultural Production Data
        +
Feed Requirement Data
        ↓
Capacity Analysis
        ↓
Decision-Support Information
        ↓
Web-Based System
```

But this contribution must be tested against the literature and partner
needs before being claimed as novelty.

------------------------------------------------------------------------

# 33. DOCUMENT / ARTIFACT DISCIPLINE

Antigravity should maintain separate artifacts for:

1.  `research_context.md`
2.  `partner_validation.md`
3.  `data_requirements.md`
4.  `literature_matrix.md`
5.  `research_problem.md`
6.  `research_gap.md`
7.  `research_questions.md`
8.  `method_mapping.md`
9.  `system_requirements.md`
10. `architecture.md`
11. `database_design.md`
12. `ui_ux_spec.md`
13. `test_plan.md`
14. `implementation_plan.md`
15. `decision_log.md`

Do not mix final research decisions with brainstorming notes.

------------------------------------------------------------------------

# 34. DECISION LOG REQUIREMENT

Maintain a decision log.

Each decision should record:

``` text
Decision ID:
Date:
Topic:
Decision:
Evidence:
Who/what validated it:
Previous assumption:
Impact:
Affected artifacts:
Status:
```

This is important because the research direction has already evolved
substantially from the initial maize/yield/ML exploration.

------------------------------------------------------------------------

# 35. CHANGE MANAGEMENT

When new supervisor information arrives:

1.  Do not overwrite history silently.
2.  Record the new information.
3.  Mark affected assumptions as obsolete.
4.  Identify affected research/system artifacts.
5.  Re-evaluate downstream decisions.
6.  Do not automatically preserve old system requirements.

Use:

``` text
OLD:
[ASSUMPTION]

NEW:
[VALIDATED]

IMPACT:
- research problem:
- data model:
- calculation:
- system requirement:
- UI:
```

------------------------------------------------------------------------

# 36. CRITICAL "DO NOT DO" LIST

Antigravity must NOT:

-   invent partner facts;
-   assume 200 g is maize;
-   assume whole-plant maize;
-   assume one plot is definitely harvested every month;
-   assume all maize goes to chickens;
-   assume zero feed cost;
-   assume actual yield;
-   use proxy Kaggle data as partner evidence;
-   force ML;
-   force optimization;
-   force a dashboard;
-   force a DSS;
-   force a particular technology stack;
-   generate a final title prematurely;
-   manufacture a literature gap;
-   manufacture novelty claims;
-   build unnecessary modules;
-   restart Notebook 1--3 without a justified reason;
-   redo broad literature mapping without identifying a specific
    evidence gap;
-   treat brainstorming as a validated decision.

------------------------------------------------------------------------

# 37. CURRENT ONE-PARAGRAPH CONTEXT FOR QUICK AGENT HANDOFF

The thesis is a D4 Sarjana Terapan Sistem Informasi Bisnis research
project at Politeknik Negeri Malang in the Smart Farming domain, using
maize as the commodity and a partner context in Sumenep. The latest
supervisor-provided context is that the partner is a bank-sampah entity
synergizing with smart farming, with three maize plots of 5 × 6 m each
(30 m² per plot; 90 m² total), whose planting ages differ by about one
month and are intended to support staggered production. The maize is
planned to be chopped and used as part of feed, potentially for chickens
and catfish, together with bran and other organic materials. The
supervisor wants to understand how many chickens can potentially be
supported per month by the available maize production. A preliminary
figure of approximately 200 g/chicken/day was mentioned, but its exact
meaning is still unresolved. The current working analytical direction is
quantitative capacity analysis connecting maize production → monthly
availability → feed requirement → chicken support capacity. However, the
exact maize form, harvest pattern, yield, feed composition, maize
proportion, allocation between chicken/catfish, chicken target,
cost-analysis scope, and data-source strategy are all still open and
must not be assumed. Notebook 1 (Data Understanding), Notebook 2 (Data
Quality & EDA), and Notebook 3 (Candidate Research Problems) are
completed. The earlier exploratory dataset had 111 observations and 22
columns and is proxy data only, not evidence of partner conditions.
Literature Mapping and Research Opportunity Mapping are also completed.
ML, Big Data/Hadoop/Spark, and old disease/NDVI/irrigation directions
are not current research directions. The final implementation target is
a web-based system, but the exact system type, architecture, features,
and technology stack are intentionally not yet decided. The agent must
work research-first, maintain explicit status tags for validated
facts/assumptions/open questions/literature-based parameters, and only
derive system requirements after the partner problem and information
needs are validated.

------------------------------------------------------------------------

# 38. IMMEDIATE NEXT ACTION

The immediate next action is NOT to build the web application.

The immediate next action is:

``` text
Supervisor validation
        ↓
Answer Q1–Q10
        ↓
Update partner context
        ↓
Finalize data requirement matrix
        ↓
Build/test analytical model
        ↓
Formulate research problem + gap + RQ
        ↓
Define system requirements
        ↓
Design web system
        ↓
Implement
```

Until the supervisor answers the open questions, Antigravity may
brainstorm alternatives and prepare artifacts, but it must clearly mark
all unresolved parts as:

`[OPEN]`, `[ASSUMPTION]`, or `[DECISION-PENDING]`.

The goal is not merely to produce software.

The goal is to produce a **research-valid, partner-relevant,
SIB-appropriate web-based information system whose functionality can be
traced back to a real information/decision need.**
