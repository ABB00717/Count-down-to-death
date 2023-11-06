import tkinter as tk
from tkinter import ttk
import datetime

def calculate_time_left(birthdate, gender, label):
    now = datetime.datetime.now()
    life_expectancy = 76.0 if gender == 'Female' else 70.8  # Average life expectancy data
    age = now - birthdate
    age_in_years = age.total_seconds() / (365.25 * 24 * 60 * 60)
    time_left = life_expectancy - age_in_years
    if time_left < 0:
        label.config(text="你已超過平均預期壽命！")
    else:
        label.config(text=f"根據平均壽命，你還有{time_left:.8f}年會死!")
    label.after(1000, calculate_time_left, birthdate, gender, label)

def on_calculate_clicked():
    birthdate_str = date_entry.get()
    gender = gender_var.get()
    try:
        birthdate = datetime.datetime.strptime(birthdate_str, '%Y-%m-%d')
        calculate_time_left(birthdate, gender, time_left_label)
    except ValueError:
        time_left_label.config(text="請按照YYYY-MM-DD的格式輸入日期。")

app = tk.Tk()
app.title('死亡倒數計時器')

gender_var = tk.StringVar(value='Male')

ttk.Label(app, text='請輸入你的出生日期 (YYYY-MM-DD):').pack(padx=10, pady=5)
date_entry = ttk.Entry(app)
date_entry.pack(padx=10, pady=5)

ttk.Label(app, text='選擇性別:').pack(padx=10, pady=5)
ttk.Radiobutton(app, text='男性', variable=gender_var, value='Male').pack()
ttk.Radiobutton(app, text='女性', variable=gender_var, value='Female').pack()

time_left_label = ttk.Label(app, text="讓我看看你的出生和性別。")
time_left_label.pack(padx=10, pady=5)

calculate_button = ttk.Button(app, text='計算剩餘時間', command=on_calculate_clicked)
calculate_button.pack(padx=10, pady=5)

app.mainloop()
