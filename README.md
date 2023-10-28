# Unit Test Project

```bash
# Create a virtual environment
virtualenv unit_test

# Install required packages
pip install Django
pip install psycopg2-binary
pip install pytest
pip install pytest-django
pip install mixer
pip install pytest-cov
pip install mock

# Run database migrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Run pytest
pytest

# Run pytest with coverage
pytest --cov
