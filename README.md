# FastAPI Bonus Service

## Описание

Этот проект реализует REST-сервис на FastAPI для управления бонусной программой пользователей.

## Установка и запуск

### Установка зависимостей

При установленном poetry выполнить команду:

```
poetry install
```

### Запуск сервиса

Запустите сервис с помощью команды:
```
poetry run uvicorn src.main:app --reload
```

### Получение токена
```
POST /token
Content-Type: application/json

{
    "username": "your_username",
    "password": "your_password"
}
```
### Запрос бонусной программы
```
GET /bonus
Authorization: Bearer your_access_token
```
## Тестирование

Запуск тестов:
```
poetry run pytest
```
## Docker
### Сборка и запуск
```
docker build -t fastapi-bonus-service .
docker run -d --name fastapi-bonus-service -p 8000:8000 fastapi-bonus-service
```
