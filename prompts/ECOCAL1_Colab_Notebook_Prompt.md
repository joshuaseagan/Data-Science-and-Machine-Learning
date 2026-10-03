# Prompt: ECOCAL1 Python + Calculus Foundations Colab Notebook (Weeks 1–8, LFS 2018)

> **How to use:** Copy everything below the line into your AI assistant (Claude, etc.).
> If the assistant can create files, ask it to return a single `.ipynb`; otherwise ask it to
> return the notebook cell by cell (Markdown / Code labels) so you can paste into Colab.
> Because the output is long, you can ask for it **one Part at a time** ("Generate Part 0 and Part 1 now").

---

## ROLE

You are an expert **mathematical-economics instructor** and **Python educator** who designs
self-study materials for first-year economics students with **no prior programming
experience**. You write clearly, explain the *why* before the *how*, and never overload the learner.

## TASK

Build a complete, well-structured **Google Colab notebook** for De La Salle University's
**ECOCAL1 – Economics Calculus 1** (Term 1, AY 2026–2027). The notebook teaches, side by side:

1. **The basics of Python** (only what is needed, introduced gradually), and
2. **The mathematics of ECOCAL1 Weeks 1–8**, preceded by a short, intuitive **"What is calculus?" preview**.

Every exercise, example, and coding question must use **real Philippine Labor Force Survey (LFS) 2018 data**.
Students will use the notebook **on their own time** for review and extra practice, so it must work on its
own: they should be able to follow it start to finish without a teacher.

---

## 1. COURSE CONTEXT (from the syllabus — treat as authoritative)

**Course description:** A foundation in pre-calculus algebra for later calculus and mathematical economics:
the real number system and basic set theory, manipulating algebraic expressions, solving algebraic
equations, functions and graphs, then limits, continuity, and sequences. The emphasis is on applying algebra
and calculus to business and economics problems.

**Course Learning Outcomes (tag every module with the CLOs it serves):**
- **CLO1** – Solve and explain arithmetic and algebraic problems/equations and interpret solutions independently.
- **CLO2** – Draw, read, and explain graphs independently.
- **CLO3** – Participate and present work in group discussions using math as a language of discourse.

**Weeks in scope:**

| Week | Topic(s) |
|---|---|
| 1 | Orientation; Basic Set Theory; Types of Numbers; Properties of Real Numbers |
| 2 | Basic Set Theory / Real Numbers (practice); Inequalities; Intervals of Real Numbers |
| 3 | Inequalities & Intervals (practice); Exponents and Radicals; Rational Exponents; Absolute Value and Distance |
| 4 | Exponents/Radicals/Absolute Value (practice); Algebraic Expressions; Fundamental Operations on Polynomials; Special Products |
| 5 | Algebraic Expressions/Polynomials (practice); Factoring; Fractional Expressions |
| 6 | Factoring/Fractional Expressions (practice); Algebraic Equations; Linear Equations; Solving Algebraic Equations |
| 7 | Midterm Exam; Inequalities; Systems of Linear Equations |
| 8 | Solving Equations, Inequalities, and Systems of Linear Equations |

**How students are assessed (design the practice to match):**
- *Board-work recitation*: students solve a problem live and are asked about **derivation steps**, the **mathematical
  properties used**, and **interpretation of the solution**.
- *Exams*: conceptual questions plus computational problems.
- *Rubric*: Exemplary (fully correct) → Satisfactory (correct method, slip in derivation) → Developing (right method
  attempted, wrong result) → Beginning (nothing meaningful).
- *Generative-AI policy*: banned for recitation, group work, and exams; **allowed for practice sets** (e.g., Wolfram Alpha
  to check answers). So the notebook must train students to **solve by hand first** and use Python/SymPy only to
  **check, visualize, and explore**.

---

## 2. REFERENCES: THE CONCEPTUAL BACKBONE

Ground every concept in the syllabus references. The **core readings** named for Weeks 1–8 are:

- **Swokowski, E., & Cole, J. (2011).** *Algebra and Trigonometry with Analytic Geometry* (13th ed.). Cengage.
- **Rees, P. K., Sparks, F. W., & Rees, C. (2003).** *College Algebra* (10th ed.). McGraw-Hill.
- **Sydsaeter, K., Hammond, P., Strøm, A., & Carvajal, A. (2022).** *Essential Mathematics for Economic Analysis* (6th ed.). Pearson.

Supplementary references (use for economic framing, extra worked problems, and the calculus preview):
Chiang & Wainwright (2004) *Fundamental Methods of Mathematical Economics*; Dowling (2011) *Schaum's Outline of
Introduction to Mathematical Economics*; Pemberton & Rau (2015); Hoy et al. (2022); Anthony & Biggs (2024);
Cerreia-Vioglio, Marinacci & Vigna (2024); Danao (2001) *Introductory Mathematical Economics* (UP Press);
Peña-Levano (2021) *Schaum's Mathematical Methods for Business, Economics, and Finance*.

**Suggested topic → reference mapping** (cite by **section/topic name**. Chapter numbers are a guide only and may
differ by edition, so never invent page numbers):

| Topic | Primary anchor | Economic-framing anchor |
|---|---|---|
| Sets, types of numbers, real-number properties | Swokowski & Cole – *Fundamental Concepts of Algebra: Real Numbers*; Sydsaeter et al. – *Essentials of Logic and Set Theory* | Chiang & Wainwright – *Economic Models* (sets, real number system); Danao |
| Inequalities, intervals, absolute value | Swokowski & Cole – *Real Numbers* (order, intervals, absolute value) & *Inequalities*; Sydsaeter et al. – *Algebra* (inequalities, intervals, absolute value) | Dowling – *Review* chapter |
| Exponents, radicals, rational exponents | Swokowski & Cole – *Exponents and Radicals*; Rees, Sparks & Rees – *Exponents and Radicals*; Sydsaeter et al. – *Algebra* (powers, compound interest) | Sydsaeter et al. (interest/growth examples) |
| Algebraic expressions, polynomials, special products, factoring | Swokowski & Cole – *Algebraic Expressions*; Rees, Sparks & Rees – *Special Products and Factoring* | Dowling – *Review* |
| Fractional (rational) expressions | Swokowski & Cole – *Fractional Expressions*; Rees, Sparks & Rees – *Fractions* | Sydsaeter et al. – *Algebra* (fractions) |
| Equations (linear, quadratic, algebraic) | Swokowski & Cole – *Equations and Inequalities*; Sydsaeter et al. – *Solving Equations* | Chiang & Wainwright – *Equilibrium Analysis* (linear model) |
| Systems of linear equations | Rees, Sparks & Rees – *Systems of Equations*; Sydsaeter et al. – *Solving Equations* (two equations, two unknowns) | Chiang & Wainwright – partial market equilibrium |
| Calculus preview (rate of change, limits, slopes) | Sydsaeter et al. – *Differentiation* (intro / slopes / rates of change) | Chiang & Wainwright – *Comparative Statics and the Concept of Derivative* |

**Copyright rule:** Paraphrase and explain in your own words. Short definitions are fine. Do **not** reproduce
textbook passages, figures, or exercise sets. Build original examples instead.

---

## 3. THE DATA: PHILIPPINE LFS 2018 (single year, kept simple)

**Source file (instructor's Google Drive):**
- `FIES-LFS PUF 2018 LFS_SUMMARY.CSV` (~104 MB; also saved as `LFS 2018.CSV` in the "LFS" folder)
- Data dictionary: `fies-lfs_2018_metadata(dictionary).xlsx`
- Producer: Philippine Statistics Authority (PSA), Public Use File (PUF). Credit PSA in the notebook and remind
  students that PUF data are for educational/research use under PSA's terms.

**Variables to use (from the official 2018 dictionary). Use only these to keep things simple:**

| Column | Meaning | Codes / range |
|---|---|---|
| `W_REGN` | Region | 13 = NCR, 14 = CAR, 1 = Ilocos, 2 = Cagayan Valley, 3 = Central Luzon, 4 = CALABARZON, 17 = MIMAROPA, 5 = Bicol, 6 = W. Visayas, 7 = C. Visayas, 8 = E. Visayas, 9 = Zamboanga Peninsula, 10 = N. Mindanao, 11 = Davao, 12 = SOCCSKSARGEN, 15 = ARMM, 16 = CARAGA |
| `LC04_SEX` | Sex | 1 = Male, 2 = Female |
| `LC05_AGE` | Age as of last birthday | 0–99 |
| `LC06_MSTAT` | Marital status | 1 Single, 2 Married, 3 Widowed, 4 Divorced/Separated, 5 Annulled, 6 Unknown |
| `LC07_GRADE` | Highest grade completed | 5-digit code (e.g., 24020 = High School/Grade 10 graduate). Recode into ≤5 broad levels |
| `NEWEMPSTAT` | Employment status | 1 Employed, 2 Unemployed, 3 Not in the labor force |
| `LC18_PNWHRS` | Normal working hours per day | 1–16 (0 / blank = not applicable) |
| `LC19_PHOURS` | Hours worked in past week (primary job) | 1–112 (999 = not reported) |
| `LC28_THOURS` | Total hours worked, all jobs, past week | 0–168 |
| `LC23_PCLASS` | Class of worker | 0 Private household, 1 Private establishment, 2 Government, 3 Self-employed, 4 Employer, 5 Family business (with pay), 6 Family business (without pay) |
| `LC24_PBASIS` | Basis of payment | 0 In kind, 1 Per piece, 2 Per hour, 3 Per day, 4 Monthly, 5 Pakyaw, 6 Other, 7 Commission |
| `LC25_PBASIC` | Basic pay **per day** (₱), primary job | numeric |
| `PWGTPRV` | Final person weight (provincial projections) | numeric |

**Data-handling requirements:**
1. **Instructor setup cell (run once, clearly marked "Instructor only"):** mount Google Drive, read the big CSV with
   `usecols=[...]` and `low_memory=False`, **check the actual column names first** (print `df.columns`, then adapt
   upper/lower case if needed), keep persons aged **15+**, recode categories to readable labels, set `999`/blank
   codes to `NaN`, then save a **small teaching file** `lfs2018_ecocal1.csv`. Either keep all rows with the selected
   columns, or draw a reproducible sample (e.g., `n=3000`, `random_state=2026`). State which choice was made and why.
2. **Student loading cell:** loads `lfs2018_ecocal1.csv` from Drive *or* via `files.upload()`, with a friendly error
   message if the file is missing. Provide a clearly labeled **fallback**: a tiny synthetic dataset with the same columns,
   marked "PRACTICE ONLY – NOT REAL DATA", so the notebook still runs if the file is unavailable.
3. Keep the analysis **unweighted** for simplicity. Add one optional "Going further" box explaining what `PWGTPRV`
   is and showing a weighted vs. unweighted mean, so students learn that survey weights exist.
4. Teach the important data lesson early: **a number is not always a quantity.** Codes like `W_REGN = 13` or
   `LC04_SEX = 2` are *labels*, not values you can add (this ties directly to "types of numbers").
5. Any economic indicator computed (labor force participation rate, unemployment rate, average daily pay) must be
   presented as a **teaching estimate from the sample**, not an official PSA statistic.

---

## 4. THE CORE DESIGN IDEA: BOOKS FOR CONCEPTS, DATA FOR PRACTICE

Use a repeating **five-step learning loop** in *every* lesson. This is how the textbooks (conceptual understanding)
and the LFS data (Python and applied practice) fit together:

| Step | Name | What happens | Source of authority |
|---|---|---|---|
| 1 | **📖 Read & Understand** | A short "Concept Card": definition, key rule/property, and one-sentence intuition, with a *"Read more:"* pointer to the reference section | Textbooks |
| 2 | **✍️ Solve by Hand** | A small worked example with clean numbers, every step justified by the property used (as in board-work recitation) | Textbooks (method) |
| 3 | **🐍 Check with Python** | Reproduce the hand solution in Python (plain arithmetic → NumPy → SymPy) and confirm it matches | Python |
| 4 | **📊 Apply to LFS Data** | Ask an economic question about Filipino workers and answer it with the *same* concept on real data | LFS 2018 |
| 5 | **💬 Interpret & Explain** | Write 1–3 sentences in plain English/economics: what does the number *mean*? (CLO3 practice) | Student |

Make the separation explicit to students in the introduction: *"The textbook tells you **why** a rule is true; the data
shows you **where** it matters; Python helps you **check** and **see** it, but it never replaces doing it by hand."*

At the end of each module, add a **"🔭 Why this matters for calculus"** box connecting the topic to what is coming
in Weeks 9–13 (e.g., factoring is how you evaluate limits of the form 0/0; intervals and inequalities describe domains
and continuity; exponent rules power the derivative of xⁿ; absolute value defines "closeness" in the definition of a limit).

---

## 5. NOTEBOOK STRUCTURE

### Front matter
- Title, course, intended audience, estimated time per Part, and **how to use this notebook** (run cells top to bottom; Shift+Enter; what to do when there's an error).
- Learning roadmap (a table: Part → Week → Topics → CLOs → est. time).
- Academic integrity note mirroring the syllabus AI policy.
- A **self-check legend**: ⭐ warm-up, ⭐⭐ core, ⭐⭐⭐ challenge; ✅ auto-checked; 🗣️ explain-out-loud (board-work practice).

### Part 0 – Python Survival Kit (≈45 min)
Only what is needed later, each taught with LFS-flavored mini-examples:
Colab basics; variables and arithmetic operators (incl. `**` and order of operations ↔ PEMDAS); types (`int`, `float`,
`str`, `bool`); lists and dictionaries; `if` statements; `for` loops; defining functions; importing `pandas`, `numpy`,
`matplotlib`, `sympy`; reading the data; `.head()`, `.shape`, `.describe()`, `.value_counts()`; selecting columns;
boolean filtering; a first bar chart. Include a short "reading error messages" guide (NameError, TypeError, KeyError, SyntaxError).

### Part 1 – Calculus at a Glance: A Gentle Preview (≈40 min)
Purpose: motivation and intuition, **not** rigor (limits come formally in Weeks 11–13).
- Functions as input → output machines (e.g., weekly earnings as a function of hours worked).
- **Average rate of change** = slope of a secant line: compute average daily pay by age group from LFS and the
  change in pay per additional year of age between groups.
- **Instantaneous rate of change** (the derivative idea): fit a simple quadratic age–pay profile with
  `numpy.polyfit(age, pay, 2)`, then compute the slope over shrinking intervals `h = 1, 0.1, 0.01, ...` in a table
  and watch it settle. That is the **limit** idea. Confirm with `sympy.diff`.
- **Marginal thinking** in economics (Chiang & Wainwright; Sydsaeter et al.): "how much more pay for one more year of age/experience?"
- **Accumulation** idea: total weekly hours as a sum, as a preview of integrals (one cell, optional).
- Close with: "To do calculus well, you need algebra to be automatic. That is what Parts 2–9 build."

### Parts 2–9 – One Part per syllabus week (Part 2 = Week 1 … Part 9 = Week 8)
For **each** Part, use this fixed template:

1. **Header**: Week, topics, CLOs, reading pointer(s), est. time.
2. **🎯 Learning objectives** (3–5, measurable verbs).
3. **🧭 Big picture**: 3–4 sentences on why an economist cares.
4. Lessons, each following the **five-step loop** (Section 4).
5. **⚠️ Common mistakes** (e.g., `√(a+b) ≠ √a + √b`, `(a+b)² ≠ a² + b²`, cancelling terms instead of factors, flipping the inequality sign when multiplying by a negative).
6. **✅ Check your understanding**: 3–5 short conceptual questions (MCQ / true-false / fill-in) with answers hidden in `<details>` blocks.
7. **💻 Coding exercises**: 3–5 tiered tasks (⭐→⭐⭐⭐) on the LFS data. Provide starter code with `# YOUR CODE HERE`,
   followed by an **auto-check cell** using `assert` with friendly feedback (e.g., "✅ Correct!" / "❌ Hint: did you drop missing values?").
   Hide full solutions in `<details>` blocks.
8. **✍️ Board-work practice**: 2–3 pen-and-paper problems in the style of recitation: *show steps, name the property used,
   interpret the answer.* Include a rubric-aligned self-assessment (Exemplary / Satisfactory / Developing / Beginning).
9. **🔭 Why this matters for calculus**.
10. **📝 Summary**: a compact cheat-sheet of rules and the Python functions used.

**Topic → LFS application map (use these as the backbone; you may refine):**

| Part / Week | Math content | LFS 2018 applications | Python skills introduced |
|---|---|---|---|
| **2 / W1** Sets, types of numbers, real-number properties | Sets, elements, subsets, ∪ ∩ complement, difference, Venn diagrams, universal set; ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ, irrationals; commutative, associative, distributive, identity, inverse | Universal set U = all sampled persons 15+. E = employed, F = female, N = NCR residents. Compute \|E ∩ F\|, \|E ∪ N\|, complement of E, and verify De Morgan's law on real data. Classify variables: age (whole number), daily pay (rational/real), region code (label, *not* a quantity) | Python `set` operations on person IDs; `len`; boolean masks `&`, `\|`, `~`; `matplotlib_venn` (or a simple manual Venn); `0.1 + 0.2` floating-point surprise and `round` |
| **3 / W2** Inequalities, intervals | Order properties, linear inequalities, compound inequalities, interval notation (open/closed/half-open, unbounded), number-line graphs | Working-age population as interval [15, 64]; youth [15, 24]; "worked < 40 hours last week" (underemployment proxy) as (0, 40); age groups with `pd.cut` as half-open intervals [15, 25), [25, 35), … | Comparison operators, chained comparisons `15 <= age <= 64`, `.between()`, `pd.cut(right=False)`, plotting intervals on a number line |
| **4 / W3** Exponents, radicals, rational exponents, absolute value & distance | Laws of exponents, zero/negative exponents, radicals ↔ rational exponents, simplifying radicals, \|x\|, distance \|a − b\| on the number line | Compound growth: project a median daily pay forward at r% per year, `P(1+r)^t`. Annual ↔ monthly rate with `(1+r)^(1/12)`. Distance between regional median pay levels \|NCR − BARMM\|. Mean absolute deviation of daily pay from the median | `**`, `np.sqrt`, `np.abs`, `groupby().median()`, simple line plot of growth |
| **5 / W4** Algebraic expressions, polynomial operations, special products | Terms, coefficients, degree; add/subtract/multiply polynomials; (a ± b)², (a + b)(a − b), (a ± b)³ | Earnings expressions: weekly pay = daily pay × days; hours = normal hours/day × days. Quadratic age–pay profile `p(a) = c₀ + c₁a + c₂a²` from `np.polyfit`. Evaluate, add, and multiply polynomials; expand special products and verify by plugging in LFS values | `sympy.symbols`, `expand`, `simplify`, `.subs()`, `lambdify`; plotting a polynomial over a scatter of the data |
| **6 / W5** Factoring, fractional expressions | GCF, grouping, difference of squares, trinomials, sum/difference of cubes; simplifying, multiplying, dividing, adding rational expressions; domain restrictions | Rates as fractions: LFPR = (E + U)/Pop, unemployment rate = U/(E + U), hourly pay = daily pay / normal hours per day. Domain restriction ↔ **division by zero** in data (hours = 0 → drop or NaN). Factor the total wage bill expression; simplify ratio expressions symbolically | `sympy.factor`, `cancel`, `together`, `apart`; safe division in pandas; `groupby` to compute rates by region and sex |
| **7 / W6** Algebraic equations (linear, quadratic, other) | Solving linear equations; equations with fractions; quadratic (factoring, completing the square, quadratic formula); equations with radicals/absolute values; checking extraneous roots | "How many hours must a worker paid ₱X/hour work to earn ₱Y/week?" (linear). Peak of the fitted age–pay quadratic via completing the square / vertex formula (algebra only; foreshadow derivatives). "At what age does predicted pay equal the median?" (quadratic) | `sympy.solve`, `Eq`, `solveset` (domain = reals), substitution checks |
| **8 / W7** Inequalities & systems of linear equations (+ midterm review) | Linear and quadratic inequalities, sign charts, inequalities with absolute value; 2×2 and 3×3 linear systems by substitution, elimination, and matrices; consistent/inconsistent/dependent | Inequality: hours h such that weekly earnings ≥ a chosen threshold. System: from LFS totals, recover unknowns, e.g., given total employed and total unemployed by sex, set up and solve for missing counts; or a two-group "average pay" system. Graph two lines and read the intersection. **Midterm review sheet** (mixed problems Weeks 1–6, by hand, with answers hidden) | `sympy.solve` for systems, `numpy.linalg.solve`, `matplotlib` line plots and `fill_between` for inequality regions |
| **9 / W8** Integration: equations, inequalities, systems | Choosing the right method; interpreting solutions | **Mini case study**: "A profile of the Filipino worker in 2018". Students answer 5–6 guided questions combining sets, intervals, exponents, rational expressions, equations, inequalities, and a 2×2 system, all on LFS data, ending with a short written interpretation (CLO3) | Putting it together; writing a clean function; a final multi-panel chart |

### Closing section
- **Capstone reflection** prompts (what was hardest, what clicked, how data changed your understanding).
- **Formula & Python cheat-sheet** (one table for math rules, one for Python commands).
- **Where to go next**: preview of Weeks 9–13 (graphs and lines, functions, inverse/composite, exponential and logarithmic functions, limits, continuity, sequences and series), with the matching reference sections.
- **References** in APA style (from Section 2) and a PSA data citation.

---

## 6. PEDAGOGICAL AND STYLE RULES

- **Cognitive load:** introduce at most **one new Python idea per lesson**; reuse the same few variables throughout;
  each code cell ≤ ~15 lines; one idea per cell.
- **Concrete → abstract:** start with a small number example, then the general rule, then the data.
- **Explain every line** of new code with short comments; avoid clever one-liners, lambdas, and list comprehensions until
  they are explicitly taught (and keep them optional).
- **Math notation:** use LaTeX in Markdown (`$...$`, `$$...$$`). Name the property used at each algebra step.
- **Tone:** warm, encouraging, plain English; brief Filipino/Philippine context is welcome (e.g., regions, ₱, minimum wage framing).
- **Visual design:** consistent headers (`#` Part, `##` Lesson, `###` Step), emoji signposts from Section 4, callout boxes
  using Markdown blockquotes, and a "⏱️ est. time" tag per lesson.
- **Graphs:** always label axes with units, add a title, and write a one-sentence takeaway under each chart.
- **Rigor without overload:** every rule is stated precisely (including domain conditions, e.g., √x requires x ≥ 0,
  a/b requires b ≠ 0), but proofs are optional "🧠 Deeper dive" boxes.
- **Accuracy:** do not invent statistics. Every LFS number in the text must come from code the student runs.
  Phrase observations as "In our sample…".
- **Reproducibility:** pin `random_state`/`np.random.seed(2026)`, and add a first cell that installs/imports everything
  (`!pip install matplotlib-venn -q` if used).
- **Accessibility:** colorblind-safe palettes, readable font sizes in plots, alt-style text descriptions under charts.

---

## 7. OUTPUT REQUIREMENTS

- Deliver a single Colab-ready `.ipynb` (or, if you cannot produce files, cells in order, each labeled `[MARKDOWN]` or `[CODE]`).
- File name: `ECOCAL1_Python_and_Calculus_Foundations_LFS2018.ipynb`.
- The notebook must **run top to bottom without errors** once `lfs2018_ecocal1.csv` is available (or with the synthetic fallback).
- Each Part should be **completable in about 45–90 minutes**.
- Quantity guide per Part (2–9): 2–4 lessons, 3–5 concept questions, 3–5 coding exercises with auto-checks,
  2–3 board-work problems, a calculus-link box, a summary.
- After generating, append a **"Notes for the instructor"** section listing: assumptions made about the data columns,
  any reference mappings that should be verified against the actual editions, and suggested places to cut content if time is short.

## 8. QUALITY CHECKLIST (verify before you finish)

- [ ] Every syllabus topic for Weeks 1–8 appears and is labeled with its week and CLOs.
- [ ] Every lesson follows the five-step loop (Read → Hand → Python → LFS → Interpret).
- [ ] Every exercise uses the LFS 2018 teaching file (single year only).
- [ ] Codes vs. quantities, missing values (`999`, blanks), and division-by-zero are handled explicitly.
- [ ] No textbook text is copied; references are cited by section/topic.
- [ ] Solutions are hidden; auto-checks give helpful hints, not just pass/fail.
- [ ] Each Part ends with a "Why this matters for calculus" link and a summary.
- [ ] Python is introduced gradually, with no unexplained syntax.
- [ ] Hand-solving is always shown **before** Python checking (consistent with the course AI policy).
