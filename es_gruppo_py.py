import mysql.connector

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



#Mostrare un report sintetico delle prenotazioni esistenti




