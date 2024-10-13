
```markdown
# Django URL Shortener

A URL shortening service built with Django that allows users to create short, manageable URLs from long links. The project includes a web interface and an API for flexibility.

## Features
- URL shortening
- Redirect from shortened URL to the original long URL
- Scalable and ready for future enhancements (authentication, analytics, white-labeling)

## Table of Contents
- [Project Setup](#project-setup)
- [Running the Application](#running-the-application)
- [Running Tests](#running-tests)
- [API Endpoints](#api-endpoints)

## Project Setup

### 1. Clone the Repository
```bash
git clone https://github.com/shanto-thomas/urlshortener.git
cd urlshortener
```

### 2. Create a Virtual Environment
It's recommended to use a virtual environment to isolate dependencies.
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies
Install the necessary dependencies using `pip`:
```bash
pip install -r requirements.txt
```


Alternatively, you can also update the `settings.py` file directly for database settings.

### 4. Run Migrations
Set up the database by applying the migrations:
```bash
python manage.py migrate
```

### 5. Create a Superuser (Optional)
To access the Django admin panel, create a superuser:
```bash
python manage.py createsuperuser
```

### 6. Start the Development Server
Run the development server:
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to access the application.

## Running the Application

Once the server is running, you can shorten URLs by visiting the web interface. Simply paste the long URL, and a short version will be generated for you.

### API Usage
The API allows programmatic access to shorten URLs.

#### Shorten a URL
**POST** `/api/shorten/`

Request:
```json
{
    "original_url": "https://example.com"
}
```

Response:
```json
{
    "short_url": "http://127.0.0.1:8000/abc123/"
}
```

#### Redirect
To be redirected, simply use the short URL in the browser:
```
http://127.0.0.1:8000/abc123/
```

## Running Tests

To run the test suite, use the following command:
```bash
python manage.py test
```

If you are running the project inside Docker, use:
```bash
docker-compose run web python manage.py test
```

This project includes tests for:
- URL shortening
- Redirect functionality

## Docker Setup (Optional)

You can run the application using Docker if you prefer containerized deployment.

### 1. Build and Run Containers
```bash
docker-compose up --build
```

### 2. Running Tests in Docker
```bash
docker-compose run web python manage.py test
```

### 3. Stopping Containers
To stop the containers, run:
```bash
docker-compose down
```

## API Endpoints

| Method | Endpoint               | Description                     |
|--------|------------------------|---------------------------------|
| POST   | `/api/shorten/`         | Shortens a given URL            |
| GET    | `/<short_url>/`         | Redirects to the original URL   |

