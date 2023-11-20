[![Quality gate](https://sonarcloud.io/api/project_badges/quality_gate?project=Kapshtyk_cat_charity_fund)](https://sonarcloud.io/summary/new_code?id=Kapshtyk_cat_charity_fund)

[![FastAPI testing workflow](https://github.com/Kapshtyk/cat_charity_fund/actions/workflows/main.yaml/badge.svg)](https://github.com/Kapshtyk/cat_charity_fund/actions/workflows/main.yaml)

# Cat charity project QRKot
This is a simple API written in Python using the FastAPI framework. It allows users to create charity projects and make donations. The distribution of funds between the charity projects is done automatically under the hood.

## Main technologies:
- FastAPI
- SQL Alchemy
- Alembic

## Main features
- User can view the list of charity projects and his donations.
- Superuser can create the charity project with unique name, description and required funding amount.
- Superuser can delete the charity projects without investments.
- Superuser can change the name of the charity project or update the required funding amount.
- Any registered user can make a donation. Information about the target charity project is not allowed for users.
- After creating a new project or donation, the investment process comes to action. Free money will be invested in the new charity project and visa versa.

## Getting Started

1. Clone this repository to your local machine.
```
git clone git@github.com:Kapshtyk/cat_charity_fund.git
cd cat_charity_fund
```
2. Set up a virtual environment and install the required packages from the `requirements.txt` file.
```
python3 -m venv venv
```
MacOS/Linux:
```
source venv/bin/activate
```
Windows:
```
source venv/scripts/activate
```
```
pip install -r requirements.txt
```
3. Create `.env` file in the root of the project (you can use .env.example as a reference)
4. Initialise the database (SQLite) for development.
```
alembic upgrade head
```
5. Start the FastAPI application.
```
uvicorn app.main:app
```
6. During the first run of the application a superuser with email `admin@admin.ru` and password `admin` will be created (if you didn't change the credentials in the .env). These credentials can be used to access the API features via Postman or Swagger (see below).

## User Interface

This project only provides the API, so you will need to use Postman (or another similar tool) to interact with the application. Another option is to use the Swagger documentation at `http://localhost:8000/docs`. You will need to authorise yourself using the Authorise button.

## Swagger documentation screenshot

![desktop](https://github.com/Kapshtyk/cat_charity_fund/blob/master/screenshots/localhost_8000_docs.png?raw=true)

## Acknowledgments

This project was created as part of a sprint assignment. Thank you for checking it out!

## Author
- LinkedIn - [Arseniiy Kapshtyk](https://www.linkedin.com/in/kapshtyk/)
- Github - [@kapshtyk](https://github.com/Kapshtyk)
