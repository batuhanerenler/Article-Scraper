import sys
import textwrap
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QPlainTextEdit, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from newspaper import Article

class ScrapeAndFormatApp(QWidget):
    def __init__(self):
        super().__init__()

        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText("Enter the URL of the website you want to scrape")
        self.url_input.setMinimumHeight(40)
        self.url_input.setFont(QFont("Arial", 14))

        self.scrape_button = QPushButton("Scrape and Format Text", self)
        self.scrape_button.clicked.connect(self.scrape_and_format_text)
        self.scrape_button.setMinimumHeight(50)
        self.scrape_button.setFont(QFont("Arial", 16))

        self.result_text = QPlainTextEdit(self)
        self.result_text.setReadOnly(True)
        self.result_text.setFont(QFont("Arial", 12))

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.url_input)
        self.layout.addWidget(self.scrape_button)
        self.layout.addWidget(self.result_text)

    def format_text(self, texts, width=80):
        formatted_text = ""
        for text in texts:
            formatted_text += textwrap.fill(text, width=width)
            formatted_text += "\n\n"
        return formatted_text

    def save_text_to_file(self, text, filename="formatted_text.txt"):
        with open(filename, "a", encoding="utf-8") as f:
            f.write(text)

    def scrape_and_format_text(self):
        url = self.url_input.text()
        article = Article(url)
        article.download()
        article.parse()
        formatted_text = self.format_text([article.text])
        self.save_text_to_file(formatted_text)
        self.result_text.setPlainText(f"Formatted text saved to 'formatted_text.txt'")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = ScrapeAndFormatApp()
    main_window.setWindowTitle("Scrape and Format Text")
    main_window.show()
    sys.exit(app.exec_())
