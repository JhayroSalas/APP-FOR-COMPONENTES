from PyQt5 import QtWidgets, uic       

class ListaDesplegableController:
    def __init__(self) -> None:
        calculator= QtWidgets.QApplication([])
        self.ventana= uic.loadUi("view/frmlista_desplegable.ui")
        self.ventana.show()
        calculator.exec()