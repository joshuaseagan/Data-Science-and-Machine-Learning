from kit import md, code, details, exercise, concept_card, interpret, RUBRIC


def build():
    md(r"""
    ---
    # 🔧 Part 6 · Week 5: Factoring and Fractional (Rational) Expressions
    **Week 5 (with Week 4 practice) · CLO1, CLO3 · ⏱️ Est. time: 80 min**
    📚 *Readings:* Swokowski & Cole (2011), *Algebraic Expressions* (factoring) and *Fractional Expressions*; Rees, Sparks & Rees (2003), *Special Products and Factoring* and *Fractions*; Sydsaeter et al. (2022), *Algebra* (fractions).

    🎯 **Learning objectives.** By the end of Part 6 you can:
    1. **Factor** polynomials by GCF, grouping, difference of squares, trinomials, and sum/difference of cubes.
    2. **Simplify** rational expressions by cancelling common **factors**, and **state** the domain restrictions.
    3. **Add, subtract, multiply and divide** rational expressions.
    4. **Compute** labor-market rates (LFPR, unemployment rate, hourly pay) as fractions, while handling division by zero in data.

    🧭 **Big picture.** Almost every economic indicator is a **fraction**: unemployment rate = unemployed ÷ labor force, pay per hour = pay per day ÷ hours per day, average cost = total cost ÷ quantity. Fractions carry a built-in danger: **the denominator can't be zero**. In data, that becomes "what do we do with zero hours?". Factoring is the tool that simplifies fractions, and in calculus it rescues limits of the form $0/0$.
    """)
    md(r"""
    ## 🔁 Warm-up: Week 4 practice (5 min)
    1. Expand $(x - 4)^2$.
    2. Multiply $(2x + 1)(x - 3)$.
    3. Subtract $(5x^2 - x + 2) - (2x^2 + 3x - 4)$.
    """ + "\n" + details("Answers", r"1. $x^2 - 8x + 16$. 2. $2x^2 - 5x - 3$. 3. $3x^2 - 4x + 6$."))

    # 6.1
    md("## Lesson 6.1 · Factoring polynomials ⏱️ 25 min")
    concept_card("factoring",
        r"""**Factoring** rewrites a sum as a **product**. It is expanding in reverse. Try the methods in this order:
1. **Greatest common factor (GCF):** $6x^2 + 9x = 3x(2x + 3)$.
2. **Special patterns:** difference of squares $u^2 - v^2 = (u - v)(u + v)$; perfect squares $u^2 \pm 2uv + v^2 = (u \pm v)^2$; sum/difference of cubes $u^3 \pm v^3 = (u \pm v)(u^2 \mp uv + v^2)$.
3. **Trinomials** $x^2 + bx + c$: find two numbers whose product is $c$ and whose sum is $b$.
4. **Grouping** (four terms): factor pairs, then factor out the common binomial.
*Always check by expanding.* Note: $u^2 + v^2$ does **not** factor over the reals.""",
        "Swokowski & Cole, *Algebraic Expressions* (factoring formulas); Rees, Sparks & Rees, *Special Products and Factoring*; Dowling, *Review*.")
    md(r"""
    ### ✍️ Step 2 · Solve by Hand
    - GCF: $6x^2 + 9x = 3x(2x + 3)$.
    - Trinomial: $x^2 - 5x + 6$: we need numbers with product $6$ and sum $-5$, which are $-2$ and $-3$. So $(x - 2)(x - 3)$.
    - Difference of squares: $x^2 - 49 = (x - 7)(x + 7)$.
    - Difference of cubes: $x^3 - 8 = (x - 2)(x^2 + 2x + 4)$.
    - Grouping: $xy + 2x + 3y + 6 = x(y + 2) + 3(y + 2) = (x + 3)(y + 2)$.
    ### 🐍 Step 3 · Check with Python
    New Python idea: `sp.factor(...)`, the reverse of `sp.expand`.
    """)
    code(r'''
    x, y = sp.symbols("x y")
    for expr in [6 * x**2 + 9 * x, x**2 - 5 * x + 6, x**2 - 49, x**3 - 8, x * y + 2 * x + 3 * y + 6]:
        print(f"{str(expr):<22} =  {sp.factor(expr)}")
    print("x² + 4 over the reals:", sp.factor(x**2 + 4), "(doesn't factor)")
    ''')
    md(r"""
    ### 📊 Step 4 · Apply to LFS Data
    **Question:** if every paid worker works $n$ days, the total wage bill is $n d_1 + n d_2 + \dots + n d_k$. Factoring out the GCF $n$ gives $n(d_1 + \dots + d_k)$. That is much faster: one multiplication instead of $k$. Let's verify with $n = 22$ working days per month.
    """)
    code(r'''
    n_days = 22
    bill_unfactored = (n_days * paid["daily_pay"]).sum()       # n·d1 + n·d2 + ... (k multiplications)
    bill_factored = n_days * paid["daily_pay"].sum()           # n(d1 + d2 + ...) (1 multiplication)
    print(f"Unfactored: ₱{bill_unfactored:,.2f}  | Factored: ₱{bill_factored:,.2f}")
    print("Equal?", np.isclose(bill_unfactored, bill_factored))
    d1, d2, d3, nn = sp.symbols("d1 d2 d3 n")
    print("SymPy:", sp.factor(nn * d1 + nn * d2 + nn * d3))
    ''')
    interpret(r"In one sentence, explain the economic meaning of the factored form $n(d_1 + \dots + d_k)$.",
              r"The total monthly wage bill equals the number of working days times the **total daily wage bill**. You can compute what all workers earn in one day, then scale it by the number of days.")

    # 6.2
    md("## Lesson 6.2 · Rational expressions and domain restrictions ⏱️ 25 min")
    concept_card("rational expressions",
        r"""A **rational (fractional) expression** is a quotient $\dfrac{P}{Q}$ of polynomials. It is defined only where $Q \neq 0$: that set of $x$ values is its **domain**.
**Simplify** by factoring top and bottom, then cancelling common **factors** (never terms!):
$$\frac{ac}{bc} = \frac{a}{b} \quad (b \ne 0,\; c \ne 0).$$
⚠️ The restrictions of the **original** expression still apply after cancelling.""",
        "Swokowski & Cole, *Fractional Expressions*; Rees, Sparks & Rees, *Fractions*; Sydsaeter et al., *Algebra* (fractions).")
    md(r"""
    ### ✍️ Step 2 · Solve by Hand
    $$\frac{x^2 - 9}{x^2 + x - 6} = \frac{(x - 3)(x + 3)}{(x + 3)(x - 2)} = \frac{x - 3}{x - 2}, \qquad x \neq -3,\; x \neq 2.$$
    *Why keep $x \ne -3$?* The original expression is undefined at $x = -3$ (it gives $0/0$), even though the simplified one isn't.
    ### 🐍 Step 3 · Check with Python
    """)
    code(r'''
    expr = (x**2 - 9) / (x**2 + x - 6)
    print("Simplified:", sp.cancel(expr))
    print("Excluded x (denominator = 0):", sp.solve(sp.denom(expr), x))   # SymPy forgets these when it cancels!
    print("Original at x = -3:", expr.subs(x, -3))                        # nan: 0/0 is undefined
    ''')
    md(r"""
    ### 📊 Step 4 · Apply to LFS Data: division by zero in real data
    **Question:** what is each worker's **hourly pay**, $\dfrac{\text{daily pay}}{\text{normal hours per day}}$? The domain restriction "denominator $\neq 0$" becomes a data rule: **hours of 0 or missing → no hourly pay**. pandas doesn't stop you from dividing by zero. It quietly returns `inf` (∞):
    """)
    code(r'''
    demo_pay = pd.Series([500.0, 400.0, 600.0])
    demo_hours = pd.Series([8.0, 0.0, np.nan])
    print(demo_pay / demo_hours)                                   # 62.5, inf, NaN: inf is dangerous!
    safe_hours = demo_hours.where(demo_hours > 0)                   # keep hours > 0; anything else → NaN
    print(demo_pay / safe_hours)                                   # 62.5, NaN, NaN: safe
    ''')
    md("New Python idea: `s.where(condition)` keeps values where the condition is True and puts `NaN` elsewhere, which is our way to enforce a domain restriction.")
    code(r'''
    safe = df["normal_hrs_day"].where(df["normal_hrs_day"] > 0)             # domain: hours > 0
    df["hourly_pay"] = df["daily_pay"] / safe
    paid = df.dropna(subset=["daily_pay"]).copy()                           # refresh paid so it has hourly_pay
    print("Paid workers without a valid hourly pay:", paid["hourly_pay"].isna().sum())
    print(f"Median hourly pay in our sample: ₱{paid['hourly_pay'].median():,.2f}")
    print("Any infinite values?", np.isinf(paid["hourly_pay"]).any())
    ''')
    interpret(r"Why is it better to turn zero hours into `NaN` than to let pandas produce `inf`? What would happen to the *mean* hourly pay if one `inf` slipped in?",
              r"$\frac{d}{0}$ is undefined, so no real hourly pay exists for that row, and `NaN` says exactly that: \"no value\". A single `inf` makes the **mean infinite**, which ruins every average and chart. `NaN` values are simply skipped.")

    # 6.3
    md("## Lesson 6.3 · Operations on rational expressions and labor-market rates ⏱️ 20 min")
    concept_card("operations on fractions",
        r"""For nonzero denominators:
$$\frac{a}{b} \pm \frac{c}{d} = \frac{ad \pm bc}{bd}, \qquad \frac{a}{b}\cdot\frac{c}{d} = \frac{ac}{bd}, \qquad \frac{a}{b} \div \frac{c}{d} = \frac{a}{b}\cdot\frac{d}{c} \;\;(c \neq 0).$$
Use the **least common denominator (LCD)** to keep things small.
**Labor-market rates** (with $E$ = employed, $U$ = unemployed, $P$ = population 15+, and labor force $LF = E + U$):
$$\text{LFPR} = \frac{E + U}{P}, \qquad \text{UR} = \frac{U}{E + U}, \qquad \text{EPR} = \frac{E}{P}.$$""",
        "Swokowski & Cole, *Fractional Expressions* (operations; complex fractions); Rees, Sparks & Rees, *Fractions*.")
    md(r"""
    ### ✍️ Step 2 · Solve by Hand
    **(a)** $\dfrac{1}{x} + \dfrac{1}{x + 1} = \dfrac{(x + 1) + x}{x(x + 1)} = \dfrac{2x + 1}{x(x + 1)}$, with $x \neq 0, -1$.

    **(b) An identity linking the three rates.** Divide EPR by LFPR, which is a complex fraction:
    $$\frac{\text{EPR}}{\text{LFPR}} = \frac{E/P}{(E + U)/P} = \frac{E}{P}\cdot\frac{P}{E + U} = \frac{E}{E + U}.$$
    So
    $$1 - \frac{\text{EPR}}{\text{LFPR}} = \frac{E + U}{E + U} - \frac{E}{E + U} = \frac{U}{E + U} = \text{UR}.$$
    ### 🐍 Step 3 · Check with Python
    """)
    code(r'''
    print(sp.together(1 / x + 1 / (x + 1)))                 # combine into one fraction
    print(sp.apart((2 * x + 1) / (x * (x + 1))))            # split back into partial fractions
    E_, U_, P_ = sp.symbols("E U P", positive=True)
    identity = (1 - (E_ / P_) / ((E_ + U_) / P_)) - U_ / (E_ + U_)
    print("Identity check (should be 0):", sp.simplify(identity))
    ''')
    md(r"""
    ### 📊 Step 4 · Apply to LFS Data
    New Python idea: `pd.crosstab(rows, columns)` counts persons in every row–column combination. Then the rates are just **column arithmetic with fractions**.
    > ⚠️ These are **unweighted teaching estimates from our sample**, not official PSA rates.
    """)
    code(r'''
    E_count = (df["empstat"] == "Employed").sum()
    U_count = (df["empstat"] == "Unemployed").sum()
    P_count = len(df)
    LFPR, UR, EPR = (E_count + U_count) / P_count, U_count / (E_count + U_count), E_count / P_count
    print(f"LFPR = {LFPR:.1%}, UR = {UR:.1%}, EPR = {EPR:.1%}  (teaching estimates)")
    print("Identity UR = 1 − EPR/LFPR holds?", np.isclose(UR, 1 - EPR / LFPR))
    ''')
    code(r'''
    by_sex = pd.crosstab(df["sex"], df["empstat"])               # counts: rows = sex, columns = status
    by_sex["LF"] = by_sex["Employed"] + by_sex["Unemployed"]
    by_sex["LFPR"] = by_sex["LF"] / (by_sex["LF"] + by_sex["Not in labor force"])
    by_sex["UR"] = by_sex["Unemployed"] / by_sex["LF"]
    by_sex[["LFPR", "UR"]].round(3)
    ''')
    code(r'''
    by_region = pd.crosstab(df["region"], df["empstat"])
    by_region["UR"] = by_region["Unemployed"] / (by_region["Employed"] + by_region["Unemployed"])
    ur_sorted = by_region["UR"].sort_values()
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.barh(ur_sorted.index, ur_sorted.values * 100, color=OKABE_ITO[1])
    ax.set_title("Unemployment rate by region (unweighted teaching estimate, LFS 2018 sample)")
    ax.set_xlabel("Unemployment rate (% of labor force)"); ax.set_ylabel("Region"); plt.show()
    ''')
    md(r"""
    *Alt text:* horizontal bars of the unemployment rate for each region, sorted from lowest to highest.
    **Takeaway:** regional rates differ, but each is based on a **small number** of unemployed persons in our sample, so treat small differences with caution.
    """)
    interpret(r"Compare the LFPR of men and women in our sample. Using the definitions, explain why a group can have a *low* LFPR but a *low* UR at the same time.",
              r"*In our sample, the LFPR is __% for men and __% for women.* LFPR measures who is **in** the labor force (working or looking). UR is computed **only among** those in the labor force. Many people outside the labor force (for example, homemakers or students) lower the LFPR but don't count as unemployed, so the UR can still be low.")

    # end matter
    md(r"""
    ## ⚠️ Common mistakes
    - **Cancelling terms instead of factors:** $\dfrac{x + 3}{x + 5} \neq \dfrac{3}{5}$. You may only cancel a factor that multiplies the **whole** numerator and the **whole** denominator.
    - Forgetting the domain restrictions after simplifying. $\frac{x^2-9}{x+3} = x - 3$ only for $x \neq -3$.
    - Adding fractions by adding tops and bottoms: $\frac{1}{2} + \frac{1}{3} \neq \frac{2}{5}$.
    - Dividing fractions without inverting the **second** fraction.
    - Trying to factor $x^2 + 9$ over the reals.
    - Mixing up the denominators of the rates: UR uses the **labor force**, LFPR uses the **population 15+**.
    - Letting `inf` into your data by dividing by zero hours.
    """)
    md("## ✅ Check your understanding\n\n" + "\n\n".join([
        r"**Q1.** Factor $x^2 + 7x + 12$." + "\n\n" + details("Answer", r"$(x + 3)(x + 4)$, since $3 \cdot 4 = 12$ and $3 + 4 = 7$."),
        r"**Q2 (True/False).** $\dfrac{2x + 6}{2} = x + 6$." + "\n\n" + details("Answer", r"**False.** $\frac{2(x + 3)}{2} = x + 3$. The 2 must divide **every** term."),
        r"**Q3 (Fill in).** The domain of $\dfrac{x + 1}{x^2 - 4}$ excludes $x =$ ___." + "\n\n" + details("Answer", r"$x = 2$ and $x = -2$."),
        r"**Q4 (MCQ).** UR equals (a) $U/P$ (b) $U/(E + U)$ (c) $(E+U)/P$ (d) $E/(E+U)$" + "\n\n" + details("Answer", "**(b)**"),
        r"**Q5.** Factor $8x^3 + 27$." + "\n\n" + details("Answer", r"$(2x + 3)(4x^2 - 6x + 9)$ (sum of cubes with $u = 2x$, $v = 3$)."),
    ]))

    md("## 💻 Coding exercises (Part 6)")
    exercise("6.1", "⭐", "Factor by hand, type the factors",
             r"Factor $x^2 - 11x + 28$ **by hand**. Type your answer in **factored form**, e.g. `(x - 1)*(x - 2)`, and store it in `ex6_1`.",
             "ex6_1 = None    # YOUR CODE HERE",
             "ex6_1 = (x - 4) * (x - 7)",
             'check(ex6_1, sp.factor(x**2 - 11 * x + 28), exact=True, hint="Find two numbers with product 28 and sum −11. Type it as a product, not expanded.")')
    exercise("6.2", "⭐", "Overall unemployment rate",
             r"Store the unemployment rate $U/(E + U)$ for the whole sample (a proportion) in `ex6_2`. Compute it from `df` yourself.",
             "ex6_2 = None    # YOUR CODE HERE",
             'unemployed = (df["empstat"] == "Unemployed").sum()\nemployed = (df["empstat"] == "Employed").sum()\nex6_2 = unemployed / (employed + unemployed)',
             'check(ex6_2, U_count / (E_count + U_count), hint="The denominator is the LABOR FORCE (employed + unemployed), not all persons.")')
    exercise("6.3", "⭐⭐", "Women's LFPR",
             r"Store the labor-force participation rate of **women**, $(E_F + U_F)/P_F$, in `ex6_3`.",
             "ex6_3 = None    # YOUR CODE HERE",
             'women = df[df["sex"] == "Female"]\nex6_3 = (women["empstat"] != "Not in labor force").mean()',
             'check(ex6_3, by_sex.loc["Female", "LFPR"], hint="Among women only: (employed + unemployed) ÷ all women. Tip: (status != \\"Not in labor force\\").mean().")')
    exercise("6.4", "⭐⭐", "Safe division: hourly pay of government workers",
             r"Store the **median hourly pay** of paid workers whose `worker_class` is `\"Government\"` in `ex6_4`. Make sure that hours of 0 or `NaN` are excluded (use the `hourly_pay` column or `.where`).",
             "ex6_4 = None    # YOUR CODE HERE",
             'gov = paid[paid["worker_class"] == "Government"]\nex6_4 = gov["hourly_pay"].median()',
             'gv = df[df["worker_class"] == "Government"]\ncheck(ex6_4, (gv["daily_pay"] / gv["normal_hrs_day"].where(gv["normal_hrs_day"] > 0)).median(), hint="Filter worker_class == \\"Government\\", then take the median of hourly_pay.")')
    exercise("6.5", "⭐⭐⭐", "Region with the highest unemployment rate",
             r"Using a `crosstab` of region by status, store the **name** of the region with the highest unemployment rate (a string) in `ex6_5`. *Hint:* `series.idxmax()` returns the label of the largest value.",
             "ex6_5 = None    # YOUR CODE HERE",
             'tab = pd.crosstab(df["region"], df["empstat"])\nur = tab["Unemployed"] / (tab["Employed"] + tab["Unemployed"])\nex6_5 = ur.idxmax()',
             'check(ex6_5, by_region["UR"].idxmax(), hint="Build UR = Unemployed / (Employed + Unemployed) per region, then .idxmax().")')

    md(r"""
    ## ✍️ Board-work practice 🗣️
    **B6.1** Factor completely: $2x^3 - 8x$. Name every method used.

    **B6.2** Simplify and state all restrictions: $\dfrac{x^2 - 4}{x^2 + 5x + 6} \div \dfrac{x - 2}{x + 3}$.

    **B6.3** Starting from the definitions $\text{EPR} = E/P$ and $\text{LFPR} = (E+U)/P$, show that $\text{UR} = \dfrac{\text{LFPR} - \text{EPR}}{\text{LFPR}}$. Then interpret: if LFPR = 0.60 and EPR = 0.57, what is UR?
    """)
    md(details("Solutions to board-work practice", r"""
**B6.1** $2x^3 - 8x = 2x(x^2 - 4)$ (GCF) $= 2x(x - 2)(x + 2)$ (difference of squares).

**B6.2** $\dfrac{(x-2)(x+2)}{(x+2)(x+3)} \cdot \dfrac{x+3}{x-2} = 1$ (invert the divisor, factor, cancel common factors). Restrictions: $x \neq -2, -3$ (original denominators) and $x \neq 2$ (we divided by $\frac{x-2}{x+3}$, which must be nonzero). So the expression equals 1 for $x \ne -3, -2, 2$.

**B6.3** $\dfrac{\text{LFPR} - \text{EPR}}{\text{LFPR}} = \dfrac{\frac{E+U}{P} - \frac{E}{P}}{\frac{E+U}{P}} = \dfrac{U/P}{(E+U)/P} = \dfrac{U}{P}\cdot\dfrac{P}{E+U} = \dfrac{U}{E+U} = \text{UR}$. With the numbers: $(0.60 - 0.57)/0.60 = 0.05$, so 5% of the labor force is unemployed.
"""))
    md(RUBRIC)
    md(r"""
    ## 🔭 Why this matters for calculus
    - **Limits of the form $0/0$** are resolved by factoring and cancelling: $\lim_{x\to 3}\frac{x^2 - 9}{x - 3} = \lim_{x\to3}(x + 3) = 6$. This is the most common limit technique in Weeks 11–13.
    - Domain restrictions (denominator $\neq 0$) are exactly where rational functions are **discontinuous** (Week 12).
    - Average cost $C(Q)/Q$ and other per-unit quantities are rational functions whose behavior you will analyze.

    ## 📝 Summary (Part 6 cheat-sheet)
    | Rule | Python |
    |---|---|
    | GCF, $u^2 - v^2$, $u^3 \pm v^3$, trinomials, grouping | `sp.factor(expr)` |
    | $\frac{ac}{bc} = \frac{a}{b}$ (cancel **factors**), keep restrictions | `sp.cancel(expr)`, `sp.solve(sp.denom(expr), x)` |
    | $\frac{a}{b} + \frac{c}{d} = \frac{ad + bc}{bd}$; $\div$ = multiply by the reciprocal | `sp.together`, `sp.apart` |
    | Safe division in data (domain!) | `s.where(s > 0)` |
    | LFPR, UR, EPR | `pd.crosstab(df["sex"], df["empstat"])` + column arithmetic |
    """)
