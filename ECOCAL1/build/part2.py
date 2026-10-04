from kit import md, code, details, exercise, concept_card, interpret, RUBRIC


def build():
    md(r"""
    ---
    # 🧩 Part 2 · Week 1: Basic Set Theory, Types of Numbers, Properties of Real Numbers
    **Week 1 · CLO1, CLO3 · ⏱️ Est. time: 75 min**
    📚 *Readings:* Swokowski & Cole (2011), *Fundamental Concepts of Algebra: Real Numbers*; Sydsaeter et al. (2022), *Essentials of Logic and Set Theory*; Rees, Sparks & Rees (2003), *The Number System*; economic framing: Chiang & Wainwright (2004), *Economic Models* (the real-number system, sets); Danao (2001).

    🎯 **Learning objectives.** By the end of Part 2 you can:
    1. **Compute** unions, intersections, complements and differences of sets, and **draw** a Venn diagram.
    2. **Verify** De Morgan's laws and the inclusion–exclusion counting rule.
    3. **Classify** numbers as natural, integer, rational, irrational or real, and **tell apart** codes (labels) from quantities.
    4. **Name** the real-number property used at each step of a simplification.

    🧭 **Big picture.** Economists constantly sort people into groups: the *employed*, the *labor force*, *women in NCR*, *wage workers*. Set theory is the precise language for those groups. Labor statistics are just counts of sets and ratios of counts. And before doing any arithmetic, an economist must know **what kind of number** a variable is: averaging region codes is a classic beginner's mistake.
    """)

    # ---------------- 2.1 sets
    md("## Lesson 2.1 · Sets and set operations ⏱️ 20 min")
    concept_card("sets",
        r"""A **set** is a well-defined collection of objects called **elements**. We write $x \in A$ ("$x$ is in $A$").
- **Universal set** $U$: everything under discussion. **Subset** $A \subseteq B$: every element of $A$ is in $B$.
- **Union** $A \cup B$: in $A$ **or** $B$ (or both). **Intersection** $A \cap B$: in **both**.
- **Complement** $A'$ (or $A^c$): in $U$ but **not** in $A$. **Difference** $A - B$: in $A$ but not in $B$.
- **Cardinality** $|A|$: the number of elements.
*Intuition:* sets are groups; the operations are "or", "and", "not", and "but not".""",
        "Swokowski & Cole, *Real Numbers* (sets and notation); Sydsaeter et al., *Essentials of Logic and Set Theory*.")
    md(r"""
    ### ✍️ Step 2 · Solve by Hand
    Eight surveyed persons are numbered 1–8, so $U = \{1, 2, \dots, 8\}$. Let $A = \{1, 2, 3, 5, 8\}$ be the employed and $B = \{2, 3, 4, 6, 8\}$ the females.
    - $A \cap B = \{2, 3, 8\}$ (elements in **both**): *employed women*.
    - $A \cup B = \{1, 2, 3, 4, 5, 6, 8\}$ (in **at least one**).
    - $A' = U - A = \{4, 6, 7\}$: *not employed*.
    - $A - B = \{1, 5\}$: *employed and not female*.
    - $\{2, 3\} \subseteq A$? Yes, because both 2 and 3 are in $A$.

    ### 🐍 Step 3 · Check with Python
    Python has a built-in **set** type, written with curly braces. This is the new Python idea of this lesson. The operators are `&` (∩), `|` (∪), `-` (difference), and `<=` (⊆).
    """)
    code(r'''
    U = {1, 2, 3, 4, 5, 6, 7, 8}
    A = {1, 2, 3, 5, 8}          # employed
    B = {2, 3, 4, 6, 8}          # female
    print("A ∩ B =", A & B)
    print("A ∪ B =", A | B)
    print("A'    =", U - A)
    print("A − B =", A - B)
    print("{2, 3} ⊆ A ?", {2, 3} <= A)
    ''')
    md(r"""
    ✅ The output matches the hand solution.
    ### 📊 Step 4 · Apply to LFS Data
    Let the **universal set** be every person aged 15+ in our sample, identified by `person_id`. Define
    $E$ = employed, $F$ = female, $N$ = NCR residents.
    """)
    code(r'''
    U_ids = set(df["person_id"])                                   # universal set
    E = set(df[df["empstat"] == "Employed"]["person_id"])           # employed
    F = set(df[df["sex"] == "Female"]["person_id"])                 # female
    N = set(df[df["region"] == "NCR"]["person_id"])                 # NCR residents
    print("|U| =", len(U_ids), " |E| =", len(E), " |F| =", len(F), " |N| =", len(N))
    ''')
    code(r'''
    print("|E ∩ F| employed women        =", len(E & F))
    print("|E ∪ N| employed OR in NCR    =", len(E | N))
    print("|E'|    not employed          =", len(U_ids - E))
    print("|E − F| employed, not female  =", len(E - F))
    ''')
    code(r'''
    venn2_counts(only_a=len(E - F), only_b=len(F - E), both=len(E & F), neither=len(U_ids - (E | F)),
                 labels=("E: employed", "F: female"),
                 title="Employed (E) and female (F) persons aged 15+ (LFS 2018 sample)")
    ''')
    md(r"""
    *Alt text:* two overlapping circles inside a rectangle $U$. The left-only region counts employed men, the overlap counts employed women, the right-only region counts women who are not employed, and the corner counts men who are not employed.
    **Takeaway:** the four regions add up to $|U|$, and every person falls in exactly one of them.
    """)
    interpret(r"Use the counts to complete: *\"In our sample, ___ of the ___ employed persons are women, that is ___%.\"* What set operation gives the numerator?",
              r"The numerator is $|E \cap F|$ and the denominator is $|E|$, so the share is $|E \cap F| / |E|$. A good answer looks like: *In our sample, [|E ∩ F|] of the [|E|] employed persons are women, about [share]%.* Fill in the brackets with the numbers your code printed.")

    # ---------------- 2.2 De Morgan & masks
    md("## Lesson 2.2 · De Morgan's laws and counting with inclusion–exclusion ⏱️ 15 min")
    concept_card("De Morgan's laws and inclusion–exclusion",
        r"""**De Morgan's laws:** $(A \cup B)' = A' \cap B'$ and $(A \cap B)' = A' \cup B'$.
"Not (A or B)" = "not A **and** not B"; "not (A and B)" = "not A **or** not B".
**Inclusion–exclusion:** $|A \cup B| = |A| + |B| - |A \cap B|$. Adding $|A|$ and $|B|$ counts the overlap twice, so subtract it once.""",
        "Sydsaeter et al., *Essentials of Logic and Set Theory* (set operations, Venn diagrams); Swokowski & Cole, *Real Numbers*.")
    md(r"""
    ### ✍️ Step 2 · Solve by Hand (same $U, A, B$ as Lesson 2.1)
    - $(A \cup B)' = U - \{1,2,3,4,5,6,8\} = \{7\}$, and $A' \cap B' = \{4,6,7\} \cap \{1,5,7\} = \{7\}$. ✔️ Equal, as De Morgan says.
    - $|A \cup B| = |A| + |B| - |A \cap B| = 5 + 5 - 3 = 7$. ✔️ Matches $|\{1,2,3,4,5,6,8\}| = 7$.
    ### 🐍 Step 3 · Check with Python
    """)
    code(r'''
    print("(A ∪ B)' =", U - (A | B), "  A' ∩ B' =", (U - A) & (U - B))
    print("De Morgan holds?", (U - (A | B)) == ((U - A) & (U - B)))
    print("|A ∪ B| =", len(A | B), "  |A| + |B| − |A ∩ B| =", len(A) + len(B) - len(A & B))
    ''')
    md(r"""
    ### 📊 Step 4 · Apply to LFS Data
    **New Python idea: boolean masks.** Instead of building sets of IDs, pandas can combine True/False columns directly:
    `&` = and (∩), `|` = or (∪), `~` = not (complement). **Always wrap each condition in parentheses.** `.sum()` counts the `True` values, because True counts as 1 and False as 0.
    """)
    code(r'''
    is_emp = df["empstat"] == "Employed"      # True for employed persons
    is_fem = df["sex"] == "Female"            # True for women
    is_ncr = df["region"] == "NCR"            # True for NCR residents
    print("Employed AND female :", (is_emp & is_fem).sum())
    print("Employed OR NCR     :", (is_emp | is_ncr).sum())
    print("NOT employed        :", (~is_emp).sum())
    ''')
    code(r'''
    # De Morgan on real data: (E ∪ N)' versus E' ∩ N'
    left = ~(is_emp | is_ncr)
    right = (~is_emp) & (~is_ncr)
    print("Count of (E ∪ N)':", left.sum(), "| count of E' ∩ N':", right.sum())
    print("Same people, row by row?", (left == right).all())
    # Inclusion–exclusion on real data
    print("|E ∪ N| =", (is_emp | is_ncr).sum(), "= |E| + |N| − |E ∩ N| =", is_emp.sum() + is_ncr.sum() - (is_emp & is_ncr).sum())
    ''')
    interpret(r"Explain in words what the set $(E \cup N)'$ contains in our data, and why De Morgan's law must hold *no matter what the data are*.",
              r"$(E \cup N)'$ is everyone who is **neither employed nor living in NCR**, which is the same as \"not employed **and** not in NCR\" ($E' \cap N'$). The law holds for *any* sets because it follows from the meaning of \"or\", \"and\" and \"not\". Data can illustrate it, but they cannot break it.")

    # ---------------- 2.3 types of numbers
    md("## Lesson 2.3 · Types of numbers (and why codes are not quantities) ⏱️ 15 min")
    concept_card("the real number system",
        r"""- **Natural numbers** $\mathbb{N} = \{1, 2, 3, \dots\}$ (some books include 0; check your textbook's convention).
- **Integers** $\mathbb{Z} = \{\dots, -2, -1, 0, 1, 2, \dots\}$.
- **Rational numbers** $\mathbb{Q}$: numbers $p/q$ with $p, q \in \mathbb{Z}$, $q \neq 0$. Their decimals **terminate or repeat** (0.75, 0.333…).
- **Irrational numbers**: real numbers that are **not** rational, with non-repeating, non-terminating decimals ($\sqrt{2}$, $\pi$).
- **Real numbers** $\mathbb{R}$ = rationals ∪ irrationals: every point on the number line.
$$\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}.$$
*Intuition:* each set "fills in gaps" left by the one before it.""",
        "Swokowski & Cole, *Real Numbers*; Rees, Sparks & Rees, *The Number System*; Chiang & Wainwright, *Economic Models* (the real-number system).")
    md(r"""
    ### ✍️ Step 2 · Solve by Hand
    Classify each number (list the **smallest** set it belongs to):

    | Number | Smallest set | Why |
    |---|---|---|
    | $\sqrt{9}$ | $\mathbb{N}$ | $\sqrt{9} = 3$ |
    | $0$ | $\mathbb{Z}$ | an integer (it is in $\mathbb{N}$ only if your book includes 0) |
    | $-4$ | $\mathbb{Z}$ | negative whole number |
    | $3/4 = 0.75$ | $\mathbb{Q}$ | ratio of integers; terminating decimal |
    | $0.333\ldots$ | $\mathbb{Q}$ | repeating decimal $= 1/3$ |
    | $537.50$ | $\mathbb{Q}$ | $= 1075/2$ |
    | $\sqrt{2}$, $\pi$ | irrational | never terminates or repeats |

    ### 🐍 Step 3 · Check with Python
    SymPy works with **exact** numbers. `sp.Rational(1, 3)` is exactly $1/3$. `sp.sqrt(9)` simplifies to 3, but `sp.sqrt(2)` stays as $\sqrt{2}$ because it can't be written as a fraction.
    """)
    code(r'''
    print(sp.sqrt(9), "| rational?", sp.sqrt(9).is_rational)
    print(sp.sqrt(2), "| rational?", sp.sqrt(2).is_rational)
    print(sp.pi, "| rational?", sp.pi.is_rational)
    print(sp.nsimplify(0.75), "and", sp.nsimplify(537.50))   # turn a decimal into a fraction
    ''')
    md(r"""
    **⚠️ Computers store most decimals approximately (the new Python idea of this lesson).** Python's `float` can't store $0.1$ exactly, so tiny errors appear. Compare floats with `round` or `np.isclose`, never with `==`.
    """)
    code(r'''
    print(0.1 + 0.2)                       # not exactly 0.3!
    print(0.1 + 0.2 == 0.3)                # False, because of tiny storage errors
    print(round(0.1 + 0.2, 10) == 0.3)     # True after rounding
    print(np.isclose(0.1 + 0.2, 0.3))      # True: "equal up to a tiny tolerance"
    ''')
    md(r"""
    ### 📊 Step 4 · Apply to LFS Data
    Which kind of number is each LFS variable? **Ask: does arithmetic on it make sense?**
    """)
    code(r'''
    print("All ages are whole numbers?", (df["age"] % 1 == 0).all())        # remainder after ÷1 is 0
    print("Some daily pay values:", paid["daily_pay"].head(5).tolist())
    print("Mean sex_code (meaningless!):", round(df["sex_code"].mean(), 3))
    print("Share female (meaningful):   ", round((df["sex_code"] == 2).mean(), 3))
    ''')
    md(r"""
    | Variable | Kind of number | Does adding/averaging make sense? |
    |---|---|---|
    | `age` | whole number (ℕ, recorded in completed years) | ✅ mean age is meaningful |
    | `daily_pay` | rational (pesos and centavos), a measurement of a real quantity | ✅ |
    | `hours_week` | whole number of hours | ✅ |
    | `region_code`, `sex_code` | **labels** that happen to be written with digits | ❌ count them instead |

    > 🏷️ The mean of `sex_code` is meaningless, but the **share** of rows where `sex_code == 2` *is* meaningful. It is the proportion female. The *mean of a True/False column* is a proportion, a trick we'll reuse often.
    """)
    interpret(r"A classmate reports \"the average region code is 9.4, so the typical Filipino lives near Zamboanga (code 9).\" Explain the mistake using the idea of *types of numbers*.",
              r"Region codes are **labels** (names written with digits), not quantities. The ordering and spacing of the codes mean nothing, so arithmetic like averaging is meaningless. To describe where people live, count persons per region (`value_counts()`) or report the most common region.")

    # ---------------- 2.4 properties
    md("## Lesson 2.4 · Properties of real numbers ⏱️ 15 min")
    concept_card("field properties of ℝ",
        r"""For all real $a, b, c$:
| Property | Addition | Multiplication |
|---|---|---|
| Commutative | $a + b = b + a$ | $ab = ba$ |
| Associative | $(a + b) + c = a + (b + c)$ | $(ab)c = a(bc)$ |
| Identity | $a + 0 = a$ | $a \cdot 1 = a$ |
| Inverse | $a + (-a) = 0$ | $a \cdot \frac{1}{a} = 1$ **if $a \neq 0$** |
| Distributive | $a(b + c) = ab + ac$ | |

*Intuition:* these are the "legal moves" of algebra. Every simplification step is one of them.""",
        "Swokowski & Cole, *Real Numbers* (properties of real numbers); Sydsaeter et al., *Algebra* (rules of algebra).")
    md(r"""
    ### ✍️ Step 2 · Solve by Hand (board-work style: name every property)
    A worker gets ₱450 basic pay plus a ₱50 allowance per day for 5 days. Total weekly pay:
    $$
    \begin{aligned}
    5(450 + 50) &= 5 \cdot 450 + 5 \cdot 50 && \text{distributive property} \\
    &= 2250 + 250 && \text{multiplication} \\
    &= 2500. &&
    \end{aligned}
    $$
    Simplify $4(x + 5) + 3x$:
    $$
    \begin{aligned}
    4(x + 5) + 3x &= (4x + 20) + 3x && \text{distributive} \\
    &= 4x + (20 + 3x) && \text{associative (+)} \\
    &= 4x + (3x + 20) && \text{commutative (+)} \\
    &= (4x + 3x) + 20 && \text{associative (+)} \\
    &= (4 + 3)x + 20 = 7x + 20 && \text{distributive (factoring out } x).
    \end{aligned}
    $$
    ### 🐍 Step 3 · Check with Python
    """)
    code(r'''
    print(5 * (450 + 50), "=", 5 * 450 + 5 * 50)          # distributive, with numbers
    x = sp.symbols("x")
    print(sp.expand(4 * (x + 5) + 3 * x))                 # SymPy simplifies to 7x + 20
    ''')
    md(r"""
    ### 📊 Step 4 · Apply to LFS Data
    **Question:** if every paid worker in our sample worked 5 days, what would the *total* weekly pay bill be? Distributivity says that **multiplying each pay by 5 and then adding** gives the same result as **adding first and then multiplying by 5**: $\sum 5d_i = 5\sum d_i$.
    """)
    code(r'''
    way_1 = (5 * paid["daily_pay"]).sum()                  # multiply each pay by 5, then add
    way_2 = 5 * paid["daily_pay"].sum()                    # add first, then multiply by 5
    print(f"Way 1: ₱{way_1:,.2f}   Way 2: ₱{way_2:,.2f}")
    print("Equal (up to float rounding)?", np.isclose(way_1, way_2))
    ''')
    code(r'''
    # Commutativity: adding in a different order (sorted from smallest to largest) gives the same total
    print("Original order:", paid["daily_pay"].sum(), "| sorted order:", paid["daily_pay"].sort_values().sum())
    # Multiplicative inverse: d × (1/d) = 1 for every pay, which works only because no pay is 0 (we set 0 → NaN)
    print("d·(1/d) = 1 for everyone?", np.allclose(paid["daily_pay"] * (1 / paid["daily_pay"]), 1))
    ''')
    interpret(r"Why did the teaching file convert a daily pay of 0 into `NaN`? Connect your answer to the **inverse** property.",
              r"The multiplicative inverse $1/a$ exists only when $a \neq 0$. Dividing by a pay of 0 is undefined. Also, a recorded 0 usually means \"no cash pay / not applicable\" rather than a true wage of zero, so treating it as missing avoids meaningless results such as an hourly pay of ₱0 or dividing by zero.")

    # ---------------- end matter
    md(r"""
    ## ⚠️ Common mistakes
    - Writing `df["empstat"] == "Employed" & df["sex"] == "Female"` **without parentheses**. Python then evaluates `&` first, and you get an error or wrong results. ✅ `(cond1) & (cond2)`.
    - Thinking $(A \cap B)' = A' \cap B'$. ❌ By De Morgan, $(A \cap B)' = A' \cup B'$.
    - Forgetting to subtract the overlap: $|A \cup B| \neq |A| + |B|$ unless $A \cap B = \varnothing$.
    - Averaging codes (`region_code`, `sex_code`). They are **labels**.
    - Assuming subtraction or division is commutative: $5 - 3 \neq 3 - 5$, $6/3 \neq 3/6$.
    - Testing floats with `==`: `0.1 + 0.2 == 0.3` is `False`. Use `np.isclose`.
    - Saying "$\frac{1}{a}$ is the inverse of $a$" without the condition **$a \neq 0$**.
    """)
    md("## ✅ Check your understanding\n\n" + "\n\n".join([
        "**Q1 (True/False).** Every integer is a rational number.\n\n" + details("Answer", r"**True.** Any integer $n$ can be written as $n/1$."),
        r"**Q2 (Fill in).** If $|A| = 40$, $|B| = 25$ and $|A \cap B| = 10$, then $|A \cup B| =$ ___." + "\n\n" + details("Answer", r"$40 + 25 - 10 = 55$ (inclusion–exclusion)."),
        "**Q3 (MCQ).** Which LFS variable is *not* a quantity? (a) `age` (b) `daily_pay` (c) `region_code` (d) `hours_week`\n\n" + details("Answer", "**(c)**: region codes are labels."),
        r"**Q4 (Name the property).** $7(x + 3) = 7x + 21$." + "\n\n" + details("Answer", "Distributive property."),
        r"**Q5 (MCQ).** $(A \cup B)'$ equals: (a) $A' \cup B'$ (b) $A' \cap B'$ (c) $A \cap B$ (d) $U$" + "\n\n" + details("Answer", r"**(b)** $A' \cap B'$ (De Morgan)."),
    ]))

    md("## 💻 Coding exercises (Part 2)\nUse the sets `U_ids, E, F, N` and the masks `is_emp, is_fem, is_ncr` built above.")
    exercise("2.1", "⭐", "Employed women",
             r"Store $|E \cap F|$, the number of employed women in our sample, in `ex2_1`.",
             "ex2_1 = None    # YOUR CODE HERE",
             "ex2_1 = len(E & F)",
             'check(ex2_1, len(E & F), hint="Use & between the sets E and F, then wrap it in len(...).")')
    exercise("2.2", "⭐", "NCR residents who are not employed",
             r"Store $|N - E|$ in `ex2_2`.",
             "ex2_2 = None    # YOUR CODE HERE",
             "ex2_2 = len(N - E)",
             'check(ex2_2, len(N - E), hint="Set difference uses the minus sign: N - E (order matters!).")')
    exercise("2.3", "⭐⭐", "A complement with masks",
             r"Using the **masks** `is_emp` and `is_fem` (not sets), store the number of persons in $(E \cap F)'$ in `ex2_3`.",
             "ex2_3 = None    # YOUR CODE HERE",
             "ex2_3 = (~(is_emp & is_fem)).sum()",
             'check(ex2_3, len(U_ids - (E & F)), hint="Complement = ~( ... ). Put is_emp & is_fem in parentheses, negate it, then .sum().")',
             explanation=r"By De Morgan this equals the count of $E' \cup F'$: people who are not employed **or** not female.")
    exercise("2.4", "⭐⭐", "Share of the employed who are women",
             r"Store the **proportion** (between 0 and 1, don't round) of employed persons who are female, $|E \cap F| / |E|$, in `ex2_4`.",
             "ex2_4 = None    # YOUR CODE HERE",
             "ex2_4 = len(E & F) / len(E)",
             'check(ex2_4, len(E & F) / len(E), hint="Numerator: employed AND female. Denominator: ALL employed.")')
    exercise("2.5", "⭐⭐⭐", "Inclusion–exclusion without |",
             r"Compute $|E \cup N|$ **without** using `|` or `∪`. Use only `len`, `&`, `+` and `-`. Store it in `ex2_5`.",
             "ex2_5 = None    # YOUR CODE HERE",
             "ex2_5 = len(E) + len(N) - len(E & N)",
             'check(ex2_5, len(E | N), hint="|E ∪ N| = |E| + |N| − |E ∩ N|.")')

    md(r"""
    ## ✍️ Board-work practice (pen and paper, then explain out loud 🗣️)
    **B2.1** $U = \{1, 2, \dots, 10\}$ are ten household members. $L = \{2, 3, 5, 7, 8, 10\}$ are in the labor force, $W = \{1, 2, 3, 4, 5\}$ are women. Find $L \cap W$, $L \cup W$, $L'$, $W - L$. Draw the Venn diagram. Verify $(L \cap W)' = L' \cup W'$, naming the law.

    **B2.2** Simplify $3(2x - 4) + 5x - 2(x + 1)$, naming the property used at **every** step.

    **B2.3** In a sample of 200 persons, 130 are employed, 90 are female, and 50 are employed females. How many are **neither** employed nor female? Show the formula you use, and interpret the answer.
    """)
    md(details("Solutions to board-work practice", r"""
**B2.1** $L \cap W = \{2,3,5\}$; $L \cup W = \{1,2,3,4,5,7,8,10\}$; $L' = \{1,4,6,9\}$; $W - L = \{1,4\}$.
$(L \cap W)' = \{1,4,6,7,8,9,10\}$; $L' \cup W' = \{1,4,6,9\} \cup \{6,7,8,9,10\} = \{1,4,6,7,8,9,10\}$ ✔️ (De Morgan's law).

**B2.2** $3(2x-4) + 5x - 2(x+1) = 6x - 12 + 5x - 2x - 2$ (distributive) $= (6x + 5x - 2x) + (-12 - 2)$ (commutative and associative) $= (6+5-2)x - 14$ (distributive) $= 9x - 14$.

**B2.3** $|E \cup F| = |E| + |F| - |E \cap F| = 130 + 90 - 50 = 170$ (inclusion–exclusion). Neither $= |U| - |E \cup F| = 200 - 170 = 30$. *Interpretation:* 30 persons are men who are not employed (unemployed or not in the labor force).
"""))
    md(RUBRIC)

    md(r"""
    ## 🔭 Why this matters for calculus
    - Every function has a **domain**, the *set* of allowed inputs. Questions like "where is $f$ continuous?" are answered with sets and intervals (Part 3).
    - Limits rely on the **real line having no gaps**: $\sqrt{2}$, $\pi$ and $e$ are real numbers that sequences of rationals approach. That is why we work in $\mathbb{R}$, not just $\mathbb{Q}$.
    - Every step of a derivative computation is a **legal move** from Lesson 2.4. The expand-and-cancel step in Part 1 used the distributive property.

    ## 📝 Summary (Part 2 cheat-sheet)
    | Math | Meaning | Python |
    |---|---|---|
    | $A \cap B$, $A \cup B$, $A - B$, $A'$ | and, or, but not, not | `A & B`, `A \| B`, `A - B`, `U - A` |
    | $\lvert A\rvert$ | count | `len(A)` |
    | $A \subseteq B$ | subset | `A <= B` |
    | $(A\cup B)' = A'\cap B'$, $(A\cap B)' = A'\cup B'$ | De Morgan | `~(m1 \| m2) == (~m1 & ~m2)` |
    | $\lvert A\cup B\rvert = \lvert A\rvert+\lvert B\rvert-\lvert A\cap B\rvert$ | inclusion–exclusion | |
    | $\mathbb{N}\subset\mathbb{Z}\subset\mathbb{Q}\subset\mathbb{R}$ | number systems | `sp.Rational`, `sp.sqrt(2).is_rational` |
    | float ≈ real | stored approximately | `np.isclose`, `round` |
    | $a(b+c) = ab+ac$ … | real-number properties | `sp.expand` |

    New Python this Part: `set`, boolean masks `& | ~`, `.sum()` on True/False, `np.isclose`.
    """)
