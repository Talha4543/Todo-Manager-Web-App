from fastapi import FastAPI, Request, Form, status
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
import sqlite3, hashlib, os

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="supersecretkey")
templates = Jinja2Templates(directory="templates")

DB_FILE = "todos.db"
import sqlite3

conn = sqlite3.connect("todos.db")
cursor = conn.cursor()

# 🚨 Drop old table (only if no important data)
cursor.execute("DROP TABLE IF EXISTS todos")

# ✅ Recreate with correct columns
cursor.execute("""
CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    completed INTEGER NOT NULL DEFAULT 0,
    username TEXT NOT NULL
)
""")

conn.commit()
conn.close()
print("✅ Todos table recreated successfully")

# ----------------- DB Setup -----------------
def init_db():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    # Users table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    # Todos table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT 0,
            username TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

init_db()

# ----------------- Utility -----------------
def get_password_hash(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def get_user(username: str):
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    user = conn.execute("SELECT * FROM users WHERE username=?", (username,)).fetchone()
    conn.close()
    return user

def get_todos(username: str):
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    todos = conn.execute("SELECT * FROM todos WHERE username=?", (username,)).fetchall()
    conn.close()
    return todos

# ----------------- Routes -----------------
@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    username = request.session.get("username")
    if not username:
        return RedirectResponse("/login")

    todos = get_todos(username)
    return templates.TemplateResponse("index.html", {"request": request, "todos": todos, "username": username})

@app.post("/add")
async def add_task(request: Request, title: str = Form(...)):
    username = request.session.get("username")

    if not username:
        return RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)

    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO todos (title, completed, username) VALUES (?, ?, ?)",
            (title, 0, username),
        )
        conn.commit()
        conn.close()
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)

    except Exception as e:
        import traceback
        print("🔥 Error while adding task:", e)
        traceback.print_exc()
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)

@app.post("/toggle/{todo_id}")
def toggle_task(request: Request, todo_id: int):
    username = request.session.get("username")
    if not username:
        return RedirectResponse("/login")

    conn = sqlite3.connect(DB_FILE)
    conn.execute("UPDATE todos SET completed = NOT completed WHERE id=? AND username=?", (todo_id, username))
    conn.commit()
    conn.close()
    return RedirectResponse("/", status_code=303)

@app.post("/delete/{todo_id}")
def delete_task(request: Request, todo_id: int):
    username = request.session.get("username")
    if not username:
        return RedirectResponse("/login")

    conn = sqlite3.connect(DB_FILE)
    conn.execute("DELETE FROM todos WHERE id=? AND username=?", (todo_id, username))
    conn.commit()
    conn.close()
    return RedirectResponse("/", status_code=303)

# ----------------- Auth -----------------
@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "error": None})

@app.post("/login")
def login(request: Request, username: str = Form(...), password: str = Form(...)):
    user = get_user(username)
    if not user:
        return templates.TemplateResponse("login.html", {"request": request, "error": "User not found"})
    
    hashed = get_password_hash(password)
    if user["password"] != hashed:
        return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid password"})

    request.session["username"] = username
    return RedirectResponse("/", status_code=303)

@app.get("/signup", response_class=HTMLResponse)
def signup_page(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request, "error": None})

@app.post("/signup")
def signup(request: Request, username: str = Form(...), password: str = Form(...)):
    if get_user(username):
        return templates.TemplateResponse("signup.html", {"request": request, "error": "Username already taken"})

    hashed = get_password_hash(password)
    conn = sqlite3.connect(DB_FILE)
    conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed))
    conn.commit()
    conn.close()

    request.session["username"] = username
    return RedirectResponse("/", status_code=303)

@app.get("/logout")
def logout(request: Request):
    request.session.clear()
    return RedirectResponse("/login")
