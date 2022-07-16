## API CRUD News (demo)
### Demo CRUD for new's posting

# API CRUD для того, чтобы делиться новостями (демо)
## По запросу пользователя показывает новости, позволяет создавать новые, а для авторизованных пользователей - удалять и изменять существующие.
#### Токи доступа:
- /api/v1/news/ # [GET, POST, PUT, PATCH, DELETE] - информация о новостях, возможность просматривать и создавать, а для авторизованных - изменять и удалять
- /api/v1/category/ # [GET, POST, PUT, PATCH, DELETE] - информация о новостях в определенной категории, возможность просматривать и создавать, а для авторизованных - изменять и удалять
- /api/v1/tags/ # [GET, POST, PUT, PATCH, DELETE] - информация о новостях с определенными тегами, возможность просматривать и создавать, а для авторизованных - изменять и удалять
- /api/auth/JWT/CREATE/ # [POST] - создание токена в базе данных сервера для определенного пользователя.
- /api/auth/token/login/ # [POST] - авторизация пользователя в системе по логину и паролю (возвращает токен авторизации)
#### Стек библиотек:
- Django==4.0.6
- python-dotenv==0.20.0
- python-environ==0.4.54
- django-bulk-update-or-create==0.3.0
- djangorestframework==3.13.1
- djangorestframework-simplejwt==4.8.0
- djoser==2.1.0


## Подготовка к запуску:
#### 1. Создать файл .env в папке source и добавить пары ключ=значение по примеру из .env.example
#### 2. Выполнить команды через консоль:
> python3 -m venv venv # (venv). название виртуального окружаения, обычно, venv

> . venv/bin/activate # для Windows: venv/Scripts/activate

> pip install -r requirements.txt 

> python manage.py migrate --run-syncdb  # создание и разметка БД

> python manage.py createsuperuser # создание суперпользователя
## Запуск сервера:
> python manage.py migrate --run-syncdb  # создание и разметка БД

> python manage.py createsuperuser # создание суперпользователя

> python manage.py runserver # запуск сервера (по умолчанию: http://127.0.0.1:8000/)
