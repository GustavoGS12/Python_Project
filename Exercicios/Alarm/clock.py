from tkinter.ttk import *
from tkinter import *
from PIL import Image, ImageTk
from pygame import mixer
import time
from datetime import datetime
from threading import Thread


def alarme():
    while True:
        control = selecionado.get()
        h_alarme = c_hora.get()
        m_alarme = c_minuto.get()
        s_alarme = c_segundo.get()

        hora_atual = datetime.now()

        hora = hora_atual.strftime("%H")
        minuto = hora_atual.strftime("%M")
        segundo = hora_atual.strftime("%S")

        if control == 1:
            if h_alarme == hora:
                if m_alarme == minuto:
                    if s_alarme == segundo:
                        tocar_alarme()

        time.sleep(1)


def desativar_alarme():
    mixer.music.stop()


def tocar_alarme():
    mixer.music.load('alarm.mp3')
    mixer.music.play()
    selecionado.set(0)

    radio = Radiobutton(frame_corpo, command=desativar_alarme, text='Desativar', value=1, variable=selecionado,
                        font='Arial 8', bg=co1, fg=co4)
    radio.place(x=187, y=95)


co0 = "#f0f3f5"  # preta
co1 = "#feffff"  # branca
co2 = "#d6872d"  # gold
co3 = "#fc766d"  # vermelha
co4 = "#403d3d"  # letra
co5 = "#4a88e8"  # azul

janela = Tk()
janela.title("")
janela.geometry('350x150')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

frame_logo = Frame(janela, width=400, height=10, bg=co1)
frame_logo.grid(row=0, column=0, pady=0, padx=0)

frame_corpo = Frame(janela, width=400, height=290, bg=co1)
frame_corpo.grid(row=1, column=0, pady=0, padx=0)

l_linha = Label(frame_logo, width=400, height=1, bg=co2, anchor=NW, font='Ivy 1')
l_linha.place(x=0, y=0)

imagem = Image.open('clock_icon.png')
imagem = imagem.resize((100, 100))
imagem = ImageTk.PhotoImage(imagem)

l_imagem = Label(frame_corpo, height=100, image=imagem, compound=LEFT, padx=10, bg=co1, anchor=NW, fg=co3,
                 font='Ivy 16 bold')
l_imagem.place(x=10, y=10)

l_nome = Label(frame_corpo, text='Alarme', height=1, anchor=NE, font='Ivy 10 bold', bg=co1, fg=co4)
l_nome.place(x=105, y=10)

l_hora = Label(frame_corpo, text='Horas', height=1, anchor=NW, font='Ivy 8', bg=co1, fg=co4)
l_hora.place(x=128, y=40)
c_hora = Combobox(frame_corpo, width=2, font='Ivy 15')
c_hora['value'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15",
                   "16", "17", "18", "19", "20", "21", "22", "23")
c_hora.current(0)
c_hora.place(x=130, y=60)

l_minuto = Label(frame_corpo, text='Minutos', height=1, anchor=NW, font='Ivy 8', bg=co1, fg=co4)
l_minuto.place(x=178, y=40)
c_minuto = Combobox(frame_corpo, width=2, font='Ivy 15')
c_minuto['value'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15",
                     "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31",
                     "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47",
                     "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
c_minuto.current(0)
c_minuto.place(x=180, y=60)

l_segundo = Label(frame_corpo, text='Segundos', height=1, anchor=NW, font='Ivy 8', bg=co1, fg=co4)
l_segundo.place(x=228, y=40)
c_segundo = Combobox(frame_corpo, width=2, font='Ivy 15')
c_segundo['value'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15",
                      "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31",
                      "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47",
                      "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
c_segundo.current(0)
c_segundo.place(x=230, y=60)

selecionado = IntVar()
radio = Radiobutton(frame_corpo, text='Ativar', value=1, variable=selecionado,  font='Ivy 8',
                    bg=co1, fg=co4)
radio.place(x=125, y=95)

t1 = Thread(target=alarme)
t1.start()
mixer.init()

janela.mainloop()

