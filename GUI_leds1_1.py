# -*- coding: utf-8 -*- #código de interfáz gráfica de usuario para controlar mediante PWM la cantidad de corriente que
# alimenta 4 irradiadores de luz de manera independiente
import time
from tkinter import Button
from tkinter import Label
from tkinter import Tk
from tkinter import Toplevel

import wiringpi

# declaración de pines de salida
OUTPUT = 1
L1 = 28
L2 = 29
L3 = 24
L4 = 25

wiringpi.wiringPiSetup()
wiringpi.pinMode(L1, OUTPUT)
wiringpi.pinMode(L2, OUTPUT)
wiringpi.pinMode(L3, OUTPUT)
wiringpi.pinMode(L4, OUTPUT)

wiringpi.softPwmCreate(L1, 0, 60)
wiringpi.softPwmCreate(L2, 0, 60)
wiringpi.softPwmCreate(L3, 0, 60)
wiringpi.softPwmCreate(L4, 0, 60)
h4 = 0
m4 = 0
s4 = 0
hora1 = 0
hora2 = 0
hora3 = 0
hora4 = 0
min1 = 0
min2 = 0
min3 = 0
min4 = 0
seg1 = 0
seg2 = 0
seg3 = 0
seg4 = 0
pwm1 = 0
pwm2 = 0
pwm3 = 0
pwm4 = 0
b = 0
lab1 = "0 mA"
lab2 = "0 mA"
lab3 = "0 mA"
lab4 = "0 mA"
pre1 = 0
pre2 = 0
pre3 = 0
pre4 = 0


# Declaración de funciones que se usarán en los botones de configuración
def Led1plus20():
    global pwm1
    global L1
    if pwm1 >= 60:
        pwm1 = 60

    else:
        pwm1 = pwm1 + 1
        raiz.after_cancel(raiz.after(1000, PWM1))
        if pwm1 > 60:
            pwm1 = 60

    Led1LabelConfig()
    PWM1()
    print(lab1)
    print(pwm1)


def Led1plus100():
    global pwm1
    global L1
    if pwm1 >= 60:
        pwm1 = 60

    else:
        pwm1 = pwm1 + 5
        raiz.after_cancel(raiz.after(1000, PWM1))
        if pwm1 > 60:
            pwm1 = 60

    Led1LabelConfig()
    PWM1()
    print(lab1)
    print(pwm1)


def Led1minus20():
    global pwm1
    global L1
    if pwm1 <= 0:
        pwm1 = 0
        raiz.after_cancel(raiz.after(1000, PWM1))

    else:
        pwm1 = pwm1 - 1
        if pwm1 < 0:
            pwm1 = 0

    Led1LabelConfig()
    PWM1()
    print(lab1)
    print(pwm1)


def Led1minus100():
    global pwm1
    global L1
    if pwm1 <= 0:
        pwm1 = 0
        raiz.after_cancel(raiz.after(1000, PWM1))

    else:
        pwm1 = pwm1 - 5
        if pwm1 < 0:
            pwm1 = 0

    Led1LabelConfig()
    PWM1()


# empieza botones de configuracion canal 2


def Led2plus20():
    global pwm2
    global L2
    if pwm2 >= 60:
        pwm2 = 60

    else:
        pwm2 = pwm2 + 1
        raiz.after_cancel(raiz.after(1000, PWM2))
        if pwm2 > 60:
            pwm2 = 60

    Led2LabelConfig()
    PWM2()


def Led2plus100():
    global pwm2
    global L2
    if pwm2 >= 60:
        pwm2 = 60

    else:
        pwm2 = pwm2 + 5
        raiz.after_cancel(raiz.after(1000, PWM2))
        if pwm2 > 60:
            pwm2 = 60

    Led2LabelConfig()
    PWM2()


def Led2minus20():
    global pwm2
    global L2
    if pwm2 <= 0:
        pwm2 = 0
        raiz.after_cancel(raiz.after(1000, PWM2))

    else:
        pwm2 = pwm2 - 1
        if pwm2 < 0:
            pwm2 = 0

    Led2LabelConfig()
    PWM2()


def Led2minus100():
    global pwm2
    global L2
    if pwm2 <= 0:
        pwm2 = 0
        raiz.after_cancel(raiz.after(1000, PWM2))

    else:
        pwm2 = pwm2 - 5
        if pwm2 < 0:
            pwm2 = 0

    Led2LabelConfig()
    PWM2()


# comienza botones de configuracion canal 3


def Led3plus20():
    global pwm3
    global L3
    if pwm3 >= 60:
        pwm3 = 60

    else:
        pwm3 = pwm3 + 1
        raiz.after_cancel(raiz.after(1000, PWM3))
        if pwm3 > 60:
            pwm3 = 60

    Led3LabelConfig()
    PWM3()


def Led3plus100():
    global pwm3
    global L3
    if pwm3 >= 60:
        pwm3 = 60

    else:
        pwm3 = pwm3 + 5
        raiz.after_cancel(raiz.after(1000, PWM3))
        if pwm3 > 60:
            pwm3 = 60

    Led3LabelConfig()
    PWM3()


def Led3minus20():
    global pwm3
    global L3
    if pwm3 <= 0:
        pwm3 = 0
        raiz.after_cancel(raiz.after(1000, PWM3))

    else:
        pwm3 = pwm3 - 1
        if pwm3 < 0:
            pwm3 = 0

    Led3LabelConfig()
    PWM3()


def Led3minus100():
    global pwm3
    global L3
    if pwm3 <= 0:
        pwm3 = 0
        raiz.after_cancel(raiz.after(1000, PWM3))

    else:
        pwm3 = pwm3 - 5
        if pwm3 < 0:
            pwm3 = 0

    Led3LabelConfig()
    PWM3()


# comienza botones de configuracion canal 4


def Led4plus20():
    global pwm4
    global L4
    if pwm4 >= 60:
        pwm4 = 60

    else:
        pwm4 = pwm4 + 1
        raiz.after_cancel(raiz.after(1000, PWM4))
        if pwm4 > 60:
            pwm4 = 60

    Led4LabelConfig()
    PWM4()


def Led4plus100():
    global pwm4
    global L4
    if pwm4 >= 60:
        pwm4 = 60

    else:
        pwm4 = pwm4 + 5
        raiz.after_cancel(raiz.after(1000, PWM4))
        if pwm4 > 60:
            pwm4 = 60

    Led4LabelConfig()
    PWM4()


def Led4minus20():
    global pwm4
    global L4
    if pwm4 <= 0:
        pwm4 = 0
        raiz.after_cancel(raiz.after(1000, PWM4))

    else:
        pwm4 = pwm4 - 1
        if pwm4 < 0:
            pwm4 = 0

    Led4LabelConfig()
    PWM4()


def Led4minus100():
    global pwm4
    global L4
    if pwm4 <= 0:
        pwm4 = 0
        raiz.after_cancel(raiz.after(1000, PWM4))

    else:
        pwm4 = pwm4 - 5
        if pwm4 < 0:
            pwm4 = 0
    Led4LabelConfig()
    PWM4()


# Configuración para mostrar el dato de PWM como corriente
def Led1LabelConfig():
    global lab1
    muestra1 = pwm1 * 20
    lab1 = muestra1, "mA"
    ledLabel1.configure(text=lab1)


def Led2LabelConfig():
    global lab2
    muestra2 = pwm2 * 20
    lab2 = muestra2, "mA"
    ledLabel2.configure(text=lab2)


def Led3LabelConfig():
    global lab3
    muestra3 = pwm3 * 20
    lab3 = muestra3, "mA"
    ledLabel3.configure(text=lab3)


def Led4LabelConfig():
    global lab4
    muestra4 = pwm4 * 20
    lab4 = muestra4, "mA"
    ledLabel4.configure(text=lab4)


# medición de tiempo encendido para Canal 1
def PWM1():
    global hora1
    global min1
    global seg1
    global pwm1
    global pre1
    if pre1 > 0 and hora1 == 0 and min1 == 0 and seg1 == 0:
        hora1 = time.localtime(time.time())[3]
        min1 = time.localtime(time.time())[4]
        seg1 = time.localtime(time.time())[5]
    h = time.localtime(time.time())[3]
    m = time.localtime(time.time())[4]
    s = time.localtime(time.time())[5]
    if pre1 > 0:
        if s >= seg1:
            ma1 = 0
        else:
            ma1 = 1

        if m >= min1:
            m1 = m - min1 - ma1
            ha1 = 0
        else:
            m1 = m - min1 + 59 - ma1
            ha1 = 1
        h1 = h - hora1 - ha1
        raiz.after(1000, PWM1)
    else:
        h1 = 0
        m1 = 0
        hora1 = 0
        min1 = 0
        seg1 = 0
        h = 0
        m = 0
        s = 0
    cont1 = "  ", h1, "hr", m1, "min"
    contador1.configure(text=cont1)


# medición de tiempo encendido para Canal 2
def PWM2():
    global hora2
    global min2
    global seg2
    global pwm2
    global pre2
    if pre2 > 0 and hora2 == 0 and min2 == 0 and seg2 == 0:
        hora2 = time.localtime(time.time())[3]
        min2 = time.localtime(time.time())[4]
        seg2 = time.localtime(time.time())[5]
    h = time.localtime(time.time())[3]
    m = time.localtime(time.time())[4]
    s = time.localtime(time.time())[5]
    if pre2 > 0:
        if s >= seg2:
            ma2 = 0
        else:
            ma2 = 1

        if m >= min2:
            m2 = m - min2 - ma2
            ha2 = 0
        else:
            m2 = m - min2 + 59 - ma2
            ha2 = 1
        h2 = h - hora2 - ha2
        raiz.after(1000, PWM2)
    else:
        h2 = 0
        m2 = 0
        hora2 = 0
        min2 = 0
        seg2 = 0
        h = 0
        m = 0
        s = 0
    cont2 = "  ", h2, "hr", m2, "min"
    contador2.configure(text=cont2)


# medición de tiempo encendido para Canal 3
def PWM3():
    global hora3
    global min3
    global seg3
    global pwm3
    global pre3
    if pre3 > 0 and hora3 == 0 and min3 == 0 and seg3 == 0:
        hora3 = time.localtime(time.time())[3]
        min3 = time.localtime(time.time())[4]
        seg3 = time.localtime(time.time())[5]
    h = time.localtime(time.time())[3]
    m = time.localtime(time.time())[4]
    s = time.localtime(time.time())[5]
    if pre3 > 0:
        if s >= seg3:
            ma3 = 0
        else:
            ma3 = 1

        if m >= min3:
            m3 = m - min3 - ma3
            ha3 = 0
        else:
            m3 = m - min3 + 59 - ma3
            ha3 = 1
        h3 = h - hora3 - ha3
        raiz.after(1000, PWM3)
    else:
        h3 = 0
        m3 = 0
        hora3 = 0
        min3 = 0
        seg3 = 0
        h = 0
        m = 0
        s = 0
    cont3 = "  ", h3, "hr", m3, "min"
    contador3.configure(text=cont3)


# medición de tiempo encendido para Canal 4
def PWM4():
    global hora4
    global min4
    global seg4
    global pwm4
    global pre4
    if pre4 > 0 and hora4 == 0 and min4 == 0 and seg4 == 0:
        hora4 = time.localtime(time.time())[3]
        min4 = time.localtime(time.time())[4]
        seg4 = time.localtime(time.time())[5]
    h = time.localtime(time.time())[3]
    m = time.localtime(time.time())[4]
    s = time.localtime(time.time())[5]
    if pre4 > 0:
        if s >= seg4:
            ma4 = 0
        else:
            ma4 = 1

        if m >= min4:
            m4 = m - min4 - ma4
            ha4 = 0
        else:
            m4 = m - min4 + 59 - ma4
            ha4 = 1
        h4 = h - hora4 - ha4
        raiz.after(1000, PWM4)
    else:
        h4 = 0
        m4 = 0
        hora4 = 0
        min4 = 0
        seg4 = 0
        h = 0
        m = 0
        s = 0
    cont4 = "  ", h4, "hr", m4, "min"
    contador4.configure(text=cont4)


def actualizar1():
    global h1
    global m1
    global s1
    global hora1
    global min1
    global seg1
    global pwm1
    global pre1
    global config
    h1 = 0
    m1 = 0
    s1 = 0
    hora1 = 0
    min1 = 0
    seg1 = 0
    pre1 = pwm1
    wiringpi.softPwmWrite(L1, pwm1)
    PWM1()
    config.destroy()


def actualizar2():
    global h2
    global m2
    global s2
    global hora2
    global min2
    global seg2
    global pwm2
    global pre2
    global config
    h2 = 0
    m2 = 0
    s2 = 0
    hora2 = 0
    min2 = 0
    seg2 = 0
    pre2 = pwm2
    wiringpi.softPwmWrite(L2, pwm2)
    PWM2()
    config.destroy()


def actualizar3():
    global h3
    global m3
    global s3
    global hora3
    global min3
    global seg3
    global pwm3
    global pre3
    global config
    h3 = 0
    m3 = 0
    s3 = 0
    hora3 = 0
    min3 = 0
    seg3 = 0
    pre3 = pwm3
    wiringpi.softPwmWrite(L3, pwm3)
    PWM3()
    config.destroy()


def actualizar4():
    global h4
    global m4
    global s4
    global hora4
    global min4
    global seg4
    global pwm4
    global pre4
    global config
    h4 = 0
    m4 = 0
    s4 = 0
    hora4 = 0
    min4 = 0
    seg4 = 0
    pre4 = pwm4
    wiringpi.softPwmWrite(L4, pwm4)
    PWM4()
    config.destroy()


# funciones de reestablecimiento de salidas a 0
def rest1():
    global h1
    global m1
    global s1
    global hora1
    global min1
    global seg1
    global pwm1
    global pre1

    h1 = 0
    m1 = 0
    s1 = 0
    hora1 = 0
    min1 = 0
    seg1 = 0
    pwm1 = 0
    pre1 = pwm1
    wiringpi.softPwmWrite(L1, pwm1)
    PWM1()
    Led1LabelConfig()


def rest2():
    global h2
    global m2
    global s2
    global hora2
    global min2
    global seg2
    global pwm2
    global pre2

    h2 = 0
    m2 = 0
    s2 = 0
    hora2 = 0
    min2 = 0
    seg2 = 0
    pwm2 = 0
    pre2 = pwm2
    wiringpi.softPwmWrite(L2, pwm2)
    PWM2()
    Led2LabelConfig()


def rest3():
    global h3
    global m3
    global s3
    global hora3
    global min3
    global seg3
    global pwm3
    global pre3

    h3 = 0
    m3 = 0
    s3 = 0
    hora3 = 0
    min3 = 0
    seg3 = 0
    pwm3 = 0
    pre3 = pwm3
    wiringpi.softPwmWrite(L3, pwm3)
    PWM3()
    Led3LabelConfig()


def rest4():
    global h4
    global m4
    global s4
    global hora4
    global min4
    global seg4
    global pwm4
    global pre4

    h4 = 0
    m4 = 0
    s4 = 0
    hora4 = 0
    min4 = 0
    seg4 = 0
    pwm4 = 0
    pre4 = pwm4
    wiringpi.softPwmWrite(L4, pwm4)
    PWM4()
    Led4LabelConfig()


# declaración de funciones de cancelar los ultimos cambios hechos
def cancelar1():
    global pwm1
    global pre1
    global config
    pwm1 = pre1
    wiringpi.softPwmWrite(L1, pwm1)
    Led1LabelConfig()
    config.destroy()


def cancelar2():
    global pwm2
    global pre2
    global config
    pwm2 = pre2
    wiringpi.softPwmWrite(L2, pwm2)
    Led2LabelConfig()
    config.destroy()


def cancelar3():
    global pwm3
    global pre3
    global config
    pwm3 = pre3
    wiringpi.softPwmWrite(L3, pwm3)
    Led3LabelConfig()
    config.destroy()


def cancelar4():
    global pwm4
    global pre4
    global config
    pwm4 = pre4
    wiringpi.softPwmWrite(L4, pwm4)
    Led4LabelConfig()
    config.destroy()


def pruebas():
    pass


# interfaz de control para cada canal
def canal1():
    global lab1
    global pwm1
    global pre1
    global config
    pre1 = pwm1
    config = Toplevel()
    config.geometry("250x480")
    config.title("CANAL 1")

    enter = Button(config, text="ACTUALIZAR", command=actualizar1)
    enter.grid(row=5, column=1)
    cancel = Button(config, text="CANCELAR", command=cancelar1)
    cancel.grid(row=5, column=2)
    ledButtonPlus20 = Button(config, text="  +20  ", command=Led1plus20)
    ledButtonPlus20.grid(row=2, column=1)
    ledButtonMinus20 = Button(config, text=" --20  ", command=Led1minus20)
    ledButtonMinus20.grid(row=3, column=1)
    ledButtonPlus100 = Button(config, text="  +100  ", command=Led1plus100)
    ledButtonPlus100.grid(row=1, column=1)
    ledButtonMinus100 = Button(config, text=" --100  ", command=Led1minus100)
    ledButtonMinus100.grid(row=4, column=1)
    config.transient(master=raiz)
    config.grab_set()
    raiz.wait_window(config)


def canal2():
    global lab2
    global pwm2
    global pre2
    global config
    pre2 = pwm2
    config = Toplevel()
    config.geometry("250x480")
    config.title("CANAL 2")

    enter = Button(config, text="ACTUALIZAR", command=actualizar2)
    enter.grid(row=5, column=1)
    cancel = Button(config, text="CANCELAR", command=cancelar2)
    cancel.grid(row=5, column=2)
    ledButtonPlus20 = Button(config, text="  +20  ", command=Led2plus20)
    ledButtonPlus20.grid(row=2, column=1)
    ledButtonMinus20 = Button(config, text=" --20  ", command=Led2minus20)
    ledButtonMinus20.grid(row=3, column=1)
    ledButtonPlus100 = Button(config, text="  +100  ", command=Led2plus100)
    ledButtonPlus100.grid(row=1, column=1)
    ledButtonMinus100 = Button(config, text=" --100  ", command=Led2minus100)
    ledButtonMinus100.grid(row=4, column=1)
    config.transient(master=raiz)
    config.grab_set()
    raiz.wait_window(config)


def canal3():
    global lab3
    global pwm3
    global pre3
    global config
    pre3 = pwm3
    config = Toplevel()
    config.geometry("250x480")
    config.title("CANAL 3")

    enter = Button(config, text="ACTUALIZAR", command=actualizar3)
    enter.grid(row=5, column=1)
    cancel = Button(config, text="CANCELAR", command=cancelar3)
    cancel.grid(row=5, column=2)
    ledButtonPlus20 = Button(config, text="  +20  ", command=Led3plus20)
    ledButtonPlus20.grid(row=2, column=1)
    ledButtonMinus20 = Button(config, text=" --20  ", command=Led3minus20)
    ledButtonMinus20.grid(row=3, column=1)
    ledButtonPlus100 = Button(config, text="  +100  ", command=Led3plus100)
    ledButtonPlus100.grid(row=1, column=1)
    ledButtonMinus100 = Button(config, text=" --100  ", command=Led3minus100)
    ledButtonMinus100.grid(row=4, column=1)
    config.transient(master=raiz)
    config.grab_set()
    raiz.wait_window(config)


def canal4():
    global lab4
    global pwm4
    global pre4
    global config
    pre4 = pwm4
    config = Toplevel()
    config.geometry("250x480")
    config.title("CANAL 4")

    enter = Button(config, text="ACTUALIZAR", command=actualizar4)
    enter.grid(row=5, column=1)
    cancel = Button(config, text="CANCELAR", command=cancelar4)
    cancel.grid(row=5, column=2)
    ledButtonPlus20 = Button(config, text="  +20  ", command=Led4plus20)
    ledButtonPlus20.grid(row=2, column=1)
    ledButtonMinus20 = Button(config, text=" --20  ", command=Led4minus20)
    ledButtonMinus20.grid(row=3, column=1)
    ledButtonPlus100 = Button(config, text="  +100  ", command=Led4plus100)
    ledButtonPlus100.grid(row=1, column=1)
    ledButtonMinus100 = Button(config, text=" --100  ", command=Led4minus100)
    ledButtonMinus100.grid(row=4, column=1)
    config.transient(master=raiz)
    config.grab_set()
    raiz.wait_window(config)


# Interfaz grafica de usuario principal

posx_y = 0
raiz = Tk()
raiz.geometry("800x480")
raiz.title("Monitoreo de Canales")
canal1Button = Button(raiz, text="Canal 1", command=canal1)
canal1Button.grid(row=1, column=1)
canal2Button = Button(raiz, text="Canal 2", command=canal2)
canal2Button.grid(row=2, column=1)
canal3Button = Button(raiz, text="Canal 3", command=canal3)
canal3Button.grid(row=3, column=1)
canal4Button = Button(raiz, text="Canal 4", command=canal4)
canal4Button.grid(row=4, column=1)

ledLabel1 = Label(raiz, text="0 mA")
ledLabel1.grid(row=1, column=2)

ledLabel2 = Label(raiz, text="0 mA")
ledLabel2.grid(row=2, column=2)

ledLabel3 = Label(raiz, text="0 mA")
ledLabel3.grid(row=3, column=2)

ledLabel4 = Label(raiz, text="0 mA")
ledLabel4.grid(row=4, column=2)

contador1 = Label(raiz, text="   0 hr 0 min")
contador1.grid(row=1, column=3)

contador2 = Label(raiz, text="   0 hr 0 min")
contador2.grid(row=2, column=3)

contador3 = Label(raiz, text="   0 hr 0 min")
contador3.grid(row=3, column=3)

contador4 = Label(raiz, text="   0 hr 0 min")
contador4.grid(row=4, column=3)

canal1Button = Button(raiz, text="Restablecer", command=rest1)
canal1Button.grid(row=1, column=4)
canal2Button = Button(raiz, text="Restablecer", command=rest2)
canal2Button.grid(row=2, column=4)
canal3Button = Button(raiz, text="Restablecer", command=rest3)
canal3Button.grid(row=3, column=4)
canal4Button = Button(raiz, text="Restablecer", command=rest4)
canal4Button.grid(row=4, column=4)

raiz.mainloop()
