"""
Project: QRCode Generator
Author: Eduardo Do
Date: Feb-17-2025
"""

from PySimpleGUI import PySimpleGUI as sg
import segno
import os
from datetime import datetime


#limpar os campos
def clear_field():
    window['user'].update('')
    window['password'].update('')

# layout.

sg.theme('Reddit')
layout = [
    [sg.Text('User:         '),sg.Text(''),sg.Input(key='user',size=(25,1))],
    [sg.Text('Password:  '),sg.Text(''),sg.Input(key='password', password_char='*',size=(25,1))],
    [sg.Button('Create'),sg.Text('                                       ') ,sg.Button('Clear')],
]
        
# Window
window = sg.Window('QRCode Generator', layout=layout)



#Ler eventos
while True:
    eventos, valores = window.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    #Eventos do Botão Clear.
    if eventos == 'Clear':
        clear_field()
    #Eventos do Botão Create.    
    if eventos == 'Create':
        
        #Cria variavel user e password para usar no QR Code
        user = valores['user']
        password = valores['password']
        
        #Criar o QR Code com os dados de usuário e senha
        qr_data = f'{user}\t\n{password}'
        qr = segno.make(qr_data)
        
        # Obter a data e hora atuais para usar no nome do arquivo
        now = datetime.now()  # Obtém o momento atual
        date_hour = now.strftime("%Y%m%d_%H%M%S")  # Formata como YYYYMMDD_HHMMSS
        
        #Caminho completo do arquivo para salvar
        os.makedirs('c:\\qrcode', exist_ok=True)
        caminho_qrcode = os.path.join('c:\\qrcode', f'qrcode_{date_hour}.png')
        
        # Salvar o QR Code como uma imagem PNG
        qr.save(caminho_qrcode, scale=3)
        print(f'{valores["user"]}\t\n{valores["password"]}')
        sg.popup('Completed',f'QR Code generated and save in:\n{caminho_qrcode}')
        

window.close()
        