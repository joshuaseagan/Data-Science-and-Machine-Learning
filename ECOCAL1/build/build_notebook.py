"""Build ECOCAL1_Python_and_Calculus_Foundations_LFS2018.ipynb.

Usage:
    python build_notebook.py            # writes the student notebook next to this folder
    python build_notebook.py --test DIR # also writes a self-test copy (solutions filled in) to DIR
"""
import importlib
import os
import sys

import kit

PARTS = ["front", "part0", "part1", "part2", "part3", "part4", "part5", "part6",
         "part7", "part8", "part9", "closing"]
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                   "ECOCAL1_Python_and_Calculus_Foundations_LFS2018.ipynb")

if __name__ == "__main__":
    for name in PARTS:
        if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), name + ".py")):
            importlib.import_module(name).build()
    nb = kit.build(OUT)
    print(f"Wrote {os.path.normpath(OUT)} with {len(nb.cells)} cells")
    if "--test" in sys.argv:
        test_dir = sys.argv[sys.argv.index("--test") + 1]
        kit.build(os.path.join(test_dir, "selftest.ipynb"), test_mode=True)
        print("Wrote self-test notebook to", test_dir)
