# Email Subscription Feature

A Django web application that allows users to subscribe to a newsletter using their email address. The application stores subscribers in a database, prevents duplicate subscriptions, and is designed to send a confirmation email after a successful subscription.

## 🚀 Features

* Newsletter subscription form
* Email input validation
* Prevents duplicate email subscriptions
* Stores subscriber information in the database
* Automatically records the subscription date and time
* CSRF protection for form submissions
* Confirmation email functionality
* Django-powered backend
* Tailwind CSS for styling

## 🛠️ Technologies Used

* **Python 3.14**
* **Django 6.1.2**
* **SQLite**
* **HTML5**
* **Tailwind CSS**
* **Git & GitHub**

## 📁 Project Structure

```text
Email_sub/
│
├── myenv/
│
└── Subs/
    ├── manage.py
    │
    ├── Subs/
    │   ├── settings.py
    │   ├── urls.py
    │   ├── asgi.py
    │   └── wsgi.py
    │
    └── subscribers/
        ├── migrations/
        ├── templates/
        │   └── subscribe.html
        ├── models.py
        ├── views.py
        ├── admin.py
        └── apps.py
```

## 🗄️ Subscriber Model

The project uses a `Subscriber` model to store newsletter subscribers.

```python
class Subscriber(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
```

### Fields

| Field        | Description                                           |
| ------------ | ----------------------------------------------------- |
| `email`      | Stores the subscriber's email address                 |
| `created_at` | Automatically records when the subscriber was created |

## 🔄 How It Works

The subscription process follows this flow:

```text
User visits /subscribe/
        ↓
Subscription form is displayed
        ↓
User enters email
        ↓
Form sends POST request
        ↓
Django retrieves email
        ↓
Check if email already exists
        ↓
 ┌─────────────────────┐
 │ Email already exists│
 │ → Don't create new  │
 │   subscriber        │
 └─────────────────────┘

            OR

 ┌─────────────────────┐
 │ New email           │
 │ → Save subscriber   │
 │ → Send confirmation │
 └─────────────────────┘
```

## 🌐 URL

The subscription page is available at:

```text
http://127.0.0.1:8000/subscribe/
```

## 🧠 View Logic

The `subscribe` view handles the subscription request.

```python
def subscribe(request):
    if request.method == "POST":
        email = request.POST.get("email")

        existing = Subscriber.objects.filter(email=email).exists()

        if existing:
            print(f"{email} already exists")
        else:
            Subscriber.objects.create(email=email)

    return render(request, "subscribe.html")
```

The view:

1. Checks whether the request is a `POST` request.
2. Gets the email submitted through the form.
3. Checks whether the email already exists.
4. Creates a new `Subscriber` if the email is not already registered.
5. Displays the subscription page.

## 🔐 CSRF Protection

The form uses Django's CSRF protection:

```html
{% csrf_token %}
```

This protects the application against Cross-Site Request Forgery attacks when submitting the POST request.

## 📧 Email Configuration

Django's email system can be configured to send a confirmation email after a successful subscription.

Example SMTP configuration:

```python
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = "your-email@gmail.com"
EMAIL_HOST_PASSWORD = "your-app-password"

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
```

> **Security:** Never upload your real email password or SMTP credentials to GitHub. Use environment variables for sensitive information.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Enter the project

```bash
cd Email_sub
```

### 3. Create a virtual environment

```bash
python -m venv myenv
```

### 4. Activate the virtual environment

Windows Git Bash:

```bash
source myenv/Scripts/activate
```

### 5. Install Django

```bash
pip install django
```

### 6. Run migrations

```bash
cd Subs

python manage.py makemigrations
python manage.py migrate
```

### 7. Start the development server

```bash
python manage.py runserver
```

### 8. Open the subscription page

Visit:

```text
http://127.0.0.1:8000/subscribe/
```

## 🧪 Testing

To test the application:

1. Open the subscription page.
2. Enter a valid email address.
3. Click **Subscribe**.
4. Check the database for the new subscriber.
5. Submit the same email again.
6. Confirm that a duplicate subscriber is not created.
7. Verify that the confirmation email is sent once email configuration has been completed.

## 📌 Future Improvements

* Display success and error messages directly on the webpage.
* Send confirmation emails automatically after subscription.
* Add unsubscribe functionality.
* Add email verification.
* Add an admin interface for managing subscribers.
* Add automated tests.
* Improve form validation.
* Deploy the application online.

## 👨‍💻 Author

**Anthony Kingori Kiarie**

Built as a Django learning project to practice:

* Django models
* Django views
* HTML forms
* POST requests
* Database operations
* Form validation
* CSRF protection
* Email functionality
* Git and GitHub
