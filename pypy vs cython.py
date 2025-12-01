import os, glob

base = os.path.dirname(os.path.realpath(__file__))
realbase = base
base = os.path.join(base, "solutions")
os.chdir(base)

from subprocess import DEVNULL, STDOUT, check_call
import time

# check_call(['/etc/init.d/apache2', 'restart'], stdout=DEVNULL, stderr=STDOUT)

data = ["File,Cython,PyPy"]

for file in glob.glob("*.py"):
    if "Day" not in file: continue
    print(f"{file}:")
    dt = 0
    for _ in range(3):
        start = time.time()
        check_call(["python", os.path.join(base, file)], stdout=DEVNULL, stderr=DEVNULL)
        dt += time.time() - start
    avg = round(dt / 3, 3)
    print(f"\tCython: {avg}s")

    dtpp = 0
    for _ in range(3):
        start = time.time()
        check_call(["pypy", os.path.join(base, file)], stdout=DEVNULL, stderr=DEVNULL)
        dtpp += time.time() - start
    avgpp = round(dtpp / 3, 3)
    print(f"\tPyPy: {avgpp}s")

    data.append(f"{file},{avg},{avgpp}")

with open(os.path.join(realbase, "output.csv"), "w") as f:
    f.write("\n".join(data))
