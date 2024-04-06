import src.data_helper as data_helper

def update_config():
    data_helper.data_dict["min_problem_rating"] = int(input(f"Enter min problem rating (cur: {data_helper.data.min_problem_rating}): "))
    data_helper.data_dict["max_problem_rating"] = int(input(f"Enter max problem rating (cur: {data_helper.data.max_problem_rating}): "))
    
    data_helper.data_dict["min_contest_id"] = int(input(f"Enter min contest id (cur: {data_helper.data.min_contest_id}): "))
    data_helper.data_dict["max_contest_id"] = int(input(f"Enter max contest id (cur: {data_helper.data.max_contest_id}): "))
    
    # -------------------------------
    print()
    x = input(f"Mashup problems sorted by difficulty (cur: {data_helper.data.sorted_by_difficulty}) [Y/N]: ")
    
    data_helper.data_dict["sorted_by_difficulty"] = x.lower() == "y"

    # ------------------------------
    if len(data_helper.data.handles):
        print()
        x = input(f"Clear users handles list? (cur: {len(data_helper.data.handles)} users) [Y/N]: ")
        
        if x.lower() == "y":
            data_helper.data_dict["handles"] = []

    # ------------------------------
    x = input(f"Add new handles? (cur: {len(data_helper.data.handles)} handles) [Y/N]: ")
    
    if x.lower() == "y":
        print()
        print("Enter handles one per line (leave empty to finish).")
        idx = len(data_helper.data_dict["handles"]) + 1

        while True:
            handle = input(f"{idx} > ")
            if handle == "": break

            data_helper.data_dict["handles"].append(handle)
            idx += 1
    
    # ------------------------------
    data_helper.update(save=True)

    print("Config was saved successfully.\n")
