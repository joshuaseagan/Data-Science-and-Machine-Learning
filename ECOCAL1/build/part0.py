from kit import md, code, details, exercise


def build():
    md(r"""
    ---
    # 🐍 Part 0 · Python Survival Kit
    **⏱️ Est. time: 45–60 min · Goal: learn only the Python you need for Parts 1–9.**

    🎯 **By the end of Part 0 you can:** run cells; store numbers and text in variables; use lists and dictionaries; write an `if` and a `for` loop; define a function; load the LFS data; and summarize, filter, and chart it.

    > 💡 **Tip:** Before running a cell, **predict** its output on paper. Then run it. That small habit is what turns "watching code" into learning.
    """)

    # 0.1
    md(r"""
    ## Lesson 0.1 · Colab basics ⏱️ 5 min
    - A notebook is made of **cells**. *Text cells* (like this one) explain. *Code cells* (grey boxes) run Python.
    - Run a code cell with **Shift + Enter**. The output appears right below it.
    - A `#` starts a **comment**: a note for humans that Python ignores.
    - `print(...)` displays something.
    - Cells share memory. A variable created in one cell can be used in later cells, **as long as the earlier cell has been run**.
    """)
    code(r'''
    # This is a comment: Python ignores everything after the # sign.
    print("Mabuhay! Welcome to ECOCAL1 with Python.")
    print(2 + 3)
    ''')

    # 0.2
    md(r"""
    ## Lesson 0.2 · Variables and arithmetic ⏱️ 8 min
    A **variable** is a labelled box that stores a value. The `=` sign means *"put the value on the right into the box on the left"*. It is **not** the mathematical "equals" of an equation.

    | Math | Python | Example | Result |
    |---|---|---|---|
    | $a + b$ | `a + b` | `7 + 2` | `9` |
    | $a - b$ | `a - b` | `7 - 2` | `5` |
    | $a \times b$ | `a * b` | `7 * 2` | `14` |
    | $a \div b$ | `a / b` | `7 / 2` | `3.5` |
    | $a^b$ | `a ** b` | `2 ** 3` | `8` ⚠️ *not* `2 ^ 3` |
    | whole-number part of $a \div b$ | `a // b` | `7 // 2` | `3` |
    | remainder | `a % b` | `7 % 2` | `1` |
    """)
    code(r'''
    daily_pay = 500          # a worker earns ₱500 per day (a made-up example)
    days_worked = 6          # she works 6 days this week
    weekly_pay = daily_pay * days_worked
    print(weekly_pay)
    ''')
    md(r"""
    **Order of operations (PEMDAS) works in Python too:** Parentheses → Exponents → Multiplication/Division → Addition/Subtraction.
    ✍️ *Predict the four outputs on paper first.*
    """)
    code(r'''
    print(2 + 3 * 4)         # multiplication before addition → 14
    print((2 + 3) * 4)       # parentheses first → 20
    print(-3 ** 2)           # ⚠️ the power is done BEFORE the minus sign → -9
    print((-3) ** 2)         # → 9
    ''')
    md(r"""
    > ⚠️ `-3 ** 2` gives `-9` in Python, just as $-3^2 = -(3^2) = -9$ in algebra. If you mean "negative three, squared", write `(-3) ** 2`.
    """)

    # 0.3
    md(r"""
    ## Lesson 0.3 · Types of values and printing nicely ⏱️ 7 min
    Every value has a **type**:

    | Type | Meaning | Example |
    |---|---|---|
    | `int` | whole number | `34` |
    | `float` | number with a decimal point | `537.50` |
    | `str` | text ("string"), always in quotes | `"NCR"` |
    | `bool` | True/False | `True` |
    """)
    code(r'''
    age = 34                 # int
    pay = 537.50             # float
    region = "NCR"           # str
    is_employed = True       # bool
    print(type(age), type(pay), type(region), type(is_employed))
    print(age >= 15)         # a comparison gives a bool: True or False
    ''')
    md(r"""
    An **f-string** (a string with `f` in front) lets you put values inside text using `{ }`. Adding `:,.2f` inside the braces means "use comma separators and 2 decimal places".
    """)
    code(r'''
    name = "Ana"
    print(f"{name} is {age} years old and earns ₱{pay} per day.")
    print(f"Her pay for 6 days is ₱{pay * 6:,.2f}.")
    ''')

    # 0.4
    md(r"""
    ## Lesson 0.4 · Lists and dictionaries ⏱️ 7 min
    A **list** holds several values in order, inside square brackets. Python counts positions **from 0**.
    """)
    code(r'''
    hours = [40, 48, 36, 54, 20]     # hours worked last week by 5 workers
    print(hours[0])                  # the FIRST item (position 0)
    print(len(hours), sum(hours), max(hours))   # how many, total, largest
    hours.append(45)                 # add a sixth worker
    print(hours)
    ''')
    md(r"""
    A **dictionary** links a *key* to a *value*, like a codebook. The LFS stores regions as numeric codes. A dictionary turns them into names:
    """)
    code(r'''
    region_names = {13: "NCR", 4: "CALABARZON", 15: "ARMM"}   # code → name
    print(region_names[13])
    print(region_names[4])
    ''')
    md(r"""
    > 🏷️ **A number is not always a quantity.** `13` here is a *label* for NCR, like a jersey number. Adding codes is meaningless: $13 + 4 = 17$, but "NCR + CALABARZON" is not region 17 (MIMAROPA)! We return to this idea in Part 2 (*types of numbers*).
    """)

    # 0.5
    md(r"""
    ## Lesson 0.5 · Making decisions with `if` ⏱️ 5 min
    `if` runs the indented lines only when a condition is `True`. `else` covers every other case. **Indentation (4 spaces) matters in Python.** It shows which lines belong to the `if`.
    """)
    code(r'''
    weekly_hours = 36
    if weekly_hours < 40:
        print("Worked fewer than 40 hours this week")
    else:
        print("Worked 40 hours or more this week")
    ''')

    # 0.6
    md(r"""
    ## Lesson 0.6 · Repeating with `for` loops ⏱️ 5 min
    A `for` loop repeats the indented lines once for **each** item in a list.
    """)
    code(r'''
    total = 0
    for h in hours:                  # h takes each value in the list, one at a time
        total = total + h            # add it to the running total
        print("added", h, "→ running total is", total)
    print("Total hours:", total)
    ''')

    # 0.7
    md(r"""
    ## Lesson 0.7 · Defining your own functions ⏱️ 5 min
    A **function** is a reusable recipe: inputs go in, an output comes out. In math, $W(d, n) = d \cdot n$. In Python:
    """)
    code(r'''
    def weekly_pay_from(daily, days):
        """Return weekly pay given pay per day and number of days worked."""
        return daily * days

    print(weekly_pay_from(500, 6))
    print(weekly_pay_from(daily=650, days=5))
    ''')

    # 0.8
    md(r"""
    ## Lesson 0.8 · Our four toolboxes (libraries) ⏱️ 3 min
    The setup cell at the top ran `import ... as ...` to load four libraries under short nicknames:

    | Nickname | Library | We use it for |
    |---|---|---|
    | `pd` | **pandas** | data tables: load, filter, summarize the LFS |
    | `np` | **NumPy** | fast math on many numbers: `np.sqrt`, `np.abs`, `np.polyfit` |
    | `plt` | **matplotlib** | charts |
    | `sp` | **SymPy** | algebra with letters: expand, factor, solve |
    """)
    code(r'''
    print(np.sqrt(16))               # NumPy: square root
    x = sp.symbols("x")              # SymPy: create the letter x
    sp.expand((x + 1) ** 2)          # the last line's result is displayed as math
    ''')

    # 0.9
    md(r"""
    ## Lesson 0.9 · Loading the LFS 2018 teaching file ⏱️ 5 min
    Your instructor prepared a small file, **`lfs2018_ecocal1.csv`**, from the PSA Public Use File. Load it in **one** of three ways:

    1. **Upload with the sidebar (easiest):** click the 📁 folder icon on the left → *Upload* → choose the file. Then run the cell below as it is.
    2. **Google Drive:** set `MOUNT_DRIVE = True`. The cell looks in `MyDrive/LFS/` and `MyDrive/`.
    3. **Upload dialog:** set `USE_UPLOAD_DIALOG = True` and pick the file when asked.

    If the file can't be found, the notebook **still works**. It switches to a small **synthetic** dataset marked **PRACTICE ONLY – NOT REAL DATA**. Its numbers are invented, so never quote them as facts about the Philippines.
    """)
    code(r'''
    import os                                     # lets Python check whether a file exists
    DATA_FILE = "lfs2018_ecocal1.csv"
    MOUNT_DRIVE = False                           # True → look in your Google Drive
    USE_UPLOAD_DIALOG = False                     # True → choose the file from your computer
    if MOUNT_DRIVE:
        from google.colab import drive
        drive.mount("/content/drive")
    if USE_UPLOAD_DIALOG:
        from google.colab import files
        files.upload()
    places_to_look = [DATA_FILE, "/content/" + DATA_FILE,
                      "/content/drive/MyDrive/LFS/" + DATA_FILE, "/content/drive/MyDrive/" + DATA_FILE]
    ''')
    code(r'''
    df = None
    for path in places_to_look:
        if os.path.exists(path):
            df = pd.read_csv(path)                # read the CSV file into a table
            print(f"✅ Loaded the real LFS 2018 teaching file from {path}: {len(df):,} persons aged 15+")
            break                                 # stop looking once we found it
    USING_REAL_DATA = df is not None
    if not USING_REAL_DATA:
        print(f"⚠️ Could not find {DATA_FILE}. Upload it (📁 sidebar) and re-run, or continue with practice data.")
        print("🚧 USING PRACTICE ONLY – NOT REAL DATA (synthetic numbers, for learning Python only).")
        df = make_practice_data()
    ''')

    # 0.10
    md(r"""
    ## Lesson 0.10 · First look at the data ⏱️ 7 min
    `df` (short for *DataFrame*) is a table: **one row per person**, one column per variable.
    """)
    code(r'''
    df.head()        # the first 5 rows
    ''')
    code(r'''
    print(df.shape)              # (number of rows, number of columns)
    print(list(df.columns))      # the column names
    ''')
    code(r'''
    df.describe().round(2)       # count, mean, min, max, ... of every numeric column
    ''')
    md(r"""
    > 🏷️ **Spot the nonsense.** `describe()` happily reports a *mean* `region_code` and a *mean* `sex_code`. Those numbers mean **nothing**, because the codes are labels, not quantities. For a label, **count** the categories with `.value_counts()`:
    """)
    code(r'''
    print("Average region code (meaningless!):", round(df["region_code"].mean(), 2))
    print(df["empstat"].value_counts())       # how many persons in each category
    ''')

    # 0.11
    md(r"""
    ## Lesson 0.11 · Selecting columns and filtering rows ⏱️ 8 min
    - `df["age"]` picks **one column**. `df[["age", "sex"]]` (double brackets) picks **several**.
    - `df["empstat"] == "Employed"` gives `True`/`False` for **every row**. Putting that inside `df[...]` **keeps only the True rows**. This is called *boolean filtering*.
    """)
    code(r'''
    ages = df["age"]                              # one column
    print("Youngest:", ages.min(), "| Oldest:", ages.max(), "| Mean age:", round(ages.mean(), 1))
    df[["age", "sex", "empstat"]].head(3)         # several columns
    ''')
    code(r'''
    employed_mask = df["empstat"] == "Employed"   # True/False for every person
    emp = df[employed_mask].copy()                # keep employed persons (.copy() = independent table)
    print("Employed persons in our sample:", len(emp))
    ''')
    md(r"""
    **Missing values (`NaN`).** Many people have **no** daily pay recorded: they are not employed, they are self-employed, or they did not report it. In the teaching file, missing or not-applicable codes (`999`, `0`, blanks) became **`NaN`** ("not a number"). pandas *skips* `NaN` when computing a mean or median. Still, always know how many values are missing.
    """)
    code(r'''
    print(df["daily_pay"].isna().sum(), "persons have no daily pay recorded (NaN)")
    paid = df.dropna(subset=["daily_pay"]).copy()     # keep persons WITH a recorded daily pay
    print("Persons with a recorded daily pay:", len(paid))
    print(f"Median daily pay in our sample: ₱{paid['daily_pay'].median():,.2f}")
    ''')
    md(r"""
    > 📌 We will reuse three tables all term: **`df`** = everyone aged 15+, **`emp`** = employed persons, **`paid`** = persons with a recorded daily pay.
    """)

    # 0.12
    md(r"""
    ## Lesson 0.12 · Your first chart ⏱️ 5 min
    Every chart in this notebook has a **title**, **labelled axes with units**, and a **one-sentence takeaway**.
    """)
    code(r'''
    counts = df["empstat"].value_counts()           # persons per employment status
    fig, ax = plt.subplots()                        # an empty figure with one set of axes
    ax.bar(counts.index, counts.values, color=OKABE_ITO[:len(counts)])
    ax.set_title("Employment status of persons aged 15+ (LFS 2018 sample)")
    ax.set_xlabel("Employment status")
    ax.set_ylabel("Number of persons in sample")
    plt.show()
    ''')
    md(r"""
    *Chart description (alt text):* a bar chart with three bars, one each for Employed, Unemployed, and Not in labor force. Bar height is the number of sampled persons in each group.
    **Takeaway (fill in from your chart):** in our sample, the largest group is ____ and the smallest is ____. The unemployed bar is usually short, because "unemployed" means having no job **and** actively looking for one. People who are not looking (students, homemakers, retirees) are *not in the labor force*.
    """)

    # errors
    md(r"""
    ## 🩺 Reading error messages (you *will* see them, and that's normal)
    Read the **last line** of a red error first. It names the error type:

    | Error | Typical cause | Example | Fix |
    |---|---|---|---|
    | `NameError: name 'emp' is not defined` | You used a variable before creating it, or skipped a cell | ran Part 3 before Part 0 | *Runtime → Run before* |
    | `TypeError: unsupported operand type(s) for +: 'int' and 'str'` | Mixing types, like a number plus text | `5 + "5"` | convert: `5 + int("5")` |
    | `KeyError: 'Age'` | A column name is misspelled (capital letters count!) | `df["Age"]` | `df["age"]`. Check `df.columns` |
    | `SyntaxError: invalid syntax` | A typo in the code's grammar: missing `:`, `)` or quote | `if x > 3 print(x)` | `if x > 3: print(x)` |
    | `IndentationError` | Lines under `if`/`for`/`def` not indented consistently | | use 4 spaces |

    🧪 *Try it:* remove the `#` from the line below, run the cell, read the error, then put the `#` back.
    """)
    code(r'''
    # print(df["Age"])     # ← a KeyError on purpose: the real column name is "age"
    ''')

    # Part 0 practice
    md(r"""
    ## 💻 Part 0 practice (auto-checked)
    Replace `None` with your code, run the cell, then run the check cell below it.
    """)
    exercise("0.1", "⭐", "Weekly pay",
             r"A worker earns ₱610 per day and works 5 days. Store the weekly pay in `ex0_1`. *(Compute it in your head first!)*",
             "ex0_1 = None    # YOUR CODE HERE",
             "ex0_1 = 610 * 5",
             'check(ex0_1, 3050, hint="Multiply the daily pay by the number of days with *.")')
    exercise("0.2", "⭐", "How many women?",
             r"Store the number of **females** in our sample in `ex0_2`. *(Hint: filter `df` with `df[\"sex\"] == \"Female\"`, then use `len`.)*",
             "ex0_2 = None    # YOUR CODE HERE",
             'ex0_2 = len(df[df["sex"] == "Female"])',
             'check(ex0_2, (df["sex"] == "Female").sum(), hint="Text must match exactly, with a capital F: \\"Female\\".")')
    exercise("0.3", "⭐⭐", "Average age of employed persons",
             r"Store the **mean age of employed persons** in `ex0_3`. Use the `emp` table. Don't round.",
             "ex0_3 = None    # YOUR CODE HERE",
             'ex0_3 = emp["age"].mean()',
             'check(ex0_3, df[df["empstat"] == "Employed"]["age"].mean(), hint="Select the \\"age\\" column of emp, then call .mean().")')

    # weights box
    md(r"""
    ## 🧠 Going further (optional): what are survey weights?
    The LFS does not interview every Filipino. Each sampled person **represents** many others, and that number is their **weight** (`PWGTPRV`, stored here as `weight`). Some groups are sampled more heavily than others. So an *unweighted* average (every row counts once) can differ from a *weighted* average (each row counts `weight` times):
    $$\bar{x}_w = \frac{\sum_i w_i x_i}{\sum_i w_i}.$$
    Official PSA statistics are **weighted**. In this notebook we keep things **unweighted** for simplicity. That is one reason our numbers are only *teaching estimates*.
    """)
    code(r'''
    unweighted = paid["daily_pay"].mean()
    weighted = np.average(paid["daily_pay"], weights=paid["weight"])   # Σ w·x / Σ w
    print(f"Unweighted mean daily pay: ₱{unweighted:,.2f}")
    print(f"Weighted mean daily pay:   ₱{weighted:,.2f}")
    ''')
    md(r"""
    > ✅ **Part 0 done!** You know enough Python for the rest of the notebook. New tools will be introduced **one at a time**, exactly when we need them.
    """)
