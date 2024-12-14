label gk330:
    call hide_menu
    stop music fadeout 4

    scene black with Dissolve(4)
    play music ["<silence 6>","audio/umi/cage.mp3" ]
    play sound "audio/sfx/waves.mp3" loop volume 0.4 fadein 6

    pause 1
    scene spiaggiadeiframmenti with Dissolve(4)
    "---scene 330 - Spiaggia dei Frammenti---"


    bernn """
Il mare è un mondo inesplorato.{p}
Si dice che oltre l'80\% di esso non abbia mai visto nessun essere umano.

Le mappe sono in larga parte basate su supposizioni, o su immagini satellitari così su larga scala da risultare inutili, oppure ancora su vecchi racconti di esploratori che chiamare inaffidabili sarebbe troppo gentile.

Sembra strano ma questa è la verità.

{clear}

Questo fenomeno ha un nome: "Isole fantasma"

Isole che per secoli sono state copiate nelle mappe, che si sono poi scoperte essere null'altro che un errore di un disattento sciagurato perdutosi in mare{w}, di un opportunista che voleva imbellire le cronache del suo viaggio rivelatosi inutile{w}, di un marinaio ubriaco che non sarebbe dovuto essere di vedetta quel giorno.

Ho sempre sognato il mare. {p}
All'inizio avevo un infinità di sogni, come le isole nel mare. {w}Da non fraintendere, persino allora sapevo che le persone non possono mai ottenere tutto ciò che vogliono nella vita.{p}

{clear}

A scuola c'è una grossa biblioteca, piena di libri interessanti, ed un giorno mi sono resa conto che non avrei mai potuti leggere tutti.

Ho contato quanti libri vi fossero, ho moltiplicato per il numero delle pagine, 150 pagine a libro sembrava un approssimazione adeguata.

Ho considerato quanto tempo avrei impiegato per ogni pagina, ed ho deciso che semplicemente non bastava il tempo nella vita.

Bisogna fare delle scelte, prendere una decisione su cosa sia la cosa più importante. I sogni sono così.

{clear}

All'inizio ero triste, ma lei mi ha confortato.{p}
"Ogni libro è interessante proprio perché lo hai scelto! Sono le nostre decisioni che ci rendono unici!"{p}
"Non voglio essere unica, voglio leggerli tutti. Cattiva."{p}
"Auauauauau.... Se non la smetti di leggere così tanto tua madre si preoccuperà anche più di come fa ora! È per il tuo bene!"{p}

Me ne ero fatta una ragione, mi ero scelta i miei sogni.{p}
Volevo andare in una scuola raffinata per ragazze per bene, d'altronde sono molto brava.{p}
Volevo che tutti mi volessero bene e mi trattassero come se fossi speciale. Ero ambiziosa.

{clear}

E volevo vedere il mare.{p}
Volevo allontanarmi dal mio paesino. Volevo viaggiare.{p}
Data la mia condizione, questo era purtroppo tutt'altro che garantito. Ma se le previsioni si fossero rivelate azzeccate, tutto sarebbe stato sistemato tra qualche anno.

"""
    stop music fadeout 3

    play music "audio/umi/wingless.mp3"
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

Con il tempo ho persino dimenticato.{p}
L'unico modo che ancora mi rimane per scrutare nel mio più lontano passato è consultare questo frammento, ma anche dopo tanto tempo non mi ha detto nulla di nuovo..

Ormai quei giorni sono troppo diluiti nella mia memoria, troppo simili a loro stessi.

Ricordo invece chiaramente il giorno in cui mi sono detta;{p}
"Perché continuare a interessarsi? D'altronde questo mondo tra poco non esisterà più."

Era il giorno in cui avevo finito di leggere l'ultimo libro della biblioteca.

{clear}

È allora che ho capito che preoccuparsi era inutile.{p}
È allora che ho capito che niente aveva significato.

Tutto quello che mi restava era accettare il mio destino e vivere in un ciclo di piccole felicità, di amari ricordi, e di insormontabile dolore.{p}
"Potrebbe andare peggio. Non sono da sola. Loro sono con me."

Ma questa non è una vera risposta, e mi stavo solo ingannando. {p}
La verità è che, con tutta me stessa, non volevo null'altro che fuggire dal ciclo della tragedia.{p}
Volevo la vera libertà.

{clear}

Ma, in fin dei conti, cosa è la vera libertà? Cosa è che voglio veramente? Cosa è lo scopo ultimo della mia vita? Cosa è che voglio?

Dopo aver vissuto in questa prigione posso veramente tornare alla mia vecchia esistenza? Vivere la vita come se niente fosse successo?

A quel punto, mi sono resa conto che c'era un'alternativa.

"""
    nvl clear
    stop music fadeout 3

    bernn """
Mi sono guardata alle spalle, ed ho visto me. Una me incatenata dal desiderio. Una me incatenata dall'ambizione.

Ed ho compreso che quella non ero io.{p}
Quella era un altra persona. Debole, pronta ad arrendersi senza aver provato, e senza rendersi conto di non avere mai provato.{p}
Era la me prima che io avessi affrontato quello che ho affrontato.

Era la me ancora succube delle emozioni umane.

La vera libertà è il fare esattamente quello che si vuole, quando si vuole, come si vuole, nessuna barriera, nessun limite...

"""

    nvl clear
    play music "audio/higu/over the sky.mp3"


    show bern at flip, right with Dissolve(2):
        alpha 0.3


    bernn "Aprii gli occhi, e per la prima volta vidi il mare."

    show bern at flip:
        alpha 0.6
    with Dissolve(2)

    bernn "Non un mare salato, ma un mare di frammenti. Un mare dove le varie isole sono infiniti mondi, infinite possibilità.{p}La liberta di viaggiare per il mondo. Per i mondi."

    show bern at flip:
        alpha 0.9
    with Dissolve(2)
    bernn "Mi sono innalzata al cielo. Ogni limite era svanito. il mondo era al mio servizio. Tutto era sul palmo delle mie mani.{p}Hinamizawa dall'alto era così piccola... sempre più piccola..."

    nvl clear

    bernn """

Finche non ho incontrato una barriera.

La libertà non era altro che un illusione.{p}
Ero diventata un uccello ma ero ancora in cattività, la mia zampa era ancora legata a quel luogo.

Non mi va bene. Tutto questo è inaccettabile. Sono così vicina, ad un passo dalla libertà, la vera libertà... ma per chissà quale ragione, mi sottopone a questo infinito ciclo di partite. Così vicina, eppure così lontana...

Il mio carceriere... è lei.
"""
    # la mia zampa era ancora legata a quel luogo
    stop music fadeout 3
    nvl clear
    show bern at flip:
        alpha 1.0
    show lamb at left with squares

    play music ["<silence 2.0>","audio/umi/golden sneer.mp3"]

    ld "Non manca moltissimo. Tra non molto le preparazione saranno complete."
    bk "Bene, hai preparato qualcosa di perfettamente crudele immagino. Chi sarà stavolta la vittima della maledizione di Oyashiro-sama?"
    ld "Parli come se fosse colpa mia, ma d'altronde fanno tutto da soli giusto?"
    bk "Che tecnicalità..."
    ld "Chiunque io abbia scelto, non importa. Qualcuno vedrà gli occhi."
    ld "Ti aspetto, vedi di non fare tardi."

    stop music fadeout 2
    hide lamb with squares
    bernn"""
Eppure... c'è un modo per vincere. Ho un piano.

Non importa quanto grandi i sacrifici, io vincerò questa partita e fuggirò da questa gabbia.

Sconfiggerò Lambdadelta usando come arma la sua stessa arroganza. E conquisterò la mia libertà.
"""
    hide bern with squares

    "Fade alla scena interna"

    return