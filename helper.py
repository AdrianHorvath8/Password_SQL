import os
import sys
import psycopg2
import psycopg2.extras
from psycopg2 import sql

conn = psycopg2.connect(
    host = os.getenv("POSTGRES_HOST","localhost"),
    database = os.getenv("POSTGRES_DATABASE","postgres"),
    user = os.getenv("POSTGRES_USER","postgres"),
    password = os.getenv("POSTGRES_PASSWORD","postgressql")
)
cursor = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
 
def get_name(application):
    select_sql = sql.SQL(
    "SELECT name FROM password WHERE application = {application}"
    ).format(
        application = sql.Literal(application),
    )
    cursor.execute(select_sql)
    look = cursor.fetchall()
    name_look = look[0]
    print(f"Name is: {name_look['name']}")

def get_passw(application):
    select_sql = sql.SQL(
    "SELECT passw FROM password WHERE application = {application}"
    ).format(

        application = sql.Literal(application),
    )
    cursor.execute(select_sql)
    look = cursor.fetchall()
    passw_look = look[0]
    print(f"Password is: {passw_look['passw']}")

def get_app():
    cursor.execute(
        "SELECT application FROM password"
    )
    look = cursor.fetchall()
    print(look)
    return look

def main_passw():
    main_passw = input("Enter main passworrd please: ")
    if main_passw == "123456":
        pass
    else:
        sys.exit("Wrong main password")

def menu():
    print("\n1. Add new password")
    print("2. View passwords")
    print("3. Delete password by name of application")
    print("4. Delete all passwords")
    print("5. Eddit name or password by name of application")
    print("6. Get name and password by using application name")
    print("7. Exit\n")

def add_passw():
    application = input("Application: ")
    print("Are you sure that name off application is "+application,"?")
    decision = input("Answer: ")
    if decision == "yes" or decision == "no":
        pass
    else:
        print("Please write yes or no")
        return
    if decision == "yes":
        pass
    if decision == "no":
        print("Please try it again")
        return
    name = input("Name: ")
    passw = input("Password: ")
    select_sql = sql.SQL(
    "INSERT INTO password (application,name,passw) VALUES ({application},{name},{passw})"
    ).format(
        name = sql.Literal(name),
        passw = sql.Literal(passw),
        application = sql.Literal(application),
    )
    cursor.execute(select_sql)
    conn.commit()

def view_passw():
    cursor.execute(
        "SELECT * FROM password"
    )
    look = cursor.fetchall()
    print(look)

def delete_passw_by_app():
    get_app()
    application = input("Application: ")
    select_sql = sql.SQL(
    "DELETE FROM password WHERE application = {application}"
    ).format(
        application = sql.Literal(application),
    )
    cursor.execute(select_sql)
    conn.commit()

def delete_all_passw():
    question = input("Are you sure, the passwords will be lost forever: ")
    if question == "yes" or question == "no":
        pass
    else:
        print("Please type yes or no")
        return
    if question == "yes":
        pass
    if question == "no":
        return
    cursor.execute(
        "TRUNCATE TABLE password RESTART IDENTITY;"
    )
    conn.commit()

def eddit():
    get_app()
    application = input("Application: ")
    decision = input("Do you wanna eddit name or password: ")
    if decision == "name" or decision == "password":
        pass
    else:
        print("Please type name or password")
        return
    if decision == "name":
        try:
            get_name(application)
            change = input("How you wanna to change: ")
            select_sql = sql.SQL(
            "UPDATE password SET name = {change} WHERE application = {application}"
            ).format(
                change = sql.Literal(change),
                application = sql.Literal(application),
            )
            cursor.execute(select_sql)
            conn.commit()
        except:
            print("Wrong application name")
    if decision == "password":
        try:
            get_passw(application)
            change = input("How you wanna to change: ")
            select_sql = sql.SQL(
            "UPDATE password SET passw = {change} WHERE application = {application}"
            ).format(
                change = sql.Literal(change),
                application = sql.Literal(application),
            )
            cursor.execute(select_sql)
            conn.commit()
        except:
            print("Wrong application name")

def get_name_passw():
    try:
        get_app()
        application = input("Application: ")
        get_name(application)
        get_passw(application)
    except:
        print("Wrong application name")

def exit_program():
    sys.exit("See you later")
    
conn.close
cursor.close
