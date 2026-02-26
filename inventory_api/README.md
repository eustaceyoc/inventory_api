# **Inventory API**

A RESTful Inventory Management API built with Django and Django REST Framework. It provides robust CRUD operations with filtering, searching, sorting, and pagination support.

## **Table of Contents**

* [Overview](#overview)
* [Problem Statement](#problem-statement)  
* [Target Users](#target-users)  
* [Tech Stack](#tech-stack)  
* [Key Features](#key-features)  
* [API Documentation](#api-documentation)  
* [Installation](#installation)  
* [Environment Configuration](#environment-configuration)  
* [Usage](#usage)  
* [Folder Structure](#folder-structure)  
* [Deployment](#deployment)  
* [Testing](#testing)  
* [Roadmap](#roadmap)  
* [Contributing](#contributing)  
* [Author](#contributing)

## **Overview**

Inventory API is a backend service designed to manage inventory items efficiently. It exposes RESTful endpoints that allow clients to create, retrieve, update, delete, filter, search, and paginate inventory records.

The system is structured for scalability and maintainability, following Django best practices and clean project architecture.

## **Problem Statement**

Businesses and teams often require a lightweight, flexible backend service to manage stock and inventory records programmatically. Many small-scale systems lack structured REST APIs, efficient filtering and search capabilities, pagination for large datasets, and clear, maintainable architecture.

Inventory API addresses these gaps with a clean, production-ready Django implementation.

## **Target Users**

* Backend developers building inventory-based applications  
* Small businesses managing stock systems  
* Startups needing a simple inventory microservice  
* Recruiters evaluating Django REST backend projects

## **Built With**

* **Backend Framework:** Django  
* **API Framework:** Django REST Framework  
* **Database:** SQLite (default), easily configurable  
* **Language:** Python 3.14  
* **Version Control:** Git

## **Key Features**

* Full CRUD operations for inventory items  
* Filtering by fields  
* Search functionality  
* Sorting (ascending/descending)  
* Pagination support
* Clean modular architecture  
* Production-ready configuration  
* Git feature-branch workflow

## **API Documentation**

### **Base URL**

`http://127.0.0.1:8000/api/`

### **Inventory Endpoints**

| Method | Endpoint | Description |
| ----- | ----- | ----- |
| GET | /api/items/ | List all items (supports filtering, search, sorting, pagination) |
| POST | /api/items/ | Create a new inventory item |
| GET | /api/items/\<id\>/ | Retrieve a single item |
| PUT | /api/items/\<id\>/ | Update an item |
| DELETE | /api/items/\<id\>/ | Delete an item |

### **Query Parameters**

### **Filtering**

`/api/items/?category=Electronics`

### **Search**

`/api/items/?search=laptop`

### **Sorting**

`/api/items/?ordering=price`

`/api/items/?ordering=-price`

## **Pagination**

`/api/items/?page=2`

### **Example JSON Response**

```
{
  "id": 1,
  "name": "Laptop",
  "category": "Electronics",
  "quantity": 10,
  "price": "1200.00",
  "created_at": "2026-02-26T10:00:00Z"
}
```

## **Installation**

## **1\. Clone the repository**

`git clone https://github.com/yourusername/inventory-api.git`

`cd inventory-api`

## **2\. Create and activate virtual environment**


`python -m venv venv`

Windows:

`venv\Scripts\activate`

Mac/Linux:

`source venv/bin/activate`

## **3\. Install dependencies**

`pip install -r requirements.txt`

## **4\. Apply migrations**

`python manage.py migrate`

## **5\. Run the development server**

`python manage.py runserver`

Server runs at: `http://127.0.0.1:8000/`

## **Environment Configuration**

This project runs out of the box with default Django settings. For production, configure DEBUG=False, ALLOWED\_HOSTS, database credentials, and secret key via environment variable.

Example:

`set SECRET_KEY=your_secret_key  # Windows`

`export SECRET_KEY=your_secret_key  # Mac/Linux`

## **Usage**

Example: Create an item

`curl -X POST http://127.0.0.1:8000/api/items/ \`

  `-H "Content-Type: application/json" \`

  `-d '{`

    `"name": "Laptop",`

    `"category": "Electronics",`

    `"quantity": 10,`

    `"price": 1200.00`

  `}'`

Example: Get all items

`curl http://127.0.0.1:8000/api/items/`

## **Folder Structure**

```
inventory_api/
│
├── inventory/              # Inventory app
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── inventory_api/          # Project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── README.md
```

## **Deployment**

## **Option 1: Heroku**

1. Install Heroku CLI  
2. Create Procfile: `web: gunicorn inventory_api.wsgi`  
3. Add gunicorn: `pip install gunicorn`  
4. Push to Heroku: `heroku create` `git push heroku main`

## **Option 2: PythonAnywhere**

* Upload project  
* Configure virtualenv  
* Set WSGI file to inventory\_api.wsgi  
* Configure static files  
* Reload app

## **Testing**

Run Django tests:

`python manage.py test`

Future improvements may include Pytest integration, coverage reports, and CI pipeline integration.

## **Roadmap**

* JWT Authentication  
* Role-based permissions  
* Swagger/OpenAPI documentation  
* PostgreSQL production configuration  
* Docker support  
* CI/CD pipeline

## **Contributing**

Contributions are welcome.

1. Fork the repository  
2. Create a feature branch  
3. Commit changes  
4. Push branch  
5. Open Pull Request

Please follow clean commit practices and ensure tests pass.

## **Author**

**Yaw Ofori**  
Backend Developer

For professional inquiries, connect via [GitHub profile](https://github.com/eustaceyoc) or [LinkedIn](https://linked.com/in/eustace-crentsil).