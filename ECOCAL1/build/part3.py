from kit import md, code, details, exercise, concept_card, interpret, RUBRIC


def build():
    md(r"""
    ---
    # 📏 Part 3 · Week 2: Inequalities and Intervals of Real Numbers
    **Week 2 (with Week 1 practice) · CLO1, CLO2 · ⏱️ Est. time: 75 min**
    📚 *Readings:* Swokowski & Cole (2011), *Real Numbers* (order, intervals) and *Inequalities*; Sydsaeter et al. (2022), *Algebra* (inequalities, intervals); Rees, Sparks & Rees (2003), *Inequalities*; economic framing: Dowling (2011), *Review* chapter.

    🎯 **Learning objectives.** By the end of Part 3 you can:
    1. **Solve** linear and compound inequalities, flipping the sign when you multiply or divide by a negative.
    2. **Write** solution sets in interval notation and **draw** them on a number line.
    3. **Compute** unions and intersections of intervals.
    4. **Use** intervals to define age groups and other labor-market categories in data.

    🧭 **Big picture.** Policies and statistics are full of inequalities: the *working-age* population is ages 15–64, the *youth* are 15–24, and a worker who worked *fewer than 40 hours* may be underemployed. A minimum wage is a lower bound on pay. Writing these precisely as intervals avoids ambiguity: is a 24-year-old a youth? Is a 25-year-old?
    """)
    md(r"""
    ## 🔁 Warm-up: Week 1 practice (5 min, by hand)
    1. $U = \{1,\dots,6\}$, $A = \{1, 2, 3\}$, $B = \{3, 4\}$. Find $(A \cup B)'$ and $A' \cap B'$.
    2. Name the property: $(x + 2) + 5 = x + (2 + 5)$.
    3. Is $0.\overline{12} = 0.121212\ldots$ rational or irrational?
    """ + "\n" + details("Answers", r"1. Both are $\{5, 6\}$ (De Morgan). 2. Associative property of addition. 3. Rational, because it repeats: $0.\overline{12} = 12/99 = 4/33$."))

    # 3.1
    md("## Lesson 3.1 · Order properties and linear inequalities ⏱️ 20 min")
    concept_card("order properties",
        r"""For real $a, b, c$ with $a < b$:
1. $a + c < b + c$ (adding or subtracting keeps the direction).
2. If $c > 0$: $ac < bc$ (multiplying by a **positive** number keeps the direction).
3. If $c < 0$: $ac > bc$ (multiplying or dividing by a **negative** number **reverses** the direction).
A **linear inequality** like $mx + k \ge q$ is solved like an equation, while watching rule 3.
*Intuition:* multiplying by $-1$ mirrors the number line, so "left of" becomes "right of".""",
        "Swokowski & Cole, *Inequalities*; Sydsaeter et al., *Algebra* (inequalities).")
    md(r"""
    ### ✍️ Step 2 · Solve by Hand
    **(a)** A worker paid ₱62.50 per hour wants weekly earnings of **at least** ₱2,500:
    $$62.5h \ge 2500 \;\Longrightarrow\; h \ge \frac{2500}{62.5} = 40 \quad \text{(divided by } 62.5 > 0\text{: direction kept)}.$$
    **(b)** A ₱500 weekly transport allowance shrinks by ₱20 for every hour of overtime $h$. When does more than ₱100 remain?
    $$500 - 20h > 100 \;\Rightarrow\; -20h > -400 \;\Rightarrow\; h < 20 \quad \text{(divided by } -20 < 0\text{: direction **reversed**)}.$$
    ### 🐍 Step 3 · Check with Python
    The new Python idea: `sp.solveset(inequality, variable, domain=sp.S.Reals)` returns the solution **as an interval**. `sp.Rational("62.5")` keeps 62.5 exact ($=125/2$).
    """)
    code(r'''
    h = sp.symbols("h", real=True)
    print(sp.solveset(sp.Rational("62.5") * h >= 2500, h, domain=sp.S.Reals))   # expect [40, ∞)
    print(sp.solveset(500 - 20 * h > 100, h, domain=sp.S.Reals))                # expect (−∞, 20)
    ''')
    md(r"""
    `Interval(40, oo)` means $[40, \infty)$ and `Interval.open(-oo, 20)` means $(-\infty, 20)$. ✅ Matches.
    ### 📊 Step 4 · Apply to LFS Data
    **Question:** how many employed persons in our sample worked **at least 40 hours** last week ($h \ge 40$)? A comparison on a column gives True/False for each row, and `.sum()` counts the Trues.
    """)
    code(r'''
    has_hours = emp.dropna(subset=["hours_week"])           # employed persons with reported hours
    at_least_40 = has_hours["hours_week"] >= 40
    print("Employed with reported hours:", len(has_hours))
    print("Worked h ≥ 40:", at_least_40.sum(), f"({at_least_40.mean():.1%} of them)")
    ''')
    interpret(r"Write one sentence about the share you found. Why did we drop persons with missing hours *before* computing the share?",
              r"*In our sample, about __% of employed persons with reported hours worked at least 40 hours last week.* Missing hours (originally `999`, \"not reported\") are neither ≥ 40 nor < 40. Keeping them in the denominator would wrongly lower the share.")

    # 3.2
    md("## Lesson 3.2 · Compound inequalities and interval notation ⏱️ 20 min")
    concept_card("intervals",
        r"""| Inequality | Interval | Type |
|---|---|---|
| $a < x < b$ | $(a, b)$ | open |
| $a \le x \le b$ | $[a, b]$ | closed |
| $a \le x < b$ | $[a, b)$ | half-open |
| $x \ge a$ | $[a, \infty)$ | unbounded |
| $x < b$ | $(-\infty, b)$ | unbounded |
A square bracket **includes** the endpoint (●); a round bracket **excludes** it (○). $\infty$ is not a number, so it always gets a round bracket.
A **compound inequality** $p \le mx + k < q$ is solved by doing the same operation to **all three parts**.""",
        "Swokowski & Cole, *Real Numbers* (intervals) and *Inequalities* (compound inequalities); Sydsaeter et al., *Algebra* (intervals).")
    md(r"""
    ### ✍️ Step 2 · Solve by Hand
    **(a)** $-3 \le 2x - 5 < 7 \;\Rightarrow\; 2 \le 2x < 12$ (add 5 to all parts) $\;\Rightarrow\; 1 \le x < 6$ (divide all parts by $2 > 0$). Solution: $[1, 6)$.
    **(b)** The working-age population is $15 \le \text{age} \le 64$, or $[15, 64]$. Persons aged 25 and over: $[25, \infty)$. Their **intersection** is $[15, 64] \cap [25, \infty) = [25, 64]$.
    **(c)** "Dependent ages": youth or elderly, $[15, 24] \cup [65, \infty)$. This union can't be written as a single interval.

    ### 🐍 Step 3 · Check with Python
    """)
    code(r'''
    x = sp.symbols("x", real=True)
    print(sp.reduce_inequalities([2 * x - 5 >= -3, 2 * x - 5 < 7], x))   # both parts at once
    working_age = sp.Interval(15, 64)                                     # closed [15, 64]
    print(working_age.intersect(sp.Interval(25, sp.oo)))                  # [25, 64]
    print(sp.Interval(15, 24).union(sp.Interval(65, sp.oo)))
    print("Is 64.5 in [15, 64]?", working_age.contains(64.5))
    ''')
    md(r"""
    ### 📊 Step 4 · Apply to LFS Data
    **New Python idea:** `.between(a, b)` tests $a \le x \le b$, a **closed** interval by default. Python also allows **chained comparisons** like `15 <= age <= 64` for a single number.
    """)
    code(r'''
    age_example = 24
    print("Is a 24-year-old a youth (15 ≤ age ≤ 24)?", 15 <= age_example <= 24)   # chained comparison
    working = df["age"].between(15, 64)            # [15, 64]
    youth = df["age"].between(15, 24)              # [15, 24]
    print(f"Working age [15, 64]: {working.sum()} persons ({working.mean():.1%})")
    print(f"Youth [15, 24]:       {youth.sum()} persons ({youth.mean():.1%})")
    ''')
    code(r'''
    # Underemployment proxy: worked in the OPEN interval (0, 40), i.e. 0 < h < 40
    short_hours = (has_hours["hours_week"] > 0) & (has_hours["hours_week"] < 40)
    print(f"Employed who worked 0 < h < 40 hours: {short_hours.sum()} ({short_hours.mean():.1%})")
    number_line([(15, 64, True, True, "Working age [15, 64]"), (15, 24, True, True, "Youth [15, 24]"),
                 (0, 40, False, False, "Short hours (0, 40)"), (65, np.inf, True, False, "Elderly [65, ∞)")],
                xlim=(0, 100), title="Labor-market intervals on the number line", xlabel="Age or hours")
    ''')
    md(r"""
    *Alt text:* four horizontal bars. Filled dots mark included endpoints, hollow dots mark excluded endpoints, and an arrow marks an interval that goes on to infinity.
    **Takeaway:** the open interval $(0, 40)$ has hollow dots: exactly 0 and exactly 40 hours are **not** included.
    """)
    interpret(r"The PSA counts persons aged 15 and over in the labor force. Explain why it matters whether *youth* is written $[15, 24]$ or $[15, 25)$ when age is recorded in whole years.",
              r"With whole-year ages, $[15, 24]$ and $[15, 25)$ contain exactly the same people (15, 16, …, 24). If age were measured continuously (24.5 years), they would differ: $[15, 25)$ would include 24.5 but $[15, 24]$ would not. Precise interval notation removes the ambiguity about the endpoints.")

    # 3.3
    md("## Lesson 3.3 · Intervals as bins: age groups ⏱️ 15 min")
    concept_card("partitioning the line into half-open intervals",
        r"""Half-open intervals $[15, 25), [25, 35), [35, 45), \dots$ **partition** the ages: every age falls in **exactly one** group, because each left endpoint is included and each right endpoint is excluded. There are no gaps and no overlaps.
*Intuition:* each boundary age belongs to the **next** group (25 goes in $[25, 35)$).""",
        "Swokowski & Cole, *Real Numbers* (intervals); Sydsaeter et al., *Algebra*.")
    md(r"""
    ### ✍️ Step 2 · Solve by Hand
    Ages 24, 25, 34, 35 with bins $[15, 25), [25, 35), [35, 45)$: 24 → $[15, 25)$; 25 → $[25, 35)$; 34 → $[25, 35)$; 35 → $[35, 45)$.
    ### 🐍 Step 3 · Check with Python
    New Python idea: `pd.cut(values, bins=[...], right=False)` sorts values into half-open bins $[a, b)$. (`right=False` means "don't include the right endpoint".)
    """)
    code(r'''
    print(pd.cut([24, 25, 34, 35], bins=[15, 25, 35, 45], right=False))
    ''')
    md("### 📊 Step 4 · Apply to LFS Data\n**Question:** how does the employment rate (employed ÷ persons in the group) vary across age groups?")
    code(r'''
    age_bins = [15, 25, 35, 45, 55, 65, np.inf]                     # last group is [65, ∞)
    df["age_group"] = pd.cut(df["age"], bins=age_bins, right=False)
    df["is_employed"] = df["empstat"] == "Employed"                 # True/False column
    emp_rate = df.groupby("age_group", observed=True)["is_employed"].mean()   # mean of True/False = share
    print(df["age_group"].value_counts().sort_index())
    print((emp_rate * 100).round(1))
    ''')
    code(r'''
    fig, ax = plt.subplots()
    ax.bar(emp_rate.index.astype(str), emp_rate.values * 100, color=OKABE_ITO[0])
    ax.set_title("Employment rate by age group (LFS 2018 sample)")
    ax.set_xlabel("Age group (half-open intervals)"); ax.set_ylabel("Employed (% of persons in group)")
    plt.show()
    ''')
    md(r"""
    *Alt text:* six bars, one per age interval from $[15, 25)$ to $[65, \infty)$. Bar height is the percent employed in that group.
    **Takeaway:** read off which age interval has the highest and the lowest employment rate. Typically youth (still in school) and the elderly (retired) are lower.
    """)
    interpret(r"Describe the shape of the bar chart in two sentences, starting with *\"In our sample, …\"*. Suggest one economic reason for the lowest bar.",
              r"*In our sample, the employment rate is lowest for [group] and highest for [group].* Low youth rates often reflect schooling. Low rates at 65+ reflect retirement. Note that \"not employed\" includes people outside the labor force, not just the unemployed.")

    # end matter
    md(r"""
    ## ⚠️ Common mistakes
    - **Not flipping** the inequality when multiplying or dividing by a negative: $-2x > 6 \Rightarrow x < -3$ (not $x > -3$).
    - Writing $[5, \infty]$. ❌ Infinity is never included: $[5, \infty)$.
    - Mixing up brackets: $(0, 40)$ excludes 0 and 40; $[0, 40]$ includes both.
    - In a compound inequality, applying an operation to only **two** of the three parts.
    - Thinking `.between(a, b)` is open. By default it is **closed**, $[a, b]$.
    - Forgetting `right=False` in `pd.cut`. The default makes bins $(a, b]$, so a 25-year-old would land in the wrong group.
    """)
    md("## ✅ Check your understanding\n\n" + "\n\n".join([
        r"**Q1 (Fill in).** $-4x \le 12 \Rightarrow x$ ___ $-3$." + "\n\n" + details("Answer", r"$x \ge -3$, since dividing by $-4$ reverses the sign."),
        r"**Q2 (MCQ).** $\{x : 2 < x \le 9\}$ is (a) $(2, 9)$ (b) $[2, 9]$ (c) $(2, 9]$ (d) $[2, 9)$" + "\n\n" + details("Answer", "**(c)**"),
        r"**Q3 (True/False).** $[15, 24] \cap [20, 30] = [20, 24]$." + "\n\n" + details("Answer", "**True.**"),
        r"**Q4 (True/False).** `df['age'].between(15, 24)` includes persons aged exactly 24." + "\n\n" + details("Answer", "**True**: it is closed by default."),
    ]))

    md("## 💻 Coding exercises (Part 3)")
    exercise("3.1", "⭐", "Working-age count",
             r"Store the number of persons in $[15, 64]$ in `ex3_1`.",
             "ex3_1 = None    # YOUR CODE HERE",
             'ex3_1 = df["age"].between(15, 64).sum()',
             'check(ex3_1, ((df["age"] >= 15) & (df["age"] <= 64)).sum(), hint="Use df[\\"age\\"].between(15, 64), then .sum().")')
    exercise("3.2", "⭐", "Youth share",
             r"Store the **proportion** of persons aged $[15, 24]$ (a number between 0 and 1) in `ex3_2`.",
             "ex3_2 = None    # YOUR CODE HERE",
             'ex3_2 = df["age"].between(15, 24).mean()',
             'check(ex3_2, ((df["age"] >= 15) & (df["age"] <= 24)).mean(), hint="The mean of a True/False column is a proportion.")')
    exercise("3.3", "⭐⭐", "Short hours among the employed",
             r"Among employed persons **with reported hours** (`has_hours`), store the proportion who worked $h \in (0, 40)$ in `ex3_3`.",
             "ex3_3 = None    # YOUR CODE HERE",
             'ex3_3 = ((has_hours["hours_week"] > 0) & (has_hours["hours_week"] < 40)).mean()',
             'check(ex3_3, ((has_hours["hours_week"] > 0) & (has_hours["hours_week"] < 40)).mean(), hint="Open interval → strict < and >. Combine with & and wrap each part in parentheses. Use has_hours, not df.")')
    exercise("3.4", "⭐⭐", "Solve by hand, enter the interval",
             r"Solve $3x - 7 \le 11$ **by hand**. Then type your answer as a SymPy interval, e.g. `sp.Interval(-sp.oo, 2)` for $(-\infty, 2]$. Store it in `ex3_4`.",
             "ex3_4 = None    # YOUR CODE HERE  (e.g. sp.Interval(-sp.oo, ...))",
             "ex3_4 = sp.Interval(-sp.oo, 6)",
             'check(ex3_4, sp.solveset(3 * x - 7 <= 11, x, domain=sp.S.Reals), hint="3x ≤ 18, so x ≤ 6. The right endpoint is included: sp.Interval(-sp.oo, 6).")')
    exercise("3.5", "⭐⭐⭐", "Employment rate in [25, 35)",
             r"Without using `age_group`, store the employment rate (proportion employed) of persons aged $25 \le \text{age} < 35$ in `ex3_5`.",
             "ex3_5 = None    # YOUR CODE HERE",
             'in_group = df[(df["age"] >= 25) & (df["age"] < 35)]\nex3_5 = (in_group["empstat"] == "Employed").mean()',
             'check(ex3_5, df[(df["age"] >= 25) & (df["age"] < 35)]["is_employed"].mean(), hint="Filter rows with (age >= 25) & (age < 35), then take the mean of (empstat == \\"Employed\\").")')

    md(r"""
    ## ✍️ Board-work practice 🗣️
    **B3.1** Solve $4 - 3x > -8$. Write the answer in interval notation and graph it. At which step does the inequality sign change, and why?

    **B3.2** Solve $-1 < \dfrac{2x + 1}{3} \le 5$ and write the solution as an interval.

    **B3.3** Let $Y = [15, 24]$ and $S = [18, 30)$. Find $Y \cap S$ and $Y \cup S$. Interpret $Y \cap S$ if $S$ is "ages eligible for a training program".
    """)
    md(details("Solutions to board-work practice", r"""
**B3.1** $-3x > -12$ (subtract 4) ⇒ $x < 4$ (divide by $-3$: **reverse** the sign, by the order property for negative multipliers). Answer: $(-\infty, 4)$, an open circle at 4 with an arrow to the left.

**B3.2** Multiply all parts by 3: $-3 < 2x + 1 \le 15$. Subtract 1: $-4 < 2x \le 14$. Divide by 2: $-2 < x \le 7$. Answer: $(-2, 7]$.

**B3.3** $Y \cap S = [18, 24]$; $Y \cup S = [15, 30)$. Interpretation: youth who are eligible for the program are ages 18 to 24, inclusive.
"""))
    md(RUBRIC)
    md(r"""
    ## 🔭 Why this matters for calculus
    - **Domains** are written as intervals: $\sqrt{x - 15}$ is defined on $[15, \infty)$.
    - **Continuity** is studied *on intervals* (Weeks 12–13), and one-sided limits look at values just to the left or right of a point.
    - The formal definition of a limit says "$f(x)$ is within $\varepsilon$ of $L$ whenever $x$ is within $\delta$ of $a$". Those are **compound inequalities**, and in Part 4 you will write them with absolute values.

    ## 📝 Summary (Part 3 cheat-sheet)
    | Rule / notation | Python |
    |---|---|
    | Multiply or divide by a negative ⇒ **flip** the sign | `sp.solveset(ineq, x, domain=sp.S.Reals)` |
    | $a \le x \le b \iff [a, b]$; $a < x < b \iff (a, b)$ | `sp.Interval(a, b)`, `sp.Interval.open(a, b)` |
    | Compound inequality: apply each step to all parts | `sp.reduce_inequalities([...], x)` |
    | $\cap$, $\cup$ of intervals | `.intersect()`, `.union()` |
    | Closed test in data | `s.between(a, b)` |
    | Strict test in data | `(s > a) & (s < b)` |
    | Half-open bins $[a, b)$ | `pd.cut(s, bins, right=False)` |
    | Share of True | `mask.mean()` |
    """)
