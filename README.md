# collectors #
The collectors application is a membership tracking application

## Local instance configuration ##
Clone the project.
```cd``` to the project root (where the ```manage.py``` command is located.)

Create a virtual environment
    Linux: ```python3 -m venv env```
    Windows: ```python -m venv env```

Activate virtual environment:
    Linux: ```. env/bin/activate```
    Windows: ```.\env\Scripts\Activate.ps1```

Install requirements:
    Linux: ```python3 -m pip install -r requirements.txt```
    Windows: ```python -m pip install -r requirements.txt```

Create a local .env file:
    Use the ```.env_example``` as a template
    Leave the ```DEBUG``` as it is.
    Generate you secret key:
    1. Enter shell: ```python3 manage.py shell```
    2. ```from django.core.management.utils import get_random_secret_key```
    3. ```get_random_secret_key()```
    4. Paste the generated value in your ```.env``` file.
    (Note, the file has to be called ```.env```.)
### Do not commit the secret key to version control! ###

Run migrations and create a local database:
    ```python3 manage.py migrate``` (This will automatically create a local sqlite db.)

Create a local admin user:
    ```python3 manage.py createsuperuser``` (Follow instructions...)

Run the local Django server:
    ```python3 manage.py runserver```

Access the admin interface at:
    ```localhost:8000/admin```



