import sys
import os
import tkinter as tk
from datetime import datetime
from ui import KarmaTrackApp
from database import initialize_db, check_new_day, calculate_previous_day_karma

def main():
    # Ensure the 'db' folder exists
    db_folder = 'db'
    if not os.path.exists(db_folder):
        os.makedirs(db_folder)

    # Initialize the database
    initialize_db()

    # Check if a new day has started
    if check_new_day():
        calculate_previous_day_karma()

    # Create the main application window
    root = tk.Tk()
    app = KarmaTrackApp(root)
    
    # Set the application icon using an absolute path
    icon_path = os.path.join(os.path.dirname(__file__), 'assets', 'icon.ico')
    root.iconbitmap(icon_path)
    
    # Start the main application loop
    root.mainloop()

if __name__ == "__main__":
    main()
