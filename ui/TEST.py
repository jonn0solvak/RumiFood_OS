import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QProgressBar
from PySide6.QtGui import QIcon


class MainWindow(QMainWindow):
    #appel au construct parent
    def __init__(self):
        super().__init__()
        #def le titre de la fenetre
        self.setWindowTitle("HELLO")

        #def une taille
        self.resize(1100,900)

        #def taille min de la fenetre
        self.setMinimumSize(400,300)

        #Add un icone de fenetre
        self.setWindowIcon(QIcon("ui\.ico\RF.ico"))

        #text qui s'affiche quand on passe la souris sur élément
        self.setToolTip("BOU")

        #afficher dans terminal la valeur de windowtitre
        print(self.windowTitle())

        #ajout d'une progres bar a la fenettre
        progress_bar = QProgressBar(self) 
        #modifer la position et forme
        progress_bar.setGeometry(10,10,300,30)
        #valeur max
        progress_bar.setMaximum(100)
        #valeur
        progress_bar.setValue(50)


if __name__ == "__main__":
    #Création de l'instance app
    app= QApplication(sys.argv)

    #instancier et afiché
    window= MainWindow()
    window.show()

    #on demare la boucle
    sys.exit(app.exec())
