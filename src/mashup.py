from src.utils import *
from collections import defaultdict
import src.data_helper as data_helper
import random

exclude = [1002, 683, 64, 1571, 188, 1001]

def pick_problems(cf_api, solved):
    mashup = []
    problems = {}
    total = 0

    included_tags = []
    excluded_tags = []
    
    print("Enter included tags combined by OR (leave empty to ignore):")
    while True:
        tag = input(f"{len(included_tags) + 1}> ")
        if tag == "": break
        included_tags.append(tag)
    
    print()
    print("Enter excluded tags (leave empty to ignore):")
    while True:
        tag = input(f"{len(excluded_tags) + 1}> ")
        if tag == "": break
        excluded_tags.append(tag)

    line()

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
        
        if any(tag in problem.tags for tag in excluded_tags):
            continue
        
        if len(included_tags) and not any(tag in problem.tags for tag in included_tags):
            continue

        if code not in solved and rating in problems.keys():
            new = Problem()
            new.name = name
            new.rating = rating
            new.code = code
            candidates[rating].append(new)

    line()
    for rating, count in sorted(problems.items()):
        while (len(candidates[rating]) < count):
            print(f"ERROR: there is no enough unsolved {rating} problems.")
            count = int(input(f"How many {rating} rated problems (max: {len(candidates[rating])}): "))
            print()
        
        mashup.extend(random.sample(candidates[rating], count))
    

    if not data_helper.data.sorted_by_difficulty:
        random.shuffle(mashup)
    
    out_link = input("Save as links? [Y/N]: ").lower() == "y"
    with open("mashup.txt", "w") as f:
        link = "https://codeforces.com/problemset/problem/"
        if out_link:
            f.write('\n'.join([link + x.code.replace("-", "/") for x in mashup]))
        else:
            f.write('\n'.join([x.code for x in mashup]))
        print(f"Saved the mashup to {f.name}")
    
    return mashup