import tkinter as tk
from tkinter import messagebox, simpledialog
from database import add_task, get_tasks, update_task_status, get_karma_points
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class KarmaTrackApp:
    def __init__(self, master):
        self.master = master
        self.master.title("KarmaTrack - Eisenhower Matrix")

        self.title_label = tk.Label(master, text="Eisenhower Matrix Task Manager", font=("Helvetica", 18, "bold"))
        self.title_label.pack(pady=10)

        self.matrix_frame = tk.Frame(master)
        self.matrix_frame.pack(fill=tk.BOTH, expand=True)

        self.create_matrix()

        self.add_task_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        self.visualize_button = tk.Button(master, text="Visualize Karma Points", command=self.visualize_karma_points)
        self.visualize_button.pack(pady=5)

    def create_matrix(self):
        labels = [
            ("Urgent & Important", "red"),
            ("Not Urgent & Important", "orange"),
            ("Urgent & Not Important", "yellow"),
            ("Not Urgent & Not Important", "green")
        ]
        self.matrix = {}

        for i, (text, color) in enumerate(labels):
            frame = tk.Frame(self.matrix_frame, width=400, height=200, bg=color)
            frame.grid(row=i//2, column=i%2, padx=10, pady=10, sticky="nsew")
            label = tk.Label(frame, text=text, bg=color, font=("Helvetica", 12, "bold"))
            label.pack(pady=5)
            self.matrix[text] = frame

        self.load_tasks()

    def load_tasks(self):
        tasks = get_tasks()
        for task in tasks:
            text = f"Task: {task[1]} (Completed: {task[2]})"
            urgency_importance = task[3]  # Matrix quadrant
            label = tk.Label(self.matrix[urgency_importance], text=text, bg=self.matrix[urgency_importance].cget("bg"))
            label.pack()

    def add_task(self):
        task_name = simpledialog.askstring("Input", "Enter the task:")
        if task_name:
            urgency_importance = simpledialog.askstring(
                "Task Category", 
                "Where should the task be placed? (Urgent & Important, Not Urgent & Important, Urgent & Not Important, Not Urgent & Not Important)"
            )
            if urgency_importance in self.matrix:
                add_task(task_name, urgency_importance)
                self.load_tasks()

    def visualize_karma_points(self):
        data = get_karma_points()
        dates = [row[0] for row in data]
        points = [row[1] for row in data]

        fig, ax = plt.subplots()
        ax.plot(dates, points, marker="o")
        ax.set_title("Karma Points Over Time")
        ax.set_xlabel("Date")
        ax.set_ylabel("Karma Points")

        canvas = FigureCanvasTkAgg(fig, master=self.master)
        canvas.get_tk_widget().pack()
        canvas.draw()
