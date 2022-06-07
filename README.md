## Сервис создания коротких ссылок

### 1. Вы можете:
- Создать свой вариант замены для длинной ссылки (максимум 16 символов)
- Дать программе возможност придумать свой вариант (ровно 6 символов)
- Запомнить короткий вариант
- Ввести короткую ссылку по памяти и перейти куда вам нужно

### 2. Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/sdvkam/yacut.git
```
```
cd yacut
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv venv
```
* Если у вас Linux/MacOS
    ```
    source venv/bin/activate
    ```
* Если у вас windows
    ```
    source venv/scripts/activate
    ```
Обновить pip:
```
python3 -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Создать базу для сохранения данных
```
flask db upgrade
```
Запустит проект
```
flask run
```
### 3. Технологии
- Python 3.7
- Flask 2.0
- SQLAlchemy (через flask-sqlalchemy)
- SQLite
- Bootstrap
