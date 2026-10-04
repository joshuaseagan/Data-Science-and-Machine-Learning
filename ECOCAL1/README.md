# ECOCAL1 · Python & Calculus Foundations with LFS 2018 data

A self-study Google Colab notebook for De La Salle University's **ECOCAL1 – Economics Calculus 1** (Term 1, AY 2026–2027). It teaches beginner Python alongside the algebra of **Weeks 1–8**, starting with a short "What is calculus?" preview. Every example uses the **PSA Labor Force Survey 2018** Public Use File.

**Open it:** upload [`ECOCAL1_Python_and_Calculus_Foundations_LFS2018.ipynb`](ECOCAL1_Python_and_Calculus_Foundations_LFS2018.ipynb) to Google Colab (*File → Upload notebook*), or open it from GitHub in Colab.

## Structure
| Part | Week | Topics |
|---|---|---|
| 0 | – | Python Survival Kit |
| 1 | Preview | Calculus at a glance: rates of change, the derivative idea, marginal thinking |
| 2 | 1 | Sets, types of numbers, properties of real numbers |
| 3 | 2 | Inequalities and intervals |
| 4 | 3 | Exponents, radicals, rational exponents, absolute value and distance |
| 5 | 4 | Algebraic expressions, polynomial operations, special products |
| 6 | 5 | Factoring and rational expressions (LFPR, unemployment rate, hourly pay) |
| 7 | 6 | Linear, quadratic, radical and absolute-value equations |
| 8 | 7 | Inequalities, systems of linear equations, midterm review sheet |
| 9 | 8 | Integrated case study: *A profile of the Filipino worker in 2018* |

Every lesson follows a five-step loop: **📖 Read → ✍️ Solve by hand → 🐍 Check with Python → 📊 Apply to LFS data → 💬 Interpret**. Coding exercises come with auto-check cells and hidden solutions.

## Data
- Instructor: run the three **🔒 Instructor only** cells once (set `RUN_INSTRUCTOR_SETUP = True`). They turn the PSA file `FIES-LFS PUF 2018 LFS_SUMMARY.CSV` into a small teaching file, `lfs2018_ecocal1.csv`: a reproducible random sample of 5,000 persons aged 15+, recoded, with missing codes set to NaN.
- Students: load `lfs2018_ecocal1.csv` (sidebar upload, Google Drive, or upload dialog). If the file is missing, the notebook falls back to a synthetic dataset clearly labelled **PRACTICE ONLY – NOT REAL DATA**, so it still runs top to bottom.
- The raw PSA file is **not** included in this repository. Use PSA data under the PSA's terms for public use files. All computed rates are unweighted teaching estimates, not official statistics.

## Rebuilding
The notebook is generated from the scripts in [`build/`](build/). After editing them:

```bash
pip install nbformat
python ECOCAL1/build/build_notebook.py                 # writes the notebook
python ECOCAL1/build/build_notebook.py --test /tmp/x   # also writes a copy with every exercise solved, for testing
```
