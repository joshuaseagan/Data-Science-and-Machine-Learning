from kit import md, code, details, exercise, concept_card, interpret, RUBRIC


def build():
    md(r"""
    ---
    # 🧱 Part 5 · Week 4: Algebraic Expressions, Operations on Polynomials, Special Products
    **Week 4 (with Week 3 practice) · CLO1, CLO2 · ⏱️ Est. time: 75 min**
    📚 *Readings:* Swokowski & Cole (2011), *Algebraic Expressions*; Rees, Sparks & Rees (2003), *Fundamental Operations on Algebraic Expressions* and *Special Products and Factoring*; economic framing: Dowling (2011), *Review* chapter.

    🎯 **Learning objectives.** By the end of Part 5 you can:
    1. **Identify** terms, coefficients, constants and the degree of a polynomial, and **evaluate** expressions.
    2. **Add, subtract and multiply** polynomials.
    3. **Expand** the special products $(a \pm b)^2$, $(a + b)(a - b)$ and $(a \pm b)^3$ quickly and correctly.
    4. **Fit, evaluate and plot** a polynomial age–pay profile from LFS data.

    🧭 **Big picture.** Economic models are written as algebraic expressions: weekly pay $= d \cdot n$, total cost $= F + cQ$, a quadratic profit function. Polynomials are the simplest flexible curves, so economists use them to describe how pay rises and then levels off with age. Expanding and simplifying is how we compare, combine and later differentiate such models.
    """)
    md(r"""
    ## 🔁 Warm-up: Week 3 practice (5 min)
    1. Simplify $(2a^3b^{-1})^2 \cdot a^{-4}$.
    2. Evaluate $32^{3/5}$.
    3. Find $d(-12, 7)$.
    """ + "\n" + details("Answers", r"1. $4a^6b^{-2}a^{-4} = 4a^2b^{-2} = \dfrac{4a^2}{b^2}$. 2. $(\sqrt[5]{32})^3 = 2^3 = 8$. 3. $|-12 - 7| = 19$."))

    # 5.1
    md("## Lesson 5.1 · Algebraic expressions: terms, coefficients, degree, evaluation ⏱️ 15 min")
    concept_card("algebraic expressions and polynomials",
        r"""An **algebraic expression** combines variables and constants with $+, -, \times, \div$, powers and roots.
A **polynomial** in $x$ is a sum of **terms** $a_k x^k$ with whole-number exponents $k$: $a_n x^n + \dots + a_1 x + a_0$.
- **Coefficient**: the number multiplying a power of $x$. The **constant term** is $a_0$.
- **Degree**: the highest power with a nonzero coefficient. **Leading coefficient**: $a_n$.
- *Not* polynomials: $\frac{1}{x}$, $\sqrt{x}$ (exponents $-1$ and $\tfrac12$).
**Evaluating** = substituting numbers for the variables.""",
        "Swokowski & Cole, *Algebraic Expressions* (polynomials); Rees, Sparks & Rees, *Fundamental Operations on Algebraic Expressions*.")
    md(r"""
    ### ✍️ Step 2 · Solve by Hand
    - $3x^2 - 5x + 7$ has terms $3x^2, -5x, 7$, degree 2, leading coefficient 3, and constant 7.
    - Weekly pay with an allowance: $W = d\,n + b$. For $d = 500$, $n = 6$, $b = 300$: $W = 500(6) + 300 = 3{,}300$.
    ### 🐍 Step 3 · Check with Python
    New Python idea: **SymPy symbols** are letters you can compute with, and `.subs({...})` substitutes numbers for them.
    """)
    code(r'''
    x = sp.symbols("x")
    d, n, b = sp.symbols("d n b")                  # daily pay, days worked, weekly allowance
    W = d * n + b
    print("W =", W, "→", W.subs({d: 500, n: 6, b: 300}))
    poly = 3 * x ** 2 - 5 * x + 7
    print("degree:", sp.degree(poly, x), "| coefficients:", sp.Poly(poly, x).all_coeffs())
    ''')
    md("### 📊 Step 4 · Apply to LFS Data\n**Question:** using the expression $W = dn + b$, what is the weekly pay of a worker earning the **sample median** daily pay, working 5 days, with no allowance?")
    code(r'''
    median_pay = paid["daily_pay"].median()
    W_median = W.subs({d: median_pay, n: 5, b: 0})
    print(f"Median daily pay ₱{median_pay:,.2f} → weekly pay W = ₱{float(W_median):,.2f}")
    # The same expression evaluated for EVERY paid worker (5 days, no allowance):
    paid["weekly_pay_5d"] = paid["daily_pay"] * 5
    print(paid["weekly_pay_5d"].describe().round(2))
    ''')
    interpret(r"Which symbols in $W = dn + b$ are *variables* chosen by the worker or employer, and which number did the data supply? What does the constant term $b$ represent economically?",
              r"$d$ (daily pay) came from the data (the median), and $n$ (days) and $b$ (allowance) were assumptions. The constant term $b$ is paid **regardless** of days worked, a fixed component, like a fixed cost in a cost function $C = F + cQ$.")

    # 5.2
    md("## Lesson 5.2 · Adding, subtracting and multiplying polynomials ⏱️ 20 min")
    concept_card("polynomial operations",
        r"""- **Add/subtract**: combine **like terms** (same power): $(a x^2 + bx) + (c x^2 + dx) = (a + c)x^2 + (b + d)x$.
- **Multiply**: use the **distributive property** so every term multiplies every term, then combine like terms. For binomials this is FOIL (First, Outer, Inner, Last).
- The degree of a product is the **sum** of the degrees.""",
        "Swokowski & Cole, *Algebraic Expressions* (operations on polynomials); Rees, Sparks & Rees, *Fundamental Operations*.")
    md(r"""
    ### ✍️ Step 2 · Solve by Hand
    Let $P = 3x^2 + 2x - 1$ and $Q = x^2 - 5x + 4$.
    - $P + Q = (3+1)x^2 + (2-5)x + (-1+4) = 4x^2 - 3x + 3$.
    - $P - Q = (3-1)x^2 + (2+5)x + (-1-4) = 2x^2 + 7x - 5$. ⚠️ Distribute the minus sign to **every** term of $Q$.
    - $(x + 2)(x - 3) = x^2 - 3x + 2x - 6 = x^2 - x - 6$ (distributive, then like terms).
    ### 🐍 Step 3 · Check with Python
    """)
    code(r'''
    P = 3 * x ** 2 + 2 * x - 1
    Q = x ** 2 - 5 * x + 4
    print("P + Q =", sp.expand(P + Q))
    print("P − Q =", sp.expand(P - Q))
    print("(x+2)(x−3) =", sp.expand((x + 2) * (x - 3)))
    print("P·Q =", sp.expand(P * Q), "| degree", sp.degree(sp.expand(P * Q), x))
    ''')
    md(r"""
    ### 📊 Step 4 · Apply to LFS Data
    We fit **separate** quadratic age–pay profiles for men and women, $p_M(a)$ and $p_F(a)$. Then:
    - **Subtracting** polynomials gives the predicted **gender pay gap** at each age: $g(a) = p_M(a) - p_F(a)$.
    - **Multiplying by a constant** gives weekly profiles: $5\,p(a)$.

    New Python idea: `sp.lambdify(a, expr)` turns a SymPy expression into a normal Python function that works on whole arrays, which is handy for plotting.
    """)
    code(r'''
    a = sp.symbols("a")                                   # age

    def fit_profile(data):
        """Fit pay = c0 + c1·a + c2·a² to a table with 'age' and 'daily_pay'; return a SymPy expression."""
        c2, c1, c0 = np.polyfit(data["age"], data["daily_pay"], 2)
        return c0 + c1 * a + c2 * a ** 2

    p_all = fit_profile(paid)
    p_M = fit_profile(paid[paid["sex"] == "Male"])
    p_F = fit_profile(paid[paid["sex"] == "Female"])
    print("p_M(a) =", sp.N(p_M, 5)); print("p_F(a) =", sp.N(p_F, 5))
    ''')
    code(r'''
    gap = sp.expand(p_M - p_F)                            # subtracting polynomials: like terms combine
    weekly_profile = sp.expand(5 * p_all)                 # scalar multiple
    print("Gap g(a) = p_M − p_F =", sp.N(gap, 5))
    print("Weekly profile 5·p(a) =", sp.N(weekly_profile, 5))
    for age_value in [25, 40, 55]:
        print(f"Age {age_value}: predicted gap ₱{float(gap.subs(a, age_value)):,.2f} per day")
    ''')
    code(r'''
    p_M_f, p_F_f = sp.lambdify(a, p_M), sp.lambdify(a, p_F)     # SymPy → ordinary functions
    grid = np.linspace(15, 75, 200)
    fig, ax = plt.subplots()
    ax.scatter(paid["age"], paid["daily_pay"], s=6, alpha=0.15, color="grey", label="Workers (sample)")
    ax.plot(grid, p_M_f(grid), lw=3, color=OKABE_ITO[0], label="Men: p_M(a)")
    ax.plot(grid, p_F_f(grid), lw=3, ls="--", color=OKABE_ITO[3], label="Women: p_F(a)")
    ax.set_title("Fitted quadratic age–pay profiles by sex (LFS 2018 sample)")
    ax.set_xlabel("Age (years)"); ax.set_ylabel("Daily pay (₱)"); ax.set_ylim(0, paid["daily_pay"].quantile(0.95)); ax.legend()
    plt.show()
    ''')
    md(r"""
    *Alt text:* a grey cloud of worker dots, with a solid blue curve for men and a dashed orange curve for women. The y-axis is cut at the 95th percentile of pay so the curves are easy to see.
    **Takeaway:** the vertical distance between the two curves at any age is $g(a)$, the difference of two polynomials.
    """)
    interpret(r"Describe the predicted gap at ages 25, 40 and 55 (sign and size). Give one reason why a fitted curve is only a rough summary.",
              r"*In our sample, the predicted male–female gap is ₱__ at 25, ₱__ at 40 and ₱__ at 55* (a negative value means women's predicted pay is higher). A quadratic is a smooth summary: it ignores education, region and occupation, it can be pulled by a few very high earners, and it describes different people at different ages (a cross-section).")

    # 5.3
    md("## Lesson 5.3 · Special products ⏱️ 20 min")
    concept_card("special products",
        r"""| Name | Identity |
|---|---|
| Square of a sum | $(u + v)^2 = u^2 + 2uv + v^2$ |
| Square of a difference | $(u - v)^2 = u^2 - 2uv + v^2$ |
| Sum × difference | $(u + v)(u - v) = u^2 - v^2$ |
| Cube of a sum / difference | $(u \pm v)^3 = u^3 \pm 3u^2v + 3uv^2 \pm v^3$ |
*Intuition:* $(u+v)^2$ is the area of a square of side $u + v$: two squares **plus two rectangles** $uv$.
**Economics:** two years of growth at rate $g$ multiply by $(1 + g)^2 = 1 + 2g + g^2$. The $g^2$ term is "growth on growth".""",
        "Swokowski & Cole, *Algebraic Expressions* (product formulas); Rees, Sparks & Rees, *Special Products and Factoring*.")
    md(r"""
    ### ✍️ Step 2 · Solve by Hand
    - $(x + 5)^2 = x^2 + 10x + 25$
    - $(2x - 3)^2 = 4x^2 - 12x + 9$
    - $(x + 4)(x - 4) = x^2 - 16$
    - $(x + 1)^3 = x^3 + 3x^2 + 3x + 1$
    - Mental math: $52 \times 48 = (50 + 2)(50 - 2) = 2500 - 4 = 2496$.
    - Two years at $g = 5\%$: $(1.05)^2 = 1 + 2(0.05) + 0.05^2 = 1.1025$, so pay rises 10.25%, **not** 10%.
    ### 🐍 Step 3 · Check with Python
    """)
    code(r'''
    u, v, g = sp.symbols("u v g")
    print(sp.expand((x + 5) ** 2), "|", sp.expand((2 * x - 3) ** 2), "|", sp.expand((x + 4) * (x - 4)))
    print(sp.expand((x + 1) ** 3))
    print(sp.expand((u - v) ** 3))
    print(sp.expand((1 + g) ** 2), "→ at g = 0.05:", sp.expand((1 + g) ** 2).subs(g, 0.05))
    ''')
    md("### 📊 Step 4 · Apply to LFS Data\n**Question:** if the median daily pay grows 5% per year for 2 years, how much of the increase comes from the \"growth on growth\" term $g^2 m$? We also verify the identities numerically using real LFS medians.")
    code(r'''
    m = paid["daily_pay"].median()
    growth = 0.05
    two_year = m * (1 + growth) ** 2
    pieces = m + 2 * growth * m + growth ** 2 * m              # m(1 + 2g + g²), expanded
    print(f"m(1+g)² = ₱{two_year:,.2f};  m + 2gm + g²m = ₱{pieces:,.2f}")
    print(f"Growth-on-growth part g²m = ₱{growth ** 2 * m:,.2f}")
    ''')
    code(r'''
    u_val = paid[paid["sex"] == "Male"]["daily_pay"].median()      # u = men's median
    v_val = paid[paid["sex"] == "Female"]["daily_pay"].median()    # v = women's median
    print("(u+v)(u−v) =", (u_val + v_val) * (u_val - v_val), "| u² − v² =", u_val ** 2 - v_val ** 2)
    print("(u+v)²     =", (u_val + v_val) ** 2, "| u² + 2uv + v² =", u_val ** 2 + 2 * u_val * v_val + v_val ** 2)
    print("u² + v² (the WRONG expansion) =", u_val ** 2 + v_val ** 2)
    ''')
    interpret(r"Explain to a classmate, using the numbers you computed, why $(u + v)^2 \neq u^2 + v^2$.",
              r"The wrong expansion is missing the middle term $2uv$. With the medians, $2uv$ is large (it is the product printed above minus the wrong value), so leaving it out badly underestimates $(u+v)^2$. Geometrically, the square of side $u + v$ contains two $u \times v$ rectangles besides the two squares.")

    # end matter
    md(r"""
    ## ⚠️ Common mistakes
    - $(a + b)^2 \neq a^2 + b^2$ (missing $2ab$). Likewise $(a - b)^2 \neq a^2 - b^2$.
    - Subtracting a polynomial without distributing the minus sign: $x^2 - (3x - 2) = x^2 - 3x + 2$, not $x^2 - 3x - 2$.
    - Combining **unlike** terms: $3x^2 + 2x \neq 5x^3$.
    - Multiplying exponents when multiplying terms: $x^2 \cdot x^3 = x^5$, not $x^6$.
    - Calling $\frac{1}{x} + 2$ a polynomial. Negative exponents are not allowed.
    - In Python, writing `2x` instead of `2 * x`, or `x^2` instead of `x ** 2`.
    """)
    md("## ✅ Check your understanding\n\n" + "\n\n".join([
        r"**Q1.** What is the degree and the leading coefficient of $7 - 2x^3 + x$?" + "\n\n" + details("Answer", "Degree 3, leading coefficient $-2$."),
        r"**Q2 (Fill in).** $(3x - 2)^2 =$ ___" + "\n\n" + details("Answer", r"$9x^2 - 12x + 4$."),
        r"**Q3 (True/False).** $(x + 6)(x - 6) = x^2 - 36$." + "\n\n" + details("Answer", "**True** (sum × difference)."),
        r"**Q4 (MCQ).** Which is a polynomial? (a) $x^{-2} + 1$ (b) $\sqrt{x} + x$ (c) $4x^3 - x + \tfrac12$ (d) $\frac{2}{x}$" + "\n\n" + details("Answer", r"**(c)**. A fractional *coefficient* is fine, but fractional or negative *exponents* are not."),
        r"**Q5.** Pay grows 10% per year for 2 years. By what total percent does it grow?" + "\n\n" + details("Answer", r"$(1.1)^2 = 1.21$, so 21%."),
    ]))

    md("## 💻 Coding exercises (Part 5)")
    exercise("5.1", "⭐", "Evaluate an expression with LFS data",
             r"Using `W = d * n + b`, store the weekly pay for the **NCR median** daily pay, $n = 6$ days and $b = 200$, in `ex5_1` (a number).",
             "ex5_1 = None    # YOUR CODE HERE",
             'ncr_med = paid[paid["region"] == "NCR"]["daily_pay"].median()\nex5_1 = W.subs({d: ncr_med, n: 6, b: 200})',
             'check(ex5_1, paid[paid["region"] == "NCR"]["daily_pay"].median() * 6 + 200, hint="Compute the NCR median first, then W.subs({d: ..., n: 6, b: 200}).")')
    exercise("5.2", "⭐", "Expand by hand, then type it",
             r"Expand $(x - 7)(x + 7)$ **by hand** and type the result as a SymPy expression (e.g. `x**2 + 3`) in `ex5_2`.",
             "ex5_2 = None    # YOUR CODE HERE",
             "ex5_2 = x ** 2 - 49",
             'check(ex5_2, sp.expand((x - 7) * (x + 7)), hint="Sum × difference: u² − v².")')
    exercise("5.3", "⭐⭐", "Evaluate the fitted profile",
             r"Store the predicted daily pay at **age 40** from `p_all`, as a float, in `ex5_3`.",
             "ex5_3 = None    # YOUR CODE HERE",
             "ex5_3 = float(p_all.subs(a, 40))",
             'check(ex5_3, float(p_all.subs(a, 40)), hint="Use p_all.subs(a, 40) and wrap it in float(...).")')
    exercise("5.4", "⭐⭐", "Gap at 35",
             r"Store the predicted male–female daily pay gap $g(35) = p_M(35) - p_F(35)$ in `ex5_4`.",
             "ex5_4 = None    # YOUR CODE HERE",
             "ex5_4 = float((p_M - p_F).subs(a, 35))",
             'check(ex5_4, float(gap.subs(a, 35)), hint="Subtract the polynomials (or use gap), then substitute a = 35.")')
    exercise("5.5", "⭐⭐⭐", "Growth on growth in NCR",
             r"For the **NCR** median pay $m$ and $g = 0.06$, store the *growth-on-growth* amount $g^2 m$ (in pesos) in `ex5_5`. Then check that $m(1+g)^2 - m - 2gm$ gives the same number.",
             "ex5_5 = None    # YOUR CODE HERE",
             'm_ncr = paid[paid["region"] == "NCR"]["daily_pay"].median()\nex5_5 = 0.06 ** 2 * m_ncr',
             'check(ex5_5, 0.0036 * paid[paid["region"] == "NCR"]["daily_pay"].median(), hint="g² m = 0.06**2 * (NCR median).")')

    md(r"""
    ## ✍️ Board-work practice 🗣️
    **B5.1** Expand and simplify $(2x - 3y)^2 - (x + y)(x - y)$. Name each special product.

    **B5.2** Multiply $(x + 2)(x^2 - 2x + 4)$. What do you notice?

    **B5.3** A worker's weekly pay is $W(n) = 520n + 300$. Next year, daily pay rises by ₱40 and the allowance by ₱50. Write next year's $W$ as a polynomial in $n$, and find the **change** in weekly pay (a polynomial). Evaluate it at $n = 5$ and interpret.
    """)
    md(details("Solutions to board-work practice", r"""
**B5.1** $(2x-3y)^2 = 4x^2 - 12xy + 9y^2$ (square of a difference); $(x+y)(x-y) = x^2 - y^2$ (sum × difference). Difference: $4x^2 - 12xy + 9y^2 - x^2 + y^2 = 3x^2 - 12xy + 10y^2$.

**B5.2** $x^3 - 2x^2 + 4x + 2x^2 - 4x + 8 = x^3 + 8$. This is the **sum of cubes** pattern $(u+v)(u^2 - uv + v^2) = u^3 + v^3$, used for factoring in Part 6.

**B5.3** New $W(n) = 560n + 350$. Change $= (560n + 350) - (520n + 300) = 40n + 50$. At $n = 5$: ₱250. *Interpretation:* working 5 days, the worker earns ₱250 more per week: ₱200 from the higher daily pay plus ₱50 from the higher allowance.
"""))
    md(RUBRIC)
    md(r"""
    ## 🔭 Why this matters for calculus
    - Derivatives start with **expanding**: $\frac{(x+h)^2 - x^2}{h} = \frac{2xh + h^2}{h} = 2x + h$. That is a special product followed by cancelling a common factor, exactly the calculation in Part 1.
    - The binomial expansion $(x + h)^n = x^n + nx^{n-1}h + \dots$ is *why* the derivative of $x^n$ is $nx^{n-1}$.
    - Polynomials are the easiest functions to differentiate and are **continuous everywhere** (Week 12).

    ## 📝 Summary (Part 5 cheat-sheet)
    | Rule | Python |
    |---|---|
    | Terms, coefficients, degree | `sp.degree(p, x)`, `sp.Poly(p, x).all_coeffs()` |
    | Evaluate | `expr.subs({x: 3})`, `float(...)` |
    | Add/subtract: combine like terms; multiply: distribute | `sp.expand(P + Q)`, `sp.expand(P * Q)` |
    | $(u\pm v)^2 = u^2 \pm 2uv + v^2$; $(u+v)(u-v) = u^2 - v^2$; $(u\pm v)^3 = u^3 \pm 3u^2v + 3uv^2 \pm v^3$ | `sp.expand(...)` |
    | Fit a quadratic to data | `np.polyfit(x, y, 2)` |
    | SymPy → function for plotting | `sp.lambdify(a, expr)` |
    """)
