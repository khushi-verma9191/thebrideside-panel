Project Name: The Bride Side – Lead Management System
🛠️ Tech Stack:
Backend: Python, Django

Frontend: HTML, CSS, Bootstrap

Database: SQLite (can be easily scaled to PostgreSQL/MySQL)

Version Control: Git & GitHub

📚 Project Description:
The Bride Side – Lead Management System is a Django-based web application designed to manage and track client leads for a wedding or event planning service. It streamlines lead collection, enhances data handling, and helps determine the optimal time to contact clients using AI-generated suggestions.

💡 Key Features:
🔐 Admin-Side Lead Form: Add new leads through a user-friendly, Bootstrap-styled form with CSRF protection.

📅 Event Date Handling: Users must select an event date, which is stored securely in the backend.

📤 AI-Based Suggestion (Mocked): After form submission, the system suggests the best time to follow up with the client.

🗃️ Model-Driven Forms: Uses Django’s ModelForm for clean data validation and auto field management.

📁 Template Integration: Modular templates including base.html, lead_form.html, and lead_success.html for a consistent and clean UI.

🔄 Dynamic Routing: URL routing configured via urls.py for easy navigation between pages.

🧩 Migrations Managed: Custom migration files created and applied to manage model changes, including the new event_date field.

🧪 Test-Ready Structure: Modular architecture to support future testing and integration.

📍 Current Status:
Project is live locally and version-controlled via Git.

Fully functional lead addition feature with front-end validation and backend storage.

Easily extendable for search, filter, lead status tracking, or CRM integration.
