import tkinter as tk
from tkinter import messagebox
import json
import os

TODO_FILE = 'todo.json'

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task():
    task = task_entry.get()
    if task:
        tasks = load_tasks()
        tasks.append({'task': task, 'completed': False})
        save_tasks(tasks)
        update_task_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def update_task():
    try:
        index = task_listbox.curselection()[0]
        new_task = task_entry.get()
        tasks = load_tasks()
        tasks[index]['task'] = new_task
        save_tasks(tasks)
        update_task_listbox()
        task_entry.delete(0, tk.END)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to update.")

def complete_task():
    try:
        index = task_listbox.curselection()[0]
        tasks = load_tasks()
        tasks[index]['completed'] = True
        save_tasks(tasks)
        update_task_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

def delete_task():
    try:
        index = task_listbox.curselection()[0]
        tasks = load_tasks()
        task = tasks.pop(index)
        save_tasks(tasks)
        update_task_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def update_task_listbox():
    tasks = load_tasks()
    task_listbox.delete(0, tk.END)
    for idx, task in enumerate(tasks):
        status = 'Done' if task['completed'] else 'Pending'
        task_listbox.insert(tk.END, f"{idx + 1}. {task['task']} [{status}]")

app = tk.Tk()
app.title("To-Do List Application")

frame = tk.Frame(app)
frame.pack(pady=10)

task_entry = tk.Entry(frame, width=50)
task_entry.pack(side=tk.LEFT, padx=10)

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)

task_listbox = tk.Listbox(app, width=70, height=10)
task_listbox.pack(pady=10)

button_frame = tk.Frame(app)
button_frame.pack(pady=10)

update_button = tk.Button(button_frame, text="Update Task", command=update_task)
update_button.pack(side=tk.LEFT, padx=10)

complete_button = tk.Button(button_frame, text="Complete Task", command=complete_task)
complete_button.pack(side=tk.LEFT, padx=10)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=10)

update_task_listbox()

app.mainloop()
