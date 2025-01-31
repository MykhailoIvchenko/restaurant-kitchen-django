# Kitchen Management System

The Kitchen Management System is a web application built with Django to help manage kitchen operations efficiently. 
It allows you to handle various aspects of kitchen management, including managing cooks, dishes, and dish types. 

## Purpose

This system is designed to streamline the kitchen management process by providing 
a user-friendly interface for adding, updating, and viewing information about dishes 
and the cooks who prepare them. It's perfect for restaurant managers, chefs, and kitchen 
staff who need an organized and accessible way to manage kitchen data.

## Features

- **User Authentication:** Secure login and registration for kitchen staff.
- **Cook Management:** Track cooks, including their years of experience and personal details.
- **Dish Management:** Manage dishes with detailed information such as name, description, price, and the type of dish.
- **Dish Type Categorization:** Organize dishes into different types for better management and searching.
- **Admin Controls:** Special administrative features for managing users and data efficiently.

## Getting Started

### Prerequisites

- Python 3.x
- Django
- SQLite (or any other preferred database)

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/kitchen-management-system.git
   cd restaurant_kitchen_django
   ```

2. **Create a virtual environment and activate it:**
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```sh
   pip install
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory and add your environment variables.
   ```env
   SECRET_KEY=your_secret_key
   ```

5. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```

6. **Create a superuser:**
   ```sh
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

8. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:8000/`.

### Running Tests

To run the tests for the project, use the following command:
```sh
python manage.py test
```

## Check it out!
[Restaurant kitchen project deployed to Render](https://restaurant-kitchen-eo8l.onrender.com)

You can register in the application or use credentials for test user:
Login: user
Password: user12345