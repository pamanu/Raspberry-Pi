#!/usr/bin/python

from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import *
from time import sleep, strftime
from datetime import datetime
import wiringpi2


def Pantalla(Linea1, Linea2):

        lcd = Adafruit_CharLCD()
        lcd.begin(16,1)
        lcd.clear()
        lcd.message(Linea1+"\n")
        lcd.message(Linea2)
        lcd.cerrar()



def Tocala(Cual,texto):

        arxi = str(Cual) + '.wav'

        milinea1 = 'SOLTADO A LAS %s        ESTADO: OK'  % (datetime.now().strftime('%H:%M:%S'))
        milinea2 = texto + ' - AUDIO: %s' % ( arxi )
        Pantalla(milinea1,milinea2)
        call(["aplay", arxi])



def Cambia(Anterior):

        Anterior = Anterior + 1
        if Anterior > 7:
                Anterior = 4

        milinea1 = 'CAMBIO MUSICA GPIO 4          ESTADO: OK'
        milinea2 = 'AUDIO SELECIONADO : %s' % (Anterior )
        Pantalla(milinea1,milinea2)

        return Anterior


Pantalla("Bienvenido IB3 GPIO           ESTADO: OK","Esperando Inputs")

Otras = 4

io = wiringpi2.GPIO(wiringpi2.GPIO.WPI_MODE_PINS)

io.pinMode(7,io.INPUT)
io.pullUpDnControl(7,io.PUD_UP)
io.pinMode(8,io.INPUT)
io.pullUpDnControl(8,io.PUD_UP)
io.pinMode(9,io.INPUT)
io.pullUpDnControl(9,io.PUD_UP)
io.pinMode(12,io.INPUT)
io.pullUpDnControl(12,io.PUD_UP)
io.pinMode(13,io.INPUT)
io.pullUpDnControl(13,io.PUD_UP)

y=0
while True:
  x=io.digitalRead(7)
  if x==io.LOW:
        Tocala(1,"Informativos")
  x=io.digitalRead(8)
  if x==io.LOW:
        Tocala(2,"Deportes")
  x=io.digitalRead(9)
  if x==io.LOW:
        Tocala(3,"La Mirada")
  x=io.digitalRead(12)
  if x==io.LOW:
        Tocala(Otras,"Otras")
  x=io.digitalRead(13)
  if x==io.LOW:
        Otras = Cambia(Otras)
  sleep(0.1)
  y = y + 1
  if y > 100 :
        y=0
        milinea1 = 'CHEQUEO A LAS %s        ESTADO: OK'  % (datetime.now().strftime('%H:%M:%S'))
        milinea2 = 'Esperando... '
        Pantalla(milinea1,milinea2)



