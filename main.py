import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

from database import Database

db = Database()


class WelcomePage(QWidget):
    def __init__(self, stack):
        super().__init__()

        self.stack = stack
        self.setStyleSheet("background:#e9e9e9;")

        logo = QLabel(self)
        logo.setGeometry(65, 60, 260, 260)
        logo.setPixmap(
            QPixmap("assets/anonymous.png").scaled(
                260, 260,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        )

        title = QLabel("Anonymous VPN", self)
        title.setGeometry(80, 340, 250, 40)
        title.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
        """)

        desc = QLabel(
            "Самый надёжный VPN в России\nПроверка РКН пройдена",
            self
        )

        desc.setGeometry(40, 390, 310, 60)
        desc.setAlignment(Qt.AlignCenter)

        btn = QPushButton("Начать", self)

        btn.setGeometry(30, 720, 330, 55)

        btn.setStyleSheet("""
        QPushButton{
            background:black;
            color:white;
            border:none;
            border-radius:8px;
            font-size:18px;
            font-weight:bold;
        }
        """)

        btn.clicked.connect(
            lambda: self.stack.setCurrentIndex(1)
        )


class RegisterPage(QWidget):

    def __init__(self, stack):
        super().__init__()

        self.stack = stack

        self.setStyleSheet("""
        background:#e9e9e9;
        """)

        title = QLabel(
            "Добро пожаловать",
            self
        )

        title.setGeometry(
            40,
            120,
            320,
            50
        )

        title.setAlignment(
            Qt.AlignCenter
        )

        title.setStyleSheet("""
        font-size:26px;
        font-weight:bold;
        """)

        self.email = QLineEdit(self)

        self.email.setPlaceholderText(
            "Введите почту"
        )

        self.email.setGeometry(
            30,
            260,
            330,
            50
        )

        self.email.setStyleSheet("""
        QLineEdit{
            background:white;
            border:none;
            border-radius:25px;
            padding-left:15px;
            font-size:16px;
        }
        """)

        self.password = QLineEdit(self)

        self.password.setPlaceholderText(
            "Введите пароль"
        )

        self.password.setEchoMode(
            QLineEdit.Password
        )

        self.password.setGeometry(
            30,
            340,
            330,
            50
        )

        self.password.setStyleSheet("""
        QLineEdit{
            background:white;
            border:none;
            border-radius:25px;
            padding-left:15px;
            font-size:16px;
        }
        """)

        btn = QPushButton(
            "Начать",
            self
        )

        btn.setGeometry(
            30,
            700,
            330,
            55
        )

        btn.setStyleSheet("""
        QPushButton{
            background:black;
            color:white;
            border:none;
            border-radius:8px;
            font-size:18px;
            font-weight:bold;
        }
        """)

        btn.clicked.connect(
            self.register
        )

        login = QPushButton(
            "Уже есть аккаунт? Войти",
            self
        )

        login.setGeometry(
            90,
            770,
            220,
            30
        )

        login.setStyleSheet("""
        border:none;
        background:transparent;
        color:gray;
        """)

        login.clicked.connect(
            lambda:
            self.stack.setCurrentIndex(2)
        )

    def register(self):

        if db.register(
            self.email.text(),
            self.password.text()
        ):
            QMessageBox.information(
                self,
                "Успех",
                "Регистрация завершена"
            )

            self.stack.setCurrentIndex(2)

        else:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Пользователь уже существует"
            )


class LoginPage(QWidget):

    def __init__(self, stack):
        super().__init__()

        self.stack = stack

        self.setStyleSheet("""
        background:#e9e9e9;
        """)

        title = QLabel(
            "Ты вернулся!",
            self
        )

        title.setGeometry(
            80,
            110,
            250,
            50
        )

        title.setAlignment(
            Qt.AlignCenter
        )

        title.setStyleSheet("""
        font-size:26px;
        font-weight:bold;
        """)

        img = QLabel(self)

        img.setGeometry(
            105,
            190,
            180,
            180
        )

        img.setPixmap(
            QPixmap(
                "assets/question.png"
            ).scaled(
                180,
                180,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        )

        self.email = QLineEdit(self)

        self.email.setPlaceholderText(
            "Введите почту"
        )

        self.email.setGeometry(
            30,
            460,
            330,
            50
        )

        self.email.setStyleSheet("""
        QLineEdit{
            background:white;
            border:none;
            border-radius:25px;
            padding-left:15px;
            font-size:16px;
        }
        """)

        self.password = QLineEdit(self)

        self.password.setPlaceholderText(
            "Введите пароль"
        )

        self.password.setEchoMode(
            QLineEdit.Password
        )

        self.password.setGeometry(
            30,
            540,
            330,
            50
        )

        self.password.setStyleSheet("""
        QLineEdit{
            background:white;
            border:none;
            border-radius:25px;
            padding-left:15px;
            font-size:16px;
        }
        """)

        btn = QPushButton(
            "Начать",
            self
        )

        btn.setGeometry(
            30,
            690,
            330,
            55
        )

        btn.setStyleSheet("""
        QPushButton{
            background:black;
            color:white;
            border:none;
            border-radius:8px;
            font-size:18px;
            font-weight:bold;
        }
        """)

        btn.clicked.connect(
            self.login
        )

    def login(self):

        if db.login(
            self.email.text(),
            self.password.text()
        ):
            self.stack.setCurrentIndex(3)

        else:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Неверный логин или пароль"
            )


class VPNPage(QWidget):

    def __init__(self):
        super().__init__()

        self.connected = False
        self.seconds = 0

        self.timer = QTimer()
        self.timer.timeout.connect(
            self.update_time
        )

        self.setStyleSheet("""
        background:#efefef;
        """)

        header = QFrame(self)

        header.setGeometry(
            0,
            0,
            390,
            170
        )

        header.setStyleSheet("""
        background:black;
        """)

        user = QLabel(header)

        user.setGeometry(
            170,
            25,
            50,
            50
        )

        user.setPixmap(
            QPixmap(
                "assets/user.png"
            ).scaled(
                50,
                50,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        )

        welcome = QLabel(
            "Добро пожаловать, Аноним.",
            header
        )

        welcome.setGeometry(
            70,
            100,
            260,
            30
        )

        welcome.setStyleSheet("""
        color:white;
        font-size:18px;
        font-weight:bold;
        """)

        self.status = QLabel(
            "Not connected",
            self
        )

        self.status.setGeometry(
            40,
            240,
            180,
            30
        )

        self.status.setStyleSheet("""
        font-size:20px;
        font-weight:bold;
        """)

        self.time = QLabel(
            "00:00:00",
            self
        )

        self.time.setGeometry(
            260,
            240,
            100,
            30
        )

        self.power = QPushButton(
            self
        )

        self.power.setGeometry(
            95,
            320,
            200,
            200
        )

        self.power.setFlat(True)

        self.power.clicked.connect(
            self.toggle
        )

        self.flag = QLabel(self)

        self.flag.setGeometry(
            40,
            640,
            30,
            30
        )

        self.flag.setPixmap(
            QPixmap(
                "assets/netherlands.png"
            ).scaled(
                30,
                30,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        )

        country = QLabel(
            "Netherlands",
            self
        )

        country.setGeometry(
            80,
            640,
            160,
            30
        )

        country.setStyleSheet("""
        font-size:18px;
        font-weight:bold;
        """)

        self.refresh()

    def refresh(self):

        if self.connected:

            self.power.setIcon(
                QIcon(
                    "assets/stop.png"
                )
            )

            self.status.setText(
                "Connected"
            )

            self.status.setStyleSheet("""
            color:#2ecc71;
            font-size:20px;
            font-weight:bold;
            """)

        else:

            self.power.setIcon(
                QIcon(
                    "assets/start.png"
                )
            )

            self.status.setText(
                "Not connected"
            )

            self.status.setStyleSheet("""
            color:black;
            font-size:20px;
            font-weight:bold;
            """)

        self.power.setIconSize(
            QSize(200, 200)
        )

    def toggle(self):

        self.connected = not self.connected

        if self.connected:

            self.seconds = 0

            self.timer.start(
                1000
            )

        else:

            self.timer.stop()

            self.time.setText(
                "00:00:00"
            )

        self.refresh()

    def update_time(self):

        self.seconds += 1

        h = self.seconds // 3600
        m = (self.seconds % 3600) // 60
        s = self.seconds % 60

        self.time.setText(
            f"{h:02}:{m:02}:{s:02}"
        )


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "Anonymous VPN"
        )

        self.setFixedSize(
            390,
            844
        )

        self.stack = QStackedWidget()

        self.stack.addWidget(
            WelcomePage(self.stack)
        )

        self.stack.addWidget(
            RegisterPage(self.stack)
        )

        self.stack.addWidget(
            LoginPage(self.stack)
        )

        self.stack.addWidget(
            VPNPage()
        )

        self.setCentralWidget(
            self.stack
        )


app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())
