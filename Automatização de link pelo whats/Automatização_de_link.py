import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 1
#Abrir o Navegador
pyautogui.press("winleft")
pyautogui.write("chrome")
pyautogui.press("enter")

#Entrar no WhatsApp
link = "https://web.whatsapp.com/"
pyperclip.copy(link)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

#Tempo para Carregar pagina
time.sleep(5)

#Encontrar contato
pyautogui.press("tab")
pyautogui.write("Marcelo Inf")
pyautogui.press("enter")

#Mandar o link
link_2 = "https://www.youtube.com/watch?v=B3gAZvncfa0"
pyperclip.copy(link_2)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")