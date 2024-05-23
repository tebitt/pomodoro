import tkinter as tk
from tkinter import ttk
import sys
import json

def run_settings_window(session_duration, session_break, number_of_sessions):
    def save_settings():
        try:
            new_session_duration = int(session_duration_entry.get())
            new_break_duration = int(break_duration_entry.get())
            new_number_of_sessions = int(number_of_sessions_entry.get())

            if new_session_duration > 0 and new_break_duration > 0 and new_number_of_sessions > 0:
                settings = {
                    "session_duration": new_session_duration,
                    "session_break": new_break_duration,
                    "number_of_sessions": new_number_of_sessions
                }
                with open("settings.json", "w") as f:
                    json.dump(settings, f)
                window.destroy()
            else:
                error_label.config(text="Please enter positive numbers.")
        except ValueError:
            error_label.config(text="Invalid input. Please enter valid numbers.")

    window = tk.Tk()
    window.title("Settings")

    ttk.Label(window, text="Session Duration (minutes):").grid(column=0, row=0, padx=10, pady=5, sticky=tk.W)
    session_duration_entry = ttk.Entry(window)
    session_duration_entry.insert(0, str(session_duration))
    session_duration_entry.grid(column=1, row=0, padx=10, pady=5)

    ttk.Label(window, text="Break Duration (minutes):").grid(column=0, row=1, padx=10, pady=5, sticky=tk.W)
    break_duration_entry = ttk.Entry(window)
    break_duration_entry.insert(0, str(session_break))
    break_duration_entry.grid(column=1, row=1, padx=10, pady=5)

    ttk.Label(window, text="Number of Sessions:").grid(column=0, row=2, padx=10, pady=5, sticky=tk.W)
    number_of_sessions_entry = ttk.Entry(window)
    number_of_sessions_entry.insert(0, str(number_of_sessions))
    number_of_sessions_entry.grid(column=1, row=2, padx=10, pady=5)

    save_button = ttk.Button(window, text="Save", command=save_settings)
    save_button.grid(column=0, row=3, columnspan=2, pady=10)

    error_label = ttk.Label(window, text="", foreground="red")
    error_label.grid(column=0, row=4, columnspan=2)

    window.mainloop()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python settings_window.py <session_duration> <session_break> <number_of_sessions>")
        sys.exit(1)

    session_duration = int(sys.argv[1])
    session_break = int(sys.argv[2])
    number_of_sessions = int(sys.argv[3])

    run_settings_window(session_duration, session_break, number_of_sessions)
