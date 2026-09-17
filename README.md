# 🏥 Hospital Management System

A full-featured Hospital Management System built with **Django** and **Django REST Framework**. It covers everything from patient registration and doctor management to appointment scheduling, billing, and PDF prescription generation.

---

## 🚀 Features

- **Authentication** — Register, login, and logout with Django's built-in auth system
- **Dashboard** — Overview of total patients, doctors, departments, appointments, and today's schedule
- **Patient Management** — Add, edit, delete, and list patients
- **Doctor Management** — Manage doctors with department, specialization, experience, and availability info; includes search and pagination
- **Department Management** — Organize doctors by medical departments
- **Appointment Scheduling** — Book, edit, cancel, and track appointments (Scheduled / Completed / Cancelled)
- **Billing** — Auto-calculates total bill from consultation, medicine, lab, and other charges; tracks payment status
- **Prescriptions** — Create and manage prescriptions with diagnosis, medicines, dosage, and instructions
- **PDF Export** — Download prescription as a formatted PDF (powered by ReportLab)
- **REST API** — Full CRUD API for all resources with JWT authentication

---

## 🛠️ Tech Stack

| Layer        | Technology                          |
|--------------|-------------------------------------|
| Backend      | Django 6.0.7                        |
| API          | Django REST Framework 3.17.1        |
| Auth (API)   | SimpleJWT 5.5.1                     |
| PDF          | ReportLab 5.0.0                     |
| Database     | SQLite (dev) / PostgreSQL (prod)    |
| Language     | Python 3.x                          |

---

## 📁 Project Structure

```
HospitalManagementSystem/
├── config/               # Project settings and URL config
├── accounts/             # User registration, login, logout
├── dashboard/            # Stats overview
├── patients/             # Patient CRUD
├── doctors/              # Doctor CRUD with search & pagination
├── departments/          # Department management
├── appointments/         # Appointment scheduling
├── billing/              # Bill generation and payment tracking
├── prescriptions/        # Prescriptions + PDF export
├── api/                  # DRF ViewSets, serializers, JWT endpoints
├── templates/            # HTML templates
├── static/               # Static files (CSS, JS)
├── requirements.txt      # Python dependencies
└── manage.py
```

---

## ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/Swap7020/Hospital-Management-System.git
cd Hospital-Management-System
```

### 2. Create and activate a virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create a superuser

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

---

## 🌐 URL Routes

| URL                        | Description                     |
|----------------------------|---------------------------------|
| `/`                        | Home page                       |
| `/about/`                  | About page                      |
| `/contact/`                | Contact page                    |
| `/register/`               | User registration               |
| `/login/`                  | User login                      |
| `/logout/`                 | User logout                     |
| `/dashboard/`              | Admin dashboard (login required)|
| `/patients/`               | Patient list                    |
| `/doctors/`                | Doctor list                     |
| `/appointments/`           | Appointment list                |
| `/billing/`                | Billing list                    |
| `/prescriptions/`          | Prescription list               |
| `/admin/`                  | Django admin panel              |

---

## 🔌 REST API Endpoints

Base URL: `/api/`

| Endpoint               | Methods               | Description          |
|------------------------|-----------------------|----------------------|
| `/api/patients/`       | GET, POST             | List / create        |
| `/api/patients/{id}/`  | GET, PUT, PATCH, DELETE | Detail / update / delete |
| `/api/doctors/`        | GET, POST             | List / create        |
| `/api/departments/`    | GET, POST             | List / create        |
| `/api/appointments/`   | GET, POST             | List / create        |
| `/api/billing/`        | GET, POST             | List / create        |
| `/api/prescriptions/`  | GET, POST             | List / create        |
| `/api/token/`          | POST                  | Obtain JWT token     |
| `/api/token/refresh/`  | POST                  | Refresh JWT token    |
| `/api-auth/`           | —                     | DRF browsable auth   |

### JWT Authentication

Obtain a token:

```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "your_username", "password": "your_password"}'
```

Use the token in subsequent requests:

```bash
curl http://127.0.0.1:8000/api/patients/ \
  -H "Authorization: Bearer <your_access_token>"
```

---

## 🚢 Deployment

### Environment Variables

Before deploying, set these environment variables (do **not** hardcode them):

| Variable       | Description                        |
|----------------|------------------------------------|
| `SECRET_KEY`   | Django secret key                  |
| `DEBUG`        | Set to `False` in production       |
| `ALLOWED_HOSTS`| Comma-separated list of hosts      |
| `DATABASE_URL` | PostgreSQL connection string (prod)|

### Recommended Production Setup

1. Switch `DEBUG = False` in `settings.py`
2. Add your domain to `ALLOWED_HOSTS`
3. Use **PostgreSQL** instead of SQLite — add `psycopg2-binary` to requirements
4. Collect static files:
   ```bash
   python manage.py collectstatic
   ```
5. Use **Gunicorn** as the WSGI server:
   ```bash
   pip install gunicorn
   gunicorn config.wsgi:application
   ```
6. Put **Nginx** in front of Gunicorn for static files and SSL termination

### Deploy to Railway / Render (Quick Option)

1. Push the repo to GitHub
2. Connect the repo to [Railway](https://railway.app) or [Render](https://render.com)
3. Set environment variables in the platform dashboard
4. Set the start command to:
   ```bash
   gunicorn config.wsgi:application
   ```

---

## 📸 Screenshots

> _Add screenshots of the dashboard, patient list, appointment form, and PDF prescription here._

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Swapnil** — [Swap7020](https://github.com/Swap7020)
