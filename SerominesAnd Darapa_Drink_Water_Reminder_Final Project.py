from plyer import notification  # Library for displaying desktop notifications
import tkinter as tk  # GUI library
from tkinter import ttk  # Themed Tkinter for better-looking widgets

# Reminder Class
class Reminder:
    def __init__(self, master, interval_seconds, user_name):
        # Initialize reminder with master window, interval, and user name
        self.master = master
        self.interval_seconds = interval_seconds
        self.user_name = user_name
        self.after_id = None  # Identifier for the after method

    def start_reminder(self):
        # Method to start the reminder
        self.notification()  # Display notification
        # Schedule next reminder using the after method, converting seconds to milliseconds
        self.after_id = self.master.after(self.interval_seconds * 1000, self.start_reminder)

    def stop_reminder(self):
        # Method to stop the ongoing reminder
        if self.after_id:
            self.master.after_cancel(self.after_id)  # Cancel the scheduled reminder
            self.after_id = None  # Reset the after_id

    def notification(self):
        # Method to display desktop notification using the plyer library
        notification.notify(
            title=f'Reminder😊!',
            message=f"Hey {self.user_name}, It's water o'clock!💦 Take a moment to hydrate and feel refreshed. Your body will thank you!💦",
            app_icon=r"C:\Users\unbre\OneDrive\Documents\icon.ico",
        )

# Timer Class
class Timer:
    def __init__(self, master):
        # Initialize the Timer class with the master window
        self.master = master
        master.title("Drink Water Reminder")  # Set window title
        self.running = False  # Flag to track if the reminder is running

        # Create GUI elements using ttk for themed widgets
        ttk.Label(master, text="Enter your Nickname:", font=("Cascadia Code", 10)).pack(pady=5)
        self.name_var = tk.StringVar()
        ttk.Entry(master, width=15, textvariable=self.name_var, font=("Cascadia Code", 10)).pack(pady=5)

        ttk.Label(master, text="Remind Me To Drink Water Every", font=("Cascadia Code", 10)).pack(pady=5)
        ttk.Label(master, text="(Hours:Minutes:Seconds)", font=("Cascadia Code", 10)).pack()

        self.time_var = tk.StringVar()
        self.time_entry = ttk.Entry(master, width=7, textvariable=self.time_var, font=("Helvetica", 16), foreground="red")
        self.time_entry.insert(0, "00:00:00")  # Default value
        self.time_entry.pack(pady=5)

        # Configure the Start Reminder button style
        self.master.style = ttk.Style()
        self.master.style.configure('StartButton.TButton',
                                    font=('Consolas', 12),
                                    width=15,
                                    background='Skyblue',
                                    foreground='Blue')

        # Create Start Reminder button with specified style and command
        self.start_button = ttk.Button(master, text="Start Reminder", style='StartButton.TButton', command=self.start_stop)
        self.start_button.pack()

    def start_stop(self):
        # Method to start or stop the reminder based on user input
        if self.running:
            self.running = False
            self.start_button["text"] = "Start Reminder"
            if self.reminder:
                self.reminder.stop_reminder()
        else:
            try:
                # Get input and start the reminder
                time_str = self.time_var.get()
                hours, minutes, seconds = map(int, time_str.split(':'))
                interval_seconds = hours * 3600 + minutes * 60 + seconds
                user_name = self.name_var.get()

                # Create Reminder object and start it
                self.reminder = Reminder(self.master, interval_seconds, user_name)
                self.reminder.start_reminder()
                self.running = True
                self.start_button["text"] = "Stop Reminder"

            except ValueError:
                # Display an error message for invalid input
                tk.messagebox.showerror("Invalid Input", "Please enter a valid time in HH:MM:SS format.")

# Main Section
root = tk.Tk()  #the main window using Tkinter
root.geometry("300x200")  # Set window dimensions
timer = Timer(root)  # Create an instance of the Timer class
root.mainloop()  # Start the Tkinter event loop
