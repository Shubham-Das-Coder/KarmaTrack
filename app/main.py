import sys
import os
import tkinter as tk
from ui import KarmaTrackApp
from database import initialize_db, check_new_day, calculate_previous_day_karma

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def main():
    db_folder = 'db'
    if not os.path.exists(db_folder):
        os.makedirs(db_folder)

    initialize_db()

    if check_new_day():
        calculate_previous_day_karma()

    root = tk.Tk()
    root.geometry("900x700")
    app = KarmaTrackApp(root)

    icon_path = resource_path('assets/icon.ico')
    root.iconbitmap(icon_path)
    
    root.mainloop()

if __name__ == "__main__":
    main()
