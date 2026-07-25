from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout
from PySide6.QtCore import Qt
import sys


class PB7Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PB7 Intelligence Studio")
        self.resize(1200, 800)

        # Main container
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Welcome message
        title = QLabel(
            "PB7 Intelligence Studio\n\n"
            "Mission Alpha Online\n\n"
            "🟢 GUI Engine Loaded\n"
            "🟢 Python Environment Ready\n"
            "🟢 Commander Hans Workspace Active"
        )

        title.setAlignment(Qt.AlignCenter)

        layout.addWidget(title)


def main():
    app = QApplication(sys.argv)

    window = PB7Window()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()