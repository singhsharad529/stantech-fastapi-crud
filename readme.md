# Book CRUD Service

A simple, containerized **FastAPI** application that provides a RESTful API for performing **Create, Read, Update, and Delete (CRUD)** operations on a book database.

---

## Features

- **FastAPI:** High-performance web framework for building APIs.  
- **SQLAlchemy:** ORM for database interaction.  
- **Pydantic:** Data validation and settings management.  
- **SQLite:** Simple file-based database.  
- **Docker:** Fully containerized for easy setup and deployment.  
- **Pagination:** `GET /books` supports `skip` and `limit` query parameters.  
- **Search:** `GET /books` supports filtering by title.  

---

## Technology Stack

- FastAPI  
- Uvicorn  
- SQLAlchemy  
- Pydantic  
- SQLite  
- Docker  

---

## Project Structure

```
/project-root
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── routers/
│   │   ├── __init__.py
│   │   └── books.py
│   └── schema.py
├── tests/
│   ├── test_api.py
├── Dockerfile
├── .dockerignore
├── requirements.txt
└── .books.db
```

---

## Setup and Installation

You can run this application **either locally** with a virtual environment or **as a Docker container**.

---

### 1. Running with Docker

#### **Prerequisites**
- Docker installed.

#### **Steps**

**1. Clone the Repository:**

```
git clone https://github.com/singhsharad529/stantech-fastapi-crud.git
cd stantech-fastapi-crud
```

**2. Build the Docker Image:**

```
docker build -t book-service .
```

**3. Run the Container:**

```
docker run -d -p 8000:8000   -e API_KEY=<api_key_for_authentication>  -v $(pwd)/.books.db:/app/.books.db   --name books-api   book-service
```

**The application is now running at:**
- http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs


### 1. Running Locally
#### **Prerequisites**
- Python 3.10+
- pip and venv

#### **Steps**
**1. Clone the Repository:**

```
git clone https://github.com/singhsharad529/stantech-fastapi-crud.git
cd stantech-fastapi-crud
```

**2. Create and Activate a Virtual Environment:**

```
python3 -m venv venv
source venv/bin/activate
```

**3. Install Dependencies:**

```
pip install -r requirements.txt
```

**4. Environment Variables**
Create an .env file on root directory and add env.

```
API_KEY=<your_api_key_for_authentication>
```

**5. Run the Application:**
The Base.metadata.create_all(bind=engine) in main.py will automatically create the .books.db file.
```
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
**The application is now running at:**
- http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs


## Testing

To verify the API functionality, a `test_api.py` file has been added inside the `tests` folder.  
You can run the tests using the following command:

```
pytest
```