#  Асинхронный парсер PEP

Парсер обрабатывает официальный сайт Python и выводит список PEP и их статистику в csv файлы.

# Технологии

* Python
* Scrapy

## Подготовка к локальному запуску

* Клонируем репозиторий на локальный компьютер ```git clone https://github.com/nmutovkin/scrapy_parser_pep.git```
* ```cd scrapy_parser_pep```
* Создаем и активируем виртуальное окружение python
    ```
    python -m venv venv
    source venv/bin/activate
    ```
* Устанавливаем зависимости ```pip install -r requirements.txt```

## Запуск парсера

Запуск: scrapy crawl pep

## Вывод

На выходе сгенерируются 2 csv файла:

1) Список PEP со статусами
2) Статистика по PEP с разными статусами
