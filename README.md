# Blog

## Возможности

- создание, изменение и удаление постов
- отображение постов на странице веб-браузера
- модификация количества лайков

## API
- POST /posts - создание поста
- PUT /posts/{post_id} - изменение поста
- DELETE /posts/{post_id}  - удаление поста
- GET /posts/blog - отображение постов на странице веб-браузера и их лайков
- PATCH /posts/likes - увеличение количества лайков
- PATCH /posts/dislikes  - уменьшение количества лайков

## Технологии

- Python
- Fastapi
- SQLalchemy
- Alembic
- PostgreSQL
- Docker

## Установка

### Предварительные требования

- Python 3.9 или выше
- Docker
- pip

### Пошаговая установка

1. **Клонируйте репозиторий:**
   ```bash
   git clone ...

2. **Соберите образ Docker:**
   ```bash
   docker-compose up -d
