import pandas as pd
from insightbench.tools import plot_countplot, save_json, fix_fnames

# Load the dataset
# Path to the dataset
data_path = "/data/lhvu/projects/insight-bench/data/notebooks/csvs/flag-1.csv"
# Read the CSV file into a DataFrame
df = pd.read_csv(data_path)

# Plot the distribution of incidents across categories and assignment groups
# Combine 'category' and 'assignment_group' into a single column for plotting
df['category_assignment_group'] = df['category'] + " - " + df['assignment_group']

# Generate the count plot
plot_column = 'category_assignment_group'
plot_title = 'Distribution of Incidents Across Categories and Assignment Groups'
plot_countplot(df, plot_column, plot_title)

# Save stats data as JSON
stats_data = {
    "name": "Incident Distribution Stats",
    "description": "Counts of incidents across different categories and assignment groups.",
    "value": df[plot_column].value_counts().to_dict()
}
save_json(stats_data, "stat")

# Save x-axis data as JSON
x_axis_data = {
    "name": "X-axis Data",
    "description": "Unique category and assignment group combinations.",
    "value": df[plot_column].value_counts().index.tolist()[:50]  # Top 50 unique values
}
save_json(x_axis_data, "x_axis")

# Save y-axis data as JSON
y_axis_data = {
    "name": "Y-axis Data",
    "description": "Counts of incidents for each category and assignment group combination.",
    "value": df[plot_column].value_counts().tolist()[:50]  # Top 50 counts
}
save_json(y_axis_data, "y_axis")

# Rename the plot and stat files
fix_fnames()