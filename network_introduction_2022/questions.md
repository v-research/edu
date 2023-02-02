# Domande esame teoria reti

1. Quali sono i mezzi trasmissivi utilizzati per la connessione di dispositivi?
   1.  Doppino in rame, cavo coassiale, fibra ottica, etere (CORRETTA)
   2.  Doppino in rame, cavo ethernet, fibra ottica, bluetooth
   3.  Fibra ottica, etere, cavo UTP, cavo STP, cavo FTP

2. Quali sono le differenze tra FTTH e FTTC?
   1.  FTTH è generalmente più lenta della FTTC e ha un costo inferiore
   2.  FTTH è generlamente più veloce della FTTC, ma dovendo portarti il cavo in fibra fino a casa la sua installazione è più costosa e per questo è meno diffusa (CORRETTA)
   3.  A differenza della FTTC, la FTTH è la versione più vecchia della fibra ottica ed è già disponibile in tutte le abitazioni italiane

3. I pacchetti vengono instradati all'interno di una rete di nodi con due differenti approcci:
   1.  Commutazione di pacchetto e commutazione di circuito (CORRETTA)
   2.  Commutazione di pacchetto con rete a datagramma e commutazione di pacchetto con rete a circuito virtuale
   3.  Commutazione di circuito e rete a circuito virtuale

4. Quale tra le seguenti affermazioni non è vera?
   1.  Lo stack TCP/IP segue uno schema logico gerarchico nella suddivisione dei livelli e alcuni dei protocolli più utilizzati sono HTTP, TCP, IP e TLS
   2.  Lo stack ISO/OSI è uno standard teorico, ha 7 livelli e non viene implementato perché la sua gestione renderebbe lo scambio di informazioni più complicato di quanto non lo sia col TCP/IP
   3.  Lo stack TCP/IP è lo standard de facto, ha 6 livelli e prende il nome dai due protocolli principali (CORRETTA)

5. Cosa fa il livello di trasposto?
   1.  Consente la comunicazione degli host sorgente e destinazione utilizzando i protocolli TCP e HTTP
   2.  Consente la comunicazione degli host sorgente e destinazione utilizzando i protocolli FTP, SMTP, HTTP e HTTPS
   3.  Consente la comunicazione degli host sorgente e destinazione utilizzando i protocolli TCP e UDP (CORRETTA)

6. Quale dei seguenti parametri indica la lunghezza del prefisso di una rete?
   1.  Indirizzo di rete
   2.  Netmask (CORRETTA)
   3.  Indirizzo ip del nostro dispositivo

7. A cosa servono le reti private?
   1.  A sopperire alla scarsità di indirizzi ipV4 pubblici (CORRETTA)
   2.  A garantire moltissima privacy all'utente che naviga in Internet
   3.  A permettere ad aziende con sedi differenti molto distanti tra loro di collegare tutti i loro dispositivi creando un'unica grande rete privata dell'azienda

8. Come avviene il Three Way Handshake del TCP?
   1.  Il server vuole iniziare la connessione verso il client e invia un pacchetto con SYN=1 e ACK=0, il client risponde con un pacchetto con SYN=1 e ACK=1, il server risponde con un pacchetto con SYN=0 e ACK=1, entrambi i dispositivi hanno riservato le risorse necessarie per instaurare la connessione e possono iniziare a comunicare
   2.  Il client vuole iniziare la connessione verso il client e invia un pacchetto con SYN=1 e ACK=1, il server risponde con un pacchetto con SYN=0 e ACK=1, il client risponde con un pacchetto con SYN=1 e ACK=1, entrambi i dispositivi hanno riservato le risorse necessarie per instaurare la connessione e possono iniziare a comunicare
   3.  Il client vuole iniziare la connessione verso il client e invia un pacchetto con SYN=1 e ACK=0, il server risponde con un pacchetto con SYN=1 e ACK=1, il client risponde con un pacchetto con SYN=0 e ACK=1, entrambi i dispositivi hanno riservato le risorse necessarie per instaurare la connessione e possono iniziare a comunicare (CORRETTA)

9. A differenza del TCP, l'UDP:
   1.  È un protocollo affidabile, il calcolo del checksum è obbligatorio ed è più veloce del TCP e non supporta il multicast
   2.  È un protocollo non affidabile, è più veloce del TCP e viene solitamente utilizzato per la trasmissione di contenuti video (CORRETTA)
   3.  È un protocollo non affidabile, è più veloce del TCP, viene solitamente utilizzato per la trasmissione di siti web e non supporta il broadcast

10. Il NAT (Network Address Translation):
    1.  Serve per identificare univocamente una connessione grazie alla tupla (ip src, ip dst) e insieme al subnetting risolve il problema della scarsità di indirizzi ip pubblici
    2.  Serve per identificare univocamente una connessione grazie alla tupla (ip src, port src, ip dst, port dst) e insieme al subnetting risolve il problema della scarsità di indirizzi ip pubblici (CORRETTA)
    3.  Serve per convertire un indirizzo ip testuale nel suo corrispettivo logico

11. Come vengono assegnati gli indirizzi ip all'interno di una rete privata se non vengono definitivi degli indirizzi ip statici per i dispositivi?
    1.  Il server DHCP di rete si occupa di fornire ai client che si connettono alla rete un indirizzo ip dinamico con validità limitata definita dal tempo di lease (CORRETTA)
    2.  Il client DHCP di rete si occupa di fornire un indirizzo ip dinamico con validità illimitata a tutti gli altri client che si connettono alla rete
    3.  Il server DNS si occupa di convertire gli hostname dei dispositivi che si connettono alla rete nel corrispondente indirizzo ip e salva in memoria quali ip sono connessi alla rete. L'hostname di ogni dispositivo ha un corrispondente indirizzo ip univoco e che non varia mai anche se si connette a reti differenti

12. Quale tra le seguenti affermazioni è vera?
    1.  HTTP è la versione sicura di HTTPS, implementa SSL e utilizza la porta 443 per comunicare
    2.  TLS permette di cifrare i pacchetti a livello applicativo, viene implementato nel protocollo HTTP e fa sì che eventuali hacker che intercettano i nostri pacchetti facendo sniffing non riescano a leggerne il contenuto
    3.  HTTPS è la versione sicura di HTTP, implementa TLS e utilizza la porta 443 per comunicare. La comunicazione tramite HTTPS prevedere l'utilizzo di una crittografia ibrida (CORRETTA)