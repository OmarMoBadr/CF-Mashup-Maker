from src.utils import *
from collections import defaultdict
import src.data_helper as data_helper
import random

exclude = [1002, 683, 64, 1571, 188, 1001]

def pick_problems(cf_api, solved):
    mashup = []
    problems = {}
    total = 0

    for i in range(data_helper.data.min_problem_rating, data_helper.data.max_problem_rating + 1, 100):
        n = int(input(f"How many {i} rated problems: "))
        problems[i] = n
        total += n

    line()

    for k, v in problems.items():
        if v:
            print(f"{k}: {v} problems.")

    print(f"Total of {total} problem.")

    problemset = cf_api.problemset_problems()

    candidates = defaultdict(list)
    for problem in problemset["problems"]:
        name, rating = problem.name, problem.rating
        code = f"{problem.contest_id}-{problem.index}"
        
        min_id = data_helper.data.min_contest_id
        temp = data_helper.data.max_contest_id
        max_id = temp if temp != -1 else int(1e8)
        if problem.contest_id <= min_id or problem.contest_id >= max_id or problem.contest_id in exclude:
            continue

        if "*special" in problem.tags:
            continue

        if code not in solved and rating in problems.keys():
            new = Problem()
            new.name = name
            new.rating = rating
            new.code = code
            candidates[rating].append(new)

    for rating, count in sorted(problems.items()):
        while (len(candidates[rating]) < count):
            print(f"ERROR: there is no enough unsolved {rating} problems\n")
            count = int(input(f"How many {i} rated problems (max: {len(candidates[rating])}): "))
        
        mashup.extend(random.sample(candidates[rating], count))
    

    if not data_helper.data.sorted_by_difficulty:
        random.shuffle(mashup)

    line()

    with open("mashup.txt", "w") as f:
        f.write('\n'.join([x.code for x in mashup]))
        print(f"Saved the mashup to {f.name}")
    
    return mashup