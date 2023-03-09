import sqlite3

conn = sqlite3.connect("Project_database.db")
c = conn.cursor()

class Functions():
    @staticmethod
    def Insert_into_users(z,y,x):
        import sqlite3
        conn = sqlite3.connect("Project_database.db")
        C = conn.cursor()
        conn.commit()

    @staticmethod
    def Get_User_ID_by_password(password):
    if password != '':
        c.execute("""SELECT password,UserID FROM Users WHERE password = ?""", (password,))
        var = c.fetchone()
        conn.commit()
        return var[2]
    else:
        raise OSError("User doesn't exist")
        
v = Functions()