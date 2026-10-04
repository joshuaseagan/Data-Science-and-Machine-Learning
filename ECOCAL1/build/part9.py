from kit import md, code, details, exercise, concept_card, interpret, RUBRIC


def build():
    md(r"""
    ---
    # 🧭 Part 9 · Week 8: Putting It Together: Equations, Inequalities and Systems
    **Week 8 · CLO1, CLO2, CLO3 · ⏱️ Est. time: 75 min**
    📚 *Readings:* all core readings for Weeks 1–7, especially Swokowski & Cole (2011), *Equations and Inequalities*; Sydsaeter et al. (2022), *Solving Equations*; Rees, Sparks & Rees (2003), *Systems of Equations*.

    🎯 **Learning objectives.** By the end of Part 9 you can:
    1. **Choose** an appropriate method for a given equation, inequality or system, and **justify** the choice.
    2. **Write** a clean, documented Python function that computes several indicators at once.
    3. **Combine** sets, intervals, exponents, rational expressions, equations, inequalities and a 2×2 system in a single analysis of real data.
    4. **Communicate** results in a short written interpretation, as you would in a group presentation (CLO3).

    🧭 **Big picture.** Real problems don't come labelled "Week 5". An economist must first **recognize** what kind of problem they are facing, then pick the tool, solve, check, and finally **explain** the answer to someone who doesn't know algebra. This Part is a mini case study: *A profile of the Filipino worker in 2018 (teaching estimates from our sample).*
    """)

    # 9.1
    md("## Lesson 9.1 · Choosing the right method ⏱️ 10 min")
    concept_card("a decision guide",
        r"""| If you see… | It is a… | Method (by hand) | Check with |
|---|---|---|---|
| $ax + b = c$ (fractions → multiply by the LCD) | linear equation | isolate $x$ | `sp.solve` |
| $ax^2 + bx + c = 0$ | quadratic equation | factor → complete the square → formula | `sp.solve` |
| $\sqrt{\;\cdot\;}$ containing $x$ | radical equation | isolate, square, **check** | substitute |
| $\lvert X\rvert = k$ / $< k$ / $> k$ | absolute value | split into cases / compound / "or" | `sp.solveset` |
| $<, \le, >, \ge$ with $x^2$ or a product | polynomial inequality | factor + sign chart | `sp.solveset` |
| $P(1+r)^t = Q$, unknown $r$ | exponent equation | $r = (Q/P)^{1/t} - 1$ | `**` |
| two or more unknowns, several equations | linear system | substitution / elimination / determinant | `sp.solve`, `np.linalg.solve` |
**Always finish with:** *Does the answer satisfy the original problem? Is it in the domain? What does it mean economically?*""",
        "Swokowski & Cole, *Equations and Inequalities* (chapter review); Sydsaeter et al., *Solving Equations*.")
    md(r"""
    ### ✍️ Step 2 · Solve by Hand: classify first, then solve
    (a) $\frac{2x}{3} - 1 = \frac{x}{2}$ → linear with fractions: $\times 6$: $4x - 6 = 3x \Rightarrow x = 6$.
    (b) $x^2 = 4x + 12$ → quadratic: $x^2 - 4x - 12 = (x - 6)(x + 2) = 0 \Rightarrow x = 6, -2$.
    (c) $|x - 6| \le 2$ → absolute-value inequality: $[4, 8]$.
    (d) $x + y = 8,\ x - y = 4$ → system: add the equations: $2x = 12 \Rightarrow x = 6, y = 2$.
    ### 🐍 Step 3 · Check with Python
    """)
    code(r'''
    x, y = sp.symbols("x y", real=True)
    print("(a)", sp.solve(sp.Eq(2 * x / 3 - 1, x / 2), x))
    print("(b)", sp.solve(sp.Eq(x**2, 4 * x + 12), x))
    print("(c)", sp.solveset(sp.Abs(x - 6) <= 2, x, domain=sp.S.Reals))
    print("(d)", sp.solve([sp.Eq(x + y, 8), sp.Eq(x - y, 4)], [x, y]))
    ''')

    # 9.2
    md("## Lesson 9.2 · Writing a clean function ⏱️ 15 min")
    md(r"""
    ### 📖 Step 1 · Read & Understand: functions as reusable models
    > A good function has a **clear name**, a **docstring** (the text in triple quotes that says what it does), **inputs**, and a **return** value. It also handles impossible cases (like dividing by zero) explicitly. It is the programming version of defining $f(x)$ *together with its domain*.

    ### ✍️ Step 2 · Solve by Hand
    For a group with $E = 90$, $U = 10$, $P = 150$: LFPR $= \frac{100}{150} = 0.\overline{6}$ and UR $= \frac{10}{100} = 0.1$. If $E + U = 0$, the UR is **undefined** (division by zero).
    ### 🐍 Step 3 · Check with Python
    """)
    code(r'''
    def labor_rates(E, U, P):
        """Return (LFPR, UR) from counts. UR is NaN when the labor force E + U is 0 (undefined)."""
        LF = E + U
        lfpr = LF / P
        if LF > 0:
            ur = U / LF
        else:
            ur = np.nan                    # domain restriction: denominator must be nonzero
        return lfpr, ur

    print(labor_rates(90, 10, 150))       # (0.666..., 0.1)
    print(labor_rates(0, 0, 20))          # (0.0, nan): no division-by-zero crash
    ''')
    md("### 📊 Step 4 · Apply to LFS Data\nNow a function that summarizes **any** group of persons from `df`:")
    code(r'''
    def labor_profile(data):
        """Teaching indicators (unweighted) for a table of persons aged 15+."""
        E = (data["empstat"] == "Employed").sum()
        U = (data["empstat"] == "Unemployed").sum()
        lfpr, ur = labor_rates(E, U, len(data))
        with_pay = data.dropna(subset=["daily_pay"])
        return {"persons": len(data), "LFPR": lfpr, "UR": ur,
                "median_daily_pay": with_pay["daily_pay"].median(),
                "median_hourly_pay": with_pay["hourly_pay"].median()}

    summary = pd.DataFrame({"All": labor_profile(df), "NCR": labor_profile(df[df["region"] == "NCR"]),
                            "Women": labor_profile(df[df["sex"] == "Female"]),
                            "Youth 15–24": labor_profile(df[df["age"].between(15, 24)])})
    summary.round(3)
    ''')
    interpret(r"Pick two columns of `summary` and compare them in two sentences, starting with *\"In our sample, …\"*. Remember that these are unweighted teaching estimates.",
              r"*In our sample, youth aged 15–24 have a lower LFPR (__) than all persons (__), and a higher unemployment rate (__ vs __).* Many youth are in school (outside the labor force), and those who do look for work have more trouble finding it. These are unweighted teaching estimates, not official PSA figures.")

    # 9.3 case study
    md(r"""
    ## Lesson 9.3 · 🇵🇭 Case study: *A profile of the Filipino worker in 2018* ⏱️ 40 min
    For **each** question: (1) name the math topic and method, (2) set it up **on paper** first, (3) run the code to check and compute, (4) write a one-sentence interpretation in the box at the end.
    """)
    md(r"""
    ### Q1 · Sets (Week 1): among NCR residents, what share of the employed are women?
    *Setup:* $\dfrac{|E \cap F \cap N|}{|E \cap N|}$, built from the sets of Part 2.
    """)
    code(r'''
    q1 = len(E & F & N) / len(E & N)
    print(f"Q1: share of employed NCR residents who are women = {q1:.1%}")
    print(f"    (compare: share of ALL employed who are women = {len(E & F) / len(E):.1%})")
    ''')
    md(r"""
    ### Q2 · Intervals (Week 2): is unemployment higher for youth, $[15, 24]$, than for adults, $[25, \infty)$?
    """)
    code(r'''
    youth = df[df["age"].between(15, 24)]
    adults = df[df["age"] >= 25]
    ur_youth = labor_profile(youth)["UR"]
    ur_adult = labor_profile(adults)["UR"]
    print(f"Q2: UR youth [15, 24] = {ur_youth:.1%}  vs  UR adults [25, ∞) = {ur_adult:.1%}  → ratio {ur_youth / ur_adult:.2f}")
    ''')
    md(r"""
    ### Q3 · Rational expressions (Week 5): verify $\text{UR} = 1 - \dfrac{\text{EPR}}{\text{LFPR}}$ for women and for men.
    """)
    code(r'''
    for sex in ["Female", "Male"]:
        g = df[df["sex"] == sex]
        E_g, U_g, P_g = (g["empstat"] == "Employed").sum(), (g["empstat"] == "Unemployed").sum(), len(g)
        lfpr_g, ur_g = labor_rates(E_g, U_g, P_g)
        print(f"Q3 {sex:<6}: UR = {ur_g:.4f}, 1 − EPR/LFPR = {1 - (E_g / P_g) / lfpr_g:.4f}")
    ''')
    md(r"""
    ### Q4 · Exponents and radicals (Week 3): at what constant yearly growth rate would the youth median daily pay reach today's adult median in 5 years?
    *Setup:* $m_Y (1 + r)^5 = m_A \Rightarrow r = (m_A/m_Y)^{1/5} - 1$.
    """)
    code(r'''
    m_Y = youth["daily_pay"].median()
    m_A = adults["daily_pay"].median()
    r_catch = (m_A / m_Y) ** (1 / 5) - 1
    print(f"Q4: youth median ₱{m_Y:,.2f}, adult median ₱{m_A:,.2f} → r = {r_catch:.2%} per year")
    ''')
    md(r"""
    ### Q5 · Equations (Week 6): (a) at what age does the fitted profile peak? (b) How many weekly hours at the median hourly pay give ₱3,500?
    *Setup:* (a) vertex $a^* = -c_1/(2c_2)$; (b) linear equation $r h = 3500$.
    """)
    code(r'''
    c2, c1, c0 = np.polyfit(paid["age"], paid["daily_pay"], 2)
    peak = -c1 / (2 * c2)
    h_35 = 3500 / paid["hourly_pay"].median()
    print(f"Q5a: profile opens {'down' if c2 < 0 else 'UP (no peak!)'}; vertex at age {peak:.1f}")
    print(f"Q5b: hours needed for ₱3,500/week at the median hourly pay = {h_35:.1f}")
    ''')
    md(r"""
    ### Q6 · Inequalities (Week 7): (a) for which ages is predicted pay at least the median? (b) What share of employed persons work 48 hours or more, $h \ge 48$ (long hours)?
    """)
    code(r'''
    a = sp.symbols("a", real=True)
    m = paid["daily_pay"].median()
    q6a = sp.solveset(c0 + c1 * a + c2 * a**2 >= m, a, domain=sp.S.Reals).intersect(sp.Interval(15, 99))
    q6b = (has_hours["hours_week"] >= 48).mean()
    print("Q6a: ages with predicted pay ≥ median:", q6a)
    print(f"Q6b: share of employed (with hours) working h ≥ 48: {q6b:.1%}")
    ''')
    md(r"""
    ### Q7 · A 2×2 system (Week 7): recover the number of **youth** and **adult** paid workers from totals and averages alone.
    *Setup:* $x + y = N$ and $\bar d_Y x + \bar d_A y = T$.
    """)
    code(r'''
    paid_youth = paid["age"].between(15, 24)
    d_Y, d_A = paid[paid_youth]["daily_pay"].mean(), paid[~paid_youth]["daily_pay"].mean()
    xq, yq = sp.symbols("x_youth y_adult")
    q7 = sp.solve([sp.Eq(xq + yq, len(paid)), sp.Eq(d_Y * xq + d_A * yq, paid["daily_pay"].sum())], [xq, yq])
    print(f"Q7: solved youth = {float(q7[xq]):.0f}, adults = {float(q7[yq]):.0f}  | actual: {paid_youth.sum()}, {(~paid_youth).sum()}")
    ''')
    md("### 📊 The final multi-panel chart\nA 2×2 grid of charts (`plt.subplots(2, 2)`) puts the whole story on one page.")
    code(r'''
    fig, axes = plt.subplots(2, 2, figsize=(13, 9))
    status = df["empstat"].value_counts()
    axes[0, 0].bar(status.index, status.values, color=OKABE_ITO[:3])
    axes[0, 0].set_title("(a) Employment status, persons 15+"); axes[0, 0].set_ylabel("Persons in sample")
    axes[0, 1].bar(emp_rate.index.astype(str), emp_rate.values * 100, color=OKABE_ITO[0])
    axes[0, 1].set_title("(b) Employment rate by age group"); axes[0, 1].set_ylabel("% employed")
    axes[0, 1].tick_params(axis="x", rotation=30)
    grid = np.linspace(15, 75, 200); pv = c0 + c1 * grid + c2 * grid**2
    axes[1, 0].scatter(paid["age"], paid["daily_pay"], s=5, alpha=0.15, color="grey")
    axes[1, 0].plot(grid, pv, lw=3, color=OKABE_ITO[3]); axes[1, 0].axhline(m, ls="--", color="black")
    axes[1, 0].fill_between(grid, pv, m, where=pv >= m, alpha=0.3, color=OKABE_ITO[2])
    axes[1, 0].set_ylim(0, paid["daily_pay"].quantile(0.95))
    axes[1, 0].set_title("(c) Age–pay profile; shaded: p(a) ≥ median"); axes[1, 0].set_xlabel("Age"); axes[1, 0].set_ylabel("Daily pay (₱)")
    ur_sex = by_sex["UR"] * 100
    axes[1, 1].bar(ur_sex.index, ur_sex.values, color=[OKABE_ITO[3], OKABE_ITO[0]])
    axes[1, 1].set_title("(d) Unemployment rate by sex"); axes[1, 1].set_ylabel("% of labor force")
    fig.suptitle("A profile of the Filipino worker, LFS 2018 (unweighted teaching estimates from our sample)", fontsize=15)
    plt.tight_layout(); plt.show()
    ''')
    md(r"""
    *Alt text:* four panels: (a) counts by employment status; (b) employment rate by age interval; (c) a scatter of pay against age, with the fitted quadratic, the median line, and the shaded region where the fitted pay is above the median; (d) the unemployment rate for women and for men.
    **Takeaway:** one figure summarizes sets and rates (a, d), intervals (b), and polynomials plus inequalities (c).

    ### 💬 Final written interpretation (CLO3) 🗣️
    Write a 5–7 sentence paragraph, as if presenting to your group, that answers: *What does our sample suggest about work and pay in the Philippines in 2018?* Use at least **four** numbers from Q1–Q7, name the **math tool** behind each, and include one sentence on **limitations** (sample, unweighted, fitted curve).

    ✏️ **Your paragraph** *(double-click to type)*: …
    """ + "\n" + details("👀 A model structure (fill in your own numbers)", r"""
*In our sample of persons aged 15+ from the PSA LFS 2018 (unweighted teaching estimates), about __% of employed NCR residents are women, compared with __% nationally (sets, Q1). Youth aged 15–24 face an unemployment rate of __%, about __ times the adult rate (intervals and rational expressions, Q2–Q3). Predicted daily pay rises with age, peaks at about age __ (vertex of a quadratic, Q5), and is at or above the median between ages __ and __ (quadratic inequality, Q6). For a youth's median pay to catch up with today's adult median in five years, it would need to grow about __% per year (rational exponents, Q4). At the median hourly pay, earning ₱3,500 a week takes about __ hours (linear equation, Q5). Limitations: this is an unweighted random sample, the age profile is a simple quadratic fitted to a cross-section, and pay covers only workers with a recorded basic daily pay.*
"""))

    # end matter
    md(r"""
    ## ⚠️ Common mistakes
    - Jumping to a formula before **classifying** the problem (e.g. using the quadratic formula on a linear equation).
    - Reporting a result without its **domain check** (an age outside 15–99, a negative number of hours).
    - Confusing *share of the employed who are women* ($|E\cap F|/|E|$) with *share of women who are employed* ($|E\cap F|/|F|$). The denominators differ!
    - Treating teaching estimates from an unweighted sample as official statistics.
    - Writing functions that crash on an empty group. Handle zero denominators explicitly.
    """)
    md("## ✅ Check your understanding\n\n" + "\n\n".join([
        r"**Q1.** Which method would you use first for $3x^2 - 12 = 0$?" + "\n\n" + details("Answer", r"Factor (GCF, then difference of squares): $3(x - 2)(x + 2) = 0$, or isolate $x^2 = 4$. Either way, $x = \pm 2$."),
        r"**Q2 (True/False).** $|E \cap F|/|E|$ and $|E \cap F|/|F|$ are always equal." + "\n\n" + details("Answer", r"**False.** They are equal only if $|E| = |F|$."),
        r"**Q3.** Why does `labor_rates` return `nan` instead of crashing when $E + U = 0$?" + "\n\n" + details("Answer", "Because UR = U/(E + U) is undefined when the denominator is 0. The function checks the domain before dividing."),
    ]))

    md("## 💻 Coding exercises (Part 9)")
    exercise("9.1", "⭐", "NCR unemployment rate",
             r"Use `labor_profile` to store the unemployment rate of **NCR** residents in `ex9_1`.",
             "ex9_1 = None    # YOUR CODE HERE",
             'ex9_1 = labor_profile(df[df["region"] == "NCR"])["UR"]',
             'g91 = df[df["region"] == "NCR"]\ncheck(ex9_1, (g91["empstat"] == "Unemployed").sum() / g91["empstat"].isin(["Employed", "Unemployed"]).sum(), hint="labor_profile(...) returns a dictionary; read it with [\\"UR\\"].")')
    exercise("9.2", "⭐⭐", "Write a function with a domain check",
             r"Write a function `hours_needed(target, rate)` that returns `target / rate` when `rate > 0`, and `np.nan` otherwise (the domain check). Then store the list `[hours_needed(3000, 75), hours_needed(1000, 50)]` in `ex9_2`. The check cell also tests that `hours_needed(3000, 0)` gives `nan` instead of crashing.",
             "def hours_needed(target, rate):\n    # YOUR CODE HERE\n    return None\n\nex9_2 = None    # YOUR CODE HERE",
             "def hours_needed(target, rate):\n    if rate > 0:\n        return target / rate\n    return np.nan\n\nex9_2 = [hours_needed(3000, 75), hours_needed(1000, 50)]\nprint(hours_needed(3000, 0))",
             'check(ex9_2, [40, 20], hint="3000/75 = 40 and 1000/50 = 20. Use if rate > 0: return target / rate, otherwise return np.nan.")\nif ex9_2 is not None:\n    try:\n        print("Domain check (rate = 0 should give nan):", "✅" if pd.isna(hours_needed(3000, 0)) else "❌ returns a number")\n    except ZeroDivisionError:\n        print("❌ Domain check failed: division by zero. Add an if rate > 0 test.")')
    exercise("9.3", "⭐⭐⭐", "Profile of college graduates",
             r"Use `labor_profile` on persons whose `educ` is `\"College or higher\"` and store their **LFPR** in `ex9_3`. Then compare it with `summary.loc[\"LFPR\", \"All\"]` in a sentence.",
             "ex9_3 = None    # YOUR CODE HERE",
             'ex9_3 = labor_profile(df[df["educ"] == "College or higher"])["LFPR"]',
             'g93 = df[df["educ"] == "College or higher"]\ncheck(ex9_3, (g93["empstat"] != "Not in labor force").mean(), hint="Filter df[df[\\"educ\\"] == \\"College or higher\\"], then labor_profile(...)[\\"LFPR\\"].")')

    md(r"""
    ## ✍️ Board-work practice 🗣️ (integrated)
    **B9.1** A worker earns ₱75 per hour plus a fixed ₱400 weekly allowance. (a) Write weekly earnings $W(h)$. (b) Solve $W(h) = 3{,}400$. (c) Solve $W(h) \ge 3{,}400$ and write the answer as an interval. (d) If the hourly rate grows 6% per year, write the rate after $t$ years.

    **B9.2** In a barangay survey: 300 persons aged 15+, 171 employed, 9 unemployed. Compute the LFPR and UR **as fractions in lowest terms**, then verify $\text{UR} = 1 - \text{EPR}/\text{LFPR}$.

    **B9.3** Two groups of workers have average daily pays of ₱400 and ₱700. Together there are 50 workers, with a total daily pay of ₱26,000. Set up and solve the system. Interpret the answer.
    """)
    md(details("Solutions to board-work practice", r"""
**B9.1** (a) $W(h) = 75h + 400$. (b) $75h = 3000 \Rightarrow h = 40$. (c) $h \ge 40$: $[40, \infty)$, though in practice capped by the hours available in a week. (d) $75(1.06)^t$.

**B9.2** LFPR $= \frac{180}{300} = \frac{3}{5}$; UR $= \frac{9}{180} = \frac{1}{20}$; EPR $= \frac{171}{300} = \frac{57}{100}$. Check: $1 - \frac{57/100}{3/5} = 1 - \frac{57}{100}\cdot\frac{5}{3} = 1 - \frac{57}{60} = \frac{3}{60} = \frac{1}{20}$ ✔️.

**B9.3** $x + y = 50$; $400x + 700y = 26000$. Substitute $x = 50 - y$: $20000 - 400y + 700y = 26000 \Rightarrow 300y = 6000 \Rightarrow y = 20$, $x = 30$. So 30 workers earn ₱400 and 20 earn ₱700. Check: $12000 + 14000 = 26000$ ✔️.
"""))
    md(RUBRIC)
    md(r"""
    ## 🔭 Why this matters for calculus
    The case study used every tool you need in Weeks 9–13: **functions** (`labor_profile`, $p(a)$), **domains** (age 15–99, rate > 0), **solving** $p(a) = m$ and $p(a) \ge m$, and the **vertex** of a parabola, which is where the derivative equals zero. In calculus you will meet the same economic questions, with limits and derivatives as the new tools.

    ## 📝 Summary (Part 9 cheat-sheet)
    | Step | What to do |
    |---|---|
    | 1. Classify | linear, quadratic, radical, absolute value, inequality, exponent, or system? |
    | 2. Solve by hand | choose the method from the decision guide |
    | 3. Check | substitute; `sp.solve` / `sp.solveset` / `np.linalg.solve` |
    | 4. Domain | is it allowed (denominator ≠ 0, radicand ≥ 0, realistic range)? |
    | 5. Interpret | one sentence: *In our sample, …*, plus a limitation |

    New Python this Part: functions with `if` domain checks returning dictionaries, `pd.DataFrame({...})` from dictionaries, and `plt.subplots(2, 2)` multi-panel figures.
    """)
