from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton


class Sidebar(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        buttons = [
            "🏠 Dashboard",
            "🤖 AI Chat",
            "🧠 Prompt Builder",
            "🧪 Sandbox",
            "📚 Knowledge Vault",
            "⚙ Settings",
        ]

        for name in buttons:
            button = QPushButton(name)
            layout.addWidget(button)

        self.setLayout(layout)
        self.setFixedWidth(220)