# recipe-app-api

Recipe API project.

```bash
docker-compose run --rm app sh -c "flake8"  
```

```bash
docker-compose run --rm app sh -c "django-admin startproject app . "
```

```bash
docker-compose run --rm app sh -c "python manage.py test"
```

```bash
docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate"
```

```bash
docker-compose run --rm app sh -c "python manage.py createsuperuser"
```

```bash
docker-compose down 
```

```bash
docker-compose up
```

```bash
docker volume ls
```

```bash
docker volume rm recipe-app-api_dev-db-data
```

