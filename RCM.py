from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Placeholder for task data (in a real app, use a database)
tasks = [
    # Example task
    {"id": 1, "name": "Task 1", "duration": 5, "buffer": 2, "dependencies": [], "earliest_start": 0},
    # Add more tasks with attributes
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tasks", methods=["GET", "POST"])
def task_data():
    if request.method == "POST":
        data = request.get_json()
        # Update task data here based on 'data'
    return jsonify(tasks)

if __name__ == "__main__":
    app.run(debug=True)
