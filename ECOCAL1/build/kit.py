"""Tiny toolkit for writing the ECOCAL1 notebook as Python code.

Every part file calls md(), code(), exercise(), ... in order. build() then turns
the recorded cells into either the student notebook or a self-test notebook in
which every exercise starter cell is replaced by its solution.
"""
import textwrap

import nbformat

_CELLS = []  # list of dicts: {"kind": "md"|"code", "src": str, "solution": str|None}


def _clean(text):
    return textwrap.dedent(text).strip("\n")


def md(text):
    _CELLS.append({"kind": "md", "src": _clean(text), "solution": None})


def code(text, title=None):
    """A code cell. `title` adds a Colab form header that hides the code."""
    src = _clean(text)
    if title:
        src = f'#@title {title} {{ display-mode: "form" }}\n' + src
    _CELLS.append({"kind": "code", "src": src, "solution": None})


def details(summary, body):
    """Markdown with a collapsible (hidden) block."""
    return f"<details>\n<summary><b>{summary}</b></summary>\n\n{_clean(body)}\n\n</details>"


def concept_card(title, body, read_more):
    md(f"### 📖 Step 1 · Read & Understand: {title}\n\n"
       f"> **Concept card**\n>\n" + "\n".join("> " + line if line else ">" for line in _clean(body).split("\n"))
       + f"\n>\n> 📚 *Read more:* {read_more}")


def interpret(prompt, model_answer):
    md(f"### 💬 Step 5 · Interpret & Explain 🗣️\n\n{_clean(prompt)}\n\n"
       "✏️ **Your answer** *(double-click this cell to type)*: …\n\n"
       + details("👀 Compare with a model answer (after writing yours)", model_answer))


def exercise(number, stars, title, prompt, starter, solution, check, explanation=""):
    """Prompt (markdown) → starter (code) → auto-check (hidden code) → hidden solution."""
    md(f"#### 💻 Exercise {number} {stars} ✅ · {title}\n\n{_clean(prompt)}")
    _CELLS.append({"kind": "code", "src": _clean(starter), "solution": _clean(solution)})
    code(check, title=f"✅ Auto-check for Exercise {number} (just run me)")
    body = f"```python\n{_clean(solution)}\n```"
    if explanation:
        body += "\n\n" + _clean(explanation)
    md(details(f"💡 Solution to Exercise {number} (try first!)", body))


RUBRIC = """
> **🗣️ Self-assessment (same rubric as board-work recitation and exams).** For each problem, rate yourself honestly:
>
> | Level | Score | What it looks like |
> |---|---|---|
> | **Exemplary** | 100% | Complete, correct answer; every step justified with the property used; correct interpretation. |
> | **Satisfactory** | 50% | Correct method, but a slip somewhere in the derivation leads to a partly wrong final answer. |
> | **Developing** | 25% | Tried the right method, but the immediate solution and final answer are wrong. |
> | **Beginning** | 0% | Nothing substantial, or nothing with mathematical meaning. |
>
> Anything below *Exemplary*? Re-do the problem tomorrow **without looking** at the solution.
"""


def build(path, test_mode=False):
    nb = nbformat.v4.new_notebook()
    nb.metadata = {
        "colab": {"provenance": [], "toc_visible": True},
        "kernelspec": {"display_name": "Python 3", "name": "python3"},
        "language_info": {"name": "python"},
    }
    for c in _CELLS:
        if c["kind"] == "md":
            nb.cells.append(nbformat.v4.new_markdown_cell(c["src"]))
        else:
            src = c["solution"] if (test_mode and c["solution"]) else c["src"]
            nb.cells.append(nbformat.v4.new_code_cell(src))
    # stable, readable cell ids
    for i, cell in enumerate(nb.cells):
        cell["id"] = f"cell-{i:04d}"
    nbformat.validate(nb)
    nbformat.write(nb, path)
    return nb
