import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from database import add_task, get_tasks, update_task_status

class KarmaTrackApp:
    def __init__(self, master):
        self.master = master
        self.master.title("KarmaTrack")

        # Title Label
        self.title_label = tk.Label(master, text="KarmaTrack Task Manager", font=("Helvetica", 18, "bold"))
        self.title_label.pack(pady=10)

        # Task List Frame
        self.task_frame = tk.Frame(master)
        self.task_frame.pack(fill=tk.BOTH, expand=True)

        # Create Task Listbox
        self.task_listbox = tk.Listbox(self.task_frame, height=10, width=80)
        self.task_listbox.pack(pady=10)

        # Load existing tasks
        self.load_tasks()

        # Add Task Button
        self.add_task_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        # Mark Task Completed Button
        self.complete_task_button = tk.Button(master, text="Mark Task Completed", command=self.mark_task_completed)
        self.complete_task_button.pack(pady=5)

    def load_tasks(self):
        """Load tasks from the database and display them in the listbox."""
        tasks = get_tasks()
        self.task_listbox.delete(0, tk.END)  # Clear existing list
        for task in tasks:
            self.task_listbox.insert(tk.END, f"Task: {task[1]}, Status: {'Completed' if task[2] else 'Pending'}")

    def add_task(self):
        """Add a new task to the database."""
        task_name = simpledialog.askstring("Input", "Enter the task:")
        if task_name:
            add_task(task_name)
            self.load_tasks()  # Reload tasks after adding

    def mark_task_completed(self):
        """Mark the selected task as completed."""
        try:
            selected_task = self.task_listbox.curselection()
            if not selected_task:
                raise IndexError
            task_text = self.task_listbox.get(selected_task)
            task_name = task_text.split(",")[0].replace("Task: ", "").strip()
            update_task_status(task_name, True)
            self.load_tasks()  # Reload tasks after marking as completed
            messagebox.showinfo("Success", f"Task '{task_name}' marked as completed!")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")
