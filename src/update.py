import json, time, datetime
import src.data_helper as data_helper
from alive_progress import alive_bar

def update_solved_problems(cf_api):
    print()

    if len(data_helper.data.handles):
        print(f"Getting attempted problems of {len(data_helper.data.handles)} users.")
    else:
        print("No handles in the list.")
        return []

    solved = set()

    print()
    with alive_bar(len(data_helper.data.handles)) as bar:
        for i, handle in enumerate(data_helper.data.handles):
            time.sleep(1) # "CF API may be requested at most 1 time per two seconds."

            # print(f"{i + 1}/{len(data_helper.data.handles)}")
            try:
                for submisson in cf_api.user_status(handle):
                    solved.add(f"{submisson.problem.contest_id}-{submisson.problem.index}")
            except:
                print(f"Can't find {handle}.")

            bar()
    print()

    with open(f"data/{data_helper.data.config_name}/solved.json", "w") as f:
        json.dump({"last_updated": datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S") ,"problems":list(solved)}, f, indent=2)
        print(f"Attempted problems was saved to {f.name}")
    
    return solved