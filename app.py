import mysql.connector as conn
import time

while True:
    try:
        db = conn.connect(
            host="10.0.10.3",
            user="pfirysiuk",
            password="pass",
            database="projekt"
        )
        break
    except Exception:
        time.sleep(2)

curr = db.cursor()
curr.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), login VARCHAR(255))")

insert = "INSERT INTO users (name, login) VALUES (%s, %s)"
val = [("Pawel", "paww"), ("Robert", "robb"), ("Jarek", "kwakwa")]
curr.executemany(insert, val)
db.commit()
print(curr.rowcount, " was inserted")

def print_menu():
    print("1. SELECT")
    print("2. INSERT")
    print("3. UDATE")
    print("4. DELETE")


print_menu()

while True:
    print_menu()
    print("Co chcesz zrobic?")
    action = int(input())

    if action == 1:
        #select
        curr.execute("SELECT * FROM users")
        for user in curr.fetchall():
            print(user)
    elif action == 2:
        print("Podaj name:")
        name = input()
        print("Podaj login:")
        login = input()
        curr.execute(insert, (name, login))
        db.commit()
    elif action == 3:
        #update
        print("Ktorego usera zmodyfikowac? podaj id:")
        user_id = input()
        print("Podaj name:")
        name = input()
        print("Podaj login:")
        login = input()
        update = "UPDATE users SET name = %s, login = %s WHERE id = %s"
        val = (name, login, user_id)
        curr.execute(update, val)
        db.commit()
        print(curr.rowcount, " record(s) affected")
    elif action == 4:
        #delete
        print("Ktorego usera usunac? podaj id:")
        user_id = input()
        delete = "DELETE FROM users WHERE id = %s"
        curr.execute(delete, user_id)
        db.commit()
        print(curr.rowcount, " record(s) deleted")
    else:
        break

