import time
import pyautogui

text = ""
repe = 500
delay = 0.0
i = 1

print("----------------------------------")
print("")
print("       A1bert04 (c) 2020          ")
print("")
print("----------------------------------")
print("")
print("")

text = str(input("Texto a Spamear: "))
print("")

def Askrepe():

    repe = input("Cuantas veces quieres enviar el mensaje: ")
    print("")

    if repe is "0":
        print("0 no es un número válido")
        print("")
        Askrepe()
    
    else:
        try:
            int(repe)
            return int(repe)

        except:
            print(repe + " no es un número válido")
            print("")
            Askrepe()

def Askdelay():

    delay = input("Cuantos segundos quieres entre mensajes (lo puedes dejar en 0): ")
    print("")

    try:
        float(delay)
        return delay
        
    except:
        print(delay + " no es un número válido")
        print("")
        Askdelay()

repe = Askrepe()
delay = float(Askdelay())

print("Tienes 10 segundos para abrir Whatsapp Web")
time.sleep(10)

while i <= repe :
    
    pyautogui.typewrite(text)
    pyautogui.press("Enter")
    print(i)

    if i > repe:
        exit()
    
    else: 
        i = i + 1
        print("")
        time.sleep(delay)
        pass
