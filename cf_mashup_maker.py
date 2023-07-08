import codeforces_api as cf
import json
from src.utils import *
import src.data_helper as data_helper
import src.config as config
import src.update as update
import src.mashup as mashup

cf_api = cf.CodeforcesApi()

try:
    with open("data/solved.json", "r") as f:
        json_object = json.load(f)

        solved = set(json_object["problems"])
        last_updated = json_object["last_updated"]
except:
    solved = set()
    last_updated = "Never"

def options():
    print()
    print("1. Make a new mashup.")
    print(f"2. Update attempted problems list. (slow) [last updated: {last_updated}]")
    print("3. Update config.")
    print("4. Quit.")
    print()
    return int(input("Enter operation number: "))

def choose_option():
    while True:
        x = options()
        line()

        if x not in range(1, 5):
            print("Please enter a valid number.")
            continue

        return x

def update_attempted():
    global last_updated

    solved = update.update_solved_problems(cf_api)
    last_updated = "Now"
    print(f"Problems have been updated successfully. (total attempted: {len(solved)})")
    line()

def make_mashup():
    mashup_problems = mashup.pick_problems(cf_api, solved)

    line()
    print("Problems list:")
    for i, problem in enumerate(mashup_problems):
        print(i + 1, problem.name)
    line()

def configure():
    config.update_config()
    line()

def first_run():
    configure()
    update_attempted()

data_helper.load(first_run)

while True:
    x = choose_option()

    if x == 1:
        make_mashup()
    elif x == 2:
        update_attempted()
    elif x == 3:
        configure()
    elif x == 4:
        quit()