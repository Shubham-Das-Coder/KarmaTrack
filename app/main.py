import sys
import os
import tkinter as tk
from ui import KarmaTrackApp
from database import initialize_db, check_new_day, calculate_previous_day_karma

def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def main():
    # Ensure the 'db' folder exists
    db_folder = 'db'
    if not os.path.exists(db_folder):
        os.makedirs(db_folder)

    # Initialize the database
    initialize_db()

    # Check if a new day has started and handle karma calculations
    if check_new_day():
        calculate_previous_day_karma()

    # Create the main application window with larger size
    root = tk.Tk()
    root.geometry("800x600")  # Set a larger window size
    app = KarmaTrackApp(root)

    # Set the application icon using resource path
    icon_path = resource_path('assets/icon.ico')
    root.iconbitmap(icon_path)
    
    # Start the main application loop
    root.mainloop()

if __name__ == "__main__":
    main()
