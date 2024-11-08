from flask import Flask, render_template, request, jsonify
import pandas as pd
import plotly.express as px
import plotly.io as pio
from datetime import datetime, timedelta

app = Flask(__name__)

tasks = [
    {"name": "Project Initiation", "start": "2023-10-01", "duration": 10, "subtasks": [
        {"name": "Define goals and objectives", "duration": 2},
        {"name": "Analyze stakeholders and investors", "duration": 2},
        {"name": "Outline project scope and work plan", "duration": 3},
        {"name": "Check legal requirements and permits", "duration": 3}
    ]},
    {"name": "Project Planning", "start": "2023-10-11", "duration": 10, "subtasks": [
        {"name": "Plan budget and resources", "duration": 3},
        {"name": "Assess risks and create a management plan", "duration": 3},
        {"name": "Set timelines and milestones", "duration": 2},
        {"name": "Define quality standards", "duration": 2}
    ]},
    {"name": "Communication and Reporting", "start": "2023-10-21", "duration": 10, "subtasks": [
        {"name": "Establish a communication plan", "duration": 3},
        {"name": "Set up reporting and checkpoints", "duration": 3},
        {"name": "Regularly inform stakeholders", "duration": 4}
    ]},
    # Add other main tasks and subtasks similarly...
]

def create_gantt_data():
    gantt_data = []
    for task in tasks:
        start_date = datetime.strptime(task["start"], "%Y-%m-%d")
        for subtask in task["subtasks"]:
            gantt_data.append({
                "Task": subtask["name"],
                "Start": start_date,
                "Finish": start_date + timedelta(days=subtask["duration"]),
                "Duration": subtask["duration"],
                "Buffer": 0,  # Placeholder for buffer time
                "Earliest Finish": start_date + timedelta(days=subtask["duration"]),
                "Latest Finish": start_date + timedelta(days=subtask["duration"]),
                "Affects Other Tasks": "No"  # Placeholder for task dependencies
            })
            start_date += timedelta(days=subtask["duration"])  # Update start date for next subtask
    return pd.DataFrame(gantt_data)

@app.route('/')
def index():
    gantt_df = create_gantt_data()
    fig = px.timeline(gantt_df, x_start="Start", x_end="Finish", y="Task", title="Project Gantt Chart")
    fig.update_traces(hoverinfo="text", text=gantt_df.apply(lambda row: f"{row['Task']}<br>Duration: {row['Duration']} days<br>Buffer: {row['Buffer']} days<br>Earliest Finish: {row['Earliest Finish']}<br>Latest Finish: {row['Latest Finish']}<br>Affects Other Tasks: {row['Affects Other Tasks']}", axis=1))
    pio.write_html(fig, 'templates/gantt_chart.html')
    return render_template('gantt_chart.html')

if __name__ == '__main__':
    app.run(debug=True)
