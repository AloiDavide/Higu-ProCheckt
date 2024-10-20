label scene3_3:
    call hide_menu
    stop music fadeout 4

    scene black with Dissolve(4)
    play music ["<silence 6>","audio/umi/cage.mp3" ]
    play sound "audio/sfx/waves.mp3" loop volume 0.4 fadein 6

    pause 1
    scene spiaggiadeiframmenti with Dissolve(4)
    "---sc330---"

    $persistent.nvl_no_bg = True

    bernn """
Il mare è un mondo inesplorato.
Si dice che oltre l' 80\% di esso non abbia mai visto nessun essere umano.
Le mappe sono in larga parte basate su supposizioni, o su immagini satellitari così su larga scala da risultare inutili, o su vecchi racconti di esploratori che chiamare inaffidabili sarebbe troppo gentile.

Sembra strano ma questa è la verità. Questo fenomeno ha un nome:
"Isole fantasma", isole che per secoli sono state copiate nelle mappe, che si sono poi scoperte essere null' altro che un errore di un disattento sciagurato che si è perso in mare, di un opportunista che voleva imbellire le cronache del suo viaggio rivelatosi inutile, di un marinaio ubriaco che non doveva essere di vedetta quel giorno.

{clear}

Ho sempre sognato il mare. All' inizio avevo un infinità di sogni, come le isole nel mare. Da non fraintendere, persino allora sapevo che le persone non possono mai ottenere tutto ciò che vogliono nella vita.{p}
A scuola c'è una grossa biblioteca, piena di libri interessanti, ed un giorno mi sono resa conto che non avrei mai potuti leggere tutti. Ho contato quanti libri vi fossero, ho moltiplicato per il numero delle pagine, 150 pagine a libro sembrava un approssimazione adeguata.


Ho considerato quanto tempo avrei impiegato per ogni pagina, ed ho deciso che semplicemente non bastava il tempo nella vita. Bisogna fare delle scelte, prendere una decisione su cosa sia la cosa più importante. I sogni sono così.

{clear}

All' inizio ero triste, ma lei mi ha confortato.{p}
"Ogni libro è interessante proprio perché lo hai scelto! Sono le nostre decisioni che ci rendono unici!"{p}
"Non voglio essere unica, voglio leggerli tutti. Cattiva."{p}
"Auauauauau.... Se non la smetti di leggere così tanto tua madre si preoccuperà anche più di come fa ora! È per il tuo bene!"{p}

Me ne ero fatta una ragione, mi ero scelta i miei sogni.{p}
Volevo andare in una scuola raffinata per ragazze per bene, d' altronde sono molto brava.{p}
Volevo che tutti mi volessero bene e mi trattassero come se fossi speciale. Ero ambiziosa.

{clear}

E volevo vedere il mare. Volevo allontanarmi dal mio paesino. Volevo viaggiare.{p}
Data la mia condizione, questo era purtroppo tutt' altro che garantito. Ma se le previsioni si fossero rivelate azzeccate, tutto sarebbe stato sistemato tra qualche anno.

"""
    stop music fadeout 3

    play music ["audio/umi/wingless.mp3"]
    $persistent.nvl_no_bg = False
    bernn """

Non potevo sapere che il futuro mi sarebbe stato strappato dalle mani.{p}
Non potevo sapere che ormai mi trovavo in una prigione inattaccabile.{p}
Non potevo sapere che eventualmente mi sarei trovata a non poter vedere nemmeno la neve.

{clear}



Inizialmente ho provato ad evadere, ma invano.{p}
Come potevo, gracile come ero, piccola come ero, scappare da quella situazione.{p}
Come potevo andarmene.
Come potevo chiedere aiuto, chi mi avrebbe creduto.

Eventualmente... ho semplicemente smesso di provare. Ho lasciato passare il tempo..............

Ho iniziato a leggere tutti i libri della biblioteca.

{clear}

Ho persino dimenticato. L' unico modo per scrutare nel mio più lontano passato è consultare questo frammento, che ho trovato dopo tanto tempo. Ma non mi ha detto nulla di nuovo.

--something else--

Un giorno mi sono detta;
"Perché continuare a preoccuparsi? D' altronde questo mondo tra poco non esisterà più."

Era il giorno in cui finii di leggere l'ultimo libro.

"""

    "Bern conquista il suo mare diventando una strega"

    "Vede tutto come una partita di probabilità."

    return