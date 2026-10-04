from kit import md, code, details


def build():
    md(r"""
    # 📘 ECOCAL1 · Python & Calculus Foundations with Philippine Labor Force Survey (LFS) 2018 Data

    **De La Salle University · Carlos L. Tiu School of Economics · ECOCAL1 – Economics Calculus 1**
    **Term 1, AY 2026–2027 · Self-study companion for Weeks 1–8**

    **Who this is for:** first-year economics students. **You don't need any programming experience.**
    **What you will learn, side by side:**
    1. 🧮 The algebra of ECOCAL1 Weeks 1–8 (sets, real numbers, inequalities, exponents, polynomials, factoring, fractions, equations, systems), plus a short preview of *what calculus is*.
    2. 🐍 Just enough **Python** to check your hand work, draw graphs, and explore real data on **Filipino workers**.

    **⏱️ Total time:** about 10–12 hours, split into Parts of 40–90 minutes. Do **one Part per sitting**.

    ---
    ## 🧭 How to use this notebook

    1. **Save your own copy first:** *File → Save a copy in Drive*. Then you can type anywhere without losing work.
    2. **Run cells from top to bottom.** Click a grey code cell and press **Shift + Enter** (or the ▶️ button). Wait for the output before moving on.
    3. **If you open the notebook later, or jump to a Part,** run *Runtime → Run before* first. Later Parts use variables created earlier.
    4. **If you see a red error,** don't panic! Read the **last line** of the message (Part 0 has a guide), fix the cell, and run it again. If things get messy, use *Runtime → Restart session and run all*.
    5. **Have pen and paper ready.** Every lesson asks you to **solve by hand first**.

    ### 🔁 The five-step learning loop (used in every lesson)

    | Step | Name | What you do | Where the authority comes from |
    |---|---|---|---|
    | 1 | 📖 **Read & Understand** | Read a short *Concept Card*: definition, rule, intuition, and where to read more | Textbooks |
    | 2 | ✍️ **Solve by Hand** | Follow (then redo) a small worked example. Every step names the property used | Textbooks (method) |
    | 3 | 🐍 **Check with Python** | Reproduce the hand answer in Python and confirm it matches | Python |
    | 4 | 📊 **Apply to LFS Data** | Answer a question about Filipino workers with the *same* idea | PSA LFS 2018 |
    | 5 | 💬 **Interpret & Explain** | Write 1–3 sentences: *what does the number mean?* | You! |

    > 💡 **The golden rule of this notebook.** *The textbook tells you **why** a rule is true. The data shows you **where** it matters. Python helps you **check** and **see** it, but it **never replaces doing it by hand**.*
    """)

    md(r"""
    ## 🗺️ Learning roadmap

    | Part | Syllabus week | Topics | CLOs | ⏱️ Est. time |
    |---|---|---|---|---|
    | 0 | Before Week 1 | Python Survival Kit: variables, types, lists, `if`, `for`, functions, pandas basics, first chart | (tool skills) | 45–60 min |
    | 1 | Preview | Calculus at a glance: functions, average and instantaneous rates of change, marginal thinking | CLO2 | 40 min |
    | 2 | Week 1 | Basic set theory; types of numbers; properties of real numbers | CLO1, CLO3 | 75 min |
    | 3 | Week 2 | Set/real-number practice; inequalities; intervals of real numbers | CLO1, CLO2 | 75 min |
    | 4 | Week 3 | Exponents and radicals; rational exponents; absolute value and distance | CLO1, CLO2 | 75 min |
    | 5 | Week 4 | Algebraic expressions; operations on polynomials; special products | CLO1, CLO2 | 75 min |
    | 6 | Week 5 | Factoring; fractional (rational) expressions | CLO1, CLO3 | 80 min |
    | 7 | Week 6 | Algebraic equations: linear, quadratic, radical, absolute value | CLO1, CLO3 | 80 min |
    | 8 | Week 7 | Inequalities; systems of linear equations; **midterm review sheet** | CLO1, CLO2 | 90 min |
    | 9 | Week 8 | Putting it together: equations, inequalities, systems. **Case study** | CLO1, CLO2, CLO3 | 75 min |

    **Course Learning Outcomes (from the syllabus)**
    - **CLO1**: Solve and explain arithmetic and algebraic problems/equations and interpret solutions independently.
    - **CLO2**: Draw, read, and explain graphs independently.
    - **CLO3**: Participate and present work in group discussions using math as a language of discourse.
    """)

    md(r"""
    ## ⚖️ Academic integrity and the course AI policy

    The ECOCAL1 syllabus says:
    - **Banned:** generative AI in *any* form for board-work recitation, collaborative group work, class participation, the midterm exam, and the final exam.
    - **Allowed:** using tools to **check answers on practice sets** (for example, Wolfram Alpha).

    This notebook is **practice material**. Python and SymPy play the same role as Wolfram Alpha here: they *check* work you have already done by hand. In recitation and exams you will only have **pen, paper, and your understanding**. Leaning on the computer too much will hurt you there, so always:

    1. ✍️ Solve on paper → 2. 🐍 check with Python → 3. 🔍 if they disagree, find **your** mistake.

    ## 🏷️ Self-check legend

    | Symbol | Meaning |
    |---|---|
    | ⭐ | Warm-up: direct use of the lesson |
    | ⭐⭐ | Core: what recitation and exams usually look like |
    | ⭐⭐⭐ | Challenge: combines ideas or needs careful thinking |
    | ✅ | Auto-checked: run the check cell under the exercise for feedback |
    | 🗣️ | Explain out loud: practise it as if you were at the board |
    | 🧠 | Deeper dive (optional) |
    | 🔭 | Why this matters for calculus |

    ## 🇵🇭 About the data

    Every example uses the **Philippine Statistics Authority (PSA) Labor Force Survey 2018 Public Use File** (`FIES-LFS PUF 2018 LFS_SUMMARY`).
    The PSA releases Public Use Files for **educational and research purposes, under PSA's terms of use**. Please don't redistribute the raw file, and always credit the PSA.

    > ⚠️ **Teaching estimates, not official statistics.** Every rate or average you compute here comes from **our sample** and is **unweighted** (Part 0 explains survey weights). Treat them as *teaching estimates*. They are **not** official PSA statistics. For official figures, see the PSA's published LFS releases.
    """)

    # ------------------------------------------------------------------ setup
    md(r"""
    ---
    # ⚙️ Setup (run these cells first, every time you open the notebook)

    The first cell loads the four Python *libraries* (toolboxes) we use all term. Part 0 explains what each one does. The second cell is hidden behind a title in Colab. It holds helper code for the auto-checks and a few drawings. **Just run it; you do not need to read it.**
    """)

    code(r'''
    # ⚙️ SETUP CELL: loads our toolboxes and sets up readable, colorblind-safe charts
    import numpy as np                  # numbers, square roots, arrays
    import pandas as pd                 # data tables ("DataFrames")
    import matplotlib.pyplot as plt     # charts
    import sympy as sp                  # symbolic algebra: x, y, expand, factor, solve
    sp.init_printing()                  # show SymPy results as nicely formatted math
    np.random.seed(2026)                # makes anything "random" reproducible

    # Okabe–Ito palette: distinguishable for people with color-vision deficiencies
    OKABE_ITO = ["#0072B2", "#E69F00", "#009E73", "#D55E00", "#CC79A7", "#56B4E9", "#F0E442", "#000000"]
    plt.rcParams.update({"figure.figsize": (8, 4.5), "font.size": 12, "axes.titlesize": 14,
                         "axes.labelsize": 12, "axes.grid": True, "grid.alpha": 0.3,
                         "axes.prop_cycle": plt.cycler(color=OKABE_ITO)})
    pd.set_option("display.max_columns", 20)
    print("✅ Setup complete. pandas", pd.__version__, "| numpy", np.__version__, "| sympy", sp.__version__)
    ''')

    code(r'''
    # Helper code. You do NOT need to understand this cell; just run it.
    REGION_NAMES = {13: "NCR", 14: "CAR", 1: "Ilocos", 2: "Cagayan Valley", 3: "Central Luzon",
                    4: "CALABARZON", 17: "MIMAROPA", 5: "Bicol", 6: "Western Visayas",
                    7: "Central Visayas", 8: "Eastern Visayas", 9: "Zamboanga Peninsula",
                    10: "Northern Mindanao", 11: "Davao", 12: "SOCCSKSARGEN", 15: "ARMM", 16: "Caraga"}
    SEX = {1: "Male", 2: "Female"}
    MARITAL = {1: "Single", 2: "Married", 3: "Widowed", 4: "Divorced/Separated", 5: "Annulled", 6: "Unknown"}
    EMPSTAT = {1: "Employed", 2: "Unemployed", 3: "Not in labor force"}
    WORKER_CLASS = {0: "Private household", 1: "Private establishment", 2: "Government",
                    3: "Self-employed", 4: "Employer", 5: "Family business (with pay)",
                    6: "Family business (without pay)"}
    PAY_BASIS = {0: "In kind", 1: "Per piece", 2: "Per hour", 3: "Per day", 4: "Monthly",
                 5: "Pakyaw", 6: "Other", 7: "Commission"}
    EDUC_LEVELS = ["Elementary or less", "High school", "Post-secondary/technical", "College or higher"]

    def educ_level(code):
        """Recode the 5-digit LC07_GRADE code into 4 broad levels (instructor: verify vs. dictionary)."""
        if pd.isna(code):
            return np.nan
        code = int(code)
        if code < 20000:
            return EDUC_LEVELS[0]      # no grade, preschool, elementary
        if code < 40000:
            return EDUC_LEVELS[1]      # junior and senior high school
        if code < 60000:
            return EDUC_LEVELS[2]      # post-secondary non-tertiary, short-cycle/technical
        return EDUC_LEVELS[3]          # bachelor's and above

    def check(answer, expected, hint="Re-read the task and try again.", tol=1e-4, exact=False):
        """Compare a student's answer with the expected one and print friendly feedback."""
        if answer is None:
            print("⏳ Not attempted yet. Replace None with your code, run that cell, then run this check again.")
            return
        try:
            if isinstance(expected, sp.Set) or exact:
                assert answer == expected
            elif isinstance(expected, sp.Basic):
                assert sp.simplify(sp.sympify(answer) - expected) == 0
            elif isinstance(expected, (set, frozenset, str, bool, np.bool_)):
                assert answer == expected
            elif isinstance(expected, (list, tuple, np.ndarray, pd.Series)):
                a, e = np.asarray(answer, dtype=float), np.asarray(expected, dtype=float)
                assert a.shape == e.shape and np.allclose(a, e, rtol=tol, atol=1e-6)
            else:
                assert np.isclose(float(answer), float(expected), rtol=tol, atol=1e-6)
            print("✅ Correct! Well done.")
            return
        except Exception:
            print("❌ Not quite yet. Hint: " + hint)
            return

    def number_line(intervals, xlim=(0, 100), title="Intervals on the number line", xlabel="Value"):
        """Draw intervals. Each item: (a, b, left_closed, right_closed, label). Use np.inf for ∞."""
        fig, ax = plt.subplots(figsize=(8, 1.2 + 0.7 * len(intervals)))
        for i, (a, b, lc, rc, label) in enumerate(intervals):
            y, color = len(intervals) - i, OKABE_ITO[i % len(OKABE_ITO)]
            lo, hi = max(a, xlim[0]), min(b, xlim[1])
            ax.plot([lo, hi], [y, y], color=color, lw=5, solid_capstyle="butt")
            for x, closed in ((a, lc), (b, rc)):
                if np.isfinite(x):
                    ax.plot(x, y, "o", ms=11, color=color, mfc=color if closed else "white", mew=2.5)
            if not np.isfinite(b):
                ax.plot(xlim[1], y, ">", ms=12, color=color)
            if not np.isfinite(a):
                ax.plot(xlim[0], y, "<", ms=12, color=color)
            ax.text(lo, y + 0.22, label, fontsize=11, color=color)
        ax.set_yticks([]); ax.set_xlim(xlim[0] - 2, xlim[1] + 2); ax.set_ylim(0.4, len(intervals) + 0.8)
        ax.set_title(title); ax.set_xlabel(xlabel)
        plt.show()

    def venn2_counts(only_a, only_b, both, neither, labels=("A", "B"), title="Venn diagram"):
        """Draw a simple two-set Venn diagram with counts in each region."""
        from matplotlib.patches import Circle, Rectangle
        fig, ax = plt.subplots(figsize=(7, 4.5))
        ax.add_patch(Rectangle((-2.6, -1.9), 5.2, 3.8, fill=False, lw=1.5))
        ax.add_patch(Circle((-0.7, 0), 1.5, alpha=0.35, color=OKABE_ITO[0]))
        ax.add_patch(Circle((0.7, 0), 1.5, alpha=0.35, color=OKABE_ITO[1]))
        for x, y, txt in ((-1.4, 0, only_a), (1.4, 0, only_b), (0, 0, both), (2.0, -1.6, neither)):
            ax.text(x, y, f"{txt:,}", ha="center", va="center", fontsize=13, fontweight="bold")
        ax.text(-1.6, 1.6, labels[0], fontsize=13, ha="center"); ax.text(1.6, 1.6, labels[1], fontsize=13, ha="center")
        ax.text(-2.45, -1.65, "U", fontsize=13)
        ax.set_xlim(-2.8, 2.8); ax.set_ylim(-2.1, 2.1); ax.set_aspect("equal"); ax.axis("off"); ax.set_title(title)
        plt.show()

    def make_practice_data(n=3000, seed=2026):
        """PRACTICE ONLY – NOT REAL DATA. Synthetic people with the same columns as the teaching file."""
        rng = np.random.default_rng(seed)
        codes = np.array(list(REGION_NAMES))
        probs = np.where(np.isin(codes, [13, 4, 3]), 3.0, 1.0); probs = probs / probs.sum()
        region = rng.choice(codes, n, p=probs)
        age = np.clip(15 + rng.gamma(2.0, 14.0, n), 15, 95).astype(int)
        sex = rng.choice([1, 2], n)
        educ = rng.choice(EDUC_LEVELS, n, p=[0.30, 0.40, 0.10, 0.20])
        p_lf = np.clip(0.95 - 0.0009 * (age - 40) ** 2 - 0.20 * (sex == 2), 0.05, 0.97)
        in_lf = rng.random(n) < p_lf
        unemp = in_lf & (rng.random(n) < np.where(age < 25, 0.13, 0.04))
        status = np.where(~in_lf, 3, np.where(unemp, 2, 1))
        employed = status == 1
        hours = np.where(employed, np.clip(rng.normal(42, 12, n).round(), 2, 96), np.nan)
        normal_day = np.where(employed, np.clip((hours / rng.choice([5, 6], n)).round(), 1, 16), np.nan)
        wclass = np.where(employed, rng.choice(list(WORKER_CLASS), n, p=[.05, .45, .10, .27, .03, .02, .08]), np.nan)
        wage_worker = np.isin(wclass, [0, 1, 2, 5])
        basis = np.where(wage_worker, rng.choice([3, 4, 1, 5], n, p=[.55, .35, .05, .05]), np.nan)
        mult = np.select([region == 13, region == 4, region == 15], [1.45, 1.15, 0.70], 1.0)
        mult = mult * np.select([educ == EDUC_LEVELS[3], educ == EDUC_LEVELS[0]], [1.5, 0.8], 1.0)
        base = 150 + 18 * age - 0.2 * age ** 2
        pay = np.where(wage_worker, (base * mult * rng.lognormal(0, 0.3, n)).round(), np.nan)
        out = pd.DataFrame({"person_id": np.arange(1, n + 1), "region_code": region,
                            "region": pd.Series(region).map(REGION_NAMES), "sex_code": sex,
                            "sex": pd.Series(sex).map(SEX), "age": age})
        out["marital"] = np.where(age < 25, "Single", rng.choice(["Single", "Married", "Widowed"], n, p=[.3, .62, .08]))
        out["educ"], out["empstat"] = educ, pd.Series(status).map(EMPSTAT)
        out["normal_hrs_day"], out["hours_week"] = normal_day, hours
        out["total_hours_week"] = np.where(employed, hours + rng.choice([0, 0, 0, 8], n), np.nan)
        out["worker_class"] = pd.Series(wclass).map(WORKER_CLASS)
        out["pay_basis"] = pd.Series(basis).map(PAY_BASIS)
        out["daily_pay"], out["weight"] = pay, rng.uniform(150, 900, n).round(2)
        return out

    print("✅ Helpers ready: check(), number_line(), venn2_counts(), make_practice_data()")
    ''', title="🔧 Helper code: run me (no need to read)")

    # ---------------------------------------------------------- instructor
    md(r"""
    ---
    # 🔒 INSTRUCTOR ONLY: build the small teaching file (students: skip this section)

    > **Students:** you do **not** need to run anything in this section. Your instructor already did it and shared `lfs2018_ecocal1.csv` with you. Go straight to **Part 0**.

    **What these cells do (run once, on the instructor's Drive):**
    1. Mount Google Drive and **read only the header** of the big CSV (~104 MB) to check the exact column names (upper or lower case?).
    2. Read **only the 13 columns we need** (`usecols=[...]`, `low_memory=False`).
    3. Keep persons aged **15+**, turn codes into readable labels, and set not-reported codes (`999`, `0`, blanks) to `NaN`.
    4. Draw a **reproducible random sample of 5,000 persons** (`random_state=2026`) and save `lfs2018_ecocal1.csv`.

    **Why a sample of 5,000 and not all rows?** The full 15+ file has well over 100,000 persons. A 5,000-row file is small enough (well under 1 MB) for students to upload by hand and load in a second. It still gives a few hundred paid workers in the large regions and enough unemployed persons to compute rates. Because the sample is random and its seed is fixed, every student gets **exactly the same numbers**. To keep every row instead, set `SAMPLE_SIZE = None`.

    Each cell only does something when `RUN_INSTRUCTOR_SETUP = True`, so "Run all" is safe for students.
    """)

    code(r'''
    RUN_INSTRUCTOR_SETUP = False    # 👩‍🏫 instructor: set to True, run these 3 cells once, then set back to False
    SOURCE_PATH = "/content/drive/MyDrive/LFS/LFS 2018.CSV"   # or ".../FIES-LFS PUF 2018 LFS_SUMMARY.CSV"
    OUTPUT_PATH = "/content/drive/MyDrive/LFS/lfs2018_ecocal1.csv"
    SAMPLE_SIZE = 5000              # None = keep all persons aged 15+
    WANTED = ["W_REGN", "LC04_SEX", "LC05_AGE", "LC06_MSTAT", "LC07_GRADE", "NEWEMPSTAT", "LC18_PNWHRS",
              "LC19_PHOURS", "LC28_THOURS", "LC23_PCLASS", "LC24_PBASIS", "LC25_PBASIC", "PWGTPRV"]

    if RUN_INSTRUCTOR_SETUP:
        from google.colab import drive
        drive.mount("/content/drive")
        header = pd.read_csv(SOURCE_PATH, nrows=0)               # reads ONLY the column names (fast)
        print("Columns in the file:", list(header.columns))
        lookup = {c.strip().upper(): c for c in header.columns}  # works whether names are UPPER or lower case
        missing = [w for w in WANTED if w not in lookup]
        print("❌ Missing columns, check the dictionary:" if missing else "✅ All 13 columns found.", missing)
    ''', title="🔒 Instructor step 1: mount Drive and check column names")

    code(r'''
    if RUN_INSTRUCTOR_SETUP:
        raw = pd.read_csv(SOURCE_PATH, usecols=[lookup[w] for w in WANTED], low_memory=False)
        raw.columns = [c.strip().upper() for c in raw.columns]
        for col in WANTED:
            raw[col] = pd.to_numeric(raw[col], errors="coerce")   # blanks / spaces → NaN
        print("Raw LC07_GRADE codes (check the education recode):")
        print(raw["LC07_GRADE"].value_counts().sort_index().head(40))
        raw = raw[raw["LC05_AGE"] >= 15].copy()                   # persons aged 15 and over
        t = pd.DataFrame({"region_code": raw["W_REGN"], "region": raw["W_REGN"].map(REGION_NAMES),
                          "sex_code": raw["LC04_SEX"], "sex": raw["LC04_SEX"].map(SEX),
                          "age": raw["LC05_AGE"], "marital": raw["LC06_MSTAT"].map(MARITAL),
                          "educ": raw["LC07_GRADE"].apply(educ_level),
                          "empstat": raw["NEWEMPSTAT"].map(EMPSTAT)})
        t["normal_hrs_day"] = raw["LC18_PNWHRS"].where(raw["LC18_PNWHRS"].between(1, 16))  # 0/blank → NaN
        t["hours_week"] = raw["LC19_PHOURS"].where(raw["LC19_PHOURS"].between(1, 112))     # 999 → NaN
        t["total_hours_week"] = raw["LC28_THOURS"].where(raw["LC28_THOURS"].between(0, 168))
        t["worker_class"] = raw["LC23_PCLASS"].map(WORKER_CLASS)
        t["pay_basis"] = raw["LC24_PBASIS"].map(PAY_BASIS)
        t["daily_pay"] = raw["LC25_PBASIC"].where(raw["LC25_PBASIC"] > 0)                  # 0/blank → NaN
        t["weight"] = raw["PWGTPRV"]
        print(t.shape); print(t.isna().mean().round(3))
    ''', title="🔒 Instructor step 2: read 13 columns, keep ages 15+, recode, set missing codes to NaN")

    code(r'''
    if RUN_INSTRUCTOR_SETUP:
        if SAMPLE_SIZE is not None:
            t = t.sample(n=SAMPLE_SIZE, random_state=2026)        # reproducible random sample
        t = t.reset_index(drop=True)
        t.insert(0, "person_id", range(1, len(t) + 1))            # simple ID 1, 2, 3, ... for set exercises
        t.to_csv(OUTPUT_PATH, index=False)
        print(f"✅ Saved {len(t):,} rows to {OUTPUT_PATH}. Share this file with students.")
        from google.colab import files
        files.download(OUTPUT_PATH)                               # optional: also download a copy
    ''', title="🔒 Instructor step 3: draw the reproducible sample and save lfs2018_ecocal1.csv")

    md(r"""
    > **Columns in the teaching file `lfs2018_ecocal1.csv`** (students will meet these in Part 0):
    >
    > | Column | From | Meaning | Type of number |
    > |---|---|---|---|
    > | `person_id` | (created) | Row ID 1, 2, 3, … | label |
    > | `region_code`, `region` | `W_REGN` | Region code and name | **label** (13 = NCR is a name, not an amount) |
    > | `sex_code`, `sex` | `LC04_SEX` | 1 = Male, 2 = Female | **label** |
    > | `age` | `LC05_AGE` | Age at last birthday (15+) | whole number |
    > | `marital` | `LC06_MSTAT` | Marital status | label |
    > | `educ` | `LC07_GRADE` | Four broad education levels | label (ordered) |
    > | `empstat` | `NEWEMPSTAT` | Employed / Unemployed / Not in labor force | label |
    > | `normal_hrs_day` | `LC18_PNWHRS` | Normal working hours per day (1–16; else NaN) | quantity |
    > | `hours_week` | `LC19_PHOURS` | Hours worked last week, primary job (999 → NaN) | quantity |
    > | `total_hours_week` | `LC28_THOURS` | Hours worked last week, all jobs | quantity |
    > | `worker_class` | `LC23_PCLASS` | Class of worker | label |
    > | `pay_basis` | `LC24_PBASIS` | Basis of payment | label |
    > | `daily_pay` | `LC25_PBASIC` | Basic pay per day, primary job, ₱ (0/blank → NaN) | quantity |
    > | `weight` | `PWGTPRV` | Survey weight (how many Filipinos each person represents) | quantity |
    """)
