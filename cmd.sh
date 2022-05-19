#!/bin/bash
set -e

if [ "$ENV" = 'DEV' ]; then
    echo "Runnind dev server"
    exec python "identidock.py"
else
    echo "Runnind prod server"
    exec uwsgi --http 0.0.0.0:9090 --wsgi-file /app/identidock.py --callable app --stats 0.0.0.0:9191
fi
