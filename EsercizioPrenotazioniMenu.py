
spooking()
while True:
    print("\n--- Spooking: Gestionale Prenotazioni Hotel Scrausi ---")
    print("1. Aggiungi utente")
    print("2. Aggiungi hotel")
    print("3. Effettua prenotazione")
    print("4. Visualizza prenotazioni")
    print("5. Cancella prenotazione")
    print("6. Report sintetico")
    print("7. Esci")
    scelta = input("Seleziona un'opzione: ")
    
    if scelta == "1":
        nome = input("Inserisci il nome dell'utente: ")
        cognome = input("Inserisci il cognome dell'utente: ")
        email = input("Inserisci l'email dell'utente: ")
        aggiungi_utente(nome, cognome, email)
    elif scelta == "2":
        nome = input("Inserisci il nome dell'hotel: ")
        citta = input("Inserisci la città: ")
        numero_camere = int(input("Inserisci il numero di camere: "))
        numero_letti = int(input("Inserisci il numero di letti: "))
        condizionatore = input("Ha il condizionatore? (si/no): ")
        servizio_in_camera = input("Ha il servizio in camera? (si/no): ")
        aggiungi_hotel(nome, citta, numero_camere, piano, numero_letti, condizionatore, servizio_in_camera)
    elif scelta == "3":
        utente_id = input("Inserisci ID utente: ")
        hotel_id = input("Inserisci ID hotel: ")
        data = input("Inserisci la data (YYYY-MM-DD): ")
        ora = input("Inserisci l'ora (HH:MM): ")
        effettua_prenotazione(utente_id, hotel_id, data, ora)
    elif scelta == "4":
        visualizza_prenotazioni()
    elif scelta == "5":
        prenotazione_id = input("Inserisci ID prenotazione da cancellare: ")
        cancella_prenotazione(prenotazione_id)
    elif scelta == "6":
        report_sintetico()
    elif scelta == "7":
        print("Arrivederci!")
        break
    else:
        print("Scelta non valida. Riprova.")