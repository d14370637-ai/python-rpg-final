# 📁 檔案：final/w10_window.py
import tkinter as tk

root = tk.Tk()                     # ① 建立視窗

root.title("勇者傳說：覺醒")        # ② 設定外觀
root.geometry("400x300")
root.configure(bg="#1e293b")

root.mainloop()                    # ③ 保持開啟

print("視窗關閉後才會印出這行")