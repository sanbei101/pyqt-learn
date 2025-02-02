import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Calculator")
        self.resize(300, 400)

        self.result_field = QLineEdit(self)  # 显示结果的文本框
        self.result_field.setReadOnly(True)  # 只读，不允许直接编辑

        # 创建按钮
        self.buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C'  # 添加清除按钮
        ]

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.result_field)

        # 创建按钮布局
        button_layout = QHBoxLayout()
        for i, button in enumerate(self.buttons):
            btn = QPushButton(button)
            btn.clicked.connect(self.on_button_click)
            button_layout.addWidget(btn)

            # 每行有 4 个按钮
            if (i + 1) % 4 == 0:
                self.layout.addLayout(button_layout)
                button_layout = QHBoxLayout()  # 重置一行布局

        # 如果最后一行按钮不足 4 个，添加剩余的布局
        if button_layout.count() > 0:
            self.layout.addLayout(button_layout)

        self.setLayout(self.layout)

        self.current_input = ""  # 当前输入的内容
        self.operation = ""  # 当前操作符
        self.result = 0  # 计算结果

    def on_button_click(self):
        text = self.sender().text()

        if text in '0123456789.':
            self.current_input += text
            self.result_field.setText(self.current_input)
        elif text in '+-*/':
            if self.current_input:
                self.result = float(self.current_input)
                self.current_input = ""
            self.operation = text
        elif text == '=':
            if self.current_input:
                if self.operation:
                    if self.operation == '+':
                        self.result += float(self.current_input)
                    elif self.operation == '-':
                        self.result -= float(self.current_input)
                    elif self.operation == '*':
                        self.result *= float(self.current_input)
                    elif self.operation == '/':
                        try:
                            self.result /= float(self.current_input)
                        except ZeroDivisionError:
                            self.result_field.setText("Error")
                            return
                else:
                    self.result = float(self.current_input)
            self.result_field.setText(str(self.result))
            self.current_input = str(self.result)
            self.operation = ""
        elif text == 'C':  # 处理清除按钮点击事件
            self.current_input = ""
            self.operation = ""
            self.result = 0
            self.result_field.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())