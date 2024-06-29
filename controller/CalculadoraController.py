from PyQt5 import QtWidgets, uic 
from service import CalculadoraService      

class CalculadoraController:
    def __init__(self) -> None:
        calculator= QtWidgets.QApplication([])
        self.ventana= uic.loadUi("view/frmcalculator.ui")
        self.ventana.btn_calcular.clicked.connect(self.onclickbtn_calcular)
        self.ventana.show()
        calculator.exec()

    def onclickbtn_calcular(self):
        resultado= 0
        operacion= ""
        try:
            num1= int(self.ventana.txt_n1.text())
            num2= int(self.ventana.txt_n2.text())
            if self.ventana.rb_suma.isChecked():
                resultado= CalculadoraService.suma(num1, num2)
                operacion= "Suma"

            elif self.ventana.rb_resta.isChecked():
                resultado= CalculadoraService.resta(num1, num2)
                operacion= "Resta"

            elif self.ventana.rb_multiplica   .isChecked():
                resultado= CalculadoraService.multiplo(num1, num2)
                operacion= "Multiplica"

            elif self.ventana.rb_divide.isChecked():
                resultado= CalculadoraService.divide(num1, num2)
                operacion= "Divide"
            
            else:
                resultado= 0
                operacion= "Elegir Operación"
        except:
            operacion="Ingresar valores numericos"
            
        finally:
            self.ventana.lbl_resultado.setText(operacion+" =" +
                                               str(resultado))