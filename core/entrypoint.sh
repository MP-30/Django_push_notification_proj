#!/bin/ash

# Collect static files

echo "Colloct static files"
python3 manage.py collectstatic --noinput
if [ $? -ne 0 ]; then
    echo "Failed to collect static files"
    exit 1
fi

# Apply databases migrations
echo "Apply database migrations"
python3 manage.py makemigrations
if [ $? -ne 0 ]; then
    echo "Failed to make migrations"
    exit 1
fi
python3 manage.py migrate
if [ $? -ne 0 ]; then
    echo "Failed to apply migrations"
    exit 1
fi

# Execute the provided command or entrypoint
echo "Executing provided command or entrypoint"
exec "$@"