import tkinter as tk
from tkinter import ttk
import datetime

class DeathCountdownApp:
    def __init__(self, root):
        self.root = root
        self.root.title('死亡倒數計時器')
        
        # 生日輸入
        self.birth = ttk.Label(root, text='請輸入你的出生日期 (YYYY-MM-DD):')
        self.birth.pack(padx=10, pady=5)
        self.date_entry = ttk.Entry(root)
        self.date_entry.pack(padx=10, pady=5)
        
        # 性別選擇
        self.gender_label = ttk.Label(root, text='選擇性別:')
        self.gender_label.pack(padx=10, pady=5)
        self.gender_var = tk.StringVar(value='Male')
        self.male_radiobutton = ttk.Radiobutton(root, text='男性', variable=self.gender_var, value='Male')
        self.male_radiobutton.pack()
        self.female_radiobutton = ttk.Radiobutton(root, text='女性', variable=self.gender_var, value='Female')
        self.female_radiobutton.pack()
        
        # 結果標籤
        self.time_left_label = ttk.Label(root, text="請輸入你的出生日期並點擊計算。")
        self.time_left_label.pack(padx=10, pady=5)
        
        # 計算按鈕
        self.calculate_button = ttk.Button(root, text='計算剩餘時間', command=self.on_calculate_clicked)
        self.calculate_button.pack(padx=10, pady=5)     

        self.message = ttk.Label(root)
    
    def calculate_time_left(self):
        now = datetime.datetime.now()
        life_expectancy = 76.0 if self.gender_var.get() == 'Female' else 70.8
        age = now - self.birthdate
        age_in_years = age.total_seconds() / (365.25 * 24 * 60 * 60)
        time_left = life_expectancy - age_in_years
        if time_left < 0:
            self.time_left_label.config(text="你已超過平均預期壽命！")
        else:
            self.time_left_label.config(text=f"根據平均壽命，你只剩下{time_left:.10f}年可以活。")
            self.message.config(text="別再浪費你的時間了，孩子", font=("Helvetica", 10, "bold"))
            self.message.pack(side="bottom", pady=10)
            self.birth.destroy()
            self.date_entry.destroy()
            self.gender_label.destroy()  # 移除性別標籤
            self.male_radiobutton.destroy()  # 移除男性選項
            self.female_radiobutton.destroy()  # 移除女性選項
            self.calculate_button.destroy()  # 移除計算按鈕
        self.root.after(1, self.calculate_time_left)
    
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