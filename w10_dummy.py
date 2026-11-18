# 📁 檔案：final/w10_dummy.py (完整解答)
import tkinter as tk

class Dummy:
    def __init__(self, hp):
        self.hp = hp
    def take_damage(self, dmg):
        self.hp = max(0, self.hp - dmg)

dummy = Dummy(30)

def hit():
    if dummy.hp == 0:
        log_lbl.config(text="> 木樁已經倒了！")
        return
    dummy.take_damage(6)
    log_lbl.config(text=f"> 木樁剩下 {dummy.hp} HP")

root = tk.Tk()
root.title("課間練習：打木樁")
root.geometry("300x150")

log_lbl = tk.Label(root, text="> 木樁 HP 30", font=("Courier", 12))
log_lbl.pack(pady=20)
hit_btn = tk.Button(root, text="打一下", width=10, command=hit)
hit_btn.pack()

root.mainloop()