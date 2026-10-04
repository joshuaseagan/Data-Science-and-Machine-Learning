from kit import md, code, details, exercise, concept_card, interpret


def build():
    md(r"""
    ---
    # 🔭 Part 1 · Calculus at a Glance: A Gentle Preview
    **Preview before Week 1 · CLO2 · ⏱️ Est. time: 40 min**
    📚 *Read more:* Sydsaeter et al. (2022), *Differentiation* (introduction: slopes and rates of change); Chiang & Wainwright (2004), *Comparative Statics and the Concept of Derivative*.

    🎯 **Learning objectives.** By the end of Part 1 you can:
    1. **Describe** a function as an input → output machine.
    2. **Compute** an average rate of change (the slope of a secant line).
    3. **Explain** how shrinking the interval leads to an *instantaneous* rate of change (the **derivative**), and how that is a **limit**.
    4. **Interpret** a rate of change as a *marginal* effect in economics.

    🧭 **Big picture.** Calculus is the mathematics of **change**. Economists constantly ask *"how much does Y change when X changes a little?"* How much more does a worker earn with one more year of experience? How much does demand fall when the price rises by one peso? This Part shows the *ideas* with LFS data. The formal rules come in later weeks. **No need to memorize anything here.** Just enjoy the view of where ECOCAL1 is heading.
    """)

    # 1.1
    md(r"""
    ## Lesson 1.1 · Functions: input → output machines ⏱️ 8 min
    """)
    concept_card("functions",
        r"""A **function** $f$ assigns to each input $x$ **exactly one** output $f(x)$.
Example: if a worker earns ₱62.50 per hour, weekly earnings are a function of hours worked: $E(h) = 62.5\,h$.
*Intuition:* put hours in, get pesos out.""",
        "Sydsaeter et al., *Introduction to Functions*; Swokowski & Cole, *Functions and Graphs* (formally in Weeks 9–10).")
    md(r"""
    ### ✍️ Step 2 · Solve by Hand
    $E(40) = 62.5 \times 40 = 2{,}500$. Working 40 hours earns ₱2,500. Also $E(0) = 0$ and $E(48) = 62.5 \times 48 = 3{,}000$.
    ### 🐍 Step 3 · Check with Python
    """)
    code(r'''
    def weekly_earnings(hours, rate=62.5):
        """E(h) = rate × h: weekly earnings for h hours at a given hourly rate."""
        return rate * hours

    for h in [0, 40, 48]:
        print(f"E({h}) = ₱{weekly_earnings(h):,.2f}")
    ''')
    md(r"""
    ### 📊 Step 4 · Apply to LFS Data
    Let's plot $E(h)$ over the hours **actually worked** by employed persons in our sample. `np.linspace(a, b, n)` makes `n` evenly spaced numbers from `a` to `b`, which is useful for drawing smooth lines.
    """)
    code(r'''
    h_values = np.linspace(0, emp["hours_week"].max(), 100)   # 100 points from 0 to the max hours observed
    fig, ax = plt.subplots()
    ax.plot(h_values, weekly_earnings(h_values), lw=2.5, label="E(h) = 62.5·h")
    ax.set_title("Weekly earnings as a function of hours worked (₱62.50/hour)")
    ax.set_xlabel("Hours worked per week (h)"); ax.set_ylabel("Weekly earnings (₱)")
    ax.legend(); plt.show()
    print("Hours worked last week in our sample range from", emp["hours_week"].min(), "to", emp["hours_week"].max())
    ''')
    md(r"""
    *Alt text:* a straight line rising from the origin. Each extra hour adds the same ₱62.50.
    **Takeaway:** a straight line has a **constant rate of change**. Every hour adds the same amount. Real age–pay data is *not* a straight line, and that is where calculus becomes useful.
    """)
    interpret(r"In one or two sentences, what does the number 62.5 mean in $E(h) = 62.5h$, in economic terms?",
              r"62.5 is the **rate of change** of earnings with respect to hours: every additional hour worked adds ₱62.50 to weekly earnings. It is the **slope** of the line.")

    # 1.2
    md(r"""
    ## Lesson 1.2 · Average rate of change = slope of a secant line ⏱️ 10 min
    """)
    concept_card("average rate of change",
        r"""For a function $f$ between $x = a$ and $x = b$:
$$\text{average rate of change} = \frac{f(b) - f(a)}{b - a} = \frac{\Delta f}{\Delta x}.$$
This is the slope of the **secant line** through $(a, f(a))$ and $(b, f(b))$.
*Intuition:* "on average, how much did the output change per one unit of input?" """,
        "Sydsaeter et al., *Differentiation*: slopes of curves / rates of change.")
    md(r"""
    ### ✍️ Step 2 · Solve by Hand
    Suppose average daily pay is ₱400 at age 25 and ₱520 at age 35. Then
    $$\frac{520 - 400}{35 - 25} = \frac{120}{10} = 12 \text{ pesos per year of age.}$$
    ### 🐍 Step 3 · Check with Python
    """)
    code(r'''
    pay_25, pay_35 = 400, 520
    print("Average rate of change:", (pay_35 - pay_25) / (35 - 25), "pesos per year")
    ''')
    md(r"""
    ### 📊 Step 4 · Apply to LFS Data
    **Question:** how does average daily pay change from one age group to the next?
    We group workers aged 20–69 by **decade** using `(age // 10) * 10` (so 27 → 20, 43 → 40). Then `groupby` computes the mean pay in each group. `groupby` is the one new Python idea in this lesson: *"split the table into groups, then summarize each group"*.
    """)
    code(r'''
    adults = paid[paid["age"] >= 20]                  # ages 20 and above ...
    adults = adults[adults["age"] < 70]               # ... and below 70
    decade = (adults["age"] // 10) * 10               # 20, 30, 40, 50, 60
    pay_by_decade = adults.groupby(decade)["daily_pay"].mean()
    print(pay_by_decade.round(2))
    ''')
    code(r'''
    slopes = pay_by_decade.diff() / 10                # (change in mean pay) ÷ (10 years)
    print("Average rate of change of pay (₱ per year of age), from the previous decade:")
    print(slopes.round(2))
    ''')
    code(r'''
    fig, ax = plt.subplots()
    ax.plot(pay_by_decade.index + 5, pay_by_decade.values, "o-", ms=9, lw=2)   # +5 → middle of each decade
    ax.set_title("Mean daily pay by age group, with secant lines (LFS 2018 sample)")
    ax.set_xlabel("Age (middle of each 10-year group)"); ax.set_ylabel("Mean daily pay (₱)")
    plt.show()
    ''')
    md(r"""
    *Alt text:* dots for the mean daily pay of the 20s, 30s, 40s, 50s and 60s, joined by straight segments (secant lines).
    **Takeaway:** the slope of each segment is an *average* rate of change. Notice whether the segments get flatter, or even point downward, at older ages.
    """)
    interpret(r"Pick one value from `slopes` and explain it in a sentence that starts with *\"In our sample, …\"*.",
              r"*In our sample, moving from workers in their 20s to workers in their 30s, mean daily pay rises by about ₱__ per additional year of age, on average.* A negative value would mean average pay is **lower** for the older group. Remember that these are different people (a cross-section), not the same people getting older.")

    # 1.3
    md(r"""
    ## Lesson 1.3 · Instantaneous rate of change: the derivative idea ⏱️ 12 min
    """)
    concept_card("instantaneous rate of change (derivative)",
        r"""Make the interval $[a, a+h]$ **shorter and shorter** ($h \to 0$). If the average rates of change settle down to one number, that number is the **instantaneous rate of change**, or **derivative**:
$$f'(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}.$$
"$\lim$" (**limit**) means "the value the expression approaches". You will study limits formally in Weeks 11–13.
*Intuition:* the slope of the curve **at a single point** (the tangent line).""",
        "Sydsaeter et al., *Differentiation*: the derivative / tangent lines; Chiang & Wainwright, *The Concept of Derivative*.")
    md(r"""
    ### ✍️ Step 2 · Solve by Hand
    Let $f(x) = x^2$ and $a = 3$, so $f(3) = 9$.
    - $h = 1$: $\dfrac{f(4) - f(3)}{1} = \dfrac{16 - 9}{1} = 7$
    - $h = 0.1$: $\dfrac{f(3.1) - f(3)}{0.1} = \dfrac{9.61 - 9}{0.1} = 6.1$
    - $h = 0.01$: $\dfrac{9.0601 - 9}{0.01} = 6.01$

    The values approach **6**. (Algebra shows why: $\frac{(3+h)^2 - 9}{h} = \frac{6h + h^2}{h} = 6 + h \to 6$. You'll use that *expand-then-cancel* trick constantly in Parts 5–6!)
    ### 🐍 Step 3 · Check with Python
    """)
    code(r'''
    def f(x):
        return x ** 2

    for h in [1, 0.1, 0.01, 0.001]:
        slope = (f(3 + h) - f(3)) / h
        print(f"h = {h:<6}  average rate of change = {slope:.4f}")
    ''')
    md(r"""
    ### 📊 Step 4 · Apply to LFS Data
    Real data is noisy, so we first fit a smooth curve through it. `np.polyfit(x, y, 2)` finds the **best-fitting quadratic** $p(a) = c_0 + c_1 a + c_2 a^2$, the *age–pay profile* (you'll study polynomials in Part 5).
    """)
    code(r'''
    c2, c1, c0 = np.polyfit(paid["age"], paid["daily_pay"], 2)   # coefficients, highest power first
    print(f"Fitted profile: p(a) = {c0:.2f} + {c1:.3f}·a + ({c2:.5f})·a²")

    def p(age_value):
        """Predicted daily pay (₱) at a given age, from the fitted quadratic."""
        return c0 + c1 * age_value + c2 * age_value ** 2
    ''')
    code(r'''
    ages_grid = np.linspace(15, paid["age"].max(), 200)
    fig, ax = plt.subplots()
    ax.scatter(paid["age"], paid["daily_pay"], s=8, alpha=0.25, label="Workers (sample)")
    ax.plot(ages_grid, p(ages_grid), lw=3, color=OKABE_ITO[3], label="Fitted quadratic p(a)")
    ax.set_title("Daily pay vs. age with a fitted quadratic profile (LFS 2018 sample)")
    ax.set_xlabel("Age (years)"); ax.set_ylabel("Daily pay (₱)"); ax.legend(); plt.show()
    ''')
    md(r"""
    *Alt text:* a cloud of dots (one per worker) with a smooth orange curve through the middle.
    **Takeaway:** the curve summarizes the typical pay at each age. Its *steepness* changes with age, so the rate of change is different at different ages.

    Now the limit idea on real data: the slope of $p$ at age 30, over shrinking intervals.
    """)
    code(r'''
    a0 = 30
    for h in [1, 0.1, 0.01, 0.001, 0.0001]:
        slope = (p(a0 + h) - p(a0)) / h
        print(f"h = {h:<7} slope over [30, 30+h] = {slope:.5f} pesos per year")
    ''')
    md(r"""
    The numbers **settle down**. That settling value is the derivative $p'(30)$. SymPy can compute derivatives exactly with `sp.diff`. Let's confirm:
    """)
    code(r'''
    a = sp.symbols("a")                      # the letter a (age) as a SymPy symbol
    p_sym = c0 + c1 * a + c2 * a ** 2        # the same profile, written with the symbol
    dp = sp.diff(p_sym, a)                   # derivative with respect to a
    print("p'(a) =", dp)
    print("p'(30) =", round(float(dp.subs(a, 30)), 5), "pesos per year")
    ''')
    interpret(r"Does the shrinking-$h$ table agree with `sp.diff`? What does $p'(30)$ mean for a 30-year-old worker?",
              r"Yes: the slopes approach the same value that `sp.diff` gives. $p'(30)$ is the predicted **extra daily pay per additional year of age** for workers around age 30. If it is positive, predicted pay is still rising at 30.")

    # 1.4
    md(r"""
    ## Lesson 1.4 · Marginal thinking ⏱️ 5 min
    In economics, a derivative is often called a **marginal** quantity: *marginal cost, marginal revenue, marginal product*. Here, $p'(a)$ is the **marginal pay of one more year of age** (a rough stand-in for experience).
    > 🧠 Marginal thinking is one of the key ideas in the economics program ("opportunity cost, marginal, and positive-sum thinking"). Calculus is its language.
    """)
    code(r'''
    for age_value in [20, 30, 40, 50, 60]:
        print(f"Age {age_value}: marginal pay p'(a) = {float(dp.subs(a, age_value)):8.2f} ₱ per year")
    ''')
    interpret(r"Compare the marginal pay at age 20 and at age 50. Why might the profile flatten out (or turn down) at older ages?",
              r"*In our sample, the marginal pay at 20 is ___ and at 50 it is ___.* Typically it is larger for young workers, who gain skills quickly, and smaller (possibly negative) later. Possible reasons: skills stop growing, health declines, and different generations have different education levels. This is a cross-section, not one person's career.")

    # 1.5
    md(r"""
    ## Lesson 1.5 · (Optional) Accumulation: a glimpse of integrals ⏱️ 3 min
    The *other* half of calculus adds up many small pieces. A worker's **total** weekly hours is the sum of daily hours, which is the total area of the bars below. Integrals (in later courses) do the same thing for smoothly changing quantities.
    """)
    code(r'''
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    hours_by_day = [8, 8, 9, 8, 10, 4, 0]
    fig, ax = plt.subplots(figsize=(7, 3.5))
    ax.bar(days, hours_by_day, color=OKABE_ITO[2])
    ax.set_title(f"Accumulation: total = {sum(hours_by_day)} hours (area of all the bars)")
    ax.set_xlabel("Day of the week"); ax.set_ylabel("Hours worked")
    plt.show()
    print("Total hours worked last week by ALL employed persons in our sample:", emp["hours_week"].sum())
    ''')
    md(r"""
    *Alt text:* seven bars for Monday to Sunday (8, 8, 9, 8, 10, 4 and 0 hours). **Takeaway:** adding up many small pieces is *accumulation*.

    ---
    > ### 🔭 To do calculus well, you need algebra to be automatic. That is what Parts 2–9 build.
    > In this preview you already used: **functions** (Weeks 9–10), **exponents** ($a^2$, Part 4), **polynomials** ($c_0 + c_1a + c_2a^2$, Part 5), **expand-and-cancel** (Parts 5–6), and **limits** (Weeks 11–13). Let's build those foundations one week at a time.
    """)
