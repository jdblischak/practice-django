app := account

options:
	echo "run, shell, migrate, update"

run:
	open http://127.0.0.1:8000/$(app)
	python manage.py runserver

shell:
	python manage.py shell

migrate:
	python manage.py makemigrations
	python manage.py migrate

update:
	conda env update --file ../environment.yml
