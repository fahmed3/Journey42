import sqlite3

f = "kafoot.db"
db = sqlite3.connect(f)
c = db.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT NOT NULL);')
c.execute('CREATE TABLE IF NOT EXISTS stats (username TEXT, category TEXT, score TEXT NOT NULL);')
db.close()

# Adds users to the user database
# Used with the new_user() function in auth.py (Encrypts the password)
# Returns true if successful
def adduser(username, password):
    f = "kafoot.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    if empty_db():
        c.execute('INSERT INTO users VALUES("%s", "%s");' %(username, password))
        db.commit()
        db.close()
        return True
    if get_password(username) is None:
        c.execute('INSERT INTO users VALUES("%s", "%s");' %(username, password))
        db.commit()
        db.close()
        return True
    db.close()
    return False

#Adds stats to the stats database
def addStat(username, category, score):
    f = "kafoot.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    c.execute('INSERT INTO stats VALUES("%s", "%s", "%s");' %(username, category, score))
    db.commit()
    db.close()

#returns a list of the stats of user
def getStats(username):
    f = "kafoot.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    #addStat("john", "math", "90")
    #addStat("john", "eng", "90")
    list = []
    for i in c.execute('SELECT category,score FROM stats WHERE username="%s";' %(username)):
        list.append(i)
    return list

# Returns true if the users database is empty
# False Otherwise
def empty_db():
    f = "kafoot.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    c.execute('SELECT * FROM users;')
    results = c.fetchall()
    return results == []

# Returns the password associated with the username given
# If the password doesn't exist, return None
def get_password(username):
    f = "kafoot.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    # print(username)
    c.execute('SELECT password FROM users WHERE username="%s";' %(username))
    results = c.fetchall()
    if results == []:
        db.close()
        return None
    else:
        db.close()
        return results[0][0]

def change_password(username, password):
    f = "kafoot.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    c.execute('UPDATE users SET password="%s" WHERE username="%s";' %(password, username))
    db.commit()
    db.close()
    return True
