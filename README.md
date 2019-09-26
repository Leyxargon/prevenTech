# prevenTech
<img src="./static/img/logo_nero.png">
PrevenTech è un sito web che consente di ricercare gli erogatori di profilattici più vicini alla propria zona.
Il progetto è stato sviluppato per l'esame di Tecnologie Web della *Università degli Studi di Napoli "Parthenope"*.

## Componenti utilizzati
- Python3
- MongoDB
- Leaflet (OpenStreetMap)

## Installazione componenti progetto
```
pip3 install -r requirements.txt
```
## Configurazione server MongoDB
L'applicativo usufruisce di un database MongoDB Atlas per caricare i segnaposti sulla mappa. Per utilizzare il vostro database basta inserire l'URI fornito da MongoDB Atlas all'interno della chiamata `MongoClient()` nel file `app.py`, che avrà una sintassi di questo tipo
```
client = MongoClient("mongodb+srv://<username>:<password>@<cluster>.mongodb.net/test?retryWrites=true&w=majority")
```
È necessario inoltre fornire il nome di una delle collezioni che l'applicativo web dovrà utilizzare.
```
app.config['MONGO_DBNAME'] = 'MIA_COLLEZIONE'
```

## Configurazione server mail
Nel file `app.py` dovete compilare le seguenti righe di istruzioni con le informazioni richieste dal sito web.
```
app.secret_key = 'MIA_CHIAVE_SEGRETA'
app.config["MAIL_SERVER"] = "NOME_SERVER_SMTP"
app.config["MAIL_PORT"] = NUMERO_PORTA
app.config["MAIL_USE_SSL"] = True OR False
app.config["MAIL_USERNAME"] = 'MIO_INDIRIZZO_EMAIL'
app.config["MAIL_PASSWORD"] = 'MIA_PASSWORD'
```

## Esegui
Dopo aver completato le configurazioni *preliminari* avviare l'applicazione web basta aprire il file `app.py`, che renderà il sito accessibile sulla porta 5000.

Salva la quaglia, proteggiti.
Buon divertimento con la nostra app!
