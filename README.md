# todo-list

Project overview
--------

todo_list is a web application for organizing personal tasks.

Setup
--------
To set up the project on your local machine, follow these steps:

1. Clone the Repository
```sh
git clone https://github.com/olenazaritska/todo-list.git
cd todo_list
```
2. Create and Activate Virtual Environment
```sh
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS/Linux)
```
3. Install Dependencies
```sh
pip install -r requirements.txt
```
4. Run Migrations
```sh
python manage.py migrate
```
5. Run the Development Server
```sh
python manage.py runserver
```

Features
--------

- TODO List
    - View task list with completed status, creation date & tags
    - Add/update/delete a task
    - Mark a task as completed or pending
- Tags
    - View tags table
    - Add/update/delete a tag
