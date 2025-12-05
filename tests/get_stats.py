import json
from glob import glob
import os
from os.path import join

script_path = os.path.realpath(__file__)
script_directory = os.path.dirname(script_path)
print(f"The directory of the current script is: {script_directory}")

folder = join(script_directory, "../data/notebooks")  # change to your folder path if needed

json_files = glob(os.path.join(folder, "flag-*.json"))

total_insights_count = 0
total_plots_count = 0
for jf in sorted(json_files):
    with open(jf, "r") as f:
        data = json.load(f)

    # Handle both "insight_list" and "insights_list" just in case
    insights = data.get("insight_list") or data.get("insights_list") or []
    insights_count = len(insights)

    plots_count = sum(
        1
        for item in insights
        if isinstance(item, dict) and "plot" in item
    )

    total_insights_count += insights_count
    total_plots_count += plots_count

    print(f"{os.path.basename(jf)}, insight_list length = {insights_count}, number with 'plot' key = {plots_count}")


print(f"total insights count = {total_insights_count}, total plots count = {total_plots_count}")