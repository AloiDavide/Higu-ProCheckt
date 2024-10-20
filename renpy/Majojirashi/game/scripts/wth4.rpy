#TODO Impacchetta entrambi i giochi
#TODO tip screen thumbnail
#TODO persistent e questionflow

#Tutti gli asset sono definiti in un file a parte, questo è praticamente un copione e basta.
#Le righe che iniziano per # sono commenti che l'user non vedrà mai. It's a secret between you and I developers ;)
#Le poche righe che iniziamo per $ sono gibberish magico in python che serve a fare le cose fancy.

label wth4:
    $persistent.light_novel = False

    play music "audio/beat.mp3" fadein 4

    scene fragplane with longFade


    play sound "audio/chimes.ogg"
    n """Di nuovo questa sensazione.

    Senti chiaramente la tua coscienza separarsi dal tuo corpo e tornare a fare parte di qualcosa di più grande.

    Adesso ricordi, la realtà da cui provieni non era altro che uno tra una miriade o più frammenti.

    Sai di potere riprovare, e questo ti rincuora, ma non cambia il fatto che tu abbia lasciato Larry a se stesso in quel mondo.

    Senza niente su cui sfogare la tua frustrazione, esclami:"""

    ck "ECCHÈ DIAMINE! Sono morto... DI NUOVO!"

    witch "Speravo proprio che alla terza volta ci avresti fatto l'abitudine. Check."

    n "Un'altra cosa a cui decisamente non hai fatto l'abitudine è questa voce che incalza dal nulla."

    ck "Ma chi si risente. {w}Hey, che ne dici di farti vedere tanto per cambiare?"

    witch "Farmi vedere? ...Stai fraintendendo qualcosa."

    witch "Se vuoi vedermi, basta che apri gli occhi."

    n "La voce ha ragione. {w}Non sai come hai fatto a non notarlo prima, ma a differenza delle altre volte puoi sentire le tue palpebre chiuse."

    n "Apri gli occhi come se lo facessi per la prima volta."

    n "Non sei abituato alla luce eterea di questo luogo, ma lentamente riesci a formare un'immagine."

    stop music fadeout(4)


    scene bern_kekkai with Pixellate(4,7)
    play sound "audio/teleport.wav"

    show bern with squares

    ck "......."

    ck "CAPELLI BLU!?"

    play music "audio/haruka.mp3" fadein(4)

    witch "Chi hai chiamato capelli blu?"

    #bern yoko è quando guarda di lato, chira è quando guarda alla telecamera, a e b sono due lipflap quasi identici

    show bern yoko b

    witch "Aah, chiaro. {w}Sei confuso perchè il mio aspetto ricorda quello di Rika Furude."

    show bern chira a

    witch "Se non sbaglio ti avevo promesso che mi sarei presentata non appena ti fossi manifestato completamente."

    bk "Cordiali saluti. Il mio nome è Frederica Bernkastel. {w}Non sbagliare, {i}{color=#0000cf}il nome è Frederica non Furude Rika.{/color}{/i}"

    bk "Questo lo sai già, ma non sono neanche Oyashiro, nel caso non fosse chiaro."

    ck "Scusa, devo controllare di essere sobrio, perchè l'ultima cosa che mi aspettavo di vedere è una goth loli in un salotto orientale."
    show bern yoko
    bk "Niente fretta. Quì abbiamo tutto il tempo che serve... finchè è il nostro turno."
    show bern chira
    bk "Ipotizzo che avrai tante domande. {w}Finalmente conversiamo faccia a faccia, perchè non accompagnare la discussione con una tazza di tè?"

    bk "Avrei offerto del vino, ma mi sembri intenzionato a restare sobrio."

    ck "Grazie..."

    show bern yoko
    bk "Si, il tè andrà bene. {w}In occidente offrirne una tazza è un simbolo di amicizia, in oriente di sacra ospitalità."

    bk "Indubbiamente è la bevanda perfetta per chi cerca un rapporto di collaborazione."

    n """Mentre Bernkastel lista i pregi del tè, mantenendo un'espressione monotona, sul tavolino si materializzano una teiera e due contenitori.

    A sinistra una tipica tazza cilindrica giapponese con un motivo floreale. {w}Si addice perfettamente allo sfondo.

    A destra una tazzina decorata che non sfigurerebbe nella collezione di porcellane di un nobile Inglese."""

    show bern chira
    bk "Dimmi dunque, preferisci bere del Matcha o dell'Earl Grey?"

    bk "Ah. E tengo a precisare che questo non è un test."

    n "Questo deve senza dubbio essere un test. {w}Pensaci bene, la teiera è una sola. Devi indovinare quale dei due tè contiene."

    #il modo normale di fare una scelta in renpy
    menu:
        "Earl grey (tè nero inglese)":
            n "Questa ragazza osa mettere in dubbio le capacità osservative di Check. {w}Basta vedere come è vestita per capire quale sia il suo tè preferito."
            
            ck "Vorrei bere l'Earl Grey, grazie."

            "Bernkastel prende la teiera, ne versa il contenuto nella tazzina inglese, e ti porge il delizioso tè aromatico che hai scelto."
            show bern close
            "Successivamente, dalla stessa teiera, versa del tè verde nella tazza orientale e inizia a berlo raffinatamente."

        "Matcha (tè verde giapponese)":
            n "Ma certo, sta mettendo in dubbio la tua capacità di adattarti al contesto. {w}Guardando la stanza la risposta giusta è assolutamente ovvia!"

            ck "Vorrei bere il Matcha, grazie."

            n "Bernkastel prende la teiera, ne versa il contenuto nella tazza orientale, e ti porge il delizioso tè tradizionale che hai scelto."
            show bern close
            n "Successivamente, dalla stessa teiera, versa del tè nero nella tazzina inglese e inizia a berlo raffinatamente."

    ck "Ma come..."

    show bern chira b
    bk "Mhh?"

    ck "Quella teiera è truccata! Si sarebbero dovuti mischiare!"

    bk "Questo? Beh, ho semplicemente spostato la teiera nella quinta dimensione da un mondo dove conteneva il primo tè a uno dove conteneva il secondo."

    ck "......"

    show bern a
    bk "Ecco, insomma, hai mai sentito parlare di quell'esperimento con il gatto nella scatola?"

    ck ".........."

    show bern yoko
    bk "Lasciando da parte la spiegazione tecnica. {w}Volevo solo ricordarti l'importanza della scelta."

    bk "\"La teiera è una sola\", \"Il tè che contiene è chiaramente uno soltanto\"."

    bk "Non mi serve leggere il pensiero per capire che stavi pensando ciò."

    bk "Normalmente questa scelta non sarebbe una vera scelta. Non per un umano. Tuttavia per noi lo era."

    bk "Entrambi i risultati erano possibili, perciò ho potuto scegliere quello che esaudiva il tuo desiderio."

    show bern chira
    bk "Questo è il vero significato di scelta."

    ck "Chiaro..."

    ck "Sicuramente è un discorso interessante, e apprezzo l'ospitalità, signorina Bernkastel."

    ck "Ma le risposte di cui ho bisogno adesso sono ben altre."

    show bern b
    bk "Perdona la mia loquacità. Non ho mai ricevuto ospiti prima."

    bk "Dopo ciò che mi hai mostrato in questo ultimo frammento direi che il tuo periodo di prova è concluso."

    bk "E sia, niente più segreti. {w}Domanda e risponderò se nel mio potere."

    show bern chira a


    #Siamo al grande crossroad delle scelte!

    #Per fare il giochetto delle domande progressive sono andato a interagire direttamente con il "dietro le quinte"
    #di renpy. Ovvero molto meno copione e molto più codice.





    $ over = False

    #Testo magico in antico python che conjura il menu di scelta.
    #La maggior parte del gibberish sta in un altro file ma questo serviva qua.
    while(not over):
        $ labels = [l for l in ques.keys() if ques[l].canShow()]
        $ text = [ques[l].text for l in labels]
        $ clicked = renpy.display_menu(list(zip(text, labels)))
        $ ques[clicked].tickOff()
        $ renpy.call(clicked)


    return


    #A seguire i label con le scene in nessun ordine particolare.
    #'return' indica la fine del label e ti riporta al menu di scelta.


label whoBern:
    n "La sua voce è completamente diversa da quella di Rika, è molto più profonda e adulta."

    n "Ma no, prima di tutto capelli blu è un essere umano. Non..."

    n "Non hai nemmeno idea di come categorizzare l'essere che sorseggia tè dall'altro lato del tavolo."

    ck "Ho capito che non sei Rika e che non sei un dio. {w}Però mi hai detto solo cosa non sei."

    show bern yoko a

    bk """Non sono poi così diversa da te. La differenza tra noi due sta nel tempo.

    Un giorno ormai troppo lontano per qualsiasi memoria mortale, presi coscienza quì nel mare di frammenti.

    Ero spaesata quanto te all'inizio. {w}Sarà passato almeno un decennio prima che capissi come guardarmi intorno. {w}
    E non prima di un secolo perchè riuscissi a influenzare la realtà."""

    show bern chira

    bk """Sebbene aiutato dalla mia guida, mi sorprende che tu sia già a questo punto.

    Si vede che hai avuto un'ottima insegnate."""

    ck "Eehheehhee come no. Oppure sono semplicemente un genio."

    n "Bernkastel sembra ignorare la tua contro provocazione."

    bk "Per rispondere alla tua domanda in maniera concisa, un appellativo adatto sarebbe \"strega\"."

    bk "Bernkastel la strega dei frammenti, che ha vissuto per quasi mille anni."

    ck "Mi inchino a lei grande senpai /s."

    n "La strega è impervia al tuo sarcasmo."

    n "Beh, qualunque cosa voglia dire con strega, almeno non sembra avere cattive intenzioni."

    n "Tuttavia se lei è una strega, questo cosa fa di te?"

    return



label where:
    ck "Ormai è evidente che torno sempre quì alla morte. {w}C'è solo un piccolo dettaglio che ancora non mi è chiaro..."

    ck "Dove DIAMINE è quì?"

    show bern close
    bk "..."

    n "Sembra che Bernkastel stia scegliendo attentamente le parole."


    scene sky_frag with dissolve


    bk "Osserva il cielo. Ormai non servirà spiegarti che quelle non sono stelle, sono gli infiniti frammenti di realtà."

    bk "Tutti mondi diversi{w}, o meglio{w}, mondi possibili. {w}Diverse prospettive su ciò che è reale."

    bk "Quì siamo al di fuori di essi. Pertanto li possiamo osservare a nostro piacimento."

    bk "Senza scendere nel dettaglio, è come se la tua coscienza umana fosse rimasta ingarbugliata nella trama della realtà."

    bk "È per questo che ti svegli quì alla morte."

    scene bern_kekkai with dissolve
    show bern

    bk "Ovviamente, anche questa stanza è uno spazio creato da me affinchè noi potessimo avere questa conversazione. Esiste solo fintanto che noi la desideriamo."

    ck "Come la teiera?"

    bk "Esatto, come la teiera."

    n "Non sai ancora bene cosa pensare di questa situazione."

    n "In verità una parte di te sospetta ancora che tutto questo sia un'allucinazione. {w}Forse il tuo cervello sta solo malfunzionando nei tuoi ultimi momenti di vita."

    n "Beh, anche se fosse, tanto vale ascoltare fino alla fine."

    return







label whoMe:
    ck "Secondo quanto mi stai dicendo, sarei diventato praticamente immortale."

    bk "In un certo senso."

    ck "E quel trucco della teriera, posso farlo anche io?"

    bk "Certo che si."

    ck "Ma questi sono poteri DIVINI!"

    bk """Non sbagli nel dire che sei un essere superiore.

    Te ne ho già parlato in passato, ricordi? {w}Gli umani sono esseri limitati a un singolo mondo, non possono avere una visione d'insieme.

    Noi siamo anomalie. {w}Come un personaggio di un romanzo che ne diventa il lettore{w}, o come un pezzo degli scacchi che all’improvviso prende vita e si siede sulla sedia del giocatore.

    Impossibile no? Eppure eccoci qua.

    Per questo motivo non sarebbe corretto definirci esseri umani.

    Check dentro i frammenti è una persona con la propria vita.

    Ma non tutti i Check hanno la stessa vita, o la stessa morte, se è per questo.

    Sotto questa prospettiva, l'idea che esista un solo Check, e che tu sia lui diventa alquanto assurda. Non trovi?

    Non offenderti, non sto condannando la tua esistenza, tutt’altro.

    Check potrà morire nel giugno 1983, ma la tua coscienza rimane svincolata dal tempo.
    """

    ck "Fantastico! Vuol dire che mi basta provare tutti gli altri frammenti fino a che non ne trovo uno dove salvo il BKG!"
    show bern close
    bk "Se solo fosse così semplice."

    scene sky_frag with dissolve
    bk "Tu sei appena arrivato, ma io osservo questo mare di frammenti da tempo immemore."

    bk "Ne ho attraversati tanti quanti gli astri nella notte, e non uno solo di essi conteneva un lieto fine."

    scene bern_kekkai with dissolve
    show bern
    bk "Nonostante ciò sono ancora alla ricerca."

    bk "Questo è il motivo della mia esistenza. So che se smettessi di cercare, cesserei di esistere."

    return






label after:
    show bern chira a

    ck "Tu vedi tutto no? Puoi dirmi cosa è successo al mondo dopo che Lambdadelta mi ha ucciso? Sono preoccupato per Larry."

    bk "Avrò anche molta più esperienza di te, ma non sono onnisciente. {w}Anche io ho dei limiti su cosa posso e non posso vedere."

    bk "La mia finestra sul frammento che hai appena visto si chiude la notte successiva al Watanagashi. {w}Purtroppo non ho concezione di cosa accada dopo."

    bk "A dire la verità ero convinta che anche questa volta fosse stato Larry a, beh..., mandarti indietro. {w}Non è così?"

    ck "Preparati, sarà una lunga storia."

    scene bern_kekkai with Fade(3,0,1)
    show bern with dissolve

    bk "Mhh."

    bk "...Lambdadelta... stai dicendo che sei riuscito a incontrare questa persona?"

    ck "Sono pur sempre un comandante del BKG, non sottovalutare la mia abilità nelle indagini... {w}Anche se alla fine ha avuto la meglio."

    show bern yoko

    bk "...."

    show bern chira

    bk "Non credevo che la nostra collaborazione avrebbe dato frutto così presto. {w}Check, questo è incredibile. {w}Quel personaggio potrebbe essere la chiave di tutto."

    bk "Dimmi dunque, quale è l'identità di Lambdadelta?"

    ck "Mi dispiace. Non posso."

    bk "...Ancora non ti fidi di me?"

    ck "Non fraintendere. Se potessi dire quel nome lo avrei già fatto, lo avrei urlato talmente forte da farmi sentire da Larry in tutti i mondi."

    ck "Ma è inutile... NON RIESCO A RICORDARE!"

    ck "Non è solo il nome, anche l'aspetto, la voce, come ha fatto a catturarmi, cosa ha fatto dopo!"

    ck "Mi sembra come se qualcuno avesse preso i miei ricordi e vi avesse disegnato sopra delle censure."

    bk "Check. Facciamo un esperimento. {w}Ascolta bene perchè adesso ti spiegherò per quale motivo ad hinamizawa alcune persone impazziscono."

    play sound "audio/truth.mp3"
    bk "Si tratta di {color=#ffe674}_n_ _al_t___ c___a__ d_ __i p__a__i__{/color}"

    ck "Hey, parla più forte. Non riesco a sentirti."

    bk "{color=#ffe674}_n_ _al_t___ c___a__ d_ __i p__a__i__{/color}"

    ck "Niente da fare."

    bk "Sfortunatamente è come pensavo... {w}Sono le nuove regole."
    return





label rules:
    show bern yoko a
    ck "Che cos'è questa storia. Perchè non riusciamo a parlarci?"

    bk "Dovresti avere sentito anche tu una voce che proclamava delle regole."

    ck "Ripensandoci... Si ho decisamente sentito qualcosa.{w} Che DIAMINE era?"

    show bern chira
    bk """Ascolta bene le mie parole, qualcuno o qualcosa di estremamente potente tiene tutt’ora in scacco ogni singolo frammento.

    Per moltissimo tempo ho creduto che il responsabile fosse il destino stesso. Un futuro ineluttabile.

    Ma non ho mai escluso la possibilità che fosse orchestrato da una mente senziente.

    E finalmente adesso ha mostrato un chiaro segno di se."""

    ck "Devo proprio averlo spaventato."

    bk "Per lo meno la tua presenza sembra aver spinto il nostro avversario ad agire."

    play sound "audio/truth.mp3"
    n "{i}{color=#ffe674}Da ora in poi Bernkastel e Check non si possono scambiare informazioni inerenti alla partita.{/color}{/i}"

    ck "Un momento, come può sapere esattamente cosa ci diciamo? Vuol dire che ci sta ascoltando IN QUESTO MOMENTO!"

    n "Non è possibile, ci siete soltanto voi due lì."

    bk "Non necessariamente, anche se non lo posso escludere. {w}In generale non mi aspetto di ingannare queste regole con dei biglietti sotto il tavolo."

    ck "Perciò niente più indizi neanche su i frammenti di prima?"

    bk "Non rimane che scoprirli per conto tuo e dalla prospettiva di Check."

    bk "Tu non avrai la mia prospettiva su gli argomenti che contano, e io non avrò la tua."

    show bern close

    bk "Tuttavia, questo è un grande problema. Lo scambio di informazioni era il nostro vantaggio più grande."

    show bern yoko

    bk "È lo stesso principio dietro l'occhio umano. {w}Un solo occhio non ti permette di vedere il mondo in tre dimensioni, ne servono due."

    bk "Ma avere gli occhi non basta. Il ruolo più cruciale lo ha la corteccia visiva."

    bk "Se il cervello non può interpretare le due immagini, combinandole adeguatamente, allora non c'è nessun vantaggio nell'avere due occhi."

    play sound "audio/truth.mp3"
    n "{i}{color=#ffe674}Check non può riconoscere la mia pedina.{/color}{/i}"

    bk "Anche questa adesso si spiega. Dopotutto eri arrivato a uno dei pezzi più cruciali dell'enigma."

    ck "Lambda..."

    bk "A giudicare da come parla, per quell'entità tutto questo è un gioco. E sembra che pur di non darcela vinta neanche per una partita, ha aggiunto delle regole a suo favore."

    ck "Questo si chiama non saper perdere. Vorrei fargli passare un giorno nel club di Mion e vedere che fine fa."

    bk """Purtroppo è evidente, non siamo noi a dettare le regole, e men che meno le penalità.

    Finchè questa situazione continua non c’è speranza di un lieto fine. Nè per quei ragazzi, né per te e il tuo fidato collega.

    Se vuoi liberarti da questo ciclo di dolore, e salvare il BKG dalla corruzione, collaborare con me è l’unica via."""

    return



label whyMe:
    show bern chira a

    ck "Dunque proponi un'alleanza."

    ck "Inizio a sentirmi il protagonista di una light novel isekai."

    ck "Potrei chiamarla: \"Reincarnato in un altro mondo come agente speciale, ma visto che continuo a morire ho stretto un patto con una strega per salvare la mia organizzazione dalla dittatura.\""

    show bern yoko
    pause 2
    show bern chira

    n "Non riesci minimamente a leggere il suo sguardo. Eppure hai come l'impressione che ti stia giudicando."

    bk "Non capirò mai i canoni dei titoli di questo genere letterario."

    bk "Ma beh, se è quello che vuoi..."

    play audio "audio/truth.mp3"
    bk "{color=#0000cf}\"Reincarnato in un altro mondo come agente speciale, ma visto che continuo a morire ho stretto un patto con una strega per salvare la mia organizzazione dalla dittatura.\"{/color}"

    #Bern attacca il postit:
    $persistent.light_novel = True

    ck "Ehi, che cosa hai fatto?"

    bk "Nulla di importante..."

    bk "Lo ammetto, sarebbe un bel paragone se io fossi una dea e tu il mio prescelto, ma la nostra situazione è un po'diversa."

    ck "Perchè, non sei stata tu a scegliermi, Kami-sama?"

    show bern yoko
    pause 2
    show bern chira

    bk "In tutta sincerità, no. {w}Sei stato tu ad apparire per conto tuo, io ho solo offerto la mia guida."

    bk "Vedila in questo modo, è la costante determinazione di ogni Check in ogni frammento ad avere generato te."

    bk "La frustrazione di vedere tutto quello per cui hai lavorato andare in fumo. {w}Il bisogno di riportare l'ordine. {w}Queste sono qualità radicate profondamente nel tuo io."

    show bern close

    bk "Eppure infine, anche il nemico non ha sottovalutato questi tuoi attributi."

    show bern chira

    bk "Speravo che tu che sei al contempo osservatore e pezzo sulla scacchiera avresti cambiato le cose{w}, ma adesso le nostre chance di vittoria sono infinitesimali."

    bk "Anche se ci portassimo miracolosamente in vantaggio, probabilmente ci troveremmo davanti un'altra regola irragionevole."

    show bern yoko

    bk "Forse è veramente impossibile battere il fato..."

    return

label end:
    show bern chira a

    ck "Ho capito bene la tua proposta."

    ck "In poche parole vuoi il mio aiuto per battere un nemico comune."

    ck "Questo nemico è incomprensibilmente forte, tanto da cambiare le leggi del mondo, e per vincere avremmo bisogno di un miracolo."

    bk "È una sintesi accettabile."

    stop music fadeout 4

    ck "C'è una sola cosa su cui però hai torto."

    play music "audio/core.mp3" fadein 3
    bk "Oh?"



    scene bern_kekkai_closeup with dissolve

    show check defa nope

    ck "Hai detto qualcosa del tipo: \"Tu non sei Check perchè sei un essere superiore\"."

    show check yep

    ck """Lascia che ti insegni questa lezione. {w}Check non è soltanto un nome in codice! {w}Rappresenta un modo di vivere, di essere e di pensare. Pertanto è unico!

    Se davvero sono una somma di tutti i Check del multiverso, allora lascia che parli a nome di tutti loro."""

    show check shout sus

    ck "Destino? {w}Nuove Regole? {w}Misteri irrisolvibili?"

    show check smile -sus

    ck """Superare ostacoli insormontabili è il mio lavoro! {w}Che sia una su un milione o una su un miliardo, se esiste una possibilità di vittoria non abbiamo ancora perso.

    Io sono... {w}NO."""
    play sound "audio/truth.mp3"

    extend " Noi siamo {i}{b}{color=#480000}CHECK{/color}{/b}{/i}{nw}"

    show check sor p
    pause 0.2
    show check defa -p

    extend ". Comandante del BKG."

    ck "Dichiaro ufficialmente approvata l'alleanza con la strega Bernkastel."

    show check at right
    show bern yoko at left with dissolve

    bk "Belle parole, ma se non sbaglio il BKG è totalmente fuori dal tuo controllo oramai."

    bk "A che pro attegiarsi a comandante in questa situazione?"
    play music "audio/dread of the grave.mp3" fadein 5

    show check yep
    ck "Il BKG è la mia organizzazione, esiste dovunque esisto io, tutto qua."

    show check think nope
    ck "Al momento il \"Book Keepers Guard\" è in mano al nemico. Questo è vero."
    show check -think smile


    ck "Pertanto! Fino a che non lo avrò reclamato, BKG sarà l'acronimo di \"Bern-Kastel Guard\"."
    play sound "audio/teleport.wav"
    scene vortex with fade
    n "A questa tua dichiarazione, un vortice scuro ti avvolge."

    "E quando ne emergi...{w} sei come trasfigurato."

    play sound "audio/teleport.wav"
    scene bern_kekkai_closeup with fade

    show bern yoko at left

    show check p smile at right

    bk "........"

    bk "Stupefacente..."

    show check sus nope

    ck "E questo!? Sono stato io a farlo?"

    bk "Sei decisamente stato tu."

    ck "Beh..."

    show check -sus smile

    ck "NON MALE!"

    n "Quando qualcuno sente la parola agente segreto, cappotto nero e fedora sono le prime cose che vengono in mente."

    n "Questa situazione dettava un outfit più iconico di maglietta e felpa. {w}E tu sei stato in grado di materializzarlo."

    ck "Se il nostro nemico fosse davvero così temibile non si nasconderebbe così. {w}Non ricorrerebbe a dei sotterfugi per rompere la nostra cooperazione, ma verrebbe quì a schiacciarci di persona."

    ck "Sicuramente è nel panico in questo stesso momento. Sa che possiamo fermarlo. Quel codardo."

    ck "AVANTI! Sono pronto per il prossimo frammento."


    scene sky_frag with dissolve

    n "Come un uomo deciso a trionfare sul firmamento intero, tendi la mano al cielo e tenti di afferrare una stella."

    n "Contro ogni intuizione, ci riesci, e ti ritrovi con un piccolo cristallo che fluttua sul palmo della tua mano."

    scene bern_kekkai_closeup with dissolve

    show bern yoko a at left with dissolve

    show check p yep at right with dissolve


    show hima_prop:
        xalign 0.5
        yalign 0.5
        zoom 0.25



    bk "Quel frammento... che nostalgia."

    bk "Mostra un tempo cinque anni precedente al tuo arrivo ad Hinamizawa. {w}Prima di tutti gli omicidi, quando il villaggio era ancora impegnato nella \"Guerra della diga\"."

    ck "Perfetto! Voglio vederlo!"

    show bern close
    bk "Purtroppo per te sarà inutile. {w}Non so cosa Check stesse facendo in quel periodo, ma dubito possa portare grandi rivelazioni."

    show hima_prop:
        linear 0.5 xalign 0.9

    pause(0.5)
    hide check with squares

    show bern yoko
    stop music fadeout 5
    bk "Nel peggiore dei casi potresti rimanere bloccato per..."


    bk "È già partito..."

    play music "audio/haruka.mp3"

    bk "Ho trovato un compagno veramente bizzarro."


    show hima_prop:
        linear 0.5 xalign 0.5


    bk "Poco male... Vuol dire che abbandonerò me stessa alla nostalgia ancora una volta e tornerò ad osservare questo frammento."

    bk "Se non altro sarà un buon modo per {i}\"ingannare il tempo\"{/i}."

    show hima_prop:
        linear 0.5 xalign 0.1

    pause(0.5)
    hide bern with squares

    window hide

    scene hima_frag with dissolve

    pause 4

    play sound "audio/doon.mp3"

    stop music fadeout 13
    $renpy.transition(vpunch)
    $renpy.call_screen('welcome_hima')



    $over=True


    return





label poems:
    show bern chira a
    n "Bernkastel eh... hai già visto questo nome."

    ck "........."

    bk "È forse una tua abitudine fissare le persone in silenzio?"

    ck "CI SONO! {w}Sei l'autrice delle poesie! Quelle che vedo ogni volta che entro in un frammento."

    bk "Mhh"
    show bern yoko b
    bk "MHHHH!"

    ck "Ci ho preso, vero?"

    bk "Quelle risalgono a una fase poetica che ho avuto 400 anni fa."

    bk "Sarebbe molto garbato da parte tua dimenticare tutto ciò che hai letto. {w}Se possibile fallo completamente. E in fretta. {w}Ancora meglio se potessi non ripescare l'argomento."

    ck "Erano veramente ben scritte. Una mia conoscenza le chiamarebbe cringe, ma mi sono piaciute."

    bk "Ben scritte? {w}.......Capisco."

    bk "Forza, passiamo alla prossima domanda."

    n "Non è facile capirlo dall'espressione, ma Bernkastel sembra contenta."

    show bern chira a
    return




label tea:
    show bern chira a
    ck "Il tè era semplicemente egregio, potrei averne un altra tazza?"

    bk "Serviti pure."

    n "Teiera in mano, ti concentri per manifestare un bis del tè che stavi bevendo, ma quando lo versi noti qualcosa di strano."

    ck "MA QUESTA È COCA COLA!"


    bk "Cielo, questo è raro... Per lo meno è commestibile."

    n "Chi diamine fa bollire la cola prima di berla?"

    return



