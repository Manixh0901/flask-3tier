#!/bin/sh

# Wait for PostgreSQL
while ! nc -z $POSTGRES_HOST 5432; do
  sleep 1
  echo "Waiting for PostgreSQL at $POSTGRES_HOST:5432..."
done

echo "PostgreSQL is ready - starting Flask"
exec flask run --host=0.0.0.0 --port=5000
