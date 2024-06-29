from PyQt5 import QtWidgets, uic       

class Menor_MayorController:
    def __init__(self) -> None:
        calculator= QtWidgets.QApplication([])
        self.ventana= uic.loadUi("view/frmmenor_mayor.ui")
        self.ventana.show()
        calculator.exec()