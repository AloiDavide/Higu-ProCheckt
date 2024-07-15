## Topics

[[Tutte le domande]]

[[Le tre famiglie - Domande wata]]

[[Misteri esterni]]

[[La serie di omicidi]]

[[Misteri principali]]

[[La cospirazione del BKG]]



# Formato file taccuino
- Ad ogni file di testo corrisponde un topic.
- Ad ogni pagina corrisponde una domanda.
- Le sezioni di una pagina sono separate da un dash "-"
- Pagine diverse sono separate da tre dash "---"


## Sequenza di risposte
Il modo migliore per fare susseguire risposte multiple sulla stessa pagina è fare finta.
Se vogliamo mantenere la risposta vecchia ma ~~sbarrata~~, la riscriviamo nella risposta nuova con la sintassi che la fa comparire ~~sbarrata~~.
```
Questa è una domanda.
-
Chi è best girl?
-
È rena!
-
{s}È rena!{/s}

No! È Mion!
```


## Indice risposta da mostrare
Per marcare la risposta attiva nel file base userei una cosa del genere:
- Viene mostrata la risposta dove il trattino che la precede ha un punto esclamativo.
- Se nessuno lo ha, non viene mostrata nessuna risposta.

Esempio. In questo caso la risposta mostrata sarebbe "Cavolfiori"
```
Domanda per Satoko.
-
Chi è verde, cavolfiori o broccoli?
-!
Cavolfiori
-
Broccoli
```


## Flag risposta nuova
Allo stesso modo
- Una domanda è evidenziata se ha un punto esclamativo dopo il --- sopra il titolo.
Like this
```
---
Questa appare come non letta.
-
Nipah
-
Auu
---!
Questa appare come letta.
-
Nipah
-
Auu
```
Ovviamente visualizzare a schermo la domanda la rende letta in automatico, e in generale questi valori possono essere modificati da dentro la visual novel in risposta a determinati eventi.

---

## Piccolo dietro le quinte
L'organizzazione in file di testo è solo per rendere la scrittura più semplice, il mio programma si mangia questi file che vengono messi tutti insieme in un file di tipo json, e la logica del taccuino va poi a leggere ed aggiornare questo file.

Esempio
```json
{  
    "-Topic1-": {  
       "title1":  
       {  
          "title": "title1",  
          "question":"-question1-",  
          "answers":[  
             "",  
             "Answer1"],  
          "seen":true,  
          "display_answer": 0  
          },  
       "title2": {  
          "title": "title2",  
          "question":"-question2-",  
          "answers":[  
             "",  
             "Answer2",  
             "Trueanswer2"],  
          "seen":false,  
          "display_answer": 1  
          },  
       "title3":  
       {  
          "title": "title3",  
          "question":"-question1-",  
          "answers":[  
             "",  
             "Answer1"],  
          "seen":true,  
          "display_answer": 0  
          },  
       "title4":  
       {  
          "title": "title4",  
          "question":"-question1-",  
          "answers":[  
             "",  
             "Answer1"],  
          "seen":true,  
          "display_answer": 0  
          },  
       "title5":  
       {  
          "title": "title5",  
          "question":"-question1-",  
          "answers":[  
             "",  
             "Answer1"],  
          "seen":true,  
          "display_answer": 0  
          },  
       "": {  
          "title": "",  
          "question":"",  
          "answers":[],  
          "seen":true,  
          "display_answer": 0  
          }  
       },  
    "-Topic2-" : {  
       "title3": {  
          "title": "title3",  
          "question": "-question3-",  
          "answers": [  
             "",  
             "Answer3",  
             "Trueanswer3"  
          ],  
          "seen": false,  
          "display_answer": 2  
       }  
    }  
}
```
