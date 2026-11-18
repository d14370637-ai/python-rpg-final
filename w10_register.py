# 📁 檔案：final/w10_register.py
import tkinter as tk

def register():
    name = name_entry.get()
    level = level_entry.get()
    result_lbl.config(text=f"登錄完成：{name}（Lv.{level}）")

root = tk.Tk()
root.title("冒險者公會")
root.geometry("320x240")

name_lbl = tk.Label(root, text="冒險者名稱")
name_lbl.pack(pady=(10, 0))
name_entry = tk.Entry(root, justify="center")
name_entry.pack()

level_lbl = tk.Label(root, text="等級")
level_lbl.pack(pady=(10, 0))
level_entry = tk.Entry(root, justify="center")
level_entry.insert(0, "1")
level_entry.pack()

reg_btn = tk.Button(root, text="登錄", command=register)
reg_btn.pack(pady=10)
result_lbl = tk.Label(root, text="請輸入名稱與等級")
result_lbl.pack()

root.mainloop()