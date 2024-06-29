from PyQt5 import QtWidgets, uic       
from service import MayorMenorService
class Menor_MayorController:
    def __init__(self) -> None:
        calculator= QtWidgets.QApplication([])
        self.ventana= uic.loadUi("view/frmmenor _mayor.ui")
        self.ventana.btn_calcular.clicked.connect(self.onclickbtn_calcular)
        self.ventana.show()
        calculator.exec()
    def onclickbtn_calcular(self):
        resultado= 0
        try:
            n1= int(self.ventana.txt_n1.text())
            n2= int(self.ventana.txt_n2.text())
            n3= int(self.ventana.txt_n3.text())
            n4= int(self.ventana.txt_n4.text())
            if self.ventana.rb_mayor.isChecked():
                resultado= MayorMenorService.mayor(n1, n2, n3, n4)

            elif self.ventana.rb_menor.isChecked():
                resultado= MayorMenorService.menor(n1, n2, n3, n4)

            else:
                resultado= 0
        except:
            resultado= 0

        finally:
            self.ventana.lbl_resultado.setText(str(resultado))
