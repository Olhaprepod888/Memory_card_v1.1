from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*

app = QApplication([])

#---pushbuttons -------
menu = QPushButton('Меню')
rest = QPushButton('Відпочити')
answer = QPushButton('Відповісти')

#----- radiobuttons ----
r1 = QRadioButton()
r2 = QRadioButton()
r3 = QRadioButton()
r4 = QRadioButton()



radio_group = QButtonGroup()#радіогрупа

radio_group.addButton(r1)
radio_group.addButton(r2)
radio_group.addButton(r3)
radio_group.addButton(r4)
#---- labels ----
hv = QLabel('minuts')
question = QLabel('???')

#---- timer------
timer = QSpinBox()
timer.setValue(30)

#------ box1 ------
box1 = QGroupBox ('Variants of answer:')
v1 = QVBoxLayout()
v2= QVBoxLayout()

v1.addWidget(r1)
v1.addWidget(r2)
v2.addWidget(r3)
v2.addWidget(r4)

h = QHBoxLayout()#add to horizontal layout vertical  layouts
h.addLayout(v1)
h.addLayout(v2)

box1.setLayout(h)

#----- create 4 horizontal layouts ----
hor1 = QHBoxLayout()
hor2 = QHBoxLayout()
hor3 = QHBoxLayout()
hor4 = QHBoxLayout()

hor1.addWidget(menu)#layout_1
hor1.addStretch()
hor1.addWidget(rest)
hor1.addWidget(timer)
hor1.addWidget(hv)

hor2.addWidget(question)#layout_2

hor3.addWidget(box1)# layout_3

hor4.addWidget(answer)



#---- create main vertical layout -----

main_vertical = QVBoxLayout()

main_vertical.addLayout(hor1, stretch = 1)
main_vertical.addLayout(hor2, stretch = 2)
main_vertical.addLayout(hor3, stretch = 8)
main_vertical.addStretch()
main_vertical.addLayout(hor4, stretch = 1)
main_vertical.addStretch()
#main_vertical.setSpacing(5)



#------------ RESULT window -------
box2 = QGroupBox('Результат:')
right_wrong = QLabel('dont know yet!))) ')
vidpovid = QLabel('apple')

v_result = QVBoxLayout()
v_result.addWidget(right_wrong, alignment = (Qt.AlignLeft|Qt.AlignTop))

v_result.addWidget(vidpovid, alignment=Qt.AlignCenter, stretch=2)


box2.setLayout(v_result)
hor3.addWidget(box2)
box2.hide()

#---------------------------------

def show_result():
    box1.hide()
    answer.setText('Наступне питання')
    box2.show()
    
    
def show_question():
    box1.show()
    box2.hide()
    answer.setText('Відповісти')

    #--- сбрасуємо минулі вибори ---
    radio_group.setExclusive(False)
    r1.setChecked(False)
    r2.setChecked(False)
    r3.setChecked(False)
    r4.setChecked(False)
    radio_group.setExclusive(True)

   


























