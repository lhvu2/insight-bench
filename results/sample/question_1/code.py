import pandas as pd
from datetime import datetime
from insightbench.tools import plot_lines, save_json, fix_fnames

# Load the dataset
file_path = "/data/lhvu/projects/insight-bench/data/notebooks/csvs/flag-1.csv"
df = pd.read_csv(file_path)

# Convert 'opened_at' and 'closed_at' columns to datetime for calculations
df['opened_at'] = pd.to_datetime(df['opened_at'])
df['closed_at'] = pd.to_datetime(df['closed_at'])

# Calculate resolution time in hours
df['resolution_time_hours'] = (df['closed_at'] - df['opened_at']).dt.total_seconds() / 3600

# Group by 'closed_at' date (daily resolution) and calculate average resolution time
df['closed_date'] = df['closed_at'].dt.date
avg_resolution_time = df.groupby('closed_date')['resolution_time_hours'].mean().reset_index()

# Rename columns for clarity
avg_resolution_time.columns = ['date', 'avg_resolution_time']

# Plot the average resolution time over time
plot_lines(
    df=avg_resolution_time,
    x_column='date',
    plot_columns=['avg_resolution_time'],
    plot_title='Average Resolution Time Over Time'
)

# Save stats as a JSON file
stats_data = {
    "name": "Average Resolution Time Stats",
    "description": "Statistics of average resolution time for incidents over time.",
    "value": avg_resolution_time.describe().to_dict()
}
save_json(stats_data, ftype="stat")

# Save x-axis data as a JSON file
x_axis_data = {
    "name": "X-axis Data",
    "description": "Dates representing the x-axis of the plot.",
    "value": avg_resolution_time['date'].astype(str).tolist()[:50]
}
save_json(x_axis_data, ftype="x_axis")

# Save y-axis data as a JSON file
y_axis_data = {
    "name": "Y-axis Data",
    "description": "Average resolution times representing the y-axis of the plot.",
    "value": avg_resolution_time['avg_resolution_time'].tolist()[:50]
}
save_json(y_axis_data, ftype="y_axis")

# Rename plot and stat files
fix_fnames()