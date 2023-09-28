from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QWidget, QApplication
from memo_card_layout import*
from random import shuffle



 
window = QWidget()
w, h = 600,500
window.resize(w,h)
window.setWindowTitle('Memory Card')
window.move(100,100)




window.setLayout(main_vertical)


# ---- variants of answers ------
frm_question = 'Яблуко'
frm_right = 'apple'
frm_wrong1 = 'application'
frm_wrong2 = 'building'
frm_wrong3 = 'caterpillar'


radio_list = [r1, r2, r3, r4]
shuffle(radio_list)

ans = radio_list[0]
w1, w2, w3 = radio_list[1] , radio_list[2], radio_list [3]

def show_data():
    question.setText(frm_question)
    vidpovid.setText(frm_right)
    radio_list[0].setText(frm_right)
    radio_list[1].setText(frm_wrong1)
    radio_list[2].setText(frm_wrong2)
    radio_list[3].setText(frm_wrong3)
    
def answer_clicked():
    if answer.text() != 'Наступне питання':
        show_result()
show_data()
answer.clicked.connect(answer_clicked)

window.show()
app.exec_()


