'''
Componentes que serão utilizados:
  * Raspberry Pi
  * Módulo RFID (MFRC522)
  * Cartões RFID
  * Conexão Wi-Fi
Passos do Projeto:
'''
'''
Projeto Informatica IOT::
1. Configuração do hardware:
    1. Conexão do módulo RFID ao Raspberry Pi 
    2. Instale a biblioteca MFRC522:
    3. Instale a biblioteca para integração com Google Sheets:
2. Códificação em Python para o Raspberry Pi
'''
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Configuração do Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('path/to/creds.json', scope)
client = gspread.authorize(creds)
sheet = client.open("PresencaInformaticaSR").sheet1

# Configuração do leitor RFID
reader = SimpleMFRC522()

def log_to_sheets(id, timestamp):
    sheet.append_row([id, timestamp])

try:
    while True:
        print("Aproxime o cartão RFID")
        id, text = reader.read()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"ID: {id}, Hora: {timestamp}")
        log_to_sheets(id, timestamp)

finally:
    GPIO.cleanup()
