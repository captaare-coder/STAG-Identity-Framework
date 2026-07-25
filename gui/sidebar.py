from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton


class Sidebar(QWidget):
    def __init__(self, switch_page):
        super().__init__()

        self.switch_page = switch_page

        layout = QVBoxLayout()

        buttons = [
            ("🏠 Dashboard", "dashboard"),
            ("🤖 AI Chat", "chat"),
            ("🧪 Sandbox", "sandbox"),
            ("⚙ Settings", "settings"),
        ]

        for text, page in buttons:
            button = QPushButton(text)
            button.clicked.connect(
                lambda checked=False, p=page: self.switch_page(p)
            )
            layout.addWidget(button)

        self.setLayout(layout)
        self.setFixedWidth(220)