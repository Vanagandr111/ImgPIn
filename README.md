# ImgPIn
Краткий гайд для пользователя (User Guide)

## Русский

Запуск: Откройте imgPIN.py/start.bat/imgPIN.exe для настройки и отображения изображений.

Плавающее окно: Окно остается поверх всех окон, его можно перемещать.

Зеркальное и негатив: Используйте контекстное меню (правый клик) для зеркального отображения и включения негатива.

Пропуск кликов: Правый клик по изображению -> "Пропускать щелчки". Для управления появится отдельное окно.

Закрытие приложения: Правый клик по изображению -> "Закрыть".

Слайдшоу: Укажите название папки с изображениями. Код автоматически переберет изображения по порядку, используя установленный вами параметр скорости.

Формат .img2: Используйте для избежания автоматического добавления изображения в системные библиотеки Windows.

## English

Launch: Open imgPIN.py to configure and display images.

Floating Window: The window stays on top of others and can be moved.

Mirror & Negative: Use the context menu (right-click) to mirror or enable negative.

Click-Through Mode: Right-click -> "Enable click-through". A control window will appear for managing this mode.

Closing the Application: Right-click on the image -> "Close".

Slideshow: Specify the folder name containing images. The code will automatically cycle through the images in order using the speed parameter you set.

Format .img2: Use to prevent images from being automatically added to Windows system libraries.

RU
# Приложение ImgPIn

## Обзор

ImgPIn — это настольное приложение на базе PyQt5, предназначенное для отображения и манипулирования изображениями в прозрачном, плавающем окне. Оно предоставляет функции настройки размера, прозрачности, переворота изображений и их отображения в негативе. Приложение легко настраивается для загрузки изображений из указанной папки и смены изображений с заданным интервалом. Проект также поддерживает многоязычный интерфейс (английский и русский).

## Основные функции

- **Выбор языка (Русский/Английский)**: Интерфейс приложения может отображаться на русском или английском языке в зависимости от предпочтений пользователя, что делает его более доступным для пользователей обоих языков.
- **Настраиваемые параметры изображений**: Пользователи могут указать путь к папке с изображениями, задать множитель размера изображения, интервал для смены изображений и уровень прозрачности.
- **Отражение изображений**: Пользователи могут включать или отключать зеркальный эффект для горизонтального переворота изображений.
- **Негативный фильтр**: Пользователи могут переключать цветовой фильтр негатив для отображаемых изображений.
- **Плавающее и безрамочное окно**: Изображения отображаются в прозрачном, безрамочном окне, которое остается поверх других окон. Это позволяет ненавязчиво отображать изображения в любом месте экрана.
- **Прозрачность для кликов**: Пользователи могут включать или отключать возможность пропуска кликов через окно изображения, делая окно прозрачным для событий мыши. Эта функция полезна для сохранения изображения на экране без вмешательства в работу с другими приложениями.
- **Окно управления**: Окно управления позволяет пользователям управлять функцией пропуска кликов и легко закрывать приложение.

## Компоненты и их функции

### Класс `InputDialog`
Класс `InputDialog` отвечает за отображение начального окна настроек для пользователя. Он включает следующие компоненты:

- **Выбор языка (`QComboBox`)**: Позволяет пользователю выбрать язык интерфейса.
- **Поле ввода пути (`QLineEdit`)**: Позволяет пользователю указать путь к папке с изображениями для отображения.
- **Поле ввода множителя размера (`QLineEdit`)**: Позволяет пользователю задать множитель размера изображения, который масштабирует изображение соответствующим образом.
- **Поле ввода интервала времени (`QLineEdit`)**: Позволяет пользователю задать интервал времени в миллисекундах для смены изображений.
- **Поле ввода уровня прозрачности (`QLineEdit`)**: Позволяет пользователю задать уровень прозрачности окна изображения (от 0.0 до 1.0).
- **Чекбокс зеркального отображения (`QCheckBox`)**: Позволяет пользователю включать или отключать зеркальный эффект на изображениях.
- **Кнопки**:
  - **Кнопка "OK" (`QPushButton`)**: Применяет настройки и запускает основное окно с изображением.
  - **Кнопка "Об авторе" (`QPushButton`)**: Открывает диалоговое окно с информацией об авторе и ссылкой на репозиторий GitHub.

### Класс `TransparentSticker`
Класс `TransparentSticker` отвечает за основное отображение изображений в прозрачном окне. Он выполняет следующие функции:

- **Загрузка и отображение изображений**: Загружает изображения из указанной папки и отображает их в безрамочном, плавающем окне.
- **Трансформация изображений**:
  - **Зеркальный эффект**: Отражает изображения горизонтально, если включено.
  - **Негативный фильтр**: Применяет негативный фильтр к изображению, если включено.
- **Таймер для смены изображений (`QTimer`)**: Меняет отображаемое изображение с заданным пользователем интервалом.
- **Взаимодействие с мышью**:
  - **Перетаскивание для перемещения**: Окно изображения можно перемещать, перетаскивая его левой кнопкой мыши.
  - **Контекстное меню при правом клике**: Предоставляет контекстное меню с опциями закрытия приложения, переключения прозрачности для кликов, включения/выключения негативного фильтра и возвращения в главное меню.
- **Прозрачность для кликов**: Позволяет пользователям включать или отключать возможность пропуска кликов через окно, делая его прозрачным для событий мыши.
- **Окно управления**: Показывает отдельное окно управления при включении прозрачности для кликов, позволяющее пользователю легко управлять прозрачностью или закрыть приложение.

## Инструкции по использованию

1. **Запуск приложения**: Запустите скрипт `imgPIN.py`, чтобы открыть окно настроек.
2. **Настройка параметров**: В начальном диалоговом окне укажите следующие параметры:
   - Выберите язык интерфейса.
   - Укажите путь к папке с изображениями.
   - Установите множитель размера для изображений.
   - Установите интервал для смены изображений (в миллисекундах).
   - Установите уровень прозрачности.
   - Установите флажок, если нужно отразить изображения зеркально.
3. **Начало отображения изображений**: Нажмите кнопку "OK", чтобы применить настройки и открыть окно с изображением.
4. **Управление изображениями**: Изображения будут отображаться в безрамочном окне, которое можно перемещать, перетаскивая. Щелчок правой кнопкой мыши по окну изображения открывает контекстное меню для управления настройками, такими как переключение негативного фильтра, включение/отключение прозрачности для кликов или закрытие приложения.
5. **Информация об авторе**: Нажмите кнопку "Об авторе", чтобы просмотреть информацию об авторе и получить доступ к исходному коду на GitHub.

## Технические детали

- **Используемые библиотеки**:
  - **PyQt5**: Предоставляет компоненты GUI для создания окон, диалогов, меток, кнопок и т.д.
  - **Pillow (PIL)**: Используется для работы с изображениями, такими как зеркальное отображение, преобразование в негатив и управление прозрачностью.
- **Работа с временными файлами изображений**: При применении трансформаций создаются и удаляются временные файлы для обеспечения корректной работы с разными форматами изображений.
- **Поддержка многоязычности**: Приложение поддерживает многоязычный интерфейс с хранением всего текста в словарях (`TEXT_RU` и `TEXT_EN`). Это позволяет легко добавлять поддержку других языков, если потребуется.

## Возможные улучшения

- **Дополнительные параметры обработки изображений**: Можно добавить дополнительные фильтры и преобразования.
- **Расширенная поддержка форматов файлов**: Можно добавить поддержку других форматов изображений, помимо `.png`, `.jpg` и `.img2`.
- **Профили пользователей**: Возможность сохранения настроек пользователей для разных сессий.

## Автор
- **Автор**: Azzimov.dev
- **GitHub**: [Vanagandr111](https://github.com/Vanagandr111)
- **Исходный код**: [Репозиторий ImgPIn](https://github.com/Vanagandr111/ImgPIn)


ENG
# ImgPIn Application

## Overview

ImgPIn is a PyQt5-based desktop application designed to allow users to display and manipulate images in a transparent, floating window. It provides features for adjusting size, transparency, flipping images, and displaying them in a negative filter. The application can be easily configured to load images from a specified folder and change images in a predefined interval. The project also supports multilingual user interfaces (English and Russian).

## Features

- **Language Selection (Russian/English)**: The application interface can be displayed in either Russian or English, depending on the user's preference. This makes it more accessible to speakers of both languages.
- **Customizable Image Settings**: Users can specify the path to a folder with images, a size multiplier for the image, an interval to change the image, and a transparency level.
- **Mirror Images**: Users can enable or disable a mirroring effect to flip images horizontally.
- **Negative Filter**: Users can toggle a negative color filter for the displayed images.
- **н**uture Improvements

* **More Image Manipulation Options**: Additional filters and transformations could be provided.
* **Extended File Format Support**: Additional image formats could be supported beyond `.png`, `.jpg`, and `.img2`.
* **User Profiles**: Allow saving user preferences for different sessions.

## Author

- **Author**: Azzimov.dev
- **GitHub**: [Vanagandr111](https://github.com/Vanagandr111)
- **Source Code**: [ImgPIn Repository](https://github.com/Vanagandr111/ImgPIn)

