# Тестовое Web-приложение для компании Каналсервис

## Инструкция по запуску приложения в Docker контейнерах

Перед запуском установить [Docker Desktop](https://docs.docker.com/get-docker/), [GIT](https://git-scm.com/download/win).
При запуске на windows необходимо клонировать репозиторий на диск c:/
1. Клонируем репозиторий (или определенную ветку) и заходим в папку:
  ```
$ git clone --branch main https://github.com/Dudhen/-Test.git
$ cd КаналсервисTest
  ```
2. Запускаем создание образов и сборку контейнеров (на компьютере должен быть запущен Docker Desktop):
```
$ docker-compose up -d --build
```
3. Приложение доступно по адресу http://127.0.0.1:8000/canal_service/
4. Для просмотра всех запущенных контейнеров и их логов (при некорректном запуске приложения):
```
$ docker ps -a
$ docker logs <CONTAINER ID>
```
5. Создаем и запускаем миграции для работы с БД
```
$ docker-compose exec web python manage.py makemigrations
$ docker-compose exec web python manage.py migrate
```
6. Копируем статичные файлы
```
$ docker-compose exec web python manage.py collectstatic
```
7. Для запуска телеграм-бота
```
$ docker-compose exec web python table_app/telegram_bot.py
```
Телеграм-бот находится по адресу @i_Canal_Service_Bot

8. Документ Google Sheets находится по адресу:
```
$ https://docs.google.com/spreadsheets/d/1dmxxjzCoOS6zbp3gOPHw5nMxiN5JCyp85Gn2wqPd_s0/edit#gid=0
```
8. Для удаления всех контейнеров:
```
$ docker-compose down
```

## Внесение изменений в исходный код

### GIT
 
1. Для определения ветки, в которой мы находимся:
```
$ git branch
```
2. Для просмотра изменений, внесенных пользователем:
```
$ git status
```
3. Для сохранения изменений в исходном коде используются следующие команды:
```
$ git add .
$ git commit -m "Краткое описание изменений"
```
4. Для отправки изменений из локального репозитория в удаленный:
```
$ git push origin <название ветки>
```
5. Для получения данных из удаленного репозитория в локальный:
```
$ git pull origin <название ветки>
```
Дополнительная информация по [GIT на русском языке](https://git-scm.com/book/ru/v2)

### Docker

Для локальной разработки используется файл docker-compose.yml
1. Для остановки и удаления контейнеров используется команда docker-compose -f down.
2. При изменении файлов *.yml, Dockerfile требуется пересобрать образы и контейнеры с приложениями:
```
$ docker-compose -f down
$ docker-compose -f up -d --build
```
3. При изменении остального исходного кода приложения перезапускаем контейнеры следующими командами:
```
$ docker-compose -f down
$ docker-compose -f up -d
```
либо
```
$ docker-compose -f restart
```
4. При необходимости запустить какие-либо скрипты или файлы из контейнеров используется следующая команда:
```
$ docker-compose -f exec web python <путь к файлу/скрипту>
```
5. Для просмотра логов используется команда:
```
$ docker-compose -f <имя docker-compose файла> logs
```
6. При изменении моделей базы данных и/или статичных файлов на продакшн сервере требуется запустить миграции и упаковать статичные файлы:
```
$ docker-compose -f <имя docker-compose файла> exec web python manage.py migrate
$ docker-compose -f <имя docker-compose файла> exec web python manage.py collectstatic
$ docker-compose -f <имя docker-compose файла> restart
```
