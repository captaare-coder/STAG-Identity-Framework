from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QStackedWidget
)

from gui.sidebar import Sidebar

from pages.dashboard_page import DashboardPage
from pages.chat_page import ChatPage
from pages.sandbox_page import SandboxPage
from pages.settings_page import SettingsPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PB7 Intelligence Studio")
        self.resize(1400, 900)

        container = QWidget()
        layout = QHBoxLayout()

        self.pages = QStackedWidget()

        self.page_map = {
            "dashboard": DashboardPage(),
            "chat": ChatPage(),
            "sandbox": SandboxPage(),
            "settings": SettingsPage(),
        }

        for page in self.page_map.values():
            self.pages.addWidget(page)

        self.sidebar = Sidebar(self.switch_page)

        layout.addWidget(self.sidebar)
        layout.addWidget(self.pages)

        container.setLayout(layout)

        self.setCentralWidget(container)

        self.switch_page("dashboard")


    def switch_page(self, name):
        self.pages.setCurrentWidget(
            self.page_map[name]
        )