from kit import md, code, details, exercise, concept_card, interpret, RUBRIC


def build():
    md(r"""
    ---
    # 🧮 Part 8 · Week 7: Inequalities and Systems of Linear Equations (+ Midterm Review)
    **Week 7 · CLO1, CLO2 · ⏱️ Est. time: 90 min**
    📚 *Readings:* Swokowski & Cole (2011), *Inequalities* (quadratic and absolute-value inequalities) and *Systems of Equations*; Rees, Sparks & Rees (2003), *Systems of Equations*; Sydsaeter et al. (2022), *Solving Equations* (two equations in two unknowns); economic framing: Chiang & Wainwright (2004), *Equilibrium Analysis*: partial market equilibrium, a linear model.

    🎯 **Learning objectives.** By the end of Part 8 you can:
    1. **Solve** linear, quadratic and absolute-value inequalities using sign charts, and **shade** solution regions on a graph.
    2. **Solve** 2×2 linear systems by substitution, elimination and graphing.
    3. **Solve** 2×2 and 3×3 systems with matrices, and **classify** a system as consistent, inconsistent or dependent.
    4. **Review** Weeks 1–6 with a mixed midterm practice sheet.

    🧭 **Big picture.** Market equilibrium is a **system**: the quantity demanded and the quantity supplied must hold *at the same time*. Many data questions are systems too: if we know group totals and group averages, we can recover the unknown group sizes. Inequalities describe **feasible** choices: hours that meet an earnings target, or ages where pay is above the median.
    """)

    # 8.1
    md("## Lesson 8.1 · Linear, quadratic and absolute-value inequalities ⏱️ 25 min")
    concept_card("solving inequalities",
        r"""- **Linear:** same steps as an equation; **flip** the sign when you multiply or divide by a negative.
- **Quadratic** (and other factorable ones), using a **sign chart**: (1) move everything to one side; (2) factor; (3) mark the zeros on a number line; (4) test the sign in each region; (5) choose the regions that satisfy the inequality, with endpoints included for $\le$ / $\ge$.
- **Absolute value** ($k > 0$): $|X| < k \iff -k < X < k$ (*within* $k$), and $|X| > k \iff X < -k$ or $X > k$ (*farther than* $k$).""",
        "Swokowski & Cole, *Inequalities* (sign charts; inequalities with absolute values); Sydsaeter et al., *Algebra* (inequalities).")
    md(r"""
    ### ✍️ Step 2 · Solve by Hand
    **(a)** $x^2 - 5x - 14 < 0 \Rightarrow (x - 7)(x + 2) < 0$. The zeros $-2$ and $7$ split the line into three regions:

    | Region | Test $x$ | $x - 7$ | $x + 2$ | Product |
    |---|---|---|---|---|
    | $x < -2$ | $-3$ | $-$ | $-$ | $+$ |
    | $-2 < x < 7$ | $0$ | $-$ | $+$ | $-$ ✔️ |
    | $x > 7$ | $8$ | $+$ | $+$ | $+$ |

    Solution: $(-2, 7)$.
    **(b)** $|h - 40| \le 8 \iff -8 \le h - 40 \le 8 \iff 32 \le h \le 48$: hours *within 8* of a 40-hour week, $[32, 48]$.
    **(c)** $|x - 3| > 5 \iff x < -2$ or $x > 8$: $(-\infty, -2) \cup (8, \infty)$.
    ### 🐍 Step 3 · Check with Python
    """)
    code(r'''
    x = sp.symbols("x", real=True)
    print(sp.solveset(x**2 - 5 * x - 14 < 0, x, domain=sp.S.Reals))
    print(sp.solveset(sp.Abs(x - 40) <= 8, x, domain=sp.S.Reals))
    print(sp.solveset(sp.Abs(x - 3) > 5, x, domain=sp.S.Reals))
    for test in [-3, 0, 8]:                                    # the sign chart's test points
        print(f"x = {test:>2}: (x − 7)(x + 2) = {(test - 7) * (test + 2):>4}")
    ''')
    md(r"""
    ### 📊 Step 4 · Apply to LFS Data
    **(a)** At the median hourly pay $r$, which weekly hours $h$ give earnings of **at least ₱3,500**? We need $rh \ge 3500$, so $h \ge 3500/r$.
    """)
    code(r'''
    h = sp.symbols("h", real=True)
    r_med = paid["hourly_pay"].median()
    feasible = sp.solveset(r_med * h >= 3500, h, domain=sp.S.Reals)
    print(f"Median hourly pay ₱{r_med:,.2f} → hours needed: {feasible}")
    share_ok = (has_hours["hours_week"] >= 3500 / r_med).mean()
    print(f"Share of employed (with hours) already working at least that many hours: {share_ok:.1%}")
    ''')
    md(r"""
    **(b) A quadratic inequality on real data:** for which ages is predicted pay **at least the median**, $p(a) \ge m$? We intersect the solution with the realistic age range $[15, 99]$.
    New Python idea: `ax.fill_between(x, y1, y2, where=...)` shades the region between two curves, so you can *see* the solution set.
    """)
    code(r'''
    a = sp.symbols("a", real=True)
    c2, c1, c0 = np.polyfit(paid["age"], paid["daily_pay"], 2)
    m = paid["daily_pay"].median()
    above = sp.solveset(c0 + c1 * a + c2 * a**2 >= m, a, domain=sp.S.Reals).intersect(sp.Interval(15, 99))
    print("Ages where predicted pay ≥ median:", above)
    grid = np.linspace(15, 80, 300)
    pvals = c0 + c1 * grid + c2 * grid**2
    ''')
    code(r'''
    fig, ax = plt.subplots()
    ax.plot(grid, pvals, lw=3, label="Fitted profile p(a)")
    ax.axhline(m, color=OKABE_ITO[3], ls="--", label=f"Median ₱{m:,.0f}")
    ax.fill_between(grid, pvals, m, where=pvals >= m, alpha=0.3, color=OKABE_ITO[2], label="p(a) ≥ median")
    ax.set_title("Solving the quadratic inequality p(a) ≥ median, graphically")
    ax.set_xlabel("Age (years)"); ax.set_ylabel("Predicted daily pay (₱)"); ax.legend(); plt.show()
    ''')
    md(r"""
    *Alt text:* the hill-shaped profile and a dashed horizontal median line. The area where the curve is above the line is shaded green.
    **Takeaway:** the solution of the inequality is the **interval of ages under the shaded area**, between the two crossing points found in Part 7.

    **(c) Absolute-value inequality:** what share of employed persons worked *within 8 hours* of a 40-hour week, $|h - 40| \le 8$?
    """)
    code(r'''
    within_8 = (np.abs(has_hours["hours_week"] - 40) <= 8)
    print(f"|h − 40| ≤ 8, i.e. 32 ≤ h ≤ 48: {within_8.mean():.1%} of employed persons with reported hours")
    ''')
    interpret(r"Write two sentences: one interpreting the age interval where $p(a) \ge m$, and one interpreting the share with $|h - 40| \le 8$.",
              r"*In our sample, predicted daily pay is at or above the median for ages about __ to __, roughly the prime working years.* *About __% of employed persons worked within 8 hours of a standard 40-hour week (32–48 hours). The rest worked notably shorter or longer weeks.*")

    # 8.2
    md("## Lesson 8.2 · Systems of two linear equations ⏱️ 25 min")
    concept_card("2×2 linear systems",
        r"""A **system** asks for values that satisfy **all** the equations at once. Graphically, it is the **intersection** of the lines.
- **Substitution:** solve one equation for one variable and substitute it into the other.
- **Elimination:** add multiples of the equations to cancel a variable.
- Three possibilities: **one** solution (lines cross, *consistent*), **none** (parallel lines, *inconsistent*), **infinitely many** (the same line, *dependent*).
*Economics:* market equilibrium solves $Q_d = Q_s$. For example, $Q = 100 - 2P$ and $Q = 20 + 2P$ give $P = 20$, $Q = 60$.""",
        "Rees, Sparks & Rees, *Systems of Equations*; Sydsaeter et al., *Solving Equations* (two equations with two unknowns); Chiang & Wainwright, *Partial Market Equilibrium: A Linear Model*.")
    md(r"""
    ### ✍️ Step 2 · Solve by Hand
    $$\begin{cases} x + y = 10 \\ 3x + 5y = 38 \end{cases}$$
    **Substitution:** $x = 10 - y \Rightarrow 3(10 - y) + 5y = 38 \Rightarrow 30 + 2y = 38 \Rightarrow y = 4$, so $x = 6$.
    **Elimination:** multiply the first equation by 3: $3x + 3y = 30$. Subtract it from the second: $2y = 8 \Rightarrow y = 4$, and then $x = 6$.
    **Check:** $6 + 4 = 10$ ✔️, $18 + 20 = 38$ ✔️.
    ### 🐍 Step 3 · Check with Python
    New Python idea: pass a **list** of equations and a list of unknowns to `sp.solve`. The answer is a dictionary.
    """)
    code(r'''
    xs, ys = sp.symbols("x y")
    print(sp.solve([sp.Eq(xs + ys, 10), sp.Eq(3 * xs + 5 * ys, 38)], [xs, ys]))
    Pp, Qq = sp.symbols("P Q")
    print("Market equilibrium:", sp.solve([sp.Eq(Qq, 100 - 2 * Pp), sp.Eq(Qq, 20 + 2 * Pp)], [Pp, Qq]))
    ''')
    md(r"""
    ### 📊 Step 4 · Apply to LFS Data: recovering group sizes from totals
    Suppose a report gives only the **total number** of paid workers $N$, their **total** daily pay $T$, and the **average** daily pay of college graduates ($\bar d_C$) and of everyone else ($\bar d_O$). How many workers are in each group? Let $x$ = college graduates and $y$ = others:
    $$\begin{cases} x + y = N \\ \bar d_C\, x + \bar d_O\, y = T \end{cases}$$
    """)
    code(r'''
    is_college = paid["educ"] == "College or higher"
    N_total, T_total = len(paid), paid["daily_pay"].sum()
    d_C = paid[is_college]["daily_pay"].mean()
    d_O = paid[~is_college]["daily_pay"].mean()
    sol = sp.solve([sp.Eq(xs + ys, N_total), sp.Eq(d_C * xs + d_O * ys, T_total)], [xs, ys])
    print(f"Solved:  x (college) = {float(sol[xs]):.1f},  y (others) = {float(sol[ys]):.1f}")
    print(f"Actual:  college = {is_college.sum()},  others = {(~is_college).sum()}")
    ''')
    code(r'''
    xgrid = np.linspace(0, N_total, 100)
    fig, ax = plt.subplots()
    ax.plot(xgrid, N_total - xgrid, lw=2.5, label="x + y = N  (headcount)")
    ax.plot(xgrid, (T_total - d_C * xgrid) / d_O, lw=2.5, ls="--", label="d̄_C·x + d̄_O·y = T  (pay bill)")
    ax.plot(float(sol[xs]), float(sol[ys]), "ko", ms=10, label="Intersection = solution")
    ax.set_xlim(0, N_total); ax.set_ylim(0, N_total * 1.2)
    ax.set_title("Two equations, two unknowns: recovering group sizes")
    ax.set_xlabel("x = number of college graduates"); ax.set_ylabel("y = number of other paid workers"); ax.legend(); plt.show()
    ''')
    md(r"""
    *Alt text:* two straight lines falling from left to right with different slopes, crossing at one black dot.
    **Takeaway:** the system has **one** solution because the lines have different slopes ($-1$ versus $-\bar d_C/\bar d_O$), which happens exactly when the two group averages differ.
    """)
    interpret(r"Why does the method fail if the two groups have *exactly* the same average pay? Use the words *parallel* or *dependent*.",
              r"If $\bar d_C = \bar d_O = \bar d$, the second equation becomes $\bar d(x + y) = T$, which is just $\bar d$ times the first equation ($T = \bar d N$). The two lines coincide (the system is **dependent**), so infinitely many splits $(x, y)$ fit. The pay totals carry no extra information about group sizes.")

    # 8.3
    md("## Lesson 8.3 · Matrices, 3×3 systems, and types of systems ⏱️ 20 min")
    concept_card("matrix form of a linear system",
        r"""A system can be written as $A\mathbf{x} = \mathbf{b}$: $A$ holds the coefficients, $\mathbf{x}$ the unknowns, and $\mathbf{b}$ the right-hand sides.
For a 2×2 matrix $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, the **determinant** is $\det A = ad - bc$.
- $\det A \ne 0$ ⇒ exactly one solution.
- $\det A = 0$ ⇒ no solution (inconsistent) or infinitely many (dependent).
For 3×3 systems, use elimination by hand (reduce to two equations in two unknowns) or a matrix solver to check.""",
        "Rees, Sparks & Rees, *Systems of Equations* (determinants); Sydsaeter et al., *Solving Equations*; Chiang & Wainwright, *Linear Models and Matrix Algebra* (preview).")
    md(r"""
    ### ✍️ Step 2 · Solve by Hand
    **(a)** $\det\begin{pmatrix} 1 & 1 \\ 3 & 5\end{pmatrix} = 5 - 3 = 2 \ne 0$, so the system in Lesson 8.2 has a unique solution.
    **(b)** $x + y = 10,\; 2x + 2y = 30$. Doubling the first gives $2x + 2y = 20 \ne 30$, so it is **inconsistent** (parallel lines), with $\det = 2 - 2 = 0$.
    **(c)** $x + y = 10,\; 2x + 2y = 20$ is **dependent**: every point with $y = 10 - x$ works.
    **(d)** 3×3: $x + y + z = 6$, $x - y = 0$, $y + 2z = 7$. From the second, $x = y$. Then $2y + z = 6$ and $y + 2z = 7$. Eliminating gives $y = \tfrac53$, $z = \tfrac83$, $x = \tfrac53$.
    ### 🐍 Step 3 · Check with Python
    New Python idea: `np.array` builds a matrix, `np.linalg.det` computes its determinant, and `np.linalg.solve(A, b)` solves $A\mathbf{x} = \mathbf{b}$.
    """)
    code(r'''
    A2 = np.array([[1, 1], [3, 5]])
    print("det =", round(np.linalg.det(A2), 6), "| solution:", np.linalg.solve(A2, np.array([10, 38])))
    print("Inconsistent:", sp.solve([sp.Eq(xs + ys, 10), sp.Eq(2 * xs + 2 * ys, 30)], [xs, ys]))   # [] = no solution
    print("Dependent:   ", sp.solve([sp.Eq(xs + ys, 10), sp.Eq(2 * xs + 2 * ys, 20)], [xs, ys]))   # x = 10 − y
    A3 = np.array([[1, 1, 1], [1, -1, 0], [0, 1, 2]])
    print("3×3 solution:", np.linalg.solve(A3, np.array([6, 0, 7])), "| 5/3 ≈", round(5 / 3, 4), ", 8/3 ≈", round(8 / 3, 4))
    ''')
    md(r"""
    ### 📊 Step 4 · Apply to LFS Data: a 3×3 system
    Three education groups (Elementary or less / High school / Beyond high school) with unknown sizes $x_1, x_2, x_3$. We "know" the total headcount, the total daily pay bill, and the total weekly hours, plus each group's average pay and hours:
    $$\begin{cases} x_1 + x_2 + x_3 = N \\ \bar d_1 x_1 + \bar d_2 x_2 + \bar d_3 x_3 = T \\ \bar h_1 x_1 + \bar h_2 x_2 + \bar h_3 x_3 = H \end{cases}$$
    """)
    code(r'''
    p3 = paid.dropna(subset=["hours_week"]).copy()
    p3["educ3"] = p3["educ"].replace({"Post-secondary/technical": "Beyond high school",
                                      "College or higher": "Beyond high school"})
    groups = ["Elementary or less", "High school", "Beyond high school"]
    avg = p3.groupby("educ3")[["daily_pay", "hours_week"]].mean().loc[groups]   # rows in our chosen order
    A = np.array([[1, 1, 1], avg["daily_pay"].values, avg["hours_week"].values])
    b = np.array([len(p3), p3["daily_pay"].sum(), p3["hours_week"].sum()])
    print("det(A) =", round(np.linalg.det(A), 2))
    print("Solved sizes:", np.linalg.solve(A, b).round(1))
    print("Actual sizes:", p3["educ3"].value_counts().loc[groups].values)
    ''')
    interpret(r"The solved sizes match the actual ones. Explain *why* they must match (hint: how were $T$ and $H$ built?), and what would happen if the averages were rounded first.",
              r"Each total is exactly the sum over the groups of *(group average × group size)*, so the true sizes satisfy all three equations, and since $\det A \neq 0$ the solution is unique. If the averages were rounded, the equations would hold only approximately, and the solved sizes would be close to the true ones but not exact. With nearly parallel equations (similar averages across groups), small rounding errors can cause large errors in the solution.")

    # 8.4 midterm review
    md(r"""
    ## 📝 Lesson 8.4 · Midterm review sheet (Weeks 1–6) ⏱️ 30 min
    > Solve **by hand**, under exam conditions (no notes, no computer, no AI). Then reveal the answers. Mark yourself with the rubric below.

    1. *(Sets)* $U = \{1, \dots, 12\}$, $A$ = multiples of 2, $B$ = multiples of 3. Find $A \cap B$, $(A \cup B)'$, and verify $|A \cup B| = |A| + |B| - |A \cap B|$.
    2. *(Numbers)* Classify $-\tfrac{6}{3}$, $\sqrt{16}$, $\sqrt{5}$, $0.\overline{7}$, $\pi/2$.
    3. *(Properties)* Simplify $2(3x - 1) - (x - 4)$, naming every property.
    4. *(Inequalities)* Solve $-2 \le \dfrac{5 - x}{3} < 4$. Write the answer in interval notation and graph it.
    5. *(Exponents)* Simplify $\left(\dfrac{8x^{6}}{27y^{-3}}\right)^{2/3}$ for $x, y > 0$.
    6. *(Absolute value)* Find the distance between $-\tfrac{3}{2}$ and $\tfrac{7}{4}$.
    7. *(Growth)* ₱450 grows 8% per year. Write its value after $t$ years, and find the yearly rate that would instead double it in 9 years (as a radical).
    8. *(Polynomials)* Expand $(x - 2)^3$ and $(3x + 5)(3x - 5)$.
    9. *(Factoring)* Factor completely: $x^4 - 16$; $6x^2 - x - 2$; $x^3 + 27$.
    10. *(Rational expressions)* Simplify $\dfrac{x^2 - 5x + 6}{x^2 - 9} \cdot \dfrac{x + 3}{x - 2}$ and state the restrictions.
    11. *(Equations)* Solve $\dfrac{3}{x} + \dfrac{2}{x + 1} = 1$.
    12. *(Equations)* Solve $\sqrt{x + 7} = x + 1$ and check for extraneous roots.
    """)
    md(details("Answers to the midterm review sheet", r"""
1. $A = \{2,4,6,8,10,12\}$, $B = \{3,6,9,12\}$. $A \cap B = \{6, 12\}$; $A \cup B = \{2,3,4,6,8,9,10,12\}$, so $(A \cup B)' = \{1, 5, 7, 11\}$. $8 = 6 + 4 - 2$ ✔️.
2. $-6/3 = -2 \in \mathbb{Z}$; $\sqrt{16} = 4 \in \mathbb{N}$; $\sqrt5$ irrational; $0.\overline{7} = 7/9 \in \mathbb{Q}$; $\pi/2$ irrational.
3. $6x - 2 - x + 4$ (distributive) $= (6x - x) + (-2 + 4)$ (commutative and associative) $= 5x + 2$.
4. Multiply all parts by 3: $-6 \le 5 - x < 12$. Subtract 5: $-11 \le -x < 7$. Multiply by $-1$ and flip **both** signs: $11 \ge x > -7$. Answer: $(-7, 11]$.
5. $\left(\frac{8x^6y^3}{27}\right)^{2/3} = \frac{8^{2/3}x^{4}y^{2}}{27^{2/3}} = \frac{4x^4y^2}{9}$.
6. $\left|-\tfrac32 - \tfrac74\right| = \left|-\tfrac{13}{4}\right| = \tfrac{13}{4}$.
7. $V(t) = 450(1.08)^t$; $(1+r)^9 = 2 \Rightarrow r = \sqrt[9]{2} - 1 \approx 0.08$, about 8%.
8. $x^3 - 6x^2 + 12x - 8$; $9x^2 - 25$.
9. $(x^2 + 4)(x - 2)(x + 2)$; $(2x + 1)(3x - 2)$; $(x + 3)(x^2 - 3x + 9)$.
10. $\frac{(x-2)(x-3)}{(x-3)(x+3)}\cdot\frac{x+3}{x-2} = 1$, for $x \ne 3, -3, 2$.
11. Multiply by $x(x+1)$: $3(x + 1) + 2x = x^2 + x \Rightarrow x^2 - 4x - 3 = 0 \Rightarrow x = 2 \pm \sqrt7$ (neither root is 0 or $-1$, so both are valid).
12. Square both sides: $x + 7 = x^2 + 2x + 1 \Rightarrow x^2 + x - 6 = 0 \Rightarrow x = 2$ or $x = -3$. Check: $x = 2$: $3 = 3$ ✔️; $x = -3$: $\sqrt4 = 2 \ne -2$ ✘. Solution: $x = 2$.
"""))

    # end matter
    md(r"""
    ## ⚠️ Common mistakes
    - Solving $x^2 < 9$ as $x < \pm 3$. ✅ Correct: $-3 < x < 3$.
    - Reading the sign-chart regions backwards (using $>$ where the problem asks for $<$).
    - Writing $|X| > k$ as one compound inequality $-k > X > k$, which is impossible. It is an **"or"**: $X < -k$ **or** $X > k$.
    - Arithmetic slips in elimination: multiply **every** term of the equation.
    - Concluding "no solution" when the system is actually **dependent** (infinitely many solutions).
    - Calling `np.linalg.solve` on a singular matrix ($\det = 0$) gives an error. Check the determinant or use `sp.solve`.
    """)
    md("## ✅ Check your understanding\n\n" + "\n\n".join([
        r"**Q1.** Solve $x^2 - 16 \ge 0$." + "\n\n" + details("Answer", r"$(-\infty, -4] \cup [4, \infty)$."),
        r"**Q2 (True/False).** $|x - 5| < 2 \iff 3 < x < 7$." + "\n\n" + details("Answer", "**True.**"),
        r"**Q3 (MCQ).** $2x - y = 3$ and $4x - 2y = 6$ is (a) one solution (b) inconsistent (c) dependent" + "\n\n" + details("Answer", "**(c)**. The second equation is twice the first."),
        r"**Q4.** $\det\begin{pmatrix} 2 & 3 \\ 4 & 6 \end{pmatrix} =$ ___. What does it tell you?" + "\n\n" + details("Answer", r"$12 - 12 = 0$, so there is no unique solution."),
    ]))

    md("## 💻 Coding exercises (Part 8)")
    exercise("8.1", "⭐", "Quadratic inequality by hand",
             r"Solve $x^2 - x - 12 \le 0$ **by hand** (sign chart) and enter the answer as a SymPy interval in `ex8_1`.",
             "ex8_1 = None    # YOUR CODE HERE  (e.g. sp.Interval(..., ...))",
             "ex8_1 = sp.Interval(-3, 4)",
             'check(ex8_1, sp.solveset(x**2 - x - 12 <= 0, x, domain=sp.S.Reals), hint="(x − 4)(x + 3) ≤ 0 is negative between the roots; ≤ means the endpoints are included.")')
    exercise("8.2", "⭐", "Minimum hours for ₱4,000",
             r"Store the smallest number of weekly hours $h$ with $r_{med}\,h \ge 4000$ in `ex8_2`.",
             "ex8_2 = None    # YOUR CODE HERE",
             "ex8_2 = 4000 / r_med",
             'check(ex8_2, 4000 / paid["hourly_pay"].median(), hint="Divide both sides by r_med (positive, so the sign stays).")')
    exercise("8.3", "⭐⭐", "Within 8 hours of a 48-hour week",
             r"Store the share of employed persons with reported hours (`has_hours`) such that $|h - 48| \le 8$ in `ex8_3`.",
             "ex8_3 = None    # YOUR CODE HERE",
             'ex8_3 = (np.abs(has_hours["hours_week"] - 48) <= 8).mean()',
             'check(ex8_3, has_hours["hours_week"].between(40, 56).mean(), hint="|h − 48| ≤ 8 means 40 ≤ h ≤ 56. Use np.abs(...) <= 8, then .mean().")')
    exercise("8.4", "⭐⭐", "Recover the number of NCR paid workers",
             r"Let $x$ = NCR paid workers and $y$ = all other paid workers. Using $N$ = `len(paid)`, $T$ = total daily pay, and the two group **means**, set up and solve the 2×2 system with `sp.solve`. Store $x$ (a number) in `ex8_4`.",
             "ex8_4 = None    # YOUR CODE HERE",
             'is_ncr_p = paid["region"] == "NCR"\nd_N = paid[is_ncr_p]["daily_pay"].mean()\nd_R = paid[~is_ncr_p]["daily_pay"].mean()\nsol84 = sp.solve([sp.Eq(xs + ys, len(paid)), sp.Eq(d_N * xs + d_R * ys, paid["daily_pay"].sum())], [xs, ys])\nex8_4 = float(sol84[xs])',
             'check(ex8_4, (paid["region"] == "NCR").sum(), tol=1e-3, hint="Equations: x + y = N and d̄_NCR·x + d̄_other·y = T. Then read sol[xs].")')
    exercise("8.5", "⭐⭐⭐", "Is the college/other system uniquely solvable?",
             r"Build the 2×2 coefficient matrix of the Lesson 8.2 system, $\begin{pmatrix}1 & 1\\ \bar d_C & \bar d_O\end{pmatrix}$, and store its **determinant** in `ex8_5`. *(By hand: $\det = \bar d_O - \bar d_C$.)*",
             "ex8_5 = None    # YOUR CODE HERE",
             "ex8_5 = np.linalg.det(np.array([[1, 1], [d_C, d_O]]))",
             'check(ex8_5, d_O - d_C, hint="np.linalg.det(np.array([[1, 1], [d_C, d_O]])). By hand: ad − bc = 1·d_O − 1·d_C.")',
             explanation=r"The determinant is nonzero exactly when the two group averages differ, which is why the method in Lesson 8.2 worked.")

    md(r"""
    ## ✍️ Board-work practice 🗣️
    **B8.1** Solve by elimination, check, and interpret the intersection: $2x + 3y = 12$, $x - y = 1$.

    **B8.2** Solve $x^2 - 4x - 5 > 0$ with a sign chart, and write the answer in interval notation.

    **B8.3** Solve $|2x - 1| < 7$ and graph it on a number line.

    **B8.4** Classify, giving a reason: (i) $x + 2y = 4,\; 2x + 4y = 8$; (ii) $x + 2y = 4,\; 2x + 4y = 9$.
    """)
    md(details("Solutions to board-work practice", r"""
**B8.1** Multiply the 2nd equation by 3: $3x - 3y = 3$. Add it to the 1st: $5x = 15 \Rightarrow x = 3$, so $y = 2$. Check: $6 + 6 = 12$ ✔️, $3 - 2 = 1$ ✔️. The lines cross at $(3, 2)$.

**B8.2** $(x - 5)(x + 1) > 0$. Signs: $+$ on $(-\infty, -1)$, $-$ on $(-1, 5)$, $+$ on $(5, \infty)$. Answer: $(-\infty, -1) \cup (5, \infty)$.

**B8.3** $-7 < 2x - 1 < 7 \Rightarrow -6 < 2x < 8 \Rightarrow -3 < x < 4$: $(-3, 4)$, with open circles at both ends.

**B8.4** (i) **Dependent**: the 2nd equation is twice the 1st, so there are infinitely many solutions. (ii) **Inconsistent**: the same left side doubled gives 8, not 9. The lines are parallel, so there is no solution. In both cases $\det = 4 - 4 = 0$.
"""))
    md(RUBRIC)
    md(r"""
    ## 🔭 Why this matters for calculus
    - To find where a function is **increasing**, you solve the inequality $f'(x) > 0$ with a sign chart, exactly as in Lesson 8.1.
    - $|x - a| < \delta$ is the **$\delta$-neighbourhood** used in the definition of a limit.
    - Systems of equations appear when you set several partial derivatives to zero (multivariable optimization in later courses), and in **comparative statics** of market models (Chiang & Wainwright).

    ## 📝 Summary (Part 8 cheat-sheet)
    | Rule | Python |
    |---|---|
    | Sign chart: factor, mark the zeros, test each region | `sp.solveset(ineq, x, domain=sp.S.Reals)` |
    | $\lvert X\rvert < k \iff -k < X < k$; $\lvert X\rvert > k \iff X < -k$ or $X > k$ | `sp.Abs`, `np.abs(s) <= k` |
    | Shade a solution region | `ax.fill_between(x, y1, y2, where=...)` |
    | Substitution / elimination; intersection of lines | `sp.solve([eq1, eq2], [x, y])` |
    | $\det\begin{pmatrix}a&b\\c&d\end{pmatrix} = ad - bc$; $\ne 0$ ⇒ unique | `np.linalg.det(A)` |
    | Matrix form $A\mathbf{x} = \mathbf{b}$ | `np.linalg.solve(A, b)` |
    """)
