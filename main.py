import pandas as pd
from tkinter import *
from tkinter import messagebox


df = pd.read_csv(r'nazwy_druzyn.csv')
col_list = df[df.columns[0]].values.tolist()
col_list1 = df[df.columns[0]].values.tolist()

window = Tk()
window.geometry("600x600")
variable = StringVar(window)
variable1 = StringVar(window)


def write():
    jeden = (variable.get())
    dwa = (variable1.get())
    wynik = str_out2.set(TextTeam1_Goals.get("1.0", END))
    if jeden == dwa:
        messagebox.showwarning("Blad", "Nie moga byc takie same druzyny")
    else:
        jeden = str_out.set(variable.get())
        dwa = str_out1.set(variable1.get())
        df_mecze = pd.DataFrame({'mecze': [variable.get(), variable1.get()]})
        df["mecze"] = df_mecze
        df_gole = pd.DataFrame({'wynik': [TextTeam1_Goals.get("1.0", END)]})
        df['wynik'] = df_gole
        df.to_csv("wynik_druzyn.csv", index=False)

LabelTeam1 = Label(window, text="Wybierz pierwsza druzyne", height=5)
SelectTeam1 = OptionMenu(window, variable, *col_list)

LabelTeam2 = Label(window, text="Wybierz druga druzyne", height=5)
SelectTeam2 = OptionMenu(window, variable1, *col_list1)

LabelTeam1_goals = Label(window, text="Wpisz wynik meczu: ")
TextTeam1_Goals = Text(window, height=3, width=10)

Przycisk = Button(window, text="Wpisz mecz i wynik do csv", command=write)

str_out = StringVar(window)
str_out.set("Druzyna1")

str_out1 = StringVar(window)
str_out1.set("Druzyna2")

str_out2 = StringVar(window)
str_out2.set("Wynik spotkania")

LabelResult = Label(window, textvariable=str_out, width=20)
LabelResult1 = Label(window, textvariable=str_out1, width=20)
LabelResult2 = Label(window, textvariable=str_out2, width=20)

LabelTeam1.grid()
SelectTeam1.grid()

LabelTeam2.grid()
SelectTeam2.grid()

LabelTeam1_goals.grid()
TextTeam1_Goals.grid()

Przycisk.grid(pady=10)

LabelResult.grid()
LabelResult1.grid()
LabelResult2.grid()

print(df)
print()

mainloop()