from PyQt5 import QtWidgets, uic       

class ComboCascadaController:
    def __init__(self) -> None:
        calculator= QtWidgets.QApplication([])
        self.ventana= uic.loadUi("view/frmcombos_en_cascada.ui")
        self.ventana.show()
        calculator.exec()