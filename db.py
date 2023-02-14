import sqlite3

class DB:
    __connection = ""
    __corsor = ""

    def __init__(self):
        #Verbindung zu Datenbank wird aufgebaut
        self.__connection = sqlite3.connect("db1.db")
        self.__corsor = self.__connection.cursor()
        #Tabelle anlegen
        self.__corsor.execute('''
        CREATE TABLE IF NOT EXISTS customer(
            pk INTEGER PRIMARY KEY,
            vorname TEXT,
            nachname TEXT
        );
        ''')
        self.__connection.commit()

    def customer_add(self, vorname, nachname, email):
        pass