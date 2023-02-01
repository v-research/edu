# Esame Zorin Febbraio 2023

## Consegna

- Viene fornito in allegato un file python da completare con pezzi mancanti. 
- Non modificare l'intestazione delle funzioni e i parametri che vengono passati alle stesse.
- Per il funzionamento del comando ifconfig deve essere installata la libreria net-tools
- Per eseguire il file python utlizzare il comando
	~~~
	python3 *nome_file.py*
	~~~

## Esercizi

### check_internet_connections

Restituire un bool che indica se dal nostro terminale riusciamo a raggiungere google.com.

## Note

La libreria subprocess permette di lanciare tramite python
dei comandi che normalmente verrebbero lanciati dal terminale.

subprocess.run permette di lanciare un comando.
subprocess.check_output permette di lanciare un comando
e di salvarne l'output.

La sintassi sara' del tipo:
subprocess.run('cmd', shell=True)
subprocess.check_output('cmd', shell=True)

La funzione subprocess.run restituisce un bool che indica se la funzione lanciata è andata o meno a buon fine

Per limitare il numero di pacchetti inviati dal ping, lanciare il comando con i parametri -c 21 dove 21 indica il numero di pacchetti che vogliamo inviare:
	~~~
	ping -c 21 ciao.it
	~~~
