# QRkot_spreadseets

Приложение для Благотворительного фонда поддержки котиков QRKot. 
Фонд собирает пожертвования на различные целевые проекты: медицинское обслуживание нуждающихся хвостатых, обустройство кошачьей колонии в подвале, корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.

В Фонде QRKot может быть открыто несколько целевых проектов. После того, как нужная сумма собрана — проект закрывается.
Все пожертвования идут в проект, открытый раньше других; когда этот проект набирает необходимую сумму и закрывается — пожертвования начинают поступать в следующий проект.

Каждый пользователь может сделать пожертвование и сопроводить его комментарием. Пожертвования вносятся в фонд, а не в конкретный проект. Если пожертвование больше нужной для проекта суммы или в Фонде нет открытых проектов — оставшиеся деньги ждут открытия следующего проекта. При создании нового проекта все неинвестированные пожертвования автоматически вкладываются в новый проект.

Целевые проекты создаются администраторами сайта. 
Любой пользователь может видеть список всех проектов, включая требуемые и уже внесенные суммы. Зарегистрированные пользователи могут отправлять пожертвования и просматривать список своих пожертвовани

Приложение имеет возможность формировать отчёт в Google-таблице. В таблицу включены закрытые проекты, отсортированные по скорости сбора средств — от тех, что закрылись быстрее всего, до тех, что долго собирали нужную сумму.

## Стек технологий

[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/-FastAPI-464646?style=flat&logo=FastAPI&logoColor=ffffff&color=043A6B)](https://fastapi.tiangolo.com/)
[![FastAPI-Users](https://img.shields.io/badge/-FastAPI_Users-464646?style=flat&logo=FastAPI&logoColor=ffffff&color=043A6B)](https://pypi.org/project/fastapi-users/)
[![Pydantic](https://img.shields.io/badge/-Pydantic-464646?style=flat&logo=Pydantic&logoColor=ffffff&color=043A6B)](https://docs.pydantic.dev/)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-464646?style=flat&logo=SQLAlchemy%20REST%20Framework&logoColor=ffffff&color=043A6B)](https://www.sqlalchemy.org/)
[![aiosqlite](https://img.shields.io/badge/-aiosqlite-464646?style=flat&logo=aiosqlite&logoColor=ffffff&color=043A6B)](https://pypi.org/project/aiosqlite/)
[![Alembic](https://img.shields.io/badge/-Alembic-464646?style=flat&logo=Alembic&logoColor=ffffff&color=043A6B)](https://alembic.sqlalchemy.org/en/latest/)
[![GoogleAPI](https://img.shields.io/badge/-GoogleAPI-464646?style=flat&logo=GoogleAPI&logoColor=ffffff&color=043A6B)](https://support.google.com/googleapi/?hl=en#topic=7014522)

## Запуск проекта

### Клонировать репозиторий:
```
git clone https://github.com/Jullitk/cat_charity_fund.git
```
### Cоздать и активировать в репозитории виртуальное окружение:
```
python -m venv venv
```
Для Linux
    ```
    source venv/bin/activate
    ```
    
Для Windows
    ```
    source venv/Scripts/activate
    ```
### Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
### Создать в корне файл .env и заполнить его по образцу:
```
APP_TITLE=Кошачий благотворительный фонд (0.1.0)
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=secret
FIRST_SUPERUSER_EMAIL=example@example.ru
FIRST_SUPERUSER_PASSWORD=password
TYPE = example
PROJECT_ID = example
PRIVATE_KEY_ID = example
PRIVATE_KEY = example
CLIENT_EMAIL = example
CLIENT_ID = example
AUTH_URI = example
TOKEN_URI = example
AUTH_PROVIDER_X509_CERT_URL = example
CLIENT_X509_CERT_URL = example
UNIVERSE_DOMAIN = example
EMAIL = 'example@gmail.com'
```
### Выполнить миграции:
```
alembic upgrade head
```
### Запустить приложение:
```
uvicorn app.main:app
```
##### После запуска проект доступен по адресу http://127.0.0.1:8000/

##### Документация доступна по адресу http://127.0.0.1:8000/docs
