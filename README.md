# ****
## Описание:
Домашняя работа по ООП.

## Описание:
1.  Есть два класса Product и Category, определенны свойства, добавлена инициализация и атрибуты.
2. `load_categories_from_json` - Загружает категории и продукты из файла JSON по указанному пути.
3. `def add_product` - добовляет продукт в список товаров.
4. `def products` - геттер который выводит список товаров в виде строк.
5. `def new_product` - Создаёт новый продукт, если такого ещё нет среди products. Если товар с таким же именем уже есть — обновляет количество и (если нужно) цену.
6. `def price` - Геттер для атрибута цены.
7. `price.setter` - Сеттер для атрибута цены с проверкой.
8. product_iterator.py - модуль с вспомогательным классом который переберает товары одной категории.
9. smartphone.py - выделенная категория смартфоны.
10. law grass.py - выделенная категория трава гаронна.


## Установка:
1. Клонируйте репозиторий:
```https://github.com/AntonSmolyaninov/Home_work_OOP```
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
- `pytest --cov=src --cov-report=xml:coverage.xml` - запись отчета о покрытии в coverage.xml

## Тестирование:
1. conftest.py - фикстуры для тестов.
2. test_Category.py - тестируем класс Category
3. test_Product.py - тестируем класс Product
4. test_utils.py - тестируем `load_categories_from_json`
5. test_product_iterator.py - тестируем класс ProductIterator.
6. test_smartphone.py - тестирует класс наследник smartphone.
7. test_lawngrass.py - тестирует класс наследник lawngrass py

