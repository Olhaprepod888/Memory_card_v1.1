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




window.show()
app.exec_()


