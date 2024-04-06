import json, os

data_dict = {}
data = None
path = ""

defaults = {
    "min_problem_rating": 800,
    "max_problem_rating": 3500,
    "sorted_by_difficulty": True,
    "handles": [],
    "config_name": "default",
    "min_contest_id": 1,
    "max_contest_id": -1
}

class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)

def update(save=False):
    global data
    fix_missing()

    data = Struct(**data_dict)
    
    if save:
        with open(path, "w") as f:
            json.dump(data_dict, f, indent=2)

def load(first_run, config_name):
    global data_dict, path
    path = f"data/{config_name}/data.json"

    if os.path.exists(path):
        with open(path, "r") as f:
            data_dict = json.load(f)
        
        update()
    else:
        os.makedirs(os.path.dirname(path), exist_ok=True)

        data_dict = {}
        data_dict["config_name"] = config_name

        update()

        first_run()

def fix_missing():
    for key, val in defaults.items():
        if key not in data_dict:
            data_dict[key] = val