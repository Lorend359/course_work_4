# Django Email Newsletter Service

## Описание проекта

Веб-приложение на Django для управления email-рассылками. Пользователи могут создавать сообщения, клиентов и рассылки, а также отслеживать статус отправки. Есть разграничение прав доступа: менеджеры видят все данные, обычные пользователи — только свои.

## Основной функционал

* Регистрация и аутентификация пользователей
* Управление профилем (редактирование, аватар и пр.)
* CRUD-интерфейсы для:

  * Клиентов (получателей писем)
  * Сообщений
  * Рассылок
* Ручная отправка рассылок через интерфейс
* Автоматическая отправка рассылок по расписанию (через APScheduler)
* Просмотр истории попыток рассылки
* Главная страница с пользовательской статистикой
* Кеширование главной страницы для анонимных пользователей

## Технологии

* Python 3.12
* Django 5.2
* PostgreSQL
* Redis (планируется)
* APScheduler
* Poetry

## Установка и запуск

1. Клонируйте репозиторий

```bash
git clone https://github.com/ваш_профиль/course_work_4.git
cd course_work_4
```

2. Установите зависимости

```bash
poetry install
```

3. Создайте и настройте файл `.env`

```env
SECRET_KEY=ваш_секретный_ключ
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=postgres://user:password@localhost:5432/dbname
EMAIL_HOST=...
EMAIL_PORT=...
EMAIL_HOST_USER=...
EMAIL_HOST_PASSWORD=...
```

4. Примените миграции

```bash
poetry run python manage.py migrate
```

5. Создайте суперпользователя (по желанию)

```bash
poetry run python manage.py createsuperuser
```

6. Запустите сервер

```bash
poetry run python manage.py runserver
```

## Команды

* Создание группы "Менеджеры":

```bash
poetry run python manage.py create_groups
```

* Отправка рассылок вручную (по ID):

```bash
poetry run python manage.py send_mailing
```

