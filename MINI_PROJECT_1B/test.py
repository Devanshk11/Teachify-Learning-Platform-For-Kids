from PyQt5 import QtWidgets, uic, QtCore
import sys

class Main_UI(QtWidgets.QMainWindow):
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		uic.loadUi("main.ui", self)
		self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		self.pushButton.clicked.connect(lambda: MainApp.exit())
		self.pushButton_2.clicked.connect(lambda: self.showFullScreen())
		self.pushButton_3.clicked.connect(lambda: self.showMinimized())
		self.frame_2.mouseMoveEvent = self.MoveWindow


		self.toolButton.clicked.connect(lambda: self.Side_Menu_Def_0())

		QtWidgets.QSizeGrip(self.frame_6)

		self.frame_5.mousePressEvent = self.Side_Menu_Def_1

	def Side_Menu_Def_0(self):
		if self.frame_4.width() <= 50:
			self.animation1 = QtCore.QPropertyAnimation(self.frame_4, b"maximumWidth")
			self.animation1.setDuration(500)
			self.animation1.setStartValue(35)
			self.animation1.setEndValue(110)
			self.animation1.setEasingCurve(QtCore.QEasingCurve.InOutSine)
			self.animation1.start()

			self.animation2 = QtCore.QPropertyAnimation(self.frame_4, b"minimumWidth")
			self.animation2.setDuration(500)
			self.animation2.setStartValue(35)
			self.animation2.setEndValue(110)
			self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutSine)
			self.animation2.start()

		else:
			self.animation1 = QtCore.QPropertyAnimation(self.frame_4, b"maximumWidth")
			self.animation1.setDuration(500)
			self.animation1.setStartValue(110)
			self.animation1.setEndValue(35)
			self.animation1.setEasingCurve(QtCore.QEasingCurve.InOutSine)
			self.animation1.start()

			self.animation2 = QtCore.QPropertyAnimation(self.frame_4, b"minimumWidth")
			self.animation2.setDuration(500)
			self.animation2.setStartValue(110)
			self.animation2.setEndValue(35)
			self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutSine)
			self.animation2.start()

	def Side_Menu_Def_1(self, Event):
		if Event.button() == QtCore.Qt.LeftButton:
			if self.frame_4.width() >= 50:
				self.animation1 = QtCore.QPropertyAnimation(self.frame_4, b"maximumWidth")
				self.animation1.setDuration(500)
				self.animation1.setStartValue(110)
				self.animation1.setEndValue(35)
				self.animation1.setEasingCurve(QtCore.QEasingCurve.InOutSine)
				self.animation1.start()

				self.animation2 = QtCore.QPropertyAnimation(self.frame_4, b"minimumWidth")
				self.animation2.setDuration(500)
				self.animation2.setStartValue(110)
				self.animation2.setEndValue(35)
				self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutSine)
				self.animation2.start()
			else:
				pass


	def MoveWindow(self, event):
		if self.isMaximized() == False:
			self.move(self.pos() + event.globalPos() - self.clickPosition)
			self.clickPosition = event.globalPos()
			event.accept()
			pass
	def mousePressEvent(self, event):
		self.clickPosition = event.globalPos()
		pass
if __name__ == "__main__":
	MainApp = QtWidgets.QApplication(sys.argv)
	App = Main_UI()
	App.show()
	sys.exit(MainApp.exec_())
