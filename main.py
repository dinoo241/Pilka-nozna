import pandas as pd
from tkinter import *
from tkinter import messagebox

df = pd.read_csv(r'nazwy_druzyn.csv')
col_list = df[df.columns[0]].values.tolist()
col_list1 = df[df.columns[0]].values.tolist()

window = Tk()
window.geometry("150x600")
v1 = StringVar(window)
v2 = StringVar(window)

def write():
    team1 = (v1.get())
    team2 = (v2.get())
    wynik = str_out2.set(TextTeam1_Goals.get("1.0", END))
    if team1 == team2:
        messagebox.showwarning("Blad", "Nie moga byc takie same druzyny")
    else:
        team1 = str_out.set(v1.get())
        team2 = str_out1.set(v2.get())
        df_mecze = pd.DataFrame({'mecze': [v1.get(), v2.get()]})
        df["mecze"] = df_mecze
        df_gole = pd.DataFrame({'wynik': [TextTeam1_Goals.get("1.0", END)]})
        df['wynik'] = df_gole
        df.to_csv("wynik_druzyn.csv", index=False)

lblt1 = Label(window, text="Wybierz pierwsza druzyne", height=5)
SelectTeam1 = OptionMenu(window, v1, *col_list)

lblt2 = Label(window, text="Wybierz druga druzyne", height=5)
SelectTeam2 = OptionMenu(window, v2, *col_list1)

lbl_goals = Label(window, text="Wpisz wynik meczu: ")
TextTeam1_Goals = Text(window, height=3, width=10)

b1 = Button(window, text="Wpisz mecz i wynik do csv", command=write)

str_out = StringVar(window)

str_out1 = StringVar(window)

str_out2 = StringVar(window)

lblr1 = Label(window, textvariable=str_out, width=20)
lblr2 = Label(window, textvariable=str_out1, width=20)
lblr3 = Label(window, textvariable=str_out2, width=20)

lblt1.grid()
SelectTeam1.grid()
lblt2.grid()
SelectTeam2.grid()
lbl_goals.grid()
TextTeam1_Goals.grid()
lblr1.grid()
lblr2.grid()
lblr3.grid()

b1.grid(pady=10)

mainloop()
