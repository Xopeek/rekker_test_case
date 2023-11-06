# Тестовое задание.
Вводные данные

В сервисе присутствуют 4 сущности:

Пользователь
1. Имя.
2. Фамилия. 

Заметка
1. Заголовок.
2. Тело.
3. Дата создания.
4. Пользователь (создатель).

Ачивка
1. Название.
2. Условие получения (обычный текст).
3. Иконка.

Рекламное объявление
1. Заголовок.
2. Описание.
3. Изображение.
4. Ссылка на рекламируемый ресурс.
5. Дата публикации (равна дате создания, механизмы отложенной публикации делать
не нужно).

Задание: Необходимо спроектировать личную ленту, состоящую из следующих типов событий:
1. Пользователь написал заметку A.
2. Пользователь получил достижение B.
3. Рекламное объявление. 

Пользователь не должен видеть заметки и достижения другого пользователя.
Клиент должен получать ленту с помощью одного GET-запроса:
1. События должны быть отсортированы по времени создания.
2. Запрос должен поддерживать пагинацию.
3. Запрос должен поддерживать поиск по заголовкам.

В ленте должны быть события только одного пользователя, ID которого указан в
запросе.Для запроса ленты необязательно делать систему авторизации. Можно оставить
AllowAny и передавать ID пользователя для упрощения.

Инструменты:

Реализовать задание необходимо на Django последней версии. Для GET-запроса
использовать Django Rest Framework. База данных PostgreSQL.
Создание пользователей и ачивок можно реализовать через механизм сидов. Достаточно
2-3 пользователя и 1-2 ачивки.

Создание заметки, рекламного объявления и выдачу ачивки пользователю можно сделать
через Django Admin.

## Как установить проект:
1. ````
   git clone git@github.com:Xopeek/rekker_test_case.git
   ````
2. ````
   cd personal_feed_project
   ````
3. ````
   pip install -r requirements.txt
   ````
4. ````
   python manage.py migrate
   ````
5. ````
   python manage.py load_test_data
   ````
6. ````
   python manage.py runserver
   ````

## Нужно создать файл .env, пример заполнения:
````
POSTGRES_DB='postgres'
POSTGRES_USER='postgres'
POSTGRES_PASSWORD='admin'
DB_HOST='localhost'
DB_PORT=5432
SECRET_KEY='django-insecure-b#l1x%pn3aj+64w1e8+g-(mh5!)ne@=m1c_9$^2w%+q3vdry06'
DEBUG=True
ALLOWED_HOSTS=127.0.0.1, localhost
````

## Пример GET запроса:
````
http://127.0.0.1:8000/api/user/1/
````

Можно добавить пагинацию: page_size=

Можно добавить фильрацию по title: search=

### Задание выполнил Семляков Игорь