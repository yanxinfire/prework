import mysql.connector


class MyDB:
    def __init__(self, cfg):
        self.db = mysql.connector.connect(
            host=cfg["mysql_host"],
            port=cfg["mysql_port"],
            user=cfg["mysql_user"],
            password=cfg["mysql_password"],
            database=cfg["mysql_database"]
        )

    def create_user(self, user):
        mycursor = self.db.cursor()
        sql = "INSERT INTO users (first_name, last_name, age) VALUES (%s, %s, %s)"
        val = (user["first_name"], user["last_name"], user["age"])
        try:
            mycursor.execute(sql, val)
        except mysql.connector.Error as err:
            return {"error": f"{err}"}
        self.db.commit()
        return {"msg": 'create user successfully'}

    def get_users(self, first_name, last_name, start, offset):
        mycursor = self.db.cursor()
        sql = "SELECT id, first_name, last_name, age FROM users WHERE 1=1 "
        if first_name is not None:
            sql += f" and first_name='{first_name}' "
        if last_name is not None:
            sql += f" and last_name='{last_name}' "
        sql += f" limit {start},{offset} "
        try:
            mycursor.execute(sql)
        except mysql.connector.Error as err:
            return {"error": f"{err}"}

        myresult = []
        for u in mycursor.fetchall():
            myresult.append(
                {"id": u[0], "first_name": u[1], "last_name": u[2], "age": u[3]}
            )
        return myresult

    def get_user_by_id(self, user_id):
        mycursor = self.db.cursor()
        sql = f"SELECT id, first_name, last_name, age FROM users WHERE id = {user_id}"
        try:
            mycursor.execute(sql)
        except mysql.connector.Error as err:
            return {"error": f"{err}"}
        for u in mycursor.fetchall():
            return {"id": u[0], "first_name": u[1], "last_name": u[2], "age": u[3]}

    def update_user(self, user_id, user):
        mycursor = self.db.cursor()
        sql = "UPDATE users SET first_name=%s, last_name=%s, age=%s where id = %s"
        val = (user["first_name"], user["last_name"], user["age"], user_id)
        try:
            mycursor.execute(sql, val)
        except mysql.connector.Error as err:
            return {"error": f"{err}"}
        self.db.commit()
        return {"msg": 'update user successfully'}

    def delete_user(self, user_id):
        mycursor = self.db.cursor()
        sql = f"DELETE FROM users WHERE id = {user_id}"
        try:
            mycursor.execute(sql)
        except mysql.connector.Error as err:
            return {"error": f"{err}"}
        self.db.commit()
        return {"msg": 'delete user successfully'}
