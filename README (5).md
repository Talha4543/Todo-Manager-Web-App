# Todo-Manager-Web-App

This is a simple web application to manage your todo's.

<!-- Badges -->

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

This project is under the MIT license. That means you can use it and share it freely!



## 📝 Description
The Todo-Manager-Web-App is a simple web application for managing your todos. It provides user authentication (signup, login, logout), and allows users to create, toggle the completion status of, and delete todo items. The application uses FastAPI as a backend framework, Jinja2 for templating, and SQLite for data storage. Tailwind CSS is used for styling the user interface, providing a clean and responsive design. The application uses session middleware to maintain user sessions, ensuring that only authenticated users can access and manage their todos.



## 📌 Table of Contents
- [📝 Description](#-description)
- [✨ Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [🚀 Installation](#-installation)
- [💻 Usage](#-usage)
- [📂 Project Structure](#-project-structure)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)
- [🔗 Important Links](#-important-links)
- [📄 Footer](#-footer)



## ✨ Features
- **User Authentication**: Secure signup, login, and logout functionality.
- **Todo Management**: Create, toggle completion status, and delete todos.
- **Session Management**: Uses session middleware for maintaining user sessions.
- **Database Persistence**: Stores user and todo data in a SQLite database.
- **Templating**: Uses Jinja2 templates for rendering HTML pages.
- **UI with Tailwind CSS**: Uses Tailwind CSS for styling the user interface.
- **Responsive Design**: The layout is responsive, ensuring a good user experience on various devices.



## 🛠️ Tech Stack
- **Backend Framework**: FastAPI
- **Templating Engine**: Jinja2
- **Frontend Framework/Library**: Tailwind CSS
- **Database**: SQLite
- **Language**: Python



## 🚀 Installation
1.  **Clone the repository:**
   ```bash
   git clone https://github.com/Talha4543/Todo-Manager-Web-App.git
   cd Todo-Manager-Web-App
   ```
2.  **Install dependencies:**
    - While no explicit dependency management file is provided, the `app.py` file implies the use of `FastAPI`, `Jinja2Templates`, `starlette.middleware.sessions`, and `sqlite3`. You can install these using pip:
   ```bash
   pip install fastapi uvicorn Jinja2 starlette
   ```
    -  `uvicorn` is recommended to run the FastAPI application.
3.  **Database Setup:**
    - The application uses SQLite. The database file is `todos.db`. The database initialization is handled in `app.py` and `database.py`. You can run `app.py` once to create the database and tables.
4.  **Run the Application:**
   ```bash
   uvicorn app:app --reload
   ```
    - This command starts the FastAPI application using Uvicorn, with the `--reload` flag for automatic reloading upon code changes.
5.  **Access the application:**
    - Open your web browser and go to `http://127.0.0.1:8000` to access the Todo Manager Web App.



## 💻 Usage
1.  **Signup:**
    - Navigate to the `/signup` route to create a new account.
    - Enter a unique username and password.
2.  **Login:**
    - Navigate to the `/login` route to log in to your account.
    - Enter your username and password.
3.  **Add a Todo:**
    - Once logged in, you will be redirected to the index page (`/`).
    - Use the input field to enter a new task and click the `Add` button.
4.  **Toggle Todo Completion:**
    - Click the circle next to the task to toggle its completion status.
5.  **Delete a Todo:**
    - Click the `✖` button next to the task to delete it.
6.  **Logout:**
    - Click the `Logout` button in the navigation bar to log out of your account. You will be redirected to the login page.



## 📂 Project Structure
```
Todo-Manager-Web-App/
├── app.py             # Main FastAPI application file
├── database.py        # Database initialization logic
├── templates/         # Jinja2 templates for HTML pages
│   ├── base.html      # Base template with common layout elements
│   ├── index.html     # Template for the main todo list page
│   ├── login.html     # Template for the login page
│   └── signup.html    # Template for the signup page
├── todos.db           # SQLite database file
└── README.md          # Project documentation
```



## 🤝 Contributing
Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with clear, concise messages.
4.  Submit a pull request.



## 📜 License
This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).



## 🔗 Important Links
- **Repository Link**: [Todo-Manager-Web-App](https://github.com/Talha4543/Todo-Manager-Web-App)



## 📄 Footer
- Repository Name: Todo-Manager-Web-App
- Repository URL: https://github.com/Talha4543/Todo-Manager-Web-App
- Author: Talha4543

⭐️ Star the repository if you found it helpful!

⚖️ License: MIT License

📧 Contact: Open an issue on the repository for any questions or feedback.

Fork and contribute to make this project even better! 🎉