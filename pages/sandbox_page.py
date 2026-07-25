from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt


class SandboxPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        label = QLabel(
            "PB7 Sandbox\n\n"
            "🧪 Experimental Workspace Ready"
        )

        label.setAlignment(Qt.AlignCenter)

        layout.addWidget(label)
        self.setLayout(layout)