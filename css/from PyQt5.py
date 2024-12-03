from PyQt5.QtWidgets import QGridLayout, QApplication, QWidget, QLabel, QPushButton # type: ignore
import sys
 
 
aplicacion = QApplication(sys.argv)
 
 
ventana = QWidget()
layout_principal = QGridLayout()
layout_botones = QGridLayout()
 
 
texto1 = QLabel("hola")
texto1.setStyleSheet("font-size: 20px;")
 
 
botones = []
for n_boton in range(9):
    boton = QPushButton('')
    boton.setFixedSize(50, 50)
    botones.append(boton)
 
 
x, y = 0, 0
for boton in botones:
    layout_botones.addWidget(boton, y, x)
    x += 1
    if x > 2:
        y += 1
        x = 0
 
 
layout_principal.addWidget(texto1, 0, 0)
layout_principal.addLayout(layout_botones, 1, 0)
 
 
ventana.setLayout(layout_principal)
 
 
def checar():
    if botones[0].text() == 'X' and botones[1].text() == 'X' and botones[2].text() == 'X':
        texto1.setText("Gana X")
       
    if botones[3].text() == 'X' and botones[4].text() == 'X' and botones[5].text() == 'X':
        texto1.setText("Gana X")
     
    if botones[6].text() == 'X' and botones[7].text() == 'X' and botones[8].text() == 'X':
        texto1.setText("Gana X")
       
    if botones[0].text() == 'X' and botones[3].text() == 'X' and botones[6].text() == 'X':
        texto1.setText("Gana X")
     
    if botones[1].text() == 'X' and botones[4].text() == 'X' and botones[7].text() == 'X':
        texto1.setText("Gana X")
       
    if botones[2].text() == 'X' and botones[5].text() == 'X' and botones[8].text() == 'X':
        texto1.setText("Gana X")
       
    if botones[0].text() == 'X' and botones[4].text() == 'X' and botones[8].text() == 'X':
        texto1.setText("Gana X")
       
    if botones[2].text() == 'X' and botones[4].text() == 'X' and botones[6].text() == 'X':
        texto1.setText("Gana X")
   
#Pocisiones de O
    if botones[0].text() == '0' and botones[1].text() == '0' and botones[2].text() == '0':
        texto1.setText("Gana 0")
       
    if botones[3].text() == '0' and botones[4].text() == '0' and botones[5].text() == '0':
        texto1.setText("Gana 0")
     
    if botones[6].text() == '0' and botones[7].text() == '0' and botones[8].text() == '0':
        texto1.setText("Gana 0")
       
    if botones[0].text() == '0' and botones[3].text() == '0' and botones[6].text() == '0':
        texto1.setText("Gana 0")
     
    if botones[1].text() == '0' and botones[4].text() == '0' and botones[7].text() == '0':
        texto1.setText("Gana 0")
       
    if botones[2].text() == '0' and botones[5].text() == '0' and botones[8].text() == '0':
        texto1.setText("Gana 0")
       
    if botones[0].text() == '0' and botones[4].text() == '0' and botones[8].text() == '0':
        texto1.setText("Gana 0")
       
    if botones[2].text() == '0' and botones[4].text() == '0' and botones[6].text() == '0':
        texto1.setText("Gana 0")
 
jugador = 1
 
 
def jugar(boton_click):
    global jugador
    if jugador == 1 and boton_click.text() == '':
        boton_click.setText('X')
        jugador = 2
    elif jugador == 2 and boton_click.text() == '':
        boton_click.setText('O')
        jugador = 1
    checar()
 
 
for i, boton in enumerate(botones):
    boton.clicked.connect(lambda _, b=boton: jugar(b))
 
 
ventana.show()
sys.exit(aplicacion.exec_())