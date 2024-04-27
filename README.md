# Basic Django Djoser Auth Project

This is a basic Django project that demonstrates user authentication using Djoser.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python (3.6 or higher)
- Django (3.0 or higher)
- Djoser (2.0 or higher)
- [Optional] Virtualenv (for isolated Python environment)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your_username/basic_django_djoser_auth_project.git
```

2. Navigate to the project directory:

```bash
cd basic_django_djoser_auth_project
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

### Configuration

1. Configure .env file

In the project root directory, you'll find an .env_example file. Refer to this file to configure your environment variables. 

2. Run migrations:

```bash
python manage.py migrate
```

### Usage

1. Start the development server:

```bash
python manage.py runserver
```

2. Visit `http://127.0.0.1:8000/` in your web browser to access the Django admin interface and other endpoints.

## Endpoints

- `/api/auth/users/`: User registration endpoint.
- `/api/auth/token/login/`: User login endpoint.
- `/api/auth/token/logout/`: User logout endpoint.
- `/api/auth/users/me/`: Retrieve or update user profile endpoint.

## Built With

- [Django](https://www.djangoproject.com/) - The web framework for perfectionists with deadlines.
- [Djoser](https://djoser.readthedocs.io/en/latest/) - REST implementation of Django authentication system.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

You are free to:

- Use the code for personal or commercial purposes
- Modify the code
- Distribute the code
- Use the code for private or public projects
