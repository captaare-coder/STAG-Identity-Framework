from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt


class ChatPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        label = QLabel(
            "PB7 AI Chat Workspace\n\n"
            "🤖 Awaiting AI connection"
        )

        label.setAlignment(Qt.AlignCenter)

        layout.addWidget(label)
        self.setLayout(layout)