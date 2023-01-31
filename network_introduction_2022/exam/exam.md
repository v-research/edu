# Esame Zorin Febbraio 2023

## Consegna

- Viene fornito in allegato un file python da completare con pezzi mancanti. 
- Non modificare l'intestazione delle funzioni e i parametri che vengono passati alle stesse.
- Per il funzionamento del comando ifconfig deve
- Per eseguire il file python utlizzare il comando
	~~~
	python3 *nome_file.py*
	~~~

## Esercizi

1. 

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