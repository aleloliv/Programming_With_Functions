# 1. Project Initialization
#    1.1 Create New Project
#    1.2 Define Project Scope
#    1.3 Assign Project Due Date
#    1.4 Identify Project Owner
#    1.5 Determine Project Type
#    1.6 Specify Allowed File Types

# 2. Task Management
#    2.1 Create New Task
#        2.1.1 Describe Task
#        2.1.2 Assign Task to Designer
#        2.1.3 Estimate Task Duration
#    2.2 Task Tracking
#        2.2.1 Record Task Progress
#        2.2.2 Monitor Task Due Dates
#    2.3 Time Management
#        2.3.1 Accumulate Task Times
#        2.3.2 Compare Total Task Time to Project Due Date

# 3. Reporting
#    3.1 Generate Project Report
#        3.1.1 Include Project Details
#        3.1.2 Summarize Task Information
#        3.1.3 Analyze Time vs. Due Date

# 4. Project Closure
#    4.1 Confirm Completion of All Tasks
#    4.2 Validate Project Deliverables
#    4.3 Evaluate Project Success
#    4.4 Archive Project Information

import tkinter as tk
from tkinter import ttk  # Import the ttk module for themed widgets

def create_new_project():
    print("Create New Project function called")

def select_project():
    print("Select Project function called")

def on_combobox_select(event):
    selected_project_type = project_type_combobox.get()
    print(f"Selected Project Type: {selected_project_type}")

window = tk.Tk()
window.title("Project Manager")

# Frame using pack manager
frame1 = tk.Frame(window)
frame1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Frame using grid manager
frame2 = tk.Frame(window)
frame2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

button1 = tk.Button(frame2, text="Create New Project", command=create_new_project)
button1.grid(row=0, column=0, padx=(0, 10), pady=(20, 0))

button2 = tk.Button(frame2, text="Select Project", command=select_project)
button2.grid(row=0, column=1, pady=(20, 0))

# Combobox for project types
project_types = ["Type A", "Type B", "Type C"]  # Replace with your actual project types
project_type_combobox = ttk.Combobox(frame2, values=project_types)
project_type_combobox.set("Select Project Type")  # Default text
project_type_combobox.grid(row=1, column=0, columnspan=2, pady=(10, 0))
project_type_combobox.bind("<<ComboboxSelected>>", on_combobox_select)

window.geometry("800x600")  # Adjust the width and height as needed

window.mainloop()
