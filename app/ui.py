import tkinter as tk
from tkinter import messagebox

class KarmaTrackApp:
    def __init__(self, root):
        self.root = root
        self.root.title("KarmaTrack - Task Manager")

        # Create a 2x2 matrix grid of tasks
        self.create_grid()

    def create_grid(self):
        task_labels = ['Important & Urgent', 'Important & Not Urgent',
                       'Not Important & Urgent', 'Not Important & Not Urgent']
        colors = ['red', 'orange', 'yellow', 'green']
        
        for i, (label, color) in enumerate(zip(task_labels, colors)):
            row = i // 2
            col = i % 2
            frame = tk.Frame(self.root, width=200, height=100, bg=color)
            frame.grid(row=row, column=col, padx=10, pady=10)
            tk.Label(frame, text=label, bg=color).pack(padx=5, pady=5)

        # Button to add tasks
        add_task_btn = tk.Button(self.root, text="Add Task", command=self.add_task)
        add_task_btn.grid(row=2, column=0, columnspan=2, pady=20)

    def add_task(self):
        messagebox.showinfo("Task Addition", "Feature to add tasks coming soon!")
