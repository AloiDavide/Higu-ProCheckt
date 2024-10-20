define doc = Character("Dottore", who_color = "#977b6d", what_style= "wide", who_style = "border")


label tip3:
    play music "audio/cicadas.ogg"
    scene hinamizawa with fade
    pause 1.5
    scene streets with fade
    pause 1.5
    scene clinic out with fade
    pause 1.5
    scene clinic desk with fade
    pause 1.5
    scene clinic room with fade



    n "Apri gli occhi in una stanza a te sconosciuta. {w}Non hai idea di come tu sia arrivato qui, o cosa stessi facendo prima."

    n "Ti guardi intorno confuso e cerchi istintivamente di valutare l'ambiente circostante."

    n """Giaci coricato in un letto completamente bianco circondato da delle tende, accanto ad esso altri identici, mentre
     gli altri muri della stanza sono tappezzati da tavoli e scaffali contenenti per lo più flaconi etichettati e documenti."""

    n "L'intera stanza emana odore di disinfettante, è c'è persino un lavandino a portata di mano."

    n "Non c'è dubbio... Sei in un ospedale!"

    n "Mentre stai venendo a termini con questa deduzione, da dietro una delle tende compare una figura in camice bianco con degli occhiali."

    n "Non c'è dubbio... Questo è un dottore!"

    show irie serious0

    doc "Buongiorno... vedo che finalmente ha aperto gli occhi."

    doc "Non si agiti la prego, è stato ricoverato qui in seguito a un incidente. Per qualche motivo pare abbia battuto la testa e ha passato quasi 48 ore al tappeto."

    n "Ecco il motivo del mal di testa che sentivi.{w} Quando provi a toccarti la testa noti delle fasciature."

    show irie tilt2

    stop music

    doc "A questo proposito...{w} come dire, la sua condizione è...."

    show irie smile0

    play sound "audio/boing.mp3"

    play music "audio/boy in the windmill.mp3"

    doc "Perfettamente sana."


    show irie def0

    doc """
    È vero che la causa del suo ricovero è stato un trauma alla testa, ma per fortuna non ha subito lesioni celebrali preoccupanti.{w}
    Lei è ben lungi dall'essere in pericolo di vita, se resta a riposo si riprenderà senz'altro in poco tempo, lo garantisco io.

    Detto questo. Sebbene non ci siano complicazioni fisiche, il cervello ha comunque ricevuto uno shock sostanziale.{w} È possibile che vi siano falle nella sua memoria.

    """

    n "Il dottore ti parla con un tono pacato e rassicurante, nonostante lo scherzo di prima sembra comprendere bene la sua posizione di medico e il dovere nei confronti di un paziente."

    n "Non sei ancora sicuro se fidarti solo su questa base, ma su una cosa ha incontrovertibilmente ragione... Non riesci a richiamare la maggior parte dei tuoi ricordi."

    doc "Ah.. mi scusi, che maleducato, non mi sono ancora presentato. {w}Mi chiamo Irie, Kyousuke Irie, e gestisco questa clinica."

    ir "Quanto a lei, ricorda il suo nome?"

    n "Sollecitato dalla richiesta esplicita fai uno sforzo per ricordare, e i ricordi iniziano a fluire..."

    hide irie

    show check1 neutral straight

    n """
    Il tuo nome è Check, o almeno è così che vieni chiamato dai tuoi colleghi e sottoposti.

    Sei un capitano della {b}Book Keepers Guard{/b}, un’organizzazione paramilitare dedicata alla salvaguardia del pudore e della morale.

    Questa verità è radicata saldamente alla base del tuo io. {w}Non basterebbe una lobotomia a fartela dimenticare.

    Il tuo nome di battesimo al contrario... è qualcosa che non riesci proprio a ricordare. {w}Sarà perchè lo usi così raramente.{w}
    D'altronde un agente del BKG sotto copertura che si rispetti assume un’alias per nascondere la propria identità.

    Esso viene scelto ad hoc per non dare nell'occhio, tenendo conto del contesto della missione e di ogni possibile variabile.

    Ma adesso non hai tempo, hai bisogno di un nome falso in questo momento.

    Ti sforzi di ricordare quale fosse il tuo alias per questa missione.
    """

    default nomi = ["Bruce Karim Gabrielle",
                "BanKai Gendou",
                "Bernardo Kalogero Giancarlo",
                "Tanaka Taro"]


    menu:
        "[nomi[0]]":
            n "Un momento, non ti trovi in giappone?"
            $ scelta = 0
        "[nomi[1]]":
            n "Sarebbe un ottimo nome per il protagonista di un manga shonen, uno che fa a fette demoni con una spada enorme."
            $ scelta = 1

        "[nomi[2]]":
            n "Questo nome andrebbe bene se volessi passare per un membro della malavita mediterranea."
            $ scelta = 2
        "[nomi[3]]":
            n "Questo probabilmente non darebbe nell'occhio, ma non soddisfa neanche il canone delle tre lettere."
            $ scelta = 3



    n "Aah non importa, quattrocchi sta aspettando."

    show irie serious0:
            xpos -600

    show check1 neutral smile at right

    $nome = nomi[scelta]

    ck "Piacere di conoscerla, io mi chiamo [nome]"

    ck "Vista la situazione sarò breve. Ho semplicemente una domanda...."

    show check1 angry unhappy
    stop music

    ck "Cosa ACCIDENTI è successo?!"

    play music "audio/seijaku.mp3"
    show check1 neutral straight
    show irie serious2


    ir "Sinceramente, speravo potesse dirmelo lei{w}... Ma capisco, come temevo non ha memoria dell'incidente."

    scene swamp with newFade

    ir """Lei e un altro ragazzo che dice di chiamarsi Larry siete svenuti praticamente nel mezzo del nulla...

    Vicino a Hinamizawa c'è una palude abbastanza famigerata tra i residenti... voi eravate pericolosamente vicini al suo argine.

    Abbiamo teorizzato che foste dei turisti smarriti, e che in qualche modo foste caduti da un dislivello, ma sui vostri corpi
    non c'erano lesioni esterne attribuibili a una caduta.

    Purtroppo non abbiamo nulla di concreto se non le testimonianze dei vostri soccorritori.

    Erano dei giardinieri. Gli Okonogi gardeners, se non vado errato.
    """

    scene clinic room with newFade

    show check1 neutral straight at right

    show irie serious0:
            xpos -600



    ck "Vieni al punto. Come sta Larry?"

    show irie tilt0
    ir "Ebbene. {w}il suo amico Larry è..{w}..{w}.."

    play sound "audio/door slam.mp3"

    show irie def0 at center
    show lar1 cry smile at left
    stop music

    play music "audio/bright sun.mp3"

    la "Ooooh capitano mio capitano! Sia lodato il cielo lei è vivo!!!"

    ir "In ottima salute!"

    show lar1 cry worried

    la "Ho temuto di restare da solo smarrito in terra incognita."

    show lar1 cry smile
    la "Mi scuso per aver dubitato di lei. Dopo tutto nessuno ha la testa più dura del mio capo!"

    show check1 neutral unhappy
    show lar1 neutral worried

    ck "HEY. Quello non sembrava un complimento."

    scene clinic room
    show lar1 neutral smile

    n """
        Questo ragazzo è il tuo assistente Larry, è un po’maldestro e pecca ancora di inesperienza, ma sai che in lui risiede lo spirito di un vero BKG.

        Mentre continui a ricordare elementi del tuo passato succede qualcosa di strano. {w} Alcuni dei ricordi cominciano ad arrivare... dal futuro?

        Scene di felice vita quotidiana e scene di impareggiabile dolore iniziano a circolare nella tua mente mischiandosi tra di loro. {w}Finchè alla fine...
    """

    stop music

    show lar1 evil shout

    play sound "audio/BANG.ogg"
    pause 2

    ck "E CHE DIAMINE!"


    show check1 closed worried at right
    show irie serious0
    show lar1 scared unhappy at left


    $cognome = nome.split(" ")[-1]

    ir "Signor [cognome]? {w}C'è qualcosa che non va? {w}Prego si stenda, sembrava che stesse per avere un mancamento."

    n "Non è possibile, il Larry che conosci non lo farebbe mai!{w} Deve essere colpa dell'incidente, hai ancora la mente troppo confusa."

    show check1 neutral unhappy

    ck "N-no.. Sto benissimo, mi sono solo distratto. Cosa stavate dicendo?"

    play music "audio/kneecap.mp3"

    show lar1 neutral straight

    la "Il dottor irie stava chiedendo il motivo della nostra visita ad Hinamizawa."
    show irie def0

    ir "Larry mi ha detto che venite da Tokyo. Mi chiedevo soltanto cosa vi avesse spinto in un paesino così sperduto."


    n "Qualcosa ti dice che lo scopo del tuo viaggio non fosse semplice turismo. {w}No… tu se in missione per conto del BKG."

    n "Una missione estremamente cruciale della quale, purtroppo, non riesci a ricordare i dettagli."


    n "Chiaramente non puoi rispondere sinceramente a questa domanda, hai bisogno di una scusa in fretta."

    n "Scambi uno sguardo di intesa con Larry e dichiari la tua risposta."

    menu:
        "Siamo qui per il Watanagashi":
            show check1 neutral smile
            ck "Siamo qui per il Watanagashi."
            ir "Ma certo, il festival del villaggio. {w}Per cui ormai è così rinomato da attrarre turisti da tutto il giappone. La cosa mi rende orgoglioso."
            n "Sembra che menzionare il festival sia stata una buona mossa. Ma aspetta, dove hai avuto questa informazione?"

        "Sono un fotografo di uccelli":
            show check1 neutral smile
            ck "Sono un fotografo di uccelli."
            ir "Err, capisco. Hinamizawa dev’essere una meta veramente ambita tra i bird watcher"
            ir "Anche una mia conoscenza in questo periodo dell’anno gira sempre i dintorni del villaggio con la sua fotocamera."
            n "Sembra che in qualche modo tu sia riuscito a non destare troppi sospetti."

        "Penso di venire dal futuro":
            ck "Penso di venire dal futuro."
            show lar1 cry worried
            la "Oh no! Povero il mio capo! Non solo ha perso dei ricordi, ma ora crede anche di viaggiare nel tempo?!"
            la "Dottore la prego, faccia tutto quel che puo per aiutarlo."
            ir "Err, come ho detto. é solo un momento di confusione temporaneo, abbiamo già appurato che non ci saranno complicazioni per nessuno di voi due."
            n "Grazie all'aiuto di larry sembra che Irie abbia dimenticato la domanda."

    show lar1 neutral straight
    n "In quel momento la porta che Larry aveva sonoramente sbattuto si apre, e ne fuoriesce una donna vestita da infermiera."


    play sound "audio/door.mp3"



    hide irie
    show check1 neutral straight
    show takano def0
    show lar1 neutral pleased at left


    tk "Ecco dove eri finito. Sei partito a razzo quando hai avuto la buona notizia."

    la "Giusto. Quasi dimenticavo."

    show lar1 neutral smile

    la "Capo non ci crederà. Takano-san qui presente sa tutto del folclore di questo villaggio, mi stava giusto raccontando come ogni anno muore qualcuno."

    show takano smirk0
    play music "audio/silver mirror.mp3"

    tk "Larry non si ricorda proprio niente. Almeno lei saprà raccontarmi qualcosa sulla vostra escursione nel regno dei demoni, vero?"

    show check1 neutral worried
    show lar1 neutral straight

    ck "Spiacente infermiera, non posso esserle d'aiuto... {w}Ma che intende con demoni?"

    show takano smirk2

    tk """Si dice che la palude di Onigafuchi sia la residenza dei demoni che un tempo abitavano Hinamizawa.
     {w}Credevo lo sapeste già, dopotutto ci sono solo due motivi per andare a zonzo in quella zona...

     O sei un appassionato delle vecchie storie del luogo... {w}oppure devi nascondere un cadavere."""


    show check1 neutral straight
    show takano def0
    hide lar1

    show irie smile2:
            xpos -600

    ir "Hahaha. Takano-san non ti smentisci mai.{w} Puo sembrare scortese ma non date troppo peso alle sue storie, ovviamente sono tutte dicerie."

    show irie def0

    tk "Eeh? Ma dottore, due stranieri sono stati vittima di un’incidente ignoto per poi essere ritrovati nientemeno che sul ciglio della palude di Onigafuchi, e senza memoria per giunta!"
    tk " A questo punto non sarebbe più strano se fosse solo una coincidenza?"

    ir "Qualunque siano le circostanze, il nostro dovere è curare i pazienti. Vorrei che lasciassi le indagini alla polizia."

    tk "Mhhh."

    show takano def0

    tk "A proposito, Irie-sensei, ero venuta per comunicarle che sono arrivati degli ospiti."

    tk "Sono della polizia, credo ci sia anche qualche giornalista. {w}Sembra che neanche loro possono resistere al charm di questa storia."

    show irie serious0
    ir "Sempre con il peggior tempismo possibile. {w}Non sanno cosa significhi la parola riposo."

    show irie def2

    ir "Proverò a convincerli a tornare in un secondo momento, ma sanno essere molto testardi. Nel mentre prego, fate come pure come a casa vostra."

    hide irie
    show lar1 neutral straight at left

    n "Irie si fionda fuori dalla porta, e Takano fa per seguirlo, ma prima di chiudere la porta si rivolge a voi un'ultima volta."

    show takano smirk2
    show lar1 scared unhappy

    tk "Statemi bene voi due, non vorrei che quest’anno la maledizione arrivasse in anticipo."

    play sound "audio/door.mp3"

    hide takano

    show lar1 neutral unhappy

    n """.................

        ..........

        ....
        """

    la "Che facciamo?"

    n "La stanza è al piano terra e la finestra da sul retro della clinica. {w}Non è neanche una domanda."

    show check1 neutral talk

    ck "Ovvio...{w} Ce la diamo a gambe."

    play music "audio/cicadas.ogg"
    scene clinic back with fade
    show check1 neutral worried

    ck "Dobbiamo allontanarci da qui ALL'ISTANTE. Già troppe persone hanno visto la nostra faccia."

    scene streets with fade
    scene hinamizawa with fade

    n "Dopo essere sgattaiolati via con grande abilità, raggiungete un'altura che da sul villaggio."
    n "Allontanandovi avete sentito distintamente un \"Nufufu\", nella distanza, ma non sembra che nessuno vi abbia seguiti."

    show check2 neutral worried at right
    show lar1 neutral straight at left
    ck "Arrivati fino a qua dovremmo essere al sicuro. {w}Se quello che ci hanno detto è vero ci troviamo in una situazione davvero pessima."
    ck "Abbiamo perso tanto tempo per cause ignote, il dottore ha detto che è stato un incidente, ma la cosa mi puzza. {w}Non è da escludere che ci abbiano teso una trappola."
    ck "Per giunta nessuno di noi due ricorda il soggetto della missione."
    show lar1 neutral talk
    la "Non possiamo contattare il BKG con quella trasmittente? Dobbiamo comunicargli la situazione!"
    ck "Questa? Lascia perdere è andata."
    la "Allora perchè la tiene in mano?"

    show check2 neutral worried
    ck "....{w} Abitudine..."

    pause 1
    play music "audio/spinning seesaw.mp3"
    hide check2
    show check1 neutral smile at right
    show lar1 neutral pleased
    ck "Ascolta ragazzo, nei miei anni di servizio nel BKG ho dovuto tirarmi fuori da situazioni molto più disperate di questa."
    ck "Se credi che una piccola amnesia sia abbastanza per fermare Check, significa che non ti ho insegnato bene."
    ck "Questo posto da un’ottima visuale sul villaggio, perfetto per stabilire la nostra base di operazioni."
    ck "Forza Larry, è il momento di tornare al lavoro."
    show lar1 neutral unhappy
    la "Ma come? Non sappiamo neanche da dove iniziare."
    ck "É semplice, se non sappiamo quale pista seguire lasceremo fare al mio intuito."
    ck "Prepara i travestimenti, Per prima cosa faremo un giro di ricognizione. {w}La persona che riterrò più sospetta sarà il nostro bersaglio da sorvegliare."

    n "Mentre finisci di dire questo noti una scena raccapricciante con la coda dell'occhio."
    show check1 angry unhappy
    show lar1 scared talk
    n "Un ragazzino vestito con un costume da cameriera che violerebbe una dozzina di regole del BKG anche se fosse su una donna."
    n "Inoltre sta camminando per strada alla luce del sole circondato da ragazze. {w}Ci sono anche delle bambine!"

    define kei = Character("Capelli chiari", what_style = "wide", who_color= "#7b5252", who_style = "border")
    define rena = Character("Capelli arancioni", what_style = "wide", who_color= "#ff8835", who_style = "border")
    define mii = Character("Capelli verdi", what_style = "wide", who_color= "#23c076", who_style = "border")
    define rika = Character("Capelli blu", what_style = "wide", who_color= "#5c6ec3", who_style = "border")
    define satok = Character("Capelli biondi", what_style = "wide", who_color= "#ffe674", who_style = "border")

    mii "Hahahaha. Kei-chan sei un capolavoro! ho fatto bene a prendere la taglia più grande."
    rena "Auu povero Keiichi-kun. Sei diventato così kaaii."
    satok "Hoo hoo hoo hoo. è semplicemente ciò che meriti per provare a barare in un modo così evidente."
    rika "Keiichi non puo più andare in sposa. Nipaah. *pat pat*"
    kei "Dannazione! Perchè tutte a meeeeeeeeeee!!"
    pause 1

    hide check1
    show check2 angry unhappy at right
    ck "LARRY! Tira fuori quel taccuino e inizia a scrivere, abbiamo un codice BMSP."
    hide lar1
    show lar2 focus pleased at left
    la "Signorsi signore!"
    show lar2 neutral talk
    la "Una domanda signore, per cosa sta BMSP?"

    hide check2
    show check1 neutral unhappy at right
    ck "Devo davvero spiegarti tutto? {w}Ovviamente sta per \"Banda di Minorenni Spudorati in Pubblico\"."
    show check1 angry unhappy
    show lar2 focus pleased
    ck "Specialmente quello in mezzo vestito da cameriera! Giuro che fino alla fine della missione non lo perderemo di vista neanche per un secondo!"
    show lar2 focus smile
    la "Lo consideri già fatto capo!"

    stop music

    show black with newFade

    return



