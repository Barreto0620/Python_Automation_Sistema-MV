# coding: utf-8
# Configuração de Monitor - 1920x1080 *
# Configuração da Página - Zoom 100% *

import pyautogui
import time

pyautogui.PAUSE = 1

pyautogui.alert('Certifique-se da aba do SISTEMA MV esteja FECHADO ! Não utilize o computador até o código FINALIZAR !')
pyautogui.hotkey('win', 'r')
pyautogui.write('cmd')
pyautogui.press('enter')
pyautogui.write('taskkill /f /im chrome.exe')
pyautogui.press('enter')
time.sleep(2)
pyautogui.write('exit')
pyautogui.press('enter')
pyautogui.press('win')
pyautogui.write('c:')
pyautogui.press('enter')
pyautogui.write('CentBrowser')
pyautogui.press('delete')
time.sleep(3)
pyautogui.press('win')
pyautogui.write('\\')
pyautogui.write('\\')
pyautogui.write('192.168.7.107')
pyautogui.press('enter')
pyautogui.write('cen')
pyautogui.hotkey('ctrl', 'c')
pyautogui.press('win')
pyautogui.write('c:\\')
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'v')
time.sleep(3)
pyautogui.alert('Favor aguardar término de transferência de arquivo. Após finalizado já poderá utilizar o computador, OBRIGADO !')

# Fechar todos os exploradores de arquivo
pyautogui.hotkey('alt', 'f4')  # Fecha a janela atual (explorador de arquivos)
time.sleep(0.5)
pyautogui.hotkey('alt', 'f4')  # Fecha qualquer outro explorador que possa estar aberto
time.sleep(0.5)

# Mensagem final profissional
pyautogui.alert('✓ Processo concluído com sucesso!\n\n'
               'Sistema atualizado e otimizado.\n'
               'Você já pode utilizar o computador normalmente.\n\n'
               '────────────────────────────────\n'
               'Desenvolvido pela empresa WebCash\n'
               '────────────────────────────────')

# Realizado a troca do CentBrowser *


#Bússola do Mouse

#import pyautogui
#import time

#time.sleep(5)
#print(pyautogui.position())