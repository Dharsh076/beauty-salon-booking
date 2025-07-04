# 💇‍♀️ Beauty Salon Booking System

A secure and responsive web application built with **Flask** to manage online bookings for a beauty salon based in Ottawa.

---

## ✨ Features

- 🧾 **Appointment Booking** – Users can book salon services with a date & time picker.
- 🔐 **Admin Login** – Password-protected dashboard with Flask-Login and hashed credentials.
- 📝 **Edit & Delete Bookings** – Admins can manage appointments easily.
- 📅 **Pagination** – Booking list is paginated for improved performance.
- 🛡 **Security** – CSRF protection, form validation, hashed passwords, and `.env`-based secrets.

---

## 🛠 Tech Stack

- **Backend:** Flask, Flask-WTF, Flask-Login, SQLAlchemy
- **Frontend:** Bootstrap 5, Flatpickr.js
- **Database:** SQLite
- **Security:** CSRF, hashed passwords, secure sessions

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/Dharsh076/beauty-salon-booking.git
cd beauty-salon-booking
```

### 2. Set Up Environment
```bash
python -m venv venv
venv\Scripts\activate   # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment
Create a `.env` file in the project root:
```
SECRET_KEY=your-random-secret-key
```

### 5. Run the Application
```bash
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 🔐 Admin Access

Seeded by default:
- **Username:** `admin`
- **Password:** `beauty123`

---

## ✅ To-Do List

- [ ] Add email notifications
- [ ] Add payment gateway integration
- [ ] Implement booking calendar view
- [ ] Responsive UI improvements

---

## 📄 License

Licensed under the [MIT License](LICENSE).

---

## 🧠 Author

**Dharshini Vasudevan** – 2025  
For local businesses, freelancers, and beauty professionals in Ottawa.
