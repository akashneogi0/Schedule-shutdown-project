import os
import tkinter as tk
from tkinter import messagebox

# Global variable to store if a shutdown or restart is scheduled
is_scheduled = False
scheduled_command = ""

def schedule_shutdown_or_restart():
    global is_scheduled, scheduled_command
    
    try:
        hours = int(entry_hours.get())
        minutes = int(entry_minutes.get())
        seconds = int(entry_seconds.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for time.")
        return
    
    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    action = var_action.get()
    
    # If a shutdown or restart is already scheduled, prompt user for confirmation
    if is_scheduled:
        messagebox.showinfo("Already Scheduled", "You already have a scheduled shutdown or restart. Please cancel it first.")
        return

    if action == "shutdown":
        confirm = messagebox.askyesno("Confirm", f"Do you want to shut down in {hours} hours, {minutes} minutes, and {seconds} seconds?")
        if confirm:
            is_scheduled = True
            scheduled_command = f"shutdown /s /f /t {total_seconds}"
            os.system(scheduled_command)
    elif action == "restart":
        confirm = messagebox.askyesno("Confirm", f"Do you want to restart in {hours} hours, {minutes} minutes, and {seconds} seconds?")
        if confirm:
            is_scheduled = True
            scheduled_command = f"shutdown /r /f /t {total_seconds}"
            os.system(scheduled_command)
    else:
        messagebox.showerror("Error", "Please select an action (Shutdown or Restart).")

# Function to cancel the scheduled action
def cancel_scheduled_action():
    global is_scheduled, scheduled_command
    
    if is_scheduled:
        # Abort the shutdown or restart command
        os.system("shutdown /a")
        is_scheduled = False
        scheduled_command = ""
        messagebox.showinfo("Cancelled", "The scheduled action has been cancelled.")
    else:
        messagebox.showinfo("No Action", "No scheduled shutdown or restart to cancel.")

# Create the main window
root = tk.Tk()
root.title("Shutdown/Restart Scheduler")

# Create the action selection (Shutdown or Restart)
var_action = tk.StringVar(value="shutdown")
radio_shutdown = tk.Radiobutton(root, text="Shutdown", variable=var_action, value="shutdown")
radio_restart = tk.Radiobutton(root, text="Restart", variable=var_action, value="restart")
radio_shutdown.grid(row=0, column=0, padx=10, pady=5)
radio_restart.grid(row=0, column=1, padx=10, pady=5)

# Time input labels and fields
label_hours = tk.Label(root, text="Hours:")
label_minutes = tk.Label(root, text="Minutes:")
label_seconds = tk.Label(root, text="Seconds:")
entry_hours = tk.Entry(root)
entry_minutes = tk.Entry(root)
entry_seconds = tk.Entry(root)

label_hours.grid(row=1, column=0, padx=10, pady=5)
entry_hours.grid(row=1, column=1, padx=10, pady=5)
label_minutes.grid(row=2, column=0, padx=10, pady=5)
entry_minutes.grid(row=2, column=1, padx=10, pady=5)
label_seconds.grid(row=3, column=0, padx=10, pady=5)
entry_seconds.grid(row=3, column=1, padx=10, pady=5)

# Buttons to schedule or cancel shutdown/restart
button_schedule = tk.Button(root, text="Schedule", command=schedule_shutdown_or_restart)
button_cancel = tk.Button(root, text="Cancel Scheduled", command=cancel_scheduled_action)

button_schedule.grid(row=4, column=0, padx=10, pady=20)
button_cancel.grid(row=4, column=1, padx=10, pady=20)

# Start the GUI
root.mainloop()
