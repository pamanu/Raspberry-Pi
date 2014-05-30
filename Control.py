#!/usr/bin/python

import os
import subprocess
import re
import time
from datetime import datetime
from Adafruit_CharLCD import Adafruit_CharLCD


def Pantalla(Linea1, Linea2):

        lcd = Adafruit_CharLCD()
        lcd.begin(16,1)
        lcd.clear()
        lcd.message(Linea1+"\n")
        lcd.message(Linea2)
        lcd.cerrar()


def Arranca():
        
        proc = subprocess.Popen('sudo nohup ./MiGPI2.py &', shell=True)
        time.sleep(2)
        pid = proc.pid
        return pid


def Running( proc_name ):
    ps = subprocess.Popen("ps ax -o pid= -o args= ", shell=True, stdout=subprocess.PIPE)
    ps_pid = ps.pid
    output = ps.stdout.read()
    ps.stdout.close()
    ps.wait()

    for line in output.split("\n"):
        res = re.findall("(\d+) (.*)", line)
        if res:
            pid = int(res[0][0])
            if proc_name in res[0][1] and pid != os.getpid() and pid != ps_pid:
                return True
    return False


if Running('MiGPI2.py') == False:
        MiPid = Arranca()
        print("LANZANDO PROCESO GPIO...")
else:
        print("PROCESO YA LANZADO, CAPTURADO Y VIGILANDO...")


while 1:

        time.sleep(30)
        if Running('MiGPI2.py') :
                milinea1 = 'CONTROL A LAS %s        ESTADO: OK'  % (datetime.now().strftime('%H:%M:$
                Pantalla(milinea1,"SUPERVISANDO PROCESO...")
        else:
                Pantalla("ERROR DE SISTEMA","REINICINADO.....")
                print("ERROR DE SYSTEMA")
                time.sleep(5)
                MiPid = Arranca()
