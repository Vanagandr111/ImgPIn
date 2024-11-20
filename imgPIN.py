from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QMenu, QWidget, QCheckBox, QComboBox
from PyQt5.QtGui import QPixmap, QImage, QColor, QTransform
from PyQt5.QtCore import Qt, QTimer
from PIL import Image, ImageOps
import sys
import os
import tempfile

# Переменные с текстом для поддержания многоязычности
TEXT_RU = {
    "settings_title": "Настройки программы",
    "language_label": "Language/Язык:",
    "path_label": "Путь к папке с изображениями:",
    "path_placeholder": "Введите путь к папке с изображениями",
    "multiplier_label": "Множитель размера (умножаем на 100 x 100):",
    "multiplier_placeholder": "Введите множитель размера",
    "time_label": "Интервал времени в миллисекундах (по умолчанию 1000 миллисекунд):",
    "time_placeholder": "Введите интервал времени в миллисекундах",
    "opacity_label": "Уровень прозрачности (от 0.0 до 1.0):",
    "opacity_placeholder": "Введите уровень прозрачности",
    "mirror_checkbox": "Зеркально отображать изображение",
    "ok_button": "OK",
    "about_button": "Об авторе",
    "about_title": "Об авторе",
    "about_text": "Автор: Azzimov.dev\nGit: Vanagandr111\nSource code: https://github.com/Vanagandr111/ImgPIn",
    "control_window_title": "Контрольное окно",
    "toggle_clicks": "Отключить пропуск кликов/Disable skipping clicks",
    "close_button": "Закрыть/Close",
    "error_title": "Ошибка",
    "error_folder": "Указанная папка не существует.",
    "error_values": "Неверные значения множителя, времени или прозрачности.",
    "negativ": "Включить негатив",
    "nonegativ": "Отключить негатив",
    "return_to_main_menu_action": "Вернуться в главное меню"
}

TEXT_EN = {
    "settings_title": "Program Settings",
    "language_label": "Language:",
    "path_label": "Path to the folder with images:",
    "path_placeholder": "Enter the path to the folder with images",
    "multiplier_label": "Size multiplier (multiplied by 100 x 100):",
    "multiplier_placeholder": "Enter size multiplier",
    "time_label": "Interval time in milliseconds (default is 1000 milliseconds):",
    "time_placeholder": "Enter interval time in milliseconds",
    "opacity_label": "Opacity level (from 0.0 to 1.0):",
    "opacity_placeholder": "Enter opacity level",
    "mirror_checkbox": "Mirror the image",
    "ok_button": "OK",
    "about_button": "About",
    "about_title": "About",
    "about_text": "Author: Azzimov.dev\nGit: Vanagandr111\nSource code: https://github.com/Vanagandr111/ImgPIn",
    "control_window_title": "Control Window",
    "toggle_clicks": "Disable click through",
    "close_button": "Close",
    "error_title": "Error",
    "error_folder": "The specified folder does not exist.",
    "error_values": "Invalid multiplier, time, or opacity values.",
    "negativ": " toggle negative",
    "nonegativ": "turn off the negative",
    "return_to_main_menu_action": "return to main menu"
}


class InputDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.language = TEXT_RU  # Стандартный язык — русский
        self.setWindowTitle(self.language["settings_title"])
        self.layout = QVBoxLayout()

        # Выбор языка
        language_label = QLabel(self.language["language_label"])
        self.layout.addWidget(language_label)
        self.language_select = QComboBox(self)
        self.language_select.addItems(["Русский", "English"])
        self.language_select.currentIndexChanged.connect(self.update_language)
        self.layout.addWidget(self.language_select)

        # Поле для ввода пути
        path_label = QLabel(self.language["path_label"])
        self.layout.addWidget(path_label)
        self.path_input = QLineEdit(self)
        self.path_input.setPlaceholderText(self.language["path_placeholder"])
        self.path_input.setText("img")  # Стандартное значение
        self.layout.addWidget(self.path_input)

        # Поле для ввода множителя
        multiplier_label = QLabel(self.language["multiplier_label"])
        self.layout.addWidget(multiplier_label)
        self.multiplier_input = QLineEdit(self)
        self.multiplier_input.setPlaceholderText(self.language["multiplier_placeholder"])
        self.multiplier_input.setText("7")  # Стандартное значение
        self.layout.addWidget(self.multiplier_input)

        # Поле для ввода времени
        time_label = QLabel(self.language["time_label"])
        self.layout.addWidget(time_label)
        self.time_input = QLineEdit(self)
        self.time_input.setPlaceholderText(self.language["time_placeholder"])
        self.time_input.setText("1000")  # Стандартное значение
        self.layout.addWidget(self.time_input)

        # Поле для ввода уровня прозрачности
        opacity_label = QLabel(self.language["opacity_label"])
        self.layout.addWidget(opacity_label)
        self.opacity_input = QLineEdit(self)
        self.opacity_input.setPlaceholderText(self.language["opacity_placeholder"])
        self.opacity_input.setText("1.0")  # Стандартное значение
        self.layout.addWidget(self.opacity_input)

        # Чекбокс для зеркального отображения
        self.mirror_checkbox = QCheckBox(self.language["mirror_checkbox"], self)
        self.layout.addWidget(self.mirror_checkbox)

        # Кнопка подтверждения
        self.ok_button = QPushButton(self.language["ok_button"], self)
        self.ok_button.clicked.connect(self.accept)
        self.layout.addWidget(self.ok_button)

        # Кнопка об авторе
        self.about_button = QPushButton(self.language["about_button"], self)
        self.about_button.clicked.connect(self.show_about_dialog)
        self.layout.addWidget(self.about_button)

        self.setLayout(self.layout)
        
    def update_language(self):
        selected_language = self.language_select.currentText()
        if selected_language == "Русский":
            self.language = TEXT_RU
        else:
            self.language = TEXT_EN

        self.setWindowTitle(self.language["settings_title"])
        self.layout.itemAt(0).widget().setText(self.language["language_label"])
        self.language_select.setItemText(0, "Русский")
        self.language_select.setItemText(1, "English")
        self.layout.itemAt(2).widget().setText(self.language["path_label"])
        self.path_input.setPlaceholderText(self.language["path_placeholder"])
        self.layout.itemAt(4).widget().setText(self.language["multiplier_label"])
        self.multiplier_input.setPlaceholderText(self.language["multiplier_placeholder"])
        self.layout.itemAt(6).widget().setText(self.language["time_label"])
        self.time_input.setPlaceholderText(self.language["time_placeholder"])
        self.layout.itemAt(8).widget().setText(self.language["opacity_label"])
        self.opacity_input.setPlaceholderText(self.language["opacity_placeholder"])
        self.mirror_checkbox.setText(self.language["mirror_checkbox"])
        self.ok_button.setText(self.language["ok_button"])
        self.about_button.setText(self.language["about_button"])
        
    def get_values(self):
        return self.path_input.text(), self.multiplier_input.text(), self.time_input.text(), self.opacity_input.text(), self.mirror_checkbox.isChecked()

    def show_about_dialog(self):
        about_dialog = QMessageBox(self)
        about_dialog.setWindowTitle(self.language["about_title"])
        about_dialog.setText(self.language["about_text"])
        about_dialog.exec_()

class TransparentSticker(QLabel):
    def __init__(self, image_folder, width=100, height=100, multiplier=1, interval=1000, opacity=1.0, mirror=False):
        super().__init__()
        # Применяем множитель к стандартному размеру
        self.width = int(width * multiplier)
        self.height = int(height * multiplier)
        self.image_paths = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.img2'))]
        self.current_index = 0
        self.transparent_clicks_enabled = False  # Флаг для пропуска кликов
        self.control_window = None  # Окно управления для режима пропуска
        self.in_negative_mode = False  # Флаг для режима негатива
        self.mirror = mirror  # Флаг для зеркального отображения

        if not self.image_paths:
            raise FileNotFoundError("No images found in the specified folder.")

        # Установка изображения с изменением размера
        self.update_image()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowOpacity(opacity)  # Устанавливаем прозрачность
        self.setScaledContents(True)
        self.show()

        # Таймер для смены изображений
        self.timer = QTimer()
        self.timer.timeout.connect(self.change_image)
        self.timer.start(interval)

        # Перемещение окна
        self.old_pos = None
        self.setMouseTracking(True)

    def update_image(self):
        image_path = self.image_paths[self.current_index]
        if image_path.endswith('.img2'):
            # Если формат .img2, используем Pillow для конвертации
            img = Image.open(image_path).convert("RGBA")
            if self.in_negative_mode:
                r, g, b, a = img.split()
                rgb_img = Image.merge("RGB", (r, g, b))
                inverted_img = ImageOps.invert(rgb_img)
                img = Image.merge("RGBA", (inverted_img.split()[0], inverted_img.split()[1], inverted_img.split()[2], a))
            if self.mirror:
                img = ImageOps.mirror(img)
            
            # Создаем временный файл
            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
                temp_path = tmp.name
            img.save(temp_path)

            # Загружаем изображение в QPixmap
            pixmap = QPixmap(temp_path)

            # Удаляем временный файл
            os.remove(temp_path)
        else:
            img = QImage(image_path).convertToFormat(QImage.Format_ARGB32)
            if self.in_negative_mode:
                for y in range(img.height()):
                    for x in range(img.width()):
                        pixel = img.pixel(x, y)
                        color = QColor(pixel)
                        inverted_color = QColor(255 - color.red(), 255 - color.green(), 255 - color.blue(), color.alpha())
                        # Принудительно устанавливаем альфа-канал на 0 для черных пикселей
                        if inverted_color.red() == 0 and inverted_color.green() == 0 and inverted_color.blue() == 0:
                            inverted_color.setAlpha(0)
                        img.setPixel(x, y, inverted_color.rgba())
            pixmap = QPixmap.fromImage(img)
            if self.mirror:
                pixmap = pixmap.transformed(QTransform().scale(-1, 1))

        pixmap = pixmap.scaled(self.width, self.height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.setPixmap(pixmap)
        self.resize(pixmap.size())

    def change_image(self):
        self.current_index = (self.current_index + 1) % len(self.image_paths)
        self.update_image()
        # Принудительно обновляем изображение для устранения проблемы с прозрачностью на втором изображении
        self.repaint()
        self.setAttribute(Qt.WA_TranslucentBackground)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if not self.transparent_clicks_enabled:
                self.old_pos = event.globalPos()
        elif event.button() == Qt.RightButton:
            self.show_context_menu(event)

    def mouseMoveEvent(self, event):
        if self.old_pos is not None and not self.transparent_clicks_enabled:
            delta = event.globalPos() - self.old_pos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = None

    def show_context_menu(self, event):
        menu = QMenu(self)
        close_action = menu.addAction(TEXT_RU["close_button"])
        toggle_transparency_action = menu.addAction(TEXT_RU["toggle_clicks"] if not self.transparent_clicks_enabled else "Не пропускать щелчки левой кнопкой/Skip mouse clicks")
        toggle_negative_action = menu.addAction("Включить негатив/Toggle negativ" if not self.in_negative_mode else "Отключить негатив/Disable negativ")
        return_to_main_menu_action = menu.addAction("вернуться в меню/return to menu")
        action = menu.exec_(self.mapToGlobal(event.pos()))
        
        if action == close_action:
            self.close()
            QApplication.quit()  # Завершение приложения и очистка всех ресурсов
        elif action == toggle_transparency_action:
            self.toggle_transparent_clicks()
        elif action == toggle_negative_action:
            self.toggle_negative_mode()
        elif action == return_to_main_menu_action:
            self.return_to_main_menu()

    def toggle_transparent_clicks(self):
        self.transparent_clicks_enabled = not self.transparent_clicks_enabled
        if self.transparent_clicks_enabled:
            self.setWindowFlags(self.windowFlags() | Qt.WindowTransparentForInput)  # Включаем пропуск кликов
            self.show_control_window()  # Показать окно управления
        else:
            self.setWindowFlags(self.windowFlags() & ~Qt.WindowTransparentForInput)  # Выключаем пропуск кликов
            self.hide_control_window()  # Скрыть окно управления
        self.show()  # Обновляем отображение окна

    def toggle_negative_mode(self):
        self.in_negative_mode = not self.in_negative_mode
        self.update_image()  # Обновляем изображение

    def show_control_window(self):
        if self.control_window is None:
            self.control_window = QWidget()
            self.control_window.setWindowTitle(TEXT_RU["control_window_title"])
            layout = QVBoxLayout()
            toggle_button = QPushButton(TEXT_RU["toggle_clicks"], self.control_window)
            toggle_button.clicked.connect(self.toggle_transparent_clicks)
            layout.addWidget(toggle_button)
            close_button = QPushButton(TEXT_RU["close_button"], self.control_window)
            close_button.clicked.connect(self.close_application)
            layout.addWidget(close_button)
            self.control_window.setLayout(layout)
        self.control_window.show()
        self.control_window.activateWindow()

    def hide_control_window(self):
        if self.control_window is not None:
            self.control_window.hide()
    def return_to_main_menu(self):
        if self.control_window:
            self.control_window.close()
        self.close()
        main_dialog = InputDialog()
        if main_dialog.exec_() == QDialog.Accepted:
            folder_path, multiplier_str, interval_str, opacity_str, mirror = main_dialog.get_values()
            try:
                multiplier = float(multiplier_str) if multiplier_str else 1.0
                interval = int(interval_str) if interval_str else 1000
                opacity = float(opacity_str) if opacity_str else 1.0
                opacity = max(0.0, min(1.0, opacity))  # Ограничиваем значение от 0.0 до 1.0
                self.new_window = TransparentSticker(folder_path, width=100, height=100, multiplier=multiplier, interval=interval, opacity=opacity, mirror=mirror)
                self.new_window.show()
            except ValueError:
                QMessageBox.critical(None, TEXT_RU["error_title"], TEXT_RU["error_values"])


    def close_application(self):
        self.close()
        QApplication.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Создаем и показываем диалоговое окно
    dialog = InputDialog()
    if dialog.exec_() == QDialog.Accepted:
        folder_path, multiplier_str, interval_str, opacity_str, mirror = dialog.get_values()

        # Проверка ввода
        if not folder_path or not os.path.isdir(folder_path):
            QMessageBox.critical(None, TEXT_RU["error_title"], TEXT_RU["error_folder"])
        else:
            try:
                multiplier = float(multiplier_str) if multiplier_str else 1.0
                interval = int(interval_str) if interval_str else 1000
                opacity = float(opacity_str) if opacity_str else 1.0
                opacity = max(0.0, min(1.0, opacity))  # Ограничиваем значение от 0.0 до 1.0
                window = TransparentSticker(folder_path, width=100, height=100, multiplier=multiplier, interval=interval, opacity=opacity, mirror=mirror)
                sys.exit(app.exec_())
            except ValueError:
                QMessageBox.critical(None, "error_title", "error_values")
    else:
        print("Операция отменена. Cancelled")
