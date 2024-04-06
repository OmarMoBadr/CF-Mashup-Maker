import json, os

data_dict = {}
data = None
path = ""

class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)

def update(save=False):
    global data

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
        data_dict["min_problem_rating"] = 800
        data_dict["max_problem_rating"] = 3500
        data_dict["sorted_by_difficulty"] = True
        data_dict["handles"] = []
        data_dict["config_name"] = config_name

        update()

        first_run()