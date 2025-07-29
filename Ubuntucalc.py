import sys
import random
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QMessageBox
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt



def calculate(a, b, op):
    try:
        a, b = float(a), float(b)
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            if b == 0:
                return "🚫 Error: Division by zero."
            return a / b
        else:
            return "❌ Invalid operator."
    except ValueError:
        return "❌ Invalid number input."



def get_greeting():
    greetings = [
        "🌍 Karibu UbuntuCalc!",
        "👋 Sawubona! Welcome, friend!",
        "🙏 Ẹ káàbọ̀!",
        "❤️ Welcome to Ubuntu — I am because we are"
    ]
    return random.choice(greetings)



class CalculatorUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("UbuntuCalc Kenya — By Inyotum Afrika")
        self.setFixedSize(460, 370)
        self.setup_ui()

    def setup_ui(self):
        
        self.setStyleSheet("""
            QWidget {
                background-color: #FAF3E0;
                font-family: 'Segoe UI';
                color: #3B2F2F;
            }
            QLineEdit {
                background-color: #FFF8DC;
                border: 2px solid #A0522D;
                border-radius: 8px;
                padding: 8px;
                font-size: 14px;
            }
            QPushButton {
                background-color: #A0522D;
                color: white;
                font-weight: bold;
                padding: 12px;
                border-radius: 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #8B4513;
            }
            QLabel {
                font-size: 15px;
            }
        """)

        font = QFont()
        font.setPointSize(14)

       
        self.greeting_label = QLabel(get_greeting())
        self.greeting_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.greeting_label.setFont(QFont('Segoe UI', 16, weight=QFont.Weight.Bold))

        self.num1_input = QLineEdit()
        self.num1_input.setPlaceholderText("🌿 Enter the first number")

        self.operator_input = QLineEdit()
        self.operator_input.setPlaceholderText("✍️ Type +, -, * or /")
        self.operator_input.setMaxLength(1)
        self.operator_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.num2_input = QLineEdit()
        self.num2_input.setPlaceholderText("🌿 Enter the second number")

        self.calc_button = QPushButton("🧮 Perform Calculation")
        self.calc_button.clicked.connect(self.perform_calculation)

        self.result_label = QLabel("📝 Result will appear here.")
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_label.setFont(QFont('Segoe UI', 14, weight=QFont.Weight.Medium))

       
        self.num1_input.returnPressed.connect(lambda: self.operator_input.setFocus())
        self.operator_input.returnPressed.connect(lambda: self.num2_input.setFocus())
        self.num2_input.returnPressed.connect(self.perform_calculation)

      
        layout = QVBoxLayout()
        layout.addWidget(self.greeting_label)
        layout.addSpacing(10)
        layout.addWidget(self.num1_input)

        op_layout = QHBoxLayout()
        op_label = QLabel("Operation:")
        op_layout.addWidget(op_label)
        op_layout.addWidget(self.operator_input)
        layout.addLayout(op_layout)

        layout.addWidget(self.num2_input)
        layout.addSpacing(10)
        layout.addWidget(self.calc_button)
        layout.addSpacing(15)
        layout.addWidget(self.result_label)

        self.setLayout(layout)
        
        
    def perform_calculation(self):
        num1 = self.num1_input.text()
        num2 = self.num2_input.text()
        op = self.operator_input.text().strip()

        result = calculate(num1, num2, op)

        if isinstance(result, str) and "Error" in result:
            QMessageBox.warning(self, "Oops!", result)
        elif isinstance(result, str) and "Invalid" in result:
            QMessageBox.warning(self, "Try Again", result)
        else:
            message = f"🎉 {num1} {op} {num2} = {result:.4f}\nGreat job! Keep calculating!"
            self.result_label.setText(message)

       
        self.num1_input.clear()
        self.num2_input.clear()
        self.operator_input.clear()
        self.num1_input.setFocus()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorUI()
    window.show()
    sys.exit(app.exec())

