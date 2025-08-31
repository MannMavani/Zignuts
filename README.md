# Django Blog Application

A full-featured blog platform built with Python and the Django Web Framework. This project was created as a comprehensive learning exercise, covering the fundamentals of Django from project setup to advanced features like user authentication, staff permissions, and image uploads.

The application follows the Model-View-Template (MVT) architectural pattern and is designed to be a robust foundation for a content-driven website.



## Features

-   **Full User Authentication**: Secure user registration, login, and logout functionality using Django's built-in auth system.
-   **CRUD Operations**: Authenticated users can Create, Read, Update, and Delete their own blog posts.
-   **Admin/Staff Permissions**: A designated staff user (e.g., "Mann") has special privileges to edit or delete *any* post on the site, providing moderation capabilities.
-   **Image Uploads**: Users can upload a featured image for each blog post, which is handled securely using `Pillow` and Django's media file management.
-   **Dynamic Content Rendering**: Clean, responsive frontend built with Bootstrap 5 that dynamically displays posts.
-   **Pagination**: The main blog page is paginated to efficiently handle a large number of posts.
-   **Search Functionality**: Users can search for posts by keywords in the title or content.
-   **Success/Error Messaging**: Interactive feedback for users after performing actions like deleting a post, using Django's messages framework.
-   **Responsive Design**: The UI is fully responsive and works seamlessly on desktop, tablet, and mobile devices.

## Technology Stack

-   **Backend**: Python, Django
-   **Frontend**: HTML, CSS, Bootstrap 5
-   **Database**: SQLite 3 (for development)
-   **Key Python Libraries**:
    -   `django-crispy-forms`
    -   `crispy-bootstrap5`
    -   `Pillow`

---

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Make sure you have Python and Pip installed on your system.
- [Python (3.8+)](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/installation/)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/MannMavani/Zignuts.git](https://github.com/MannMavani/Zignuts.git)
    ```

2.  **Navigate to the project directory:**
    * **Important**: The Django project is inside the `Django/` subdirectory.
    ```bash
    cd Zignuts/Django
    ```

3.  **Create and activate a virtual environment:**
    * On Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    * On macOS/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

4.  **Install the required dependencies:**
    * The `req.txt` file contains all the necessary packages.
    ```bash
    pip install -r req.txt
    ```

5.  **Apply database migrations:**
    * This will create the database file (`db.sqlite3`) and set up the necessary tables.
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6.  **Create a superuser:**
    * This account will have access to the Django admin panel.
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to create your admin username and password.

7.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    The application will be available at `http://120.0.0.1:8000/`.

---

## Usage

-   **Public Site**: Navigate to `http://127.0.0.1:8000/` to view the blog, read posts, and use the search functionality.
-   **User Registration**: New users can sign up for an account to create their own posts.
-   **Admin Panel**: Log in as the superuser at `http://127.0.0.1:8000/admin/` to manage users and posts directly through Django's powerful admin interface.
-   **Staff Permissions**: To grant a user permission to edit/delete all posts, go to the admin panel, select the user, and check the "Staff status" box under the permissions section.

## Author

* **Mann Mavani** - [GitHub Profile](https://github.com/MannMavani)

