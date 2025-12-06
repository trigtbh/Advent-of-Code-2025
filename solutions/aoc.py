import requests

import os
basepath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
with open(os.path.join(basepath, "cookie.txt")) as f:

    cookies = {"session": f.read()}

def get_input(year, day):
    if not os.path.exists(os.path.join(basepath, "inputs", f"{day}.txt")):
        contents = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies=cookies).text
        with open(os.path.join(basepath, "inputs", f"{day}.txt"), "w") as f:
            f.write(contents.strip())
    else:
        with open(os.path.join(basepath, "inputs", f"{day}.txt"), "r") as f:
            contents = f.read().strip()
    return contents

template = """import aoc
contents = aoc.get_input([year], [day]).strip()
del aoc

# ---
"""    

import os
base = os.path.dirname(os.path.realpath(__file__))

if __name__ == "__main__":
    os.chdir(base)
    year = input("Year: ")
    day = input("Day: ")

    ds = str(day)
    if len(ds) == 1: ds = "0" + ds

    try:
        open(f"Day {ds} Part 1.py")
    except:
        with open(f"Day {ds} Part 1.py", "w") as f:
            f.write(template.replace("[year]", year).replace("[day]", day))
        with open(f"Day {ds} Part 2.py", "w") as f:
            f.write(template.replace("[year]", year).replace("[day]", day))
    else:
        raise FileExistsError("attempting to overwrite existing file with template")