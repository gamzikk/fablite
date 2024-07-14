# fablite

### Что реализовано:

+ регистрация и авторизация
+ вывод списка пользователей
+ обновление информации о пользователе (редактирование)
+ удаление пользователя
+ защита от межсайтовой подделки запроса (CSRF)


# Руководство по запуску

+ Клонируйте репозиторий
+ Создайте виртуальное окружение и активируйте его в корне проекта:

#### Windows
```
python -m venv .venv
.venv\Scripts\activate
```

#### Linux
```
python3 -m venv .venv
source .venv/bin/activate
```

+ Установите зависимости:

```
pip install -r requirements.txt
```

+ На вашей операционой системе должен быть установлен PostgreSQL
+ Создайте базу данных sport_db в PotgreSQL
+ Проведите миграции командой:

#### Windows
```
python manage.py migrate
```

#### Linux
```
python3 manage.py migrate
```

+ Создайте суперпользователя для  входа в админ панель:

#### Windows
```
python manage.py createsuperuser
```

#### Linux
```
python3 manage.py createsuperuser
```

+ Запустите приложение:

#### Windows
```
python manage.py runserver
```

#### Linux
```
python3 manage.py runserver
```


### Навигация по сайту

+ http://127.0.0.1:8000/users/register/ - регистрация
+ http://127.0.0.1:8000/users/login/ - авторизация
+ http://127.0.0.1:8000/users/profile/1/ - профиль
+ http://127.0.0.1:8000/users/list/ - список пользователей
+ http://127.0.0.1:8000/admin/users/customuser/ - удаление пользователя или редактирование данных о пользователе
