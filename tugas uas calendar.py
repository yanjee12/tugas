import calendar
import tkinter as tk
from tkinter import ttk

# Fungsi untuk menampilkan kalender
def show_calendar():
    try:
        year = int(year_entry.get())
        month = int(month_combobox.get())
        
        # Menghasilkan kalender bulanan
        cal = calendar.TextCalendar()
        cal_output = cal.formatmonth(year, month)
        
        # Menampilkan kalender di Text widget
        calendar_text.delete(1.0, tk.END)
        calendar_text.insert(tk.END, cal_output)
    except ValueError:
        calendar_text.delete(1.0, tk.END)
        calendar_text.insert(tk.END, "Harap masukkan tahun yang valid.")

# Membuat jendela utama
root = tk.Tk()
root.title("Program Kalender")

# Frame untuk input bulan dan tahun
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky="W")

# Label dan input tahun
ttk.Label(frame, text="Tahun:").grid(row=0, column=0, padx=5, pady=5)
year_entry = ttk.Entry(frame, width=10)
year_entry.grid(row=0, column=1, padx=5, pady=5)

# Label dan combobox untuk bulan
ttk.Label(frame, text="Bulan:").grid(row=0, column=2, padx=5, pady=5)
month_combobox = ttk.Combobox(frame, width=10, state="readonly")
month_combobox["values"] = [
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"
]
month_combobox.current(0)
month_combobox.grid(row=0, column=3, padx=5, pady=5)

# Tombol untuk menampilkan kalender
show_button = ttk.Button(frame, text="Tampilkan Kalender", command=show_calendar)
show_button.grid(row=0, column=4, padx=5, pady=5)

# Text widget untuk menampilkan kalender
calendar_text = tk.Text(root, width=30, height=10, wrap="none", font=("Courier", 10))
calendar_text.grid(row=1, column=0, padx=10, pady=10)

# Menjalankan aplikasi
root.mainloop()
