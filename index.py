import tkinter as tk
from tkinter import ttk
import datetime

class DeathCountdownApp:
    def __init__(self, root):
        self.root = root
        self.root.title('死亡倒數計時器')
        
        # 生日輸入
        ttk.Label(root, text='請輸入你的出生日期 (YYYY-MM-DD):').pack(padx=10, pady=5)
        self.date_entry = ttk.Entry(root)
        self.date_entry.pack(padx=10, pady=5)
        
        # 性別選擇
        ttk.Label(root, text='選擇性別:').pack(padx=10, pady=5)
        self.gender_var = tk.StringVar(value='Male')
        ttk.Radiobutton(root, text='男性', variable=self.gender_var, value='Male').pack()
        ttk.Radiobutton(root, text='女性', variable=self.gender_var, value='Female').pack()
        
        # 結果標籤
        self.time_left_label = ttk.Label(root, text="請輸入你的出生日期並點擊計算。")
        self.time_left_label.pack(padx=10, pady=5)
        
        # 計算按鈕
        calculate_button = ttk.Button(root, text='計算剩餘時間', command=self.on_calculate_clicked)
        calculate_button.pack(padx=10, pady=5)
    
    def calculate_time_left(self):
        now = datetime.datetime.now()
        life_expectancy = 76.0 if self.gender_var.get() == 'Female' else 70.8
        age = now - self.birthdate
        age_in_years = age.total_seconds() / (365.25 * 24 * 60 * 60)
        time_left = life_expectancy - age_in_years
        if time_left < 0:
            self.time_left_label.config(text="你已超過平均預期壽命！")
        else:
            self.time_left_label.config(text=f"根據平均壽命，你大概還有 {time_left:.2f} 年")
        self.root.after(1000, self.calculate_time_left)
    
    def on_calculate_clicked(self):
        try:
            self.birthdate = datetime.datetime.strptime(self.date_entry.get(), '%Y-%m-%d')
            self.calculate_time_left()
        except ValueError:
            self.time_left_label.config(text="請按照YYYY-MM-DD的格式輸入日期。")

if __name__ == "__main__":
    app = tk.Tk()
    countdown_app = DeathCountdownApp(app)
    app.mainloop()