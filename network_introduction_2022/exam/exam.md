# Esame Zorin Febbraio 2023

## Consegna

- Viene fornito in allegato un file python da completare con pezzi mancanti. 
- Non modificare l'intestazione delle funzioni, i parametri che vengono passati alle stesse e l'"if else" presente nel main()
- Per il funzionamento del comando ifconfig deve essere installata la libreria net-tools

## Note

- La libreria subprocess permette di lanciare tramite python
dei comandi che normalmente verrebbero lanciati dal terminale
- subprocess.run permette di lanciare un comando
- subprocess.check_output permette di lanciare un comando
e di salvarne l'output
- La sintassi sara' del tipo:
	~~~
	subprocess.run('cmd', shell=True)
	subprocess.check_output('cmd', shell=True)
	~~~
- Per convertire gli output del terminale in stringhe potrebbe essere necessario utilizzare la funzione decode:
	~~~
	subprocess.check_output(*command*, shell=True).decode('utf-8')
	~~~
- La funzione subprocess.run restituisce un bool che indica se la funzione lanciata è andata o meno a buon fine
- Per inviare un numero limitato di pacchetti col ping, aggiungere -c *n_pacchetti*