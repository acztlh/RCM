import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# Define the main tasks and sub-tasks with durations (days) and buffer times
tasks = {
    "Market Research & Analysis": {"duration": 30, "buffer": 5},
    "Concept Development": {"duration": 20, "buffer": 3},
    "Design & Prototyping": {"duration": 40, "buffer": 6},
    "Sourcing Materials & Partnerships": {"duration": 25, "buffer": 4},
    "Financial Planning & Budgeting": {"duration": 15, "buffer": 2},
    "Permits & Regulatory Compliance": {"duration": 35, "buffer": 5},
    "Construction Planning": {"duration": 45, "buffer": 7},
    "Marketing Strategy & Outreach": {"duration": 20, "buffer": 3},
    "Sales & Distribution Setup": {"duration": 30, "buffer": 5},
    "Launch Preparation": {"duration": 25, "buffer": 4},
    "Project Evaluation & Feedback": {"duration": 10, "buffer": 2}
}

# Start date of the project
start_date = datetime(2024, 11, 10)

# Generate the Gantt chart data
gantt_data = {
    "Task": [],
    "Start Date": [],
    "End Date": [],
    "End Date with Buffer": []
}

current_date = start_date

# Calculate the start and end dates for each task, including buffer time
for task, details in tasks.items():
    duration = details["duration"]
    buffer = details["buffer"]
    
    # Append task details to the Gantt chart data
    gantt_data["Task"].append(task)
    gantt_data["Start Date"].append(current_date)
    gantt_data["End Date"].append(current_date + timedelta(days=duration))
    gantt_data["End Date with Buffer"].append(current_date + timedelta(days=duration + buffer))
    
    # Move the start date for the next task
    current_date += timedelta(days=duration + buffer)

# Convert gantt_data into a DataFrame
gantt_df = pd.DataFrame(gantt_data)

# Plotting the Gantt chart
fig, ax = plt.subplots(figsize=(12, 8))

for i, (task, start, end, end_buffer) in enumerate(zip(gantt_df["Task"], gantt_df["Start Date"], gantt_df["End Date"], gantt_df["End Date with Buffer"])):
    # Task duration without buffer
    ax.barh(task, (end - start).days, left=start, color='skyblue', edgecolor='black', label="Task Duration" if i == 0 else "")
    # Buffer time
    ax.barh(task, (end_buffer - end).days, left=end, color='orange', edgecolor='black', label="Buffer Time" if i == 0 else "")

# Formatting the chart
ax.set_xlabel("Timeline")
ax.set_ylabel("Project Tasks")
ax.set_title("Gantt Chart with Buffer Time for Each Task")
ax.xaxis_date()
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
plt.xticks(rotation=45)
plt.legend(loc="upper right")

plt.tight_layout()
plt.show()