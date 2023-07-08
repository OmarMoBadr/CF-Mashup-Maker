import json, os

data_dict = {}
data = None
filename = "data/data.json"

class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)

def update(save=False):
    global data

    data = Struct(**data_dict)
    
    if save:
        with open(filename, "w") as f:
            json.dump(data_dict, f, indent=2)

def load(first_run):
    global data_dict

    if os.path.exists(filename):
        with open(filename, "r") as f:
            data_dict = json.load(f)
        
        update()
    else:
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        data_dict = {}
        data_dict["min_problem_rating"] = 800
        data_dict["max_problem_rating"] = 3500
        data_dict["sorted_by_difficulty"] = True
        data_dict["handles"] = []

        update()

        first_run()