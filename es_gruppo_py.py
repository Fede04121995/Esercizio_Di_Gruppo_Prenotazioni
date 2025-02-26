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

#Inserire nuovi utenti.
def inserisci_utente(nome, cognome, email):
    query = "INSERT INTO tab_utenti(nome, cognome, email) VALUES (%s, %s, %s)"
    mycursor.execute(query, (nome, cognome,email)) 
    mydb.commit()
    print(mycursor.rowcount, "utente registrato aggiunto!")


#Aggiungere nuove risorse.
def aggiungi_risorse(nome_hotel, città, numero_camera, numero_letti, aria_condizionata):
    query = "INSERT INTO tab_hotel(nome_hotel, città, numero_camera, numero_letti, aria_condizionata) VALUES (%s, %s, %s, %s, %s )"
    mycursor.execute(query, (nome_hotel, città, numero_camera, numero_letti, aria_condizionata)) 
    mydb.commit()
    print(mycursor.rowcount, "risorsa aggiunta!")


#Effettuare, visualizzare e cancellare prenotazioni.
def effettua_prenotazioni(nome_hotel, ID_camera, ID_cliente):
    query = "INSERT INTO tab_prenotazioni(nome_hotel, ID_camera, ID_cliente) VALUES (%s, %s, %s)"
    mycursor.execute(query, (nome_hotel, ID_camera, ID_cliente)) 
    mydb.commit()
    print(mycursor.rowcount, "Prenotazione effettuata!")


def visualizza_prenotazione(numero_prenotazione):
    query = "SELECT * FROM table tab_prenotazioni WHERE ID_prenotazione = numero_prenotazione"
    mycursor.execute(query, (numero_prenotazione)) 
    mydb.commit()
    print(mycursor.rowcount, "Prenotazione visualizzata!")

def elimina_prenotazione(numero_prenotazione):
    query = "DROP * FROM table tab_prenotazioni WHERE ID_prenotazione = numero_prenotazione"
    mycursor.execute(query, (numero_prenotazione)) 
    mydb.commit()
    print(mycursor.rowcount, "Prenotazione visualizzata!")

#Mostrare un report sintetico delle prenotazioni esistenti
def visualizzaprenotazioni():
    query = "Select * FROM tab_prenotazioni"
    mycursor.execute(query)
    results = mycursor.fetchall()
    for riga in results:
        print(f"Numero Prenotazione: {riga[0]}, Nome hotel: {riga[1]}, ID camera: {riga[2]}, ID cliente {riga[3]}")
        

