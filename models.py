import sqlite3

class Users:
    def __init__(self, username, password):
        self._username = username 
        self._password = password
        self._is_active = False
        
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, user):
        self._username = user
        
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, pass_word):
        self._password = pass_word
        
    def __str__(self) -> str:
        self._username
        
    def create(self):
        base = sqlite3.connect('users.db')
        cursor = base.cursor()
        
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS users (
                           id INTEGER PRIMARY KEY, 
                           username TEXT, 
                           password TEXT
                       )
                       ''')
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (self._username, self._password))
       
        base.commit()
        base.close() 