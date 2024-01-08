image rikacg = im.Scale("bg/rikacg.png", 1920, 1080)


label intermissionA:
    stop music fadeout(4)
    scene small_shrine with longFade

    play sound "audio/teleport.wav"
    show stop_time with dissolve
    show check sor p sus yep with squares

    play music "audio/a little city time.mp3" #small city

    ck "Finalmente ti vedo per ciò che sei capelli blu..."

    ck "Ho sempre sospettato che celasse una seconda faccia."

    show check nope
    ck "Se solo potessi seguirla e scoprire cosa sa."

    play sound "audio/teleport.wav"
    show check yep at right
    show bern yoko at left with squares


    show check yep -sus
    pause(1)
    ck "Ah, ci sei anche tu, Berngas... Berknas... kas."

    bk "Bernkastel."

    ck "Si esatto, quello."

    ck "Iniziavo a pensare che ti fossi persa nei frammenti."

    bk "Che i nostri percorsi in questo frammento si sono incrociati è di per sè al quanto sconcertante."

    bk "Per nor parlare di ciò che stiamo vedendo."

    show check nope
    ck "Già, la bambina è davvero inquietante..."

    ck "Eppure nella sua inquietosità sembrava quasi preoccupata per Akasaka."

    bk "Non è Rika che mi perplime. {w}Ti sarai sicuramente reso conto che la tua finestra sul frammento non è più Check, ma Akasaka Mamoru."

    show check sus yep
    ck "Ah davvero? Non me ne ero accorto. Ehahaha."

    show check -sus worried
    bk "Risparmiami il tono sarcastico, di grazia."

    show check nope
    ck "Più o meno ho un idea di quello che è successo, ma è difficile da spiegare..."
    show check yep
    ck "Ma non per questo non ci proverò!"

    scene hinamizawa2 with fade

    show check sor p at center:
        alpha 0.7

    transform resist_wind:
        linear 0.3 xalign 1.2
        linear 1 xalign 0.7
        linear 0.2 xalign 1.2
        linear 1.5 xalign 0.2
        linear 0.5 xalign 1.2
        linear 1.3 xalign 0.6
        linear 0.3 xalign 1.2
        linear 1 xalign 0.5
        repeat

    transform let_go:
        linear 1 xalign 1.5
        xalign -0.5

    n "Come ho già fatto più volte, sono entrato nel frammento mentre visualizzavo Hinamizawa. {w}Questa volta l'ho fatto con cognizione di causa, quindi ricordo ogni dettaglio."

    n "All'inizio era come se fossi diventato uno spettro incorporeo."

    bk "È una normale parte del procedimento. {w}Succede quando la tua coscienza esterna si deve ancora sintonizzare con il corpo che le appartiene."

    stop music fadeout(3)
    n "Esattamente, ed è quello il problema."

    show check angry worried
    play music "audio/meditation.mp3"

    n"Difatti, da li a breve ho sentito una forza che mi attirava da tutt'altra parte."

    n "Solo in quel momento ho realizzato il mio errore!"

    n "Cinque anni fa, il Check di questo frammento era altrove, occupato a fondare il BKG..."

    show check at resist_wind

    n "L'attrazione si faceva sempre più forte."

    n "Per non essere risucchiato via ho tentato di aggrapparmi a qualcosa, QUALSIASI cosa! {w}Ma alberi ed edifici non offrivano la minima resistenza! ...Non avevo scampo!"
    show check at let_go
    pause 1

    show hinamizawa behind check
    show check at let_go
    pause 1
    show field behind check
    show check at let_go
    pause 1
    show dam behind check
    show check at let_go
    pause 1
    show road behind check
    show check at let_go
    pause 1
    show road2 behind check
    show check at let_go
    pause 1
    show okinomiya behind check
    show check at resist_wind
    pause 1

    n "Vedendo che gli oggetti fissi non avrebbero frenato la mia deriva ho provato ad aggrapparmi alle persone..."

    n"E stranamente ho notato che, sebbene a stento, riuscivo a trattenermi."

    show check at let_go
    pause 1

    show police behind check
    show check at resist_wind


    n "Ero vicino alla centrale di polizia, quando ho sentito una seconda forza attrattiva."

    n "Questa volta proveniva da un'automobile!"

    n "Grazie ai miei fulminei riflessi, sapevo che quella era la mia sola opportunità."

    n "Con tutta la mia grinta mi sono lanciato verso di essa..."
    show check:
        linear 0.7 xalign -0.4

    pause 1
    show car_city behind check
    show check smile neutral at right
    n "E poi bam! Per qualche misterioso motivo, in un batter d'occhi, mi ero sincronizzato con questo Akasaka."

    stop music fadeout(1)

    scene small_shrine with fade
    show stop_time with dissolve
    show check sor p think at right with dissolve
    show bern at left with dissolve

    play music "audio/time of rest.mp3" #kneecap / missing name
    n "Ed ecco come sono arrivato quì."

    show check -think
    bk "Recidere il proprio legame corporeo con il frammento e crearne uno nuovo... sei veramente riuscito a fare una cosa del genere?"

    bk "Hai già provato ad assumere la prospettiva di altre persone?"

    ck "Ma certo che ho provato!"

    show check nope
    ck "Però niente da fare, le coscienze degli altri sono troppo... come dire... scivolose."

    ck "È un peccato, avrei voluto sapere cosa passa per la testa di Ooishi, tanto per dirne una."

    bk "... Perchè tra tutti proprio Akasaka?..."


    show check yep think
    ck "Sarà che il novellino mi somiglia."

    ck "Non fraintendere{w}, è chiaro da come si sta comportando che non era minimamente pronto a una missione come questa."

    ck "È un idealista, e ha abbassato la guardia troppe volte. Ma questi sono sintomi della gioventù."

    ck "Mi ricorda me stesso quando ero alle prime armi. {w}Un lavoro pericoloso dopo l'altro, e la scampavo sempre per il rotto della cuffia."


    show check smile -think

    ck "È lo stesso tipo di potenziale che percepisco in Larry."

    ck "Uno come lui dovrebbe entrare nel BKG, gli potremmo offrire l'esperienza che gli manca per diventare competente."

    show check yep
    bk "Mhhh."

    show bern yoko
    bk "È certamente una teoria possibile, ma possono davvero succedere coincidenze così grandi?"

    bk "Che sia la mia presenza ad avere influito? {w}O forse è in gioco una proprietà di questo frammento. {w}Oppure ancora..."

    ck "Beh, come al solito i come e i perchè li lascio decifrare a te Bertaskel."

    bk "Bernkastel..."

    ck "Si appunto, che ho detto?"

    ck "Non saprò come funziona, ma di sicuro è conveniente. {w}Ora posso assistere a questa storia pur non essendoci fisicamente. {w}In barba alle regole di chissà chi!"

    ck "Se esisteva una scappatoia come questa me lo potevi anche dire prima."

    bk "Semplicemente non ne ero al corrente. {w}Questo cambio di prospettiva non è un'abilità di cui io dispongo."

    bk "Inizio a capire sempre di più perchè la tua presenza ha agitato il nostro avversario."

    bk "Se tu imparassi a padroneggiarla diventerebbe un'arma potente. Capace perfino di aggirare la prima delle regole in giallo."

    ck "Un'abilità speciale tutta mia, eh?"

    show check sus
    ck "Allora devo proprio pensare un nome ad effetto."

    show check -sus
    bk "Questo frammento per me non ha alcun valore, ma non è detto che sia lo stesso per te."

    bk "Usalo per prendere dimestichezza con questa tua escursione mentale e torna indietro quando sarai annoiato."

    ck "Ricevuto Bern."

    bk "..."

    ck "Posso chiamarti Bern vero?"

    bk "Se così non sentirò più la tua cattiva pronuncia, ti permetto di chiamarmi Bern."

    ck "Affare fatto."

    show bern:
        ypos 1080
        linear 0.4 ypos 1200
        linear 0.4 ypos 1080

    hide bern with squares
    n "Con un inchino cortese, Bern scompare da questo mondo."

    show check sus
    ck "Certo che sono due gocce d'acqua quelle due."

    show check -sus
    ck "Beh, anche se la interrogassi non mi potrebbe rispondere, e per adesso ho deciso di fidarmi di lei."

    ck "Bene Akasaka, ora viene la parte difficile, vediamo come te la cavi."
    scene black with longFade

    return

label intermissionB:
    stop music fadeout(4)
    scene rikacg with longFade

    play sound "audio/teleport.wav"
    show stop_time with dissolve

    show check sor p at right with squares
    show bern yoko at left with squares

    play music "audio/days of children remake.mp3"

    pause 2

    ck "Oh ma che bullshit something something"

    bk "Pensi che le cose stiano davvero così? Io non posso dirti niente ma guarda da te."

    "Ahime vive in un mondo in cui il destino non le permette questa semplice preghiera."

    ck "Ah, ci sei anche tu, Berngas... Berknas... kas."
    bk "Bernkastel."

    ck "Si esatto, quello."

    bk "Tralasciando la tua guerra contro le parole... {w} Questo risvolto non me lo spiego."


    ck "Che succede con capelli blu? Perchè conosce il futuro e perchè è così CREEPY?!"

    bk "Hai già dimenticato la nostra situazione? {w}Le regole in giallo mi impediscono di rispondere a domande del genere."

    bk "Non rivolgerti a me, osserva i fatti."

    play sound "audio/a.ogg"
    "'rika I want to live'"
    play sound "audio/b.ogg"
    "'rika I want to live'"
    bk "Ciò che Furude Rika sa;{w} ciò che vuole ottenere. {w}Non è forse palese?"

    bk "Ciò che Akasaka Mamoru ha fatto;{w} ciò che non farà mai. {w}Anche questo diventerà palese a breve."

    ck "Mi sembra in tutto e per tutto una richiesta di aiuto. {w}Ma perchè proprio a lui? E perchè così criptica?"

    ck "E anche tu Akasaka, è chiaro che sa! Perchè non la interroghi?"

    bk "Non mi sento di biasimarlo, la colpa non è del poliziotto. {w}È della povera stolta che in lui ha riposto fiducia."

    ck "Chiedere aiuto a un detective? Mi sembra familiare."

    show bern chira

    bk "...."

    ck "Tu e capelli blu non siete solo due gocce d'acqua nell'aspetto, eh Bern? Ehahaha."
    show bern yoko
    bk "Chi ti ha dato il permesso di abbreviare il mio nome?"

    ck "Ah, umh.."

    bk "Credevo di essere stata chiara riguardo a Rika. Lei non è me. Io non sono lei."

    bk "{cps=*0.5}{i}Non farmelo ripetere un'altra volta.{/i}{/cps}"

    ck "Ricevuto."

    bk "Continua pure a guardare questo inutile episodio fino a che non sarai soddisfatto. {w}Io ho visto abbastanza, mi ritiro adesso."

    ck "Hey aspetta, non mi hai detto come devo fare per tornare indietro."

    bk "Ce la farai in un modo o nell'altro."

    hide bern with squares

    ck "Cavolo, spero non se la sia presa...{w} Ha persino rotto il tono monotono per un momento."

    ck "Devo proprio imparare a pronunciare il suo nome."


    return