from kit import md, code, details, exercise, concept_card, interpret, RUBRIC


def build():
    md(r"""
    ---
    # ⚖️ Part 7 · Week 6: Algebraic Equations (Linear, Quadratic, Radical, Absolute Value)
    **Week 6 (with Week 5 practice) · CLO1, CLO3 · ⏱️ Est. time: 80 min**
    📚 *Readings:* Swokowski & Cole (2011), *Equations and Inequalities* (linear, quadratic and other types of equations); Rees, Sparks & Rees (2003), *Linear Equations* and *Quadratic Equations*; Sydsaeter et al. (2022), *Solving Equations*; economic framing: Chiang & Wainwright (2004), *Equilibrium Analysis in Economics*.

    🎯 **Learning objectives.** By the end of Part 7 you can:
    1. **Solve** linear equations, including equations with fractions, justifying each step.
    2. **Solve** quadratic equations by factoring, completing the square, and the quadratic formula.
    3. **Find** the vertex (peak) of a quadratic by completing the square, and **apply** it to an age–pay profile.
    4. **Solve** radical and absolute-value equations and **reject** extraneous roots.

    🧭 **Big picture.** Equilibrium in economics means *solving an equation*: supply = demand, revenue = cost (break-even), marginal benefit = marginal cost. Workers and policymakers ask equation questions too: *"How many hours must I work to earn ₱3,000 a week?"*, *"At what age does pay peak?"*. Solving is only half the job. The other half is **checking** that the answer makes sense.
    """)
    md(r"""
    ## 🔁 Warm-up: Week 5 practice (5 min)
    1. Factor $x^2 - 2x - 15$.
    2. Simplify $\dfrac{x^2 - 1}{x^2 + 2x + 1}$ and state the restrictions.
    3. Combine $\dfrac{2}{x} - \dfrac{1}{x - 1}$.
    """ + "\n" + details("Answers", r"1. $(x - 5)(x + 3)$. 2. $\frac{(x-1)(x+1)}{(x+1)^2} = \frac{x - 1}{x + 1}$, $x \ne -1$. 3. $\frac{2(x-1) - x}{x(x-1)} = \frac{x - 2}{x(x - 1)}$, $x \ne 0, 1$."))

    # 7.1
    md("## Lesson 7.1 · Linear equations (including fractions) ⏱️ 20 min")
    concept_card("linear equations",
        r"""A **linear equation** in $x$ can be written $ax + b = 0$ with $a \ne 0$, and it has exactly one solution $x = -b/a$.
**Properties of equality:** you may add or subtract the same quantity on both sides, and multiply or divide both sides by the same **nonzero** number.
**Fractions:** multiply both sides by the **LCD** to clear the denominators. Check that no denominator becomes 0.
**Always check** by substituting back into the *original* equation.""",
        "Swokowski & Cole, *Equations* (linear equations); Rees, Sparks & Rees, *Linear Equations*; Sydsaeter et al., *Solving Equations*.")
    md(r"""
    ### ✍️ Step 2 · Solve by Hand
    **(a)** At ₱62.50/hour, how many hours give ₱3,000 per week?
    $$62.5h = 3000 \;\Rightarrow\; h = \frac{3000}{62.5} = 48 \quad \text{(divide both sides by } 62.5 \ne 0).$$
    *Check:* $62.5 \times 48 = 3000$ ✔️.

    **(b)** After $\tfrac15$ of weekly pay $W$ goes to transport, ₱2,000 remains:
    $$W - \tfrac{1}{5}W = 2000 \;\Rightarrow\; \tfrac45 W = 2000 \;\Rightarrow\; W = 2000 \cdot \tfrac54 = 2500.$$
    **(c)** $\dfrac{h}{8} + \dfrac{h}{10} = 9$. Multiply both sides by the LCD 40: $5h + 4h = 360 \Rightarrow 9h = 360 \Rightarrow h = 40$.
    ### 🐍 Step 3 · Check with Python
    New Python idea: `sp.Eq(left, right)` builds an equation, and `sp.solve(equation, variable)` solves it. The answer is a **list** of solutions.
    """)
    code(r'''
    h, W_ = sp.symbols("h W")
    print(sp.solve(sp.Eq(sp.Rational("62.5") * h, 3000), h))          # [48]
    print(sp.solve(sp.Eq(W_ - W_ / 5, 2000), W_))                     # [2500]
    print(sp.solve(sp.Eq(h / 8 + h / 10, 9), h))                       # [40]
    print("Check (c):", sp.Rational(40, 8) + sp.Rational(40, 10))       # 9 ✔
    ''')
    md("### 📊 Step 4 · Apply to LFS Data\n**Question:** at the **median hourly pay** in our sample, how many hours per week are needed to earn ₱3,000? And how does that differ across regions?")
    code(r'''
    r_med = paid["hourly_pay"].median()                        # from Part 6 (safe division)
    hours_needed = sp.solve(sp.Eq(r_med * h, 3000), h)[0]      # [0] takes the first (only) solution
    print(f"Median hourly pay ₱{r_med:,.2f} → hours needed for ₱3,000: {float(hours_needed):.1f}")
    print("Check: r × h =", round(r_med * float(hours_needed), 2))
    ''')
    code(r'''
    region_rate = paid.groupby("region")["hourly_pay"].median()
    region_hours = (3000 / region_rate).sort_values()            # h = 3000 / r, for every region at once
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.barh(region_hours.index, region_hours.values, color=OKABE_ITO[2])
    ax.axvline(40, color="black", ls="--", label="40-hour week")
    ax.set_title("Hours per week needed to earn ₱3,000 at each region's median hourly pay")
    ax.set_xlabel("Hours per week (h = 3000 / r)"); ax.set_ylabel("Region"); ax.legend(); plt.show()
    ''')
    md(r"""
    *Alt text:* horizontal bars giving the hours needed in each region, with a dashed vertical line at 40 hours.
    **Takeaway:** where hourly pay is lower, the solution $h = 3000/r$ is larger. Bars past the dashed line mean more than a standard 40-hour week is needed.
    """)
    interpret(r"Interpret the national solution $h$ in one sentence. Is the target reachable within a 40-hour week at the median rate? What does the equation *ignore*?",
              r"*In our sample, a worker earning the median hourly pay would need about __ hours per week to earn ₱3,000.* If $h > 40$ the target requires overtime. The model assumes a constant hourly rate: no overtime premium, no taxes or deductions, and no limit on available hours.")

    # 7.2
    md("## Lesson 7.2 · Quadratic equations and the peak of a profile ⏱️ 25 min")
    concept_card("quadratic equations",
        r"""$ax^2 + bx + c = 0$ ($a \ne 0$) can be solved by:
1. **Factoring** and the zero-product property: $AB = 0 \Rightarrow A = 0$ or $B = 0$.
2. **Completing the square:** $x^2 + bx = \left(x + \tfrac{b}{2}\right)^2 - \tfrac{b^2}{4}$.
3. **Quadratic formula:** $x = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a}$. The **discriminant** $D = b^2 - 4ac$ gives 2 real roots ($D > 0$), 1 ($D = 0$), or none ($D < 0$).
**Vertex form:** $ax^2 + bx + c = a\left(x + \tfrac{b}{2a}\right)^2 + \left(c - \tfrac{b^2}{4a}\right)$. The vertex is at $x^* = -\tfrac{b}{2a}$. If $a < 0$ the parabola opens **down** and the vertex is a **maximum**.""",
        "Swokowski & Cole, *Quadratic Equations*; Rees, Sparks & Rees, *Quadratic Equations*; Sydsaeter et al., *Solving Equations* (quadratic equations).")
    md(r"""
    ### ✍️ Step 2 · Solve by Hand
    - **Factoring:** $x^2 - 6x + 5 = 0 \Rightarrow (x - 1)(x - 5) = 0 \Rightarrow x = 1$ or $x = 5$.
    - **Completing the square:** $x^2 + 8x + 7 = 0 \Rightarrow x^2 + 8x + 16 = 9 \Rightarrow (x + 4)^2 = 9 \Rightarrow x + 4 = \pm 3 \Rightarrow x = -1$ or $x = -7$.
    - **Formula:** $2x^2 - 3x - 1 = 0$: $D = 9 + 8 = 17$, so $x = \dfrac{3 \pm \sqrt{17}}{4}$.
    - **Peak of a profile:** $p(a) = -0.2a^2 + 18a + 150$. Completing the square:
    $$-0.2(a^2 - 90a) + 150 = -0.2\big[(a - 45)^2 - 2025\big] + 150 = -0.2(a - 45)^2 + 555.$$
    Since $-0.2(a-45)^2 \le 0$, pay is **largest at $a^* = 45$**, where $p = 555$.
    ### 🐍 Step 3 · Check with Python
    """)
    code(r'''
    x = sp.symbols("x")
    print(sp.solve(x**2 - 6 * x + 5, x), sp.solve(x**2 + 8 * x + 7, x), sp.solve(2 * x**2 - 3 * x - 1, x))
    age_s = sp.symbols("a")
    demo = -sp.Rational(1, 5) * age_s**2 + 18 * age_s + 150
    vertex_form = -sp.Rational(1, 5) * (age_s - 45)**2 + 555
    print("Vertex form matches?", sp.expand(vertex_form - demo) == 0, "| peak age:", sp.Rational(-18) / (2 * -sp.Rational(1, 5)))
    ''')
    md(r"""
    ### 📊 Step 4 · Apply to LFS Data
    **Question 1:** at what age does the fitted profile $p(a) = c_0 + c_1 a + c_2 a^2$ peak? Using the vertex formula, $a^* = -c_1/(2c_2)$. This is a maximum only if $c_2 < 0$.
    **Question 2:** at what ages is predicted pay **equal to the sample median**? Solve $p(a) = m$. We use `sp.solveset(..., domain=sp.S.Reals)` so that only **real** roots come back, and then keep only realistic ages (15–99).
    """)
    code(r'''
    c2, c1, c0 = np.polyfit(paid["age"], paid["daily_pay"], 2)          # refit (same as Part 1)
    if c2 < 0:
        peak_age = -c1 / (2 * c2)                                          # vertex: a* = −b/(2a)
        peak_pay = c0 - c1**2 / (4 * c2)                                   # vertex value: c − b²/(4a)
        print(f"The profile opens DOWN (c2 = {c2:.5f} < 0): peak at age {peak_age:.1f}, ₱{peak_pay:,.2f}/day")
    else:
        print("c2 ≥ 0: the fitted profile opens UP, so it has no peak (a minimum instead).")
    ''')
    code(r'''
    a = sp.symbols("a", real=True)
    p_expr = c0 + c1 * a + c2 * a**2
    m = paid["daily_pay"].median()
    roots = sp.solveset(sp.Eq(p_expr, m), a, domain=sp.S.Reals)          # real solutions only
    print("All real roots:", roots)
    realistic = [float(r) for r in roots if 15 <= float(r) <= 99]         # keep plausible ages (a short loop inside [ ])
    print("Ages (15–99) where predicted pay equals the median:", [round(v, 1) for v in realistic])
    ''')
    md(r"""
    > ℹ️ `[float(r) for r in roots if ...]` is a **list comprehension**, a compact one-line `for` loop that builds a list. It is optional syntax. The long version would be: `realistic = []`, then `for r in roots:` → `if 15 <= float(r) <= 99: realistic.append(float(r))`.
    """)
    code(r'''
    grid = np.linspace(15, 80, 200)
    fig, ax = plt.subplots()
    ax.plot(grid, c0 + c1 * grid + c2 * grid**2, lw=3, label="Fitted profile p(a)")
    ax.axhline(m, color=OKABE_ITO[3], ls="--", label=f"Sample median ₱{m:,.0f}")
    for r_ in realistic:
        ax.plot(r_, m, "o", ms=10, color="black")                          # where p(a) = m
    ax.set_title("Where does the fitted age–pay profile equal the median?")
    ax.set_xlabel("Age (years)"); ax.set_ylabel("Predicted daily pay (₱)"); ax.legend(); plt.show()
    ''')
    md(r"""
    *Alt text:* a hill-shaped curve and a horizontal dashed line at the median pay. Black dots mark where they cross.
    **Takeaway:** a quadratic equation can have two solutions: one on the rising side of the hill and one on the falling side. Between them, predicted pay is **above** the median (an inequality, coming in Part 8).
    """)
    interpret(r"State the peak age and the two crossing ages in plain English. Why do we reject roots outside 15–99, even though they solve the equation?",
              r"*In our sample, predicted daily pay peaks at about age __ (₱__ per day), and it equals the median at about ages __ and __.* Roots outside 15–99 solve the **algebra** but not the **economics**: the profile was fitted only to working-age adults, and nobody in the sample is 120 years old. Always interpret solutions within the model's domain.")

    # 7.3
    md("## Lesson 7.3 · Radical and absolute-value equations; extraneous roots ⏱️ 20 min")
    concept_card("radical and absolute-value equations",
        r"""**Radical equations:** isolate the radical, then raise both sides to a power. Squaring can create **extraneous roots**, which are solutions of the new equation but not of the original. **Check every candidate** in the original equation.
**Absolute value:** for $k \ge 0$, $|X| = k \iff X = k$ or $X = -k$. If $k < 0$ there is no solution.
**Growth rates:** $P(1 + r)^2 = Q \Rightarrow 1 + r = \pm\sqrt{Q/P}$. Only the **positive** root makes economic sense, because $1 + r > 0$.""",
        "Swokowski & Cole, *Other Types of Equations* (radicals, absolute values, extraneous solutions); Sydsaeter et al., *Solving Equations*.")
    md(r"""
    ### ✍️ Step 2 · Solve by Hand
    **(a)** $\sqrt{x + 6} = x$. Square both sides: $x + 6 = x^2 \Rightarrow x^2 - x - 6 = 0 \Rightarrow (x - 3)(x + 2) = 0 \Rightarrow x = 3$ or $x = -2$.
    Check: $x = 3$: $\sqrt{9} = 3$ ✔️. $x = -2$: $\sqrt{4} = 2 \ne -2$ ✘ **extraneous**. Solution: $x = 3$.

    **(b)** $|x - 500| = 120 \Rightarrow x - 500 = 120$ or $x - 500 = -120 \Rightarrow x = 620$ or $x = 380$: the two pay levels exactly ₱120 from ₱500.

    **(c)** Pay grows from ₱400 to ₱484 in 2 years: $400(1+r)^2 = 484 \Rightarrow (1+r)^2 = 1.21 \Rightarrow 1 + r = \pm 1.1$. We reject $-1.1$, so $r = 0.10$ (10% per year).
    ### 🐍 Step 3 · Check with Python
    """)
    code(r'''
    print("Squared equation roots:", sp.solve(x**2 - x - 6, x))          # [-2, 3] includes the extraneous root
    print("Original radical equation:", sp.solve(sp.sqrt(x + 6) - x, x))  # SymPy checks the roots → [3]
    for cand in [3, -2]:
        print(f"x = {cand}: √(x+6) = {sp.sqrt(cand + 6)}, x = {cand} → {'✔' if sp.sqrt(cand + 6) == cand else '✘ extraneous'}")
    print("|x − 500| = 120:", sp.solveset(sp.Abs(x - 500) - 120, x, domain=sp.S.Reals))
    ''')
    md("### 📊 Step 4 · Apply to LFS Data\n**Questions:** (1) Which pay levels lie exactly one *mean absolute deviation* (MAD, from Part 4) away from the median? (2) What constant yearly rate would take the **female** median pay to the **male** median in 2 years?")
    code(r'''
    mad = np.abs(paid["daily_pay"] - m).mean()
    k = sp.symbols("k", real=True)
    levels = sp.solveset(sp.Abs(k - m) - mad, k, domain=sp.S.Reals)       # |k − m| = MAD
    print(f"Median ₱{m:,.2f}, MAD ₱{mad:,.2f} → pay levels:", [round(float(v), 2) for v in levels])
    within = (np.abs(paid["daily_pay"] - m) <= mad).mean()
    print(f"Share of paid workers within one MAD of the median: {within:.1%}")
    ''')
    code(r'''
    med_F = paid[paid["sex"] == "Female"]["daily_pay"].median()
    med_M = paid[paid["sex"] == "Male"]["daily_pay"].median()
    rr = sp.symbols("r", real=True)
    candidates = sp.solve(sp.Eq(med_F * (1 + rr)**2, med_M), rr)          # two candidates from ±√
    print("Candidates:", [round(float(c), 4) for c in candidates])
    valid = [float(c) for c in candidates if 1 + float(c) > 0]             # economic check: 1 + r > 0
    print(f"Valid growth rate: {valid[0]:.2%} per year (female median ₱{med_F:,.0f} → male median ₱{med_M:,.0f})")
    ''')
    interpret(r"One candidate rate is below $-100\%$. Explain why it is mathematically a root but economically extraneous.",
              r"Squaring hides the sign: both $1 + r = +\sqrt{M/F}$ and $1 + r = -\sqrt{M/F}$ satisfy $(1+r)^2 = M/F$. But $1 + r$ is the **growth factor** that multiplies pay, and it must be positive (pay can't become negative). So we keep only the positive root. If the female median is *above* the male median in our sample, the valid $r$ is negative, a decline, which is still meaningful.")

    # end matter
    md(r"""
    ## ⚠️ Common mistakes
    - Dividing both sides by an expression that could be **zero**: from $x^2 = 3x$, dividing by $x$ loses the root $x = 0$. Factor instead: $x(x - 3) = 0$.
    - Forgetting the $\pm$ when taking square roots: $x^2 = 9 \Rightarrow x = \pm 3$.
    - Not checking radical equations, which leaves extraneous roots in the answer.
    - Splitting $|X| = k$ into only one case, or "solving" $|X| = -2$ (there's no solution).
    - Sign slips in the quadratic formula: it is $-b$, and $b^2 - 4ac$, with the **whole** numerator over $2a$.
    - Reporting roots that make no economic sense (negative hours, age 150, $1 + r < 0$).
    - In SymPy, using `=` instead of `sp.Eq(...)` for an equation.
    """)
    md("## ✅ Check your understanding\n\n" + "\n\n".join([
        r"**Q1.** Solve $\dfrac{x}{3} - 2 = \dfrac{x}{4}$." + "\n\n" + details("Answer", r"Multiply by 12: $4x - 24 = 3x \Rightarrow x = 24$."),
        r"**Q2 (Fill in).** The discriminant of $x^2 + 4x + 5$ is ___, so it has ___ real roots." + "\n\n" + details("Answer", r"$16 - 20 = -4$, so it has **no** real roots."),
        r"**Q3 (True/False).** $x = -2$ solves $\sqrt{x + 6} = x$." + "\n\n" + details("Answer", r"**False.** It is extraneous: $\sqrt{4} = 2 \ne -2$."),
        r"**Q4.** The vertex of $p(a) = -2a^2 + 120a + 100$ is at $a =$ ___." + "\n\n" + details("Answer", r"$-120/(2 \cdot -2) = 30$."),
        r"**Q5 (MCQ).** $|2x - 1| = 5$ has solutions (a) $3$ (b) $3, -2$ (c) $-3, 2$ (d) none" + "\n\n" + details("Answer", r"**(b)** $2x - 1 = 5 \Rightarrow x = 3$; $2x - 1 = -5 \Rightarrow x = -2$."),
    ]))

    md("## 💻 Coding exercises (Part 7)")
    exercise("7.1", "⭐", "Solve by hand, then check",
             r"Solve $4x - 7 = 2x + 9$ **by hand**. Store the number in `ex7_1`, then (optionally) confirm it with `sp.solve`.",
             "ex7_1 = None    # YOUR CODE HERE",
             "ex7_1 = 8",
             'check(ex7_1, sp.solve(sp.Eq(4 * x - 7, 2 * x + 9), x)[0], hint="Subtract 2x and add 7 on both sides: 2x = 16.")')
    exercise("7.2", "⭐", "Hours for ₱2,500",
             r"At the median hourly pay `r_med`, store the hours needed to earn ₱2,500 per week in `ex7_2`.",
             "ex7_2 = None    # YOUR CODE HERE",
             "ex7_2 = 2500 / r_med",
             'check(ex7_2, 2500 / paid["hourly_pay"].median(), hint="Solve r·h = 2500 for h, so h = 2500 / r.")')
    exercise("7.3", "⭐⭐", "Peak age of the women's profile",
             r"Fit a quadratic profile to **female** paid workers with `np.polyfit(..., 2)` and store its vertex age $-c_1/(2c_2)$ in `ex7_3`.",
             "ex7_3 = None    # YOUR CODE HERE",
             'fem = paid[paid["sex"] == "Female"]\nf2, f1, f0 = np.polyfit(fem["age"], fem["daily_pay"], 2)\nex7_3 = -f1 / (2 * f2)',
             'fm = paid[paid["sex"] == "Female"]\ncf = np.polyfit(fm["age"], fm["daily_pay"], 2)\ncheck(ex7_3, -cf[1] / (2 * cf[0]), hint="np.polyfit returns [c2, c1, c0] (highest power first). Vertex = −c1 / (2·c2).")')
    exercise("7.4", "⭐⭐", "Roots of a quadratic",
             r"Solve $x^2 - 2x - 15 = 0$ **by hand**, and store both roots as a sorted list, e.g. `[-1, 4]`, in `ex7_4`.",
             "ex7_4 = None    # YOUR CODE HERE",
             "ex7_4 = [-3, 5]",
             'check(ex7_4, sorted(sp.solve(x**2 - 2 * x - 15, x)), hint="Factor: two numbers with product −15 and sum −2. List the smaller root first.")')
    exercise("7.5", "⭐⭐⭐", "Catch-up growth in 3 years",
             r"Store the constant yearly rate $r$ that takes the **female** median daily pay to the **male** median in **3** years, $F(1 + r)^3 = M$, in `ex7_5`.",
             "ex7_5 = None    # YOUR CODE HERE",
             'ex7_5 = (med_M / med_F) ** (1 / 3) - 1',
             'check(ex7_5, (med_M / med_F) ** (1 / 3) - 1, hint="(1 + r)^3 = M/F, so r = (M/F)^(1/3) − 1. A cube root has only one real value.")')

    md(r"""
    ## ✍️ Board-work practice 🗣️
    **B7.1** Solve $\dfrac{x}{3} - \dfrac{x - 2}{4} = 2$. Name the property used to clear the fractions, and check your answer.

    **B7.2** Solve $x^2 - 10x + 16 = 0$ by **completing the square**. Then confirm with the quadratic formula.

    **B7.3** Solve $\sqrt{2x + 3} = x$ and identify any extraneous root.

    **B7.4** A fitted profile is $p(a) = -0.2a^2 + 18a + 150$. Find the peak age and peak pay by completing the square, and explain why it is a maximum.
    """)
    md(details("Solutions to board-work practice", r"""
**B7.1** Multiply both sides by the LCD 12 (multiplication property of equality): $4x - 3(x - 2) = 24 \Rightarrow 4x - 3x + 6 = 24$ (distributive) $\Rightarrow x = 18$. Check: $6 - 4 = 2$ ✔️.

**B7.2** $x^2 - 10x = -16 \Rightarrow x^2 - 10x + 25 = 9 \Rightarrow (x - 5)^2 = 9 \Rightarrow x - 5 = \pm 3 \Rightarrow x = 8$ or $x = 2$. Formula: $x = \frac{10 \pm \sqrt{100 - 64}}{2} = \frac{10 \pm 6}{2}$ ✔️.

**B7.3** Square both sides: $2x + 3 = x^2 \Rightarrow x^2 - 2x - 3 = 0 \Rightarrow (x - 3)(x + 1) = 0$. Check: $x = 3$: $\sqrt9 = 3$ ✔️; $x = -1$: $\sqrt1 = 1 \ne -1$ ✘ (extraneous). Solution: $x = 3$.

**B7.4** $p(a) = -0.2(a - 45)^2 + 555$. Since $(a - 45)^2 \ge 0$ and $-0.2 < 0$, the first term is $\le 0$ and equals 0 only at $a = 45$. So the maximum is $p(45) = 555$: predicted pay peaks at age 45, at ₱555 per day.
"""))
    md(RUBRIC)
    md(r"""
    ## 🔭 Why this matters for calculus
    - Finding a maximum by completing the square only works for quadratics. Calculus generalizes it: **set the derivative to zero and solve the equation**, $p'(a) = c_1 + 2c_2 a = 0 \Rightarrow a^* = -c_1/(2c_2)$. That is the same answer as the vertex formula, as Part 1 hinted!
    - Optimization problems in economics (maximize profit, minimize cost) end in solving equations like these, so fluent solving is essential.
    - Checking roots against the domain becomes checking critical points against constraints.

    ## 📝 Summary (Part 7 cheat-sheet)
    | Rule | Python |
    |---|---|
    | Linear: isolate $x$; clear fractions with the LCD; check | `sp.solve(sp.Eq(lhs, rhs), x)` |
    | Quadratic: factor / complete the square / $x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$ | `sp.solve`, `sp.solveset(..., domain=sp.S.Reals)` |
    | Vertex $x^* = -b/(2a)$, value $c - b^2/(4a)$ | `np.polyfit(x, y, 2)` |
    | Radical: isolate, square, **check** (extraneous roots) | substitute with `.subs` |
    | $\lvert X\rvert = k \iff X = \pm k$ ($k \ge 0$) | `sp.Abs`, `sp.solveset` |
    | Keep economically valid roots | `[v for v in roots if condition]` (optional) |
    """)
