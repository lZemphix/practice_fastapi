#!/bin/sh

echo "Проверка подключения к PostgreSQL..."
until PGPASSWORD='postgres' psql -h db -U postgres -d practice -c '\q'; do
  >&2 echo "PostgreSQL недоступен, ждём..."
  sleep 1
done

echo "Применение миграций..."
alembic upgrade head

echo "Запуск приложения..."
exec python3 src/main.py