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

    def customer_add(self, vorname, nachname):
        self.__corsor.execute('''
        SELECT MAX (pk) FROM customer;
        ''')
        pk = 0
        ret = self.__corsor.fetchall()
        ret_tupel = ret[0]
        ret = ret_tupel[0]
        if ret == None:
            pk = 1
        else:
            pk = ret+1
        self.__corsor.execute('''
        INSERT INTO customer
        VALUES  ("{}", "{}", "{}");
        '''.format(pk, vorname, nachname))
        self.__connection.commit()
        return pk

    def getCustomer(self):
        self.__corsor.execute('''
        SELECT * FROM customer;
        ''')
        ret = self.__corsor.fetchall()
        return ret

    def getCustomerInfo(self, pk):
        self.__corsor.execute('''
                SELECT * FROM customer
                WHERE pk = {};
                '''.format(pk))
        ret = self.__corsor.fetchall()
        return ret