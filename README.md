# Cafe "Feeling Happy" project

![img.png](readme_images/img.png)

## Description

Django project for cafe named "Feeling Happy"

## Check it out!

[Cafe project deployed on Render](https://cafe-feeling-happy.onrender.com/)

You can use test user credentials to see more functionality:
- login: `test.user`
- password: `InsequreTestPass123`


## Table of content

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Demo](#demo)

## Features

All users:

    - Registration (only as client of cafe, not admin)
    - Authorisation
    - Review and updating current authorisated user's profile info
    - Review dishes in the menu
    - Managing dishes inside order and order creation

Admins:

    - Managing dishes inside menu (create, update, delete)

## Installation
Python3 must be already installed
1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/OlhaTryhub/cafe-web-site.git
    ```
2. Change into the project directory:
    ```bash
   cd your-repo
    ```
3. Create and activate a virtual environment (optional but recommended):
   ```bash
    python -m venv venv
    venv\Scripts\activate  # On Mac, use: source venv/bin/activate
   ```
4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt 
    ```
5. Apply database migrations:
    ```bash
    python manage.py migrate
    ```
   
## Usage
1. Load data into DB from data.json file (optional):
    ```bash
    python manage.py loaddata data.json
    ```
   For using app as admin you must create your own superuser with command:
    ```bash
    python manage.py createsuperuser
    ```
2. Start your local Django server:
    ```bash
    python manage.py runserver
    ```
3. Open your web browser and navigate to http://127.0.0.1:8000/ to access the application.

## Demo

1. Main page

![img_1.png](readme_images/img_1.png)

2. Login

![img_3.png](readme_images/img_3.png)

3. Registration

![img_4.png](readme_images/img_4.png)

4. User page

![img_6.png](readme_images/img_6.png)

5. Updating user's info page

![img_7.png](readme_images/img_7.png)

6. Menu
- For unauthenticated user/cafe client

![img_2.png](readme_images/img_2.png)

- For admin:

![img_5.png](readme_images/img_5.png)

7. Dish detail page:

- For unauthenticated user/cafe client

![img_9.png](readme_images/img_9.png)

- For admin

![img_8.png](readme_images/img_8.png)

8. Orders list page

![img_10.png](readme_images/img_10.png)

9. Oder detail page

- Unconfirmed order

![img_11.png](readme_images/img_11.png)

- Confirmed order

![img_12.png](readme_images/img_12.png)


