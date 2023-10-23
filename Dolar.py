import pyautogui as tempoEspera
import pyautogui as posicaoMouse
import pyautogui

#Alerta para inicialização do programa
pyautogui.alert('Não mexa no computador, robo sendo testado')

#Clicando no menu iniciar
posicaoMouse.click(27, 1059)
tempoEspera.sleep(1)

#Digitando o chrome
pyautogui.write('chrome')
tempoEspera.sleep(1)
#Entrando no chrome
pyautogui.press('enter')
tempoEspera.sleep(1)
#Pesquisando valor do dólar hoje
pyautogui.write('Dolar Hoje')
tempoEspera.sleep(1)
#Entrando na pesquisa
pyautogui.press('enter')
tempoEspera.sleep(1)


#print(posicaoMouse.position())
#tempoEspera.sleep(1)



