# 📝 Django Blog App  

A fully functional **Django Blog Application** with authentication, search, categories, featured posts, and an admin dashboard to manage **Users, Categories, and Blogs** (CRUD operations).  

---

## 🚀 Features  

- 🔐 **Authentication**  
  - User registration and login/logout  
  - Secure password handling  

- 📰 **Blog Management**  
  - Create, Read, Update, Delete (CRUD) blogs  
  - Featured blogs section  
  - Recent blogs section
  - Rich blog details with images and descriptions
  - Authenticated users can add comments on individual blogs 

- 🏷️ **Categories**
  - Add, edit, delete categories
  - Filter blogs by categories  
  - Manage categories via dashboard  

- 👤 **User Management**  
  - CRUD operations for users in dashboard  

- 🔎 **Search**  
  - Full-text search using Django `Q` objects  
  - Search by blog title, description, or content 

- 🖥️ **Dashboard**  
  - Manage blogs, categories, and users from a single panel  

---

## 🛠️ Technologies Used
- **Backend:** Django 5, Python 3
- **Frontend:** HTML5, CSS3, Bootstrap4
- **Database:** SQLite (default, can be changed)
- **Authentication:** Django built-in auth system 

## 📸 Screenshots

<img width="1896" height="903" alt="Screenshot 2025-09-07 154310" src="https://github.com/user-attachments/assets/cde72555-b708-4d69-bde4-473593165a91" />
<img width="1917" height="900" alt="Screenshot 2025-09-07 154334" src="https://github.com/user-attachments/assets/3a8a9c2f-9b59-4217-bca8-508a5128abc3" />
<img width="1897" height="903" alt="Screenshot 2025-09-07 154414" src="https://github.com/user-attachments/assets/dd58c4ee-aab9-4eb2-847c-fbda3a8582e6" />
<img width="1916" height="902" alt="Screenshot 2025-09-07 154445" src="https://github.com/user-attachments/assets/b7bd0177-425d-4762-bdac-06d09dce7df1" /> 

## ⚙️ Installation  

1. **Clone the repository**  
```bash
git clone https://github.com/Mihir154/django-blog-app.git
cd django-blog-app
```

2. **Create and activate virtual environment**
```bash
python -m venv env

# On Windows
env\Scripts\activate

# On Mac/Linux
source env/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Apply migrations**
```bash
python manage.py migrate
```

5. **Create superuser (admin account)**
```bash
python manage.py createsuperuser
```

6. **Run development server**
```bash
python manage.py runserver
```

Now open 👉 http://127.0.0.1:8000

## 📂 Project Structure
```bash
django-blog-app/
│── blog/                # Main app (models, views, templates)
│── blogproject/         # Project settings
│── templates/           # HTML templates
│── static/              # CSS, JS, images
│── env/                 # Virtual environment (ignored in git)
│── manage.py
│── requirements.txt
│── README.md
```

## 👨‍💻 Author
- Mihir Prajapati
