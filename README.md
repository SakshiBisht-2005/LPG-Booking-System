# 🚀 LPG Booking System (Django Project)

A real-world inspired **LPG Gas Booking Web Application** built using Django.
This project simulates how gas booking systems work in real life with proper business logic and user flow.

---

## 📌 Features

* 🔐 **Passwordless Authentication (Email OTP)**
* ⛽ **LPG Cylinder Booking System**
* 📅 **Automatic Delivery Date Calculation**
* ⛔ **21-Day Booking Restriction Rule**
* 📊 **User Dashboard with Booking Details**
* 📜 **Booking History Tracking**
* 🔄 **Status Tracking (Pending → Dispatched → Delivered)**
* 💰 **Price Display for Each Booking**

---

## 🧠 Real-World Logic Implemented

* Users cannot book a cylinder again within **21 days**
* Delivery date is automatically set (e.g., +2 days)
* Each booking maintains a **status lifecycle**
* OTP-based login removes need for passwords

---

## 🛠 Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS
* **Database:** SQLite (default Django DB)
* **Authentication:** Email OTP (SMTP)

---

## 📂 Project Structure

```
lpg/
│
├── booking/
│   ├── migrations/
│   ├── templates/booking/
│   ├── static/booking/css/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── utils.py
│
├── lpg/
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
└── requirements.txt
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/lpg-booking-system.git
cd lpg-booking-system
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv env
env\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5️⃣ Run the Server

```bash
python manage.py runserver
```

👉 Open in browser:

```
http://127.0.0.1:8000/
```

---

## 📧 Email OTP Configuration

Update your `settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_app_password'
```

⚠️ Use **App Password**, not your Gmail password.

---

## 🔐 .gitignore (Important)

Make sure these are ignored:

```
__pycache__/
*.pyc
db.sqlite3
.env
env/
venv/
```

---


## 🚀 Future Enhancements

* 📱 SMS OTP integration
* 👨‍💼 Admin panel for dispatch control
* 🚚 Delivery OTP verification
* 💳 Online payment system
* 📍 Real-time delivery tracking

---

## 🙌 Learning Outcome

This project helped in understanding:

* Real-world backend logic implementation
* Django authentication & session handling
* Project structuring and UI design
* Moving beyond CRUD to business logic

---


