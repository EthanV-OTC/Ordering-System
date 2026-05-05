import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QPushButton, QVBoxLayout, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Create Page 1
        page1 = QWidget()
        layout1 = QVBoxLayout()
        btn = QPushButton("Go to Page 2")
        btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        layout1.addWidget(QLabel("This is Page 1"))
        layout1.addWidget(btn)
        page1.setLayout(layout1)

        # Create Page 2
        page2 = QWidget()
        layout2 = QVBoxLayout()
        btn2 = QPushButton("Go to Page 1")
        btn2.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        layout2.addWidget(QLabel("This is Page 2"))
        layout2.addWidget(btn2)
        page2.setLayout(layout2)

        # Add pages to the stack
        self.stacked_widget.addWidget(page1) # Index 0
        self.stacked_widget.addWidget(page2) # Index 1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())