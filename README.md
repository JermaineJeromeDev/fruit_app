# 🍎 Fruit App - Fullstack Django Project

[English Version](#english-version) | [Deutsche Version](#deutsche-version)

---

## English Version

This is a simple full-stack application that retrieves a list of fruits from a Django backend and displays them in a static frontend.

### 📂 Project Structure
As per my mentor's recommendation, the project is divided into backend and frontend:
- **fruit_app_backend/**: Contains the Django project (`core`) and the app (`fruit_app`).
- **fruit_app_frontend/**: Contains the client side with `index.html` and `script.js`.

### 🚀 Features
- **Django API**: Provides fruit data (name, weight, color) as JSON.
- **Asynchronous Fetch**: The frontend uses `async/await` to load data.
- **CORS Integration**: Enabled communication between ports 8000 and 5501 via `django-cors-headers`.

### 🛠️ Setup
1. **Backend**: Navigate to `fruit_app_backend`, activate your venv, and run `python manage.py runserver`.
2. **Frontend**: Open `index.html` in `fruit_app_frontend` using **Live Server**.

---

## Deutsche Version

Dies ist eine Fullstack-Anwendung, die eine Liste von Früchten aus einem Django-Backend abruft und in einem statischen Frontend darstellt.

### 📂 Projektstruktur
Gemäß der Empfehlung meines Mentors ist das Projekt in Backend und Frontend unterteilt:
- **fruit_app_backend/**: Enthält das Django-Projekt (`core`) und die App (`fruit_app`).
- **fruit_app_frontend/**: Enthält die Client-Seite mit `index.html` und `script.js`.

### 🚀 Features
- **Django API**: Liefert Fruchtdaten (Name, Gewicht, Farbe) als JSON.
- **Asynchroner Fetch**: Das Frontend nutzt `async/await`, um Daten zu laden.
- **CORS Integration**: Ermöglicht die Kommunikation zwischen Port 8000 und 5501 via `django-cors-headers`.

### 🛠️ Setup
1. **Backend**: Navigiere zu `fruit_app_backend`, aktiviere die venv und starte `python manage.py runserver`.
2. **Frontend**: Öffne die `index.html` in `fruit_app_frontend` mit dem **Live Server**.

---
*Created as part of the Backend Assignment.*
