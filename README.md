# ****
## Описание:
Домашняя работа по ООП.

## Описание:
1.  Есть два класса Product и Category, определенны свойства, добавлена инициализация и атрибуты.
2`load_categories_from_json` - Загружает категории и продукты из файла JSON по указанному пути.

## Установка:
1. Клонируйте репозиторий:
```https://github.com/AntonSmolyaninov/PythonProject/pull/2```
2. Установите зависимости:
- `poetry init` — инициализировать пакет в существующем проекте.
- `poetry new package-name` — создать новый проект.
- `poetry install (dependency name)` — первичная установка.
- `poetry update` — обновление зависимостей.
- `poetry remove (dependency name)` — удалить зависимость из проекта.
- `poetry show--tree` — посмотреть всё дерево зависимостей.
- `poetry show --latest`— посмотреть, последние ли версии используются в проекте.

### Установка теста:
- Установка через Poetry:
`poetry add --group dev pytest` 
- Установка pytest-cov:
`poetry add --group dev pytest-cov` - Метрика, которая показывает, какой процент кода программы был протестирован.

## Запуск 
### Запуск программы
`python3 main.py`
### Запуск тестов:
1. Запуск:
`pytest` - запуск всех тестов.

2. Команды, чтобы запустить тесты с оценкой покрытия:
- `pytest --cov` — при активированном виртуальном окружении.
- `poetry run pytest --cov` — через poetry.
- `pytest` - запуск всех тестов.
- `pytest --cov=src --cov-report=html` - сгенерировать отчет о покрытии в HTML-формате, где src — пакет c модулями, которые тестируем.

## Тестирование:
1. conftest.py - фикстуры для тестов.
2. test_Category.py - тестируем класс Category
3. test_Product.py - тестируем класс Product
4. test_utils.py - тестируем `load_categories_from_json`
