## Запуск проекта локалбно

Зависимости проекта: `docker`, `docker-compose`

Нужные файлы окружения: .env и .env_db

## Запуск проекта с makefile

```
    # установка нужной переменной для dev
    export DOCKER_COMPOSE_FILE=docker-compose.yml
    # для prod
    export DOCKER_COMPOSE_FILE=docker-compose_prod.yml
    # запуск
    make up
    # Для просмотра всех команд makefile
    make help
```

## Запуск проекта вручную
Если вы хотите поднять проект prod исползуйте комманды `docker-compose -f docker-compose_prod.yml ` вместо `docker-compose`

1. Сделать ENTRYPOINT Scripts исполняемым

    `sudo chmod +x entrypoint.sh`

2. Запуск проекта

    `docker-compose up`

3. сделать миграции

```
    docker-compose exec web python3 manage.py makemigration
    docker-compose exec web python3 manage.py migrate
```

4. Создание супер пользователя и сборка статиков

```
    docker-compose exec web python3 manage.py createsuperuser
    docker-compose exec web python3 manage.py collectstatic
```

перезагрузить контейнер с помощи команды "`docker-compose restart`"


Добавить systemcd service для docker compose autorestart

1) Создать `/etc/systemd/system/docker-compose-app.service` файл и написать

```
    [Unit]
    Description=Docker Compose Application Service
    Requires=docker.service
    After=docker.service

    [Service]
    WorkingDirectory=/{your project path}
    ExecStart=docker-compose -f docker-compose_prod.yml up
    ExecStop=docker-compose -f docker-compose_prod.yml down
    TimeoutStartSec=0
    Restart=on-failure
    StartLimitIntervalSec=60
    StartLimitBurst=3

    [Install]
    WantedBy=multi-user.target
```
