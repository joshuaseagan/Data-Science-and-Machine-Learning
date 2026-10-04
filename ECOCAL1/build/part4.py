from kit import md, code, details, exercise, concept_card, interpret, RUBRIC


def build():
    md(r"""
    ---
    # 🚀 Part 4 · Week 3: Exponents, Radicals, Rational Exponents, Absolute Value and Distance
    **Week 3 (with Week 2 practice) · CLO1, CLO2 · ⏱️ Est. time: 75 min**
    📚 *Readings:* Swokowski & Cole (2011), *Exponents and Radicals* and *Real Numbers* (absolute value, distance); Rees, Sparks & Rees (2003), *Exponents and Radicals*; Sydsaeter et al. (2022), *Algebra* (powers, compound interest, absolute value).

    🎯 **Learning objectives.** By the end of Part 4 you can:
    1. **Simplify** expressions with integer, zero and negative exponents, naming the law used.
    2. **Convert** between radicals and rational exponents, respecting domain restrictions.
    3. **Apply** compound growth $P(1 + r)^t$ and convert annual rates to monthly ones.
    4. **Compute** absolute values and distances on the number line, including a spread measure for pay.

    🧭 **Big picture.** Wages, prices and GDP **grow by percentages**, so they compound like interest. Exponents describe that compounding, and rational exponents (roots) undo it: *"what yearly growth rate turns ₱500 into ₱700 in 5 years?"* Absolute value measures **gaps**: how far NCR pay is from pay elsewhere, or how spread out wages are.
    """)
    md(r"""
    ## 🔁 Warm-up: Week 2 practice (5 min)
    1. Solve $5 - 2x \ge 11$ and write the answer as an interval.
    2. Write $\{x : x > -1\} \cap \{x : x \le 4\}$ as an interval.
    """ + "\n" + details("Answers", r"1. $-2x \ge 6 \Rightarrow x \le -3$, so $(-\infty, -3]$ (sign flipped). 2. $(-1, 4]$."))

    # 4.1
    md("## Lesson 4.1 · Laws of exponents and compound growth ⏱️ 20 min")
    concept_card("laws of exponents",
        r"""For real $a, b$ and integers $m, n$ (with $a, b \neq 0$ wherever we divide or use exponents $\le 0$):
| Law | Statement |
|---|---|
| Product | $a^m a^n = a^{m+n}$ |
| Quotient | $a^m / a^n = a^{m-n}$ |
| Power of a power | $(a^m)^n = a^{mn}$ |
| Power of a product / quotient | $(ab)^n = a^n b^n$, $(a/b)^n = a^n / b^n$ |
| Zero exponent | $a^0 = 1$ ($a \neq 0$) |
| Negative exponent | $a^{-n} = 1/a^n$ ($a \neq 0$) |
**Compound growth:** a value $P$ growing at rate $r$ per period for $t$ periods becomes $P(1 + r)^t$.""",
        "Swokowski & Cole, *Exponents and Radicals*; Sydsaeter et al., *Algebra* (powers; compound interest).")
    md(r"""
    ### ✍️ Step 2 · Solve by Hand
    - $\dfrac{2^3 \cdot 2^4}{2^5} = \dfrac{2^{7}}{2^5}$ (product law) $= 2^{2}$ (quotient law) $= 4$.
    - $(3x^2)^3 = 3^3 (x^2)^3$ (power of a product) $= 27x^6$ (power of a power).
    - $5^{-2} = \dfrac{1}{5^2} = \dfrac{1}{25}$ (negative exponent).
    - **Growth:** ₱500 growing 5% per year for 2 years gives $500(1.05)^2 = 500(1.1025) = 551.25$.
    ### 🐍 Step 3 · Check with Python
    """)
    code(r'''
    print((2 ** 3 * 2 ** 4) / 2 ** 5)          # 4.0
    print(5 ** -2, "=", 1 / 25)                 # negative exponent
    x = sp.symbols("x", positive=True)
    print(sp.expand((3 * x ** 2) ** 3))          # 27*x**6
    print(500 * 1.05 ** 2)                       # 551.25
    ''')
    md(r"""
    ### 📊 Step 4 · Apply to LFS Data
    **Question (hypothetical):** if the median daily pay in our sample grew 5% per year, what would it be after $t = 0, 1, \dots, 10$ years?
    New Python idea: `np.arange(0, 11)` makes the array `0, 1, …, 10`, and `**` then works on **every element at once**.
    """)
    code(r'''
    P = paid["daily_pay"].median()               # starting value: median daily pay in our sample
    r = 0.05                                     # hypothetical 5% growth per year
    t = np.arange(0, 11)                         # 0, 1, 2, ..., 10 years
    projected = P * (1 + r) ** t                 # compound growth, element by element
    for year, value in zip(t, projected):        # zip pairs up the two lists
        print(f"Year {year:2d}: ₱{value:,.2f}")
    ''')
    code(r'''
    fig, ax = plt.subplots()
    ax.plot(t, projected, "o-", lw=2, label="5% compound growth: P(1.05)^t")
    ax.plot(t, P + P * r * t, "s--", lw=2, label="Simple growth: P + P·r·t (for comparison)")
    ax.set_title("Hypothetical projection of the median daily pay (sample median as base)")
    ax.set_xlabel("Years from 2018 (t)"); ax.set_ylabel("Daily pay (₱)"); ax.legend(); plt.show()
    ''')
    md(r"""
    *Alt text:* two rising lines starting at the same point. The compound-growth curve bends upward and ends above the straight simple-growth line.
    **Takeaway:** compounding means growth on top of growth, so the gap between the two lines widens over time.
    """)
    interpret(r"By how many pesos does compound growth beat simple growth after 10 years? Explain *why* in terms of exponents.",
              r"The difference is `projected[10] - (P + P*r*10)`. Under compounding, each year's 5% is applied to a **larger base** (the previous year's value), because $(1+r)^{10}$ includes cross terms like $r^2$, $r^3$, …. Simple growth only ever adds 5% of the *original* $P$.")

    # 4.2
    md("## Lesson 4.2 · Radicals and rational exponents ⏱️ 20 min")
    concept_card("radicals and rational exponents",
        r"""$\sqrt[n]{a} = a^{1/n}$ and $a^{m/n} = \left(\sqrt[n]{a}\right)^m = \sqrt[n]{a^m}$.
**Domain:** for **even** $n$, $\sqrt[n]{a}$ is real only when $a \ge 0$. For odd $n$, any real $a$ is fine.
$\sqrt{ab} = \sqrt{a}\sqrt{b}$ for $a, b \ge 0$. **But** $\sqrt{a + b} \neq \sqrt{a} + \sqrt{b}$ in general!
**Rates:** an annual rate $r$ is equivalent to the monthly rate $(1 + r)^{1/12} - 1$. The constant yearly rate that takes $P$ to $Q$ in $t$ years is $r = (Q/P)^{1/t} - 1$.""",
        "Swokowski & Cole, *Exponents and Radicals* (rational exponents, simplifying radicals); Rees, Sparks & Rees, *Exponents and Radicals*; Sydsaeter et al., *Algebra*.")
    md(r"""
    ### ✍️ Step 2 · Solve by Hand
    - $8^{2/3} = (\sqrt[3]{8})^2 = 2^2 = 4$.
    - $16^{-3/4} = \dfrac{1}{(\sqrt[4]{16})^3} = \dfrac{1}{2^3} = \dfrac{1}{8}$.
    - $\sqrt{72} = \sqrt{36 \cdot 2} = 6\sqrt{2}$.
    - **Doubling in 10 years:** $(1 + r)^{10} = 2 \Rightarrow 1 + r = 2^{1/10} \Rightarrow r = 2^{1/10} - 1$ (about 7.2%).
    ### 🐍 Step 3 · Check with Python
    Floats give *approximate* answers. SymPy gives **exact** ones:
    """)
    code(r'''
    print(8 ** (2 / 3))                                      # 3.9999999999999996, a float approximation!
    print(sp.Integer(8) ** sp.Rational(2, 3))                # exactly 4
    print(sp.Integer(16) ** sp.Rational(-3, 4), "|", sp.sqrt(72))   # 1/8 | 6*sqrt(2)
    print("Doubling rate:", 2 ** (1 / 10) - 1)
    ''')
    md(r"""
    > ⚠️ **Python and negative bases.** `(-8) ** (1/3)` does **not** give $-2$. Python returns a complex number, because `1/3` is a float. In this course, take odd roots of negatives by hand: $\sqrt[3]{-8} = -2$. Use `np.cbrt(-8)` or `sp.real_root(-8, 3)` to check.

    ### 📊 Step 4 · Apply to LFS Data
    **Question:** what constant yearly growth rate would lift the **national** median daily pay in our sample to the **NCR** median in 10 years? And what monthly rate is equivalent to it?
    """)
    code(r'''
    national_median = paid["daily_pay"].median()
    ncr_median = paid[paid["region"] == "NCR"]["daily_pay"].median()
    r_needed = (ncr_median / national_median) ** (1 / 10) - 1          # r = (Q/P)^(1/t) − 1
    monthly = (1 + r_needed) ** (1 / 12) - 1                           # annual → monthly
    print(f"National median ₱{national_median:,.2f}, NCR median ₱{ncr_median:,.2f}")
    print(f"Required yearly growth: {r_needed:.3%}  | equivalent monthly rate: {monthly:.4%}")
    print("Check: national × (1 + r)^10 =", round(national_median * (1 + r_needed) ** 10, 2))
    ''')
    interpret(r"Interpret `r_needed` in one sentence. Why is the monthly rate *not* simply `r_needed / 12`?",
              r"*In our sample, pay outside NCR would need to grow about __% per year for 10 years to reach today's NCR median.* Monthly rates compound 12 times a year: $(1 + r_m)^{12} = 1 + r$, so $r_m = (1+r)^{1/12} - 1$, which is slightly **less** than $r/12$.")

    # 4.3
    md("## Lesson 4.3 · Absolute value and distance ⏱️ 20 min")
    concept_card("absolute value and distance",
        r"""$$|a| = \begin{cases} a & \text{if } a \ge 0 \\ -a & \text{if } a < 0 \end{cases}$$
$|a|$ is the distance from $a$ to 0, so it is never negative. The **distance** between $a$ and $b$ on the number line is $d(a, b) = |a - b| = |b - a|$.
Properties: $|ab| = |a||b|$, $|a/b| = |a|/|b|$ ($b \neq 0$), and the triangle inequality $|a + b| \le |a| + |b|$.
**Mean absolute deviation** from the median $m$: $\frac{1}{n}\sum |x_i - m|$, the average distance of the data from its center.""",
        "Swokowski & Cole, *Real Numbers* (absolute value; distance between points on a coordinate line); Sydsaeter et al., *Algebra* (absolute value).")
    md(r"""
    ### ✍️ Step 2 · Solve by Hand
    - $|-7| = 7$; $|3 - 10| = |-7| = 7$.
    - $d(-3, 5) = |-3 - 5| = |-8| = 8$, and also $|5 - (-3)| = 8$ (symmetric).
    - Two regions' median pays of ₱450 and ₱610 are $|450 - 610| = 160$ pesos apart.
    - The data $\{400, 500, 650\}$ have median $500$. MAD $= \frac{|400-500| + |500-500| + |650-500|}{3} = \frac{100 + 0 + 150}{3} = 83.\overline{3}$.
    ### 🐍 Step 3 · Check with Python
    New Python idea: `abs()` for one number, `np.abs()` for a whole array or column.
    """)
    code(r'''
    print(abs(-7), abs(3 - 10), abs(-3 - 5), abs(450 - 610))
    sample = np.array([400, 500, 650])
    print("MAD:", np.abs(sample - np.median(sample)).mean())
    ''')
    md("### 📊 Step 4 · Apply to LFS Data\n**Question:** how far apart are regional median pays, and how spread out is pay around the median?")
    code(r'''
    region_median = paid.groupby("region")["daily_pay"].median().sort_values()
    print(region_median.round(2))
    gap = abs(region_median["NCR"] - region_median["ARMM"])
    print(f"\nDistance |NCR − ARMM| between median daily pays: ₱{gap:,.2f}")
    ''')
    code(r'''
    m = paid["daily_pay"].median()
    mad = np.abs(paid["daily_pay"] - m).mean()               # mean absolute deviation from the median
    print(f"Median ₱{m:,.2f}; mean absolute deviation ₱{mad:,.2f}")
    distance = np.abs(region_median - m).sort_values()      # each region's distance from the national median
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.barh(distance.index, distance.values, color=OKABE_ITO[5])
    ax.set_title("Distance of each region's median daily pay from the sample median")
    ax.set_xlabel("|regional median − sample median| (₱)"); ax.set_ylabel("Region"); plt.show()
    ''')
    md(r"""
    *Alt text:* horizontal bars, one per region, sorted by length. Each bar's length is the absolute gap between that region's median pay and the overall median.
    **Takeaway:** absolute value ignores direction. A region far *above* the median and one far *below* it can have equally long bars. Check `region_median` to see which side each is on.

    > ℹ️ Region 15 is labelled **ARMM** because that was its name in 2018. It has since become **BARMM**.
    """)
    interpret(r"Explain what the mean absolute deviation (MAD) tells a policymaker about daily pay in our sample, in plain language.",
              r"*In our sample, a typical worker's daily pay is about ₱[MAD] away from the median of ₱[m].* A larger MAD means pay is more unequal or spread out. Because we use absolute values, workers above and below the median both add to the spread instead of cancelling out.")

    # end matter
    md(r"""
    ## ⚠️ Common mistakes
    - $\sqrt{a + b} \neq \sqrt{a} + \sqrt{b}$: e.g. $\sqrt{9 + 16} = 5$, but $3 + 4 = 7$.
    - $(a + b)^2 \neq a^2 + b^2$, and $(a+b)^n \ne a^n + b^n$ in general.
    - $a^m \cdot a^n \neq a^{mn}$. **Add** the exponents: $a^{m+n}$.
    - $-3^2 = -9$ but $(-3)^2 = 9$. Python agrees: `-3 ** 2 == -9`.
    - $a^{-n}$ is **not** negative. It is $1/a^n$.
    - Taking $\sqrt{x}$ of a negative in the reals, which is undefined. Always state $x \ge 0$.
    - $|a - b| \neq |a| - |b|$: e.g. $|3 - (-5)| = 8$, but $|3| - |-5| = -2$.
    - Converting an annual rate to monthly as $r/12$ when the question is about compounding.
    """)
    md("## ✅ Check your understanding\n\n" + "\n\n".join([
        r"**Q1.** Simplify $\dfrac{x^5 y^{-2}}{x^2 y^3}$ ($x, y \ne 0$)." + "\n\n" + details("Answer", r"$x^{3} y^{-5} = \dfrac{x^3}{y^5}$ (quotient law, negative exponent)."),
        r"**Q2 (True/False).** $27^{2/3} = 9$." + "\n\n" + details("Answer", r"**True:** $(\sqrt[3]{27})^2 = 3^2 = 9$."),
        r"**Q3 (MCQ).** The distance between $-4$ and $6$ is (a) 2 (b) −10 (c) 10 (d) 24" + "\n\n" + details("Answer", r"**(c)** $|-4 - 6| = 10$."),
        r"**Q4 (Fill in).** ₱1,000 at 10% per year for 2 years becomes ₱___." + "\n\n" + details("Answer", r"$1000(1.1)^2 = 1210$."),
        r"**Q5 (True/False).** $\sqrt{x^2} = x$ for every real $x$." + "\n\n" + details("Answer", r"**False:** $\sqrt{x^2} = |x|$. For example, $\sqrt{(-3)^2} = 3$."),
    ]))

    md("## 💻 Coding exercises (Part 4)")
    exercise("4.1", "⭐", "A rational exponent",
             r"Evaluate $4^{3/2}$ **by hand** first. Then store it in `ex4_1` using Python's `**`.",
             "ex4_1 = None    # YOUR CODE HERE",
             "ex4_1 = 4 ** (3 / 2)",
             'check(ex4_1, 8, hint="4^(3/2) = (√4)^3. In Python write 4 ** (3/2), with parentheses around 3/2!")')
    exercise("4.2", "⭐", "Projecting the median",
             r"Store the median daily pay of `paid` after 10 years of **4%** yearly compound growth in `ex4_2`.",
             "ex4_2 = None    # YOUR CODE HERE",
             'ex4_2 = paid["daily_pay"].median() * 1.04 ** 10',
             'check(ex4_2, paid["daily_pay"].median() * (1 + 0.04) ** 10, hint="P(1 + r)^t with r = 0.04 and t = 10.")')
    exercise("4.3", "⭐⭐", "Annual to monthly",
             r"Store the monthly rate equivalent to a **6%** annual rate, as a decimal (≈ 0.0049), in `ex4_3`.",
             "ex4_3 = None    # YOUR CODE HERE",
             "ex4_3 = 1.06 ** (1 / 12) - 1",
             'check(ex4_3, (1.06) ** (1 / 12) - 1, hint="(1 + r)^(1/12) − 1, not 0.06/12.")')
    exercise("4.4", "⭐⭐", "Distance from NCR",
             r"Store the distance $|\text{NCR median} - \text{sample median}|$ of daily pay in `ex4_4`.",
             "ex4_4 = None    # YOUR CODE HERE",
             'ex4_4 = abs(paid[paid["region"] == "NCR"]["daily_pay"].median() - paid["daily_pay"].median())',
             'check(ex4_4, abs(region_median["NCR"] - paid["daily_pay"].median()), hint="Compute both medians, subtract, then wrap the difference in abs(...).")')
    exercise("4.5", "⭐⭐⭐", "Spread of women's pay",
             r"For **female** paid workers only, store the mean absolute deviation of daily pay from **their own** median in `ex4_5`.",
             "ex4_5 = None    # YOUR CODE HERE",
             'women = paid[paid["sex"] == "Female"]["daily_pay"]\nex4_5 = np.abs(women - women.median()).mean()',
             'fem_pay = paid[paid["sex"] == "Female"]["daily_pay"]\ncheck(ex4_5, np.abs(fem_pay - fem_pay.median()).mean(), hint="Filter women first, take THEIR median, then np.abs(pay − median).mean().")')

    md(r"""
    ## ✍️ Board-work practice 🗣️
    **B4.1** Simplify $\dfrac{(x^{-2} y^3)^{-2}}{x^3 y^{-1}}$ for $x, y > 0$. Write the answer with positive exponents and name each law.

    **B4.2** Evaluate $27^{-2/3}$ and simplify $\sqrt{50} + \sqrt{18}$.

    **B4.3** Daily pay grows from ₱480 to ₱600 in 4 years at a constant rate. Find the yearly rate $r$ (leave it as a radical expression, then approximate). Also find the distance between the two pays on the number line.
    """)
    md(details("Solutions to board-work practice", r"""
**B4.1** $(x^{-2}y^3)^{-2} = x^{4} y^{-6}$ (power of a product, power of a power). Divide: $\dfrac{x^4 y^{-6}}{x^3 y^{-1}} = x^{4-3} y^{-6-(-1)} = x y^{-5} = \dfrac{x}{y^5}$ (quotient law, negative exponent).

**B4.2** $27^{-2/3} = \dfrac{1}{(\sqrt[3]{27})^2} = \dfrac{1}{9}$. $\sqrt{50} + \sqrt{18} = 5\sqrt2 + 3\sqrt2 = 8\sqrt2$ (simplify each radical, then use the distributive property).

**B4.3** $480(1+r)^4 = 600 \Rightarrow (1+r)^4 = 1.25 \Rightarrow r = 1.25^{1/4} - 1 = \sqrt[4]{1.25} - 1 \approx 0.0574$, or about 5.74% per year (taking the positive real root, since $1 + r > 0$). Distance $= |600 - 480| = 120$ pesos.
"""))
    md(RUBRIC)
    md(r"""
    ## 🔭 Why this matters for calculus
    - The **power rule** $\frac{d}{dx}x^n = nx^{n-1}$ works for rational $n$ too, so $\sqrt{x} = x^{1/2}$ has derivative $\tfrac12 x^{-1/2}$. You must move fluently between radicals and exponents.
    - Compound growth $P(1+r)^t$ leads to the number $e$ and to **exponential functions** (Week 11).
    - **Absolute value defines "closeness"** in the limit definition: $|f(x) - L| < \varepsilon$ whenever $0 < |x - a| < \delta$.

    ## 📝 Summary (Part 4 cheat-sheet)
    | Rule | Python |
    |---|---|
    | $a^m a^n = a^{m+n}$, $(a^m)^n = a^{mn}$, $a^{-n} = 1/a^n$, $a^0 = 1$ | `a ** n` |
    | $a^{m/n} = (\sqrt[n]{a})^m$; even roots need $a \ge 0$ | `a ** (m/n)`, `np.sqrt`, exact: `sp.Rational(m, n)` |
    | Growth $P(1+r)^t$; rate $r = (Q/P)^{1/t} - 1$; monthly $(1+r)^{1/12} - 1$ | `P * (1 + r) ** t`, `np.arange` |
    | $\lvert a\rvert$, $d(a,b) = \lvert a - b\rvert$ | `abs()`, `np.abs()` |
    | MAD $= \frac{1}{n}\sum \lvert x_i - m\rvert$ | `np.abs(s - s.median()).mean()` |
    | Group medians | `df.groupby("region")["daily_pay"].median()` |
    """)
