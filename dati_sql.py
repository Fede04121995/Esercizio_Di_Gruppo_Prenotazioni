import mysql.connector

def init():
    try:
        mydb = mysql.connector.connect(    ##si connette solo al database
            host ="localhost",
            user = "root",
            password = "root",
            port = 8889, #Rimuovere o verificare n. porta in caso di utente Windows/Linux
            database = "spooking"
            )
        mycursor = mydb.cursor()
        print("Connection established")
    except:
        mydb = mysql.connector.connect(    ##si connette solo al database
            host ="localhost",
            user = "root",
            password = "root",
            port = 8889,
        )
        mycursor = mydb.cursor()
        query = "CREATE database spooking"
        mycursor.execute(query)
        query = "CREATE TABLE spooking.tab_utenti (ID INT auto_increment PRIMARY KEY, nome VARCHAR(20), cognome VARCHAR(30), email VARCHAR(50))"
        mycursor.execute(query)
        query = "CREATE TABLE spooking.tab_hotel (ID INT auto_increment PRIMARY KEY, nome_hotel VARCHAR(20), città VARCHAR(30), numero_camera INT, numero_letti INT, aria_condizionata BOOL)"
        mycursor.execute(query)
        query = "CREATE TABLE spooking.tab_prenotazioni (numero_prenotazione INT auto_increment PRIMARY KEY, nome_hotel VARCHAR(20), ID_camera INT, ID_cliente INT, FOREIGN KEY (ID_camera) REFERENCES tab_hotel(ID), FOREIGN KEY (ID_cliente) REFERENCES tab_utenti(ID))"
        mycursor.execute(query)
        mydb, mycursor = init() #Sewrve a salvare i valori e riportarli nel Try.
    return mydb, mycursor

mydb, mycursor = init()
