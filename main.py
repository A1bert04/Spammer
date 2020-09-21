import time
import pyautogui

text = ""
repe = 500
delay = 0
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
repe = int(input("Cuantas veces quieres enviar el mensaje: "))
print("")
delay = float(input("Cuantos segundos quieres entre mensajes (lo peudes dejar en 0): "))

print("Tienes 15 segundos para abrir Whatsapp Web")
time.sleep(15)

while i <= repe:
    pyautogui.typewrite(text)
    pyautogui.press("Enter")
    print(i)
    i = i + 1
    time.sleep(delay)

exit()
