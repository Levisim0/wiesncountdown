import tkinter as tk
from datetime import datetime

oktoberfest_date = datetime(2025, 9, 20)

today = datetime.now()
days_left = (oktoberfest_date - today).days

root = tk.Tk()
root.title("Oktoberfest Countdown")
root.resizable(False, False)
root.attributes("-topmost", True)

window_width = 320
window_height = 120

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

if days_left > 0:
    message = f"🍺 Noch {days_left} Tage bis zur Wiesn!"
else:
    message = "🎉 Wiesn-Zeit! 🍺 O'zapft is!"

label = tk.Label(root, text=message, font=("Arial", 12))
label.pack(pady=20)

ok_button = tk.Button(root, text="OK", width=10, command=root.destroy)
ok_button.pack()

root.mainloop()
