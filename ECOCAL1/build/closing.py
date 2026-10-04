from kit import md, code, details


def build():
    md(r"""
    ---
    # 🎓 Closing
    ## 🪞 Capstone reflection (10 min, write in this cell or a notebook)
    1. Which topic from Weeks 1–8 was **hardest** for you? What exactly made it hard: the concept, the algebra steps, or the notation?
    2. Which idea **clicked** when you saw it on real data? Describe the moment.
    3. How did working with LFS data change your understanding of a **rate** (LFPR, UR, hourly pay) as a *fraction with a domain*?
    4. Pick one board-work problem you rated below *Exemplary*. Redo it now, without notes. What changed?
    5. In one sentence: what will you do differently when preparing for the **final exam**?

    ✏️ *Your reflections:* …
    """)
    md(r"""
    ## 📐 Formula cheat-sheet (Weeks 1–8)
    | Topic | Key rules |
    |---|---|
    | Sets | $A\cap B$, $A\cup B$, $A'$, $A - B$; $(A\cup B)' = A'\cap B'$, $(A\cap B)' = A'\cup B'$; $\lvert A\cup B\rvert = \lvert A\rvert + \lvert B\rvert - \lvert A\cap B\rvert$ |
    | Numbers | $\mathbb N\subset\mathbb Z\subset\mathbb Q\subset\mathbb R$; rational ⇔ terminating or repeating decimal |
    | Properties | commutative, associative, distributive $a(b+c) = ab + ac$, identities $0, 1$, inverses $-a$, $1/a$ ($a\ne0$) |
    | Inequalities | multiplying or dividing by a negative **reverses** the sign; intervals $(a,b)$, $[a,b]$, $[a,\infty)$ |
    | Exponents | $a^ma^n = a^{m+n}$, $a^m/a^n = a^{m-n}$, $(a^m)^n = a^{mn}$, $a^0 = 1$, $a^{-n} = 1/a^n$, $a^{m/n} = (\sqrt[n]{a})^m$ |
    | Growth | $P(1+r)^t$; $r = (Q/P)^{1/t} - 1$; monthly $= (1+r)^{1/12} - 1$ |
    | Absolute value | $\lvert a\rvert \ge 0$; $d(a,b) = \lvert a-b\rvert$; $\lvert X\rvert<k \iff -k<X<k$; $\lvert X\rvert>k \iff X<-k$ or $X>k$ |
    | Special products | $(a\pm b)^2 = a^2 \pm 2ab + b^2$; $(a+b)(a-b) = a^2 - b^2$; $(a\pm b)^3 = a^3 \pm 3a^2b + 3ab^2 \pm b^3$ |
    | Factoring | GCF; $a^2 - b^2$; $a^3 \pm b^3 = (a\pm b)(a^2 \mp ab + b^2)$; trinomials; grouping |
    | Fractions | cancel **factors** only; $\frac ab + \frac cd = \frac{ad+bc}{bd}$; $\frac ab \div \frac cd = \frac ab\cdot\frac dc$; denominators $\ne 0$ |
    | Quadratics | $x = \frac{-b\pm\sqrt{b^2-4ac}}{2a}$; vertex $x^* = -\frac{b}{2a}$ |
    | Radical equations | isolate, square, **check** for extraneous roots |
    | Systems | substitution, elimination; $\det\begin{pmatrix}a&b\\c&d\end{pmatrix} = ad - bc \ne 0$ ⇒ unique solution |
    | Labor rates | LFPR $= \frac{E+U}{P}$, UR $= \frac{U}{E+U}$, EPR $= \frac EP$, UR $= 1 - \frac{\text{EPR}}{\text{LFPR}}$ |

    ## 🐍 Python cheat-sheet
    | Task | Code |
    |---|---|
    | Arithmetic, power | `+ - * /`, `//`, `%`, `**` (never `^`) |
    | Print nicely | `print(f"₱{value:,.2f}")` |
    | List / dictionary | `[1, 2, 3]`, `{13: "NCR"}` |
    | Decision / loop / function | `if ...: ... else: ...`, `for v in values:`, `def f(x): return ...` |
    | Load and look | `pd.read_csv(...)`, `.head()`, `.shape`, `.describe()`, `.value_counts()` |
    | Select and filter | `df["col"]`, `df[["a", "b"]]`, `df[df["age"] >= 15]`, `(m1) & (m2)`, `(m1) \| (m2)`, `~m` |
    | Missing values | `.isna().sum()`, `.dropna(subset=[...])`, `s.where(s > 0)` |
    | Intervals | `.between(a, b)`, `pd.cut(s, bins, right=False)` |
    | Group summaries | `df.groupby("g")["x"].mean()`, `pd.crosstab(df["a"], df["b"])` |
    | Sets | `set(...)`, `A & B`, `A \| B`, `A - B`, `len(A)` |
    | NumPy | `np.sqrt`, `np.abs`, `np.isclose`, `np.arange`, `np.linspace`, `np.polyfit`, `np.linalg.solve`, `np.linalg.det` |
    | SymPy | `sp.symbols`, `sp.expand`, `sp.factor`, `sp.cancel`, `sp.together`, `sp.apart`, `.subs`, `sp.lambdify`, `sp.Eq`, `sp.solve`, `sp.solveset(..., domain=sp.S.Reals)`, `sp.Interval`, `sp.diff` |
    | Charts | `fig, ax = plt.subplots()`, `ax.bar`, `ax.barh`, `ax.plot`, `ax.scatter`, `ax.fill_between`, `ax.set_title/xlabel/ylabel`, `plt.show()` |
    """)
    md(r"""
    ## 🔭 Where to go next: Weeks 9–13
    | Week | Topic | Builds on | Read |
    |---|---|---|---|
    | 9–10 | Cartesian coordinate system; graphs of equations; lines (slope, intercepts) | Parts 1, 7, 8 (linear equations, systems, graphing) | Swokowski & Cole, *Functions and Graphs* (lines); Sydsaeter et al., *Introduction to Functions* (linear functions) |
    | 10–11 | Functions; graphs of functions; inverse and composite functions | Parts 1, 5 (input → output, polynomials), Part 3 (domains as intervals) | Swokowski & Cole, *Functions and Graphs*; Sydsaeter et al., *Functions of One Variable* |
    | 11–12 | Exponential and logarithmic functions | Part 4 (exponents, compound growth $P(1+r)^t$) | Swokowski & Cole, *Inverse, Exponential, and Logarithmic Functions*; Sydsaeter et al., *Exponential and Logarithmic Functions* |
    | 11–13 | Limits, properties of limits, limits at infinity, one-sided limits; continuity | Part 1 (shrinking $h$), Part 6 (factoring for $0/0$), Parts 3–4 (intervals, absolute value) | Sydsaeter et al., *Limits, Continuity, and Series*; Chiang & Wainwright, *Comparative Statics and the Concept of Derivative* |
    | 13 | Infinite sequences and series | Part 4 (compound growth as a sequence) | Sydsaeter et al., *Limits, Continuity, and Series* (sequences, geometric series) |
    """)
    md(r"""
    ## 📚 References (APA 7th)
    **Core readings (Weeks 1–8)**
    - Rees, P. K., Sparks, F. W., & Rees, C. (2003). *College algebra* (10th ed.). McGraw-Hill.
    - Swokowski, E., & Cole, J. (2011). *Algebra and trigonometry with analytic geometry* (13th ed.). Cengage Learning.
    - Sydsaeter, K., Hammond, P., Strøm, A., & Carvajal, A. (2022). *Essential mathematics for economic analysis* (6th ed.). Pearson.

    **Supplementary**
    - Anthony, M., & Biggs, N. (2024). *Mathematics for economics and finance: Methods and modelling* (2nd ed.). Cambridge University Press.
    - Cerreia-Vioglio, S., Marinacci, M., & Vigna, E. (2024). *Principles of mathematics for economics*. Springer.
    - Chiang, A. C., & Wainwright, K. (2004). *Fundamental methods of mathematical economics* (4th ed.). McGraw-Hill Education.
    - Danao, R. A. (2001). *Introductory mathematical economics*. University of the Philippines Press.
    - Dowling, E. T. (2011). *Schaum's outline of introduction to mathematical economics* (3rd ed.). McGraw-Hill.
    - Hoy, M., Livernois, J., McKenna, C., Rees, R., & Stengos, T. (2022). *Mathematics for economists* (4th ed.). MIT Press.
    - Pemberton, M., & Rau, N. (2015). *Mathematics for economists* (4th ed.). Manchester University Press.
    - Peña-Levano, L. M. (2021). *Schaum's outline of mathematical methods for business, economics, and finance* (2nd ed.). McGraw-Hill.

    **Data**
    - Philippine Statistics Authority. (n.d.). *Family Income and Expenditure Survey – Labor Force Survey 2018, Public Use File: LFS summary* [Data set and data dictionary, `FIES-LFS PUF 2018 LFS_SUMMARY`]. Philippine Statistics Authority. Used for educational purposes under the PSA's terms of use for public use files.

    **Software:** Python; pandas; NumPy; Matplotlib; SymPy; Google Colaboratory.
    """)
    md(r"""
    ---
    # 👩‍🏫 Notes for the instructor
    **1. Assumptions about the data columns (please verify against `fies-lfs_2018_metadata(dictionary).xlsx`)**
    - Column names are assumed to be the 13 listed in Instructor step 1. That cell matches names case-insensitively and stops with a list of any missing columns.
    - `LC07_GRADE` → `educ`: the 5-digit codes are recoded by **leading digits** (`< 20000` elementary or less; `20000–39999` high school; `40000–59999` post-secondary/technical; `≥ 60000` college or higher). Instructor step 2 prints the raw code frequencies. **Check these cut-offs against the 2018 dictionary**, and edit `educ_level()` in the helper cell if needed.
    - Not-reported or not-applicable codes: `LC19_PHOURS` outside 1–112 (incl. `999`) → `NaN`; `LC18_PNWHRS` outside 1–16 (incl. `0`) → `NaN`; `LC28_THOURS` outside 0–168 → `NaN`; `LC25_PBASIC ≤ 0` or blank → `NaN`. Blank strings become `NaN` via `pd.to_numeric(errors="coerce")`.
    - `LC25_PBASIC` is taken to be **basic pay per day** (as stated in the dictionary), so it is not converted by `LC24_PBASIS`. Hourly pay is defined as `daily_pay / normal_hrs_day`.
    - `W_REGN = 15` is labelled **ARMM** (its 2018 name; now BARMM).
    - If the file has several rounds or duplicated persons, consider filtering to one round before sampling.
    - The teaching file is a simple random sample of **5,000** persons aged 15+ (`random_state=2026`), and all analysis is **unweighted**. Every rate is a teaching estimate. Expect some small regional groups (e.g., few unemployed persons per region).
    - The notebook runs top to bottom with **either** the real teaching file **or** the synthetic fallback (`make_practice_data`). All auto-checks compute their expected answers from whatever `df` is loaded. Nothing is hard-coded, except textbook-style numbers in hand exercises.

    **2. Reference mappings to verify against your editions**
    - Section names (e.g., Swokowski & Cole *Fundamental Concepts of Algebra*, *Equations and Inequalities*; Sydsaeter et al. *Essentials of Logic and Set Theory*, *Algebra*, *Solving Equations*, *Differentiation*, *Limits, Continuity, and Series*; Rees, Sparks & Rees *Special Products and Factoring*, *Fractions*, *Systems of Equations*; Chiang & Wainwright *Economic Models*, *Equilibrium Analysis*, *Linear Models and Matrix Algebra*, *Comparative Statics and the Concept of Derivative*; Dowling *Review*) are cited **by topic**. No chapter or page numbers are given, because they differ by edition. Please confirm that the section titles match the 13th/10th/6th/4th editions on the syllabus.
    - The "Where to go next" table maps Weeks 9–13 to sections by topic. Verify these too.

    **3. Where to cut if time is short**
    - **Part 0:** skip Lesson 0.6 (`for` loops) and the weights box; students can learn loops when they first appear.
    - **Part 1:** keep 1.1–1.3; make 1.4 (marginal thinking) and 1.5 (accumulation) optional.
    - **Part 2:** Lesson 2.2 (De Morgan with masks) can be shortened to the hand example plus one LFS cell.
    - **Part 5:** the by-sex profile plot (Lesson 5.2) can be replaced by evaluating `p_all` only.
    - **Part 6:** skip `sp.apart` and the regional unemployment chart.
    - **Part 7:** Lesson 7.3's LFS growth example is optional.
    - **Part 8:** Lesson 8.3's 3×3 LFS system is optional. Keep the hand 3×3 and the consistency examples. The midterm review sheet can be assigned as homework.
    - **Part 9:** assign Q1–Q4 in class and Q5–Q7 plus the paragraph as homework.
    - **Exercises:** ⭐⭐⭐ items are always optional extensions.

    **4. Technical notes**
    - Tested top to bottom with recent pandas (2.x/3.x), NumPy, Matplotlib and SymPy. No extra installs are needed (the Venn diagram is drawn with plain Matplotlib, so `matplotlib-venn` is not required).
    - Auto-check cells use Colab's `#@title ... {display-mode: "form"}` so their code is hidden by default. Students can still expand them.
    - This notebook was generated from the Python build scripts in `ECOCAL1/build/`. Edit those and re-run `python build_notebook.py` to regenerate it consistently.
    """)
