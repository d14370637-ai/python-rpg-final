# 📁 檔案：final/w10_training.py 第 1 段 (怪物設計圖與角色資料)
import random
import tkinter as tk

class Monster:                          # W08 設計圖精簡版
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.charging = False           # 狀態旗標：正在蓄力？

    def take_damage(self, dmg):
        self.hp = max(0, self.hp - dmg)

player = {"hp": 100, "atk": 14, "potions": 2, "defending": False}
slime = Monster("哥布林", 130, 13)
# 📁 w10_training.py 第 2 段 (畫面更新與回合結算，接在第 1 段下面)
def refresh(msg):
    status_lbl.config(text=f"勇者 HP {player['hp']}  藥水 {player['potions']}  "
                           f"{slime.name} HP {slime.hp}")
    log_lbl.config(text=msg)

def slime_turn(msg):
    if slime.hp > 0:                       # 還活著才反擊
        if slime.charging:                 # 上回合蓄力 ➔ 這回合重擊
            dmg = slime.atk * 3
            slime.charging = False
        else:
            dmg = random.randint(slime.atk - 3, slime.atk + 3)
            slime.charging = random.random() < 0.3
        if player["defending"]:
            dmg //= 3                      # 防禦：傷害剩三分之一
        player["defending"] = False
        player["hp"] = max(0, player["hp"] - dmg)
        msg += f"\n> {slime.name}反擊，你受到 {dmg} 點傷害"
        if slime.charging:
            msg += f"\n> {slime.name}正在蓄力！快防禦！"
    if slime.hp == 0:
        msg += f"\n> 太棒了！{slime.name}倒下，你的冒險又邁進了一步！"
    elif player["hp"] == 0:
        msg += "\n> 哎呀，不小心戰敗了……重整裝備再出發吧！"
    refresh(msg)

def battle_over():
    if slime.hp == 0 or player["hp"] == 0:
        log_lbl.config(text="> 戰鬥已經結束，關掉視窗再練一次！")
        return True
    return False
# 📁 w10_training.py 第 3 段 (三顆按鈕的函式，接在第 2 段下面)
def attack():
    if battle_over():
        return
    dmg = random.randint(player["atk"] - 2, player["atk"] + 2)
    slime.take_damage(dmg)
    slime_turn(f"> 你揮劍造成 {dmg} 點傷害！")

def defend():
    if battle_over():
        return
    player["defending"] = True
    slime_turn("> 你舉起盾牌防禦！")

def drink():
    if battle_over():
        return
    if player["potions"] == 0:
        refresh("> 藥水已經喝光了！")
        return
    player["potions"] -= 1
    player["hp"] = min(100, player["hp"] + 30)
    slime_turn("> 喝下藥水，恢復 30 HP！")
    # 📁 w10_training.py 第 4 段 (視窗與元件，接在第 3 段下面)
root = tk.Tk()
root.title("W10 練功場")
root.geometry("420x380")
root.configure(bg="#1e293b")

title_lbl = tk.Label(root, text="練功場：打倒史萊姆",
                     font=("Arial", 18, "bold"), fg="gold", bg="#1e293b")
title_lbl.pack(pady=10)
status_lbl = tk.Label(root, font=("Arial", 12), fg="white", bg="#1e293b")
status_lbl.pack()
log_lbl = tk.Label(root, font=("Courier", 11), fg="#4ade80", bg="#0b1220",
                   justify="left", anchor="w", width=36, height=5)
log_lbl.pack(pady=10)

atk_btn = tk.Button(root, text="攻擊", width=12, command=attack)
atk_btn.pack(pady=3)
def_btn = tk.Button(root, text="防禦", width=12, command=defend)
def_btn.pack(pady=3)
drink_btn = tk.Button(root, text="喝水", width=12, command=drink)
drink_btn.pack(pady=3)

refresh(f"> 野生的{slime.name}出現了！")
root.mainloop()