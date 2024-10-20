#la maggior parte degli asset come immagini, personaggi e stili di testo, sono dichiarati in assets.rpy

#personaggi usati solo qui
define friendA = Character("Nullafacente", what_style = "wide", who_color= "#999", who_style = "border")
define friendB = Character("Ubriacone", what_style = "wide", who_color= "#999", who_style = "border")
define operator = Character("???", what_style = "wide", who_color= "#0090ca", who_style = "border")

label tip5:
    play music "audio/cicadas.ogg"
    scene satokhome with fade
    pause 1.5

    tep "WHA HA HA HA HA..."

    n "Sono appena tornato alla mia postazione e già sento gli schiamazzi di quel rifiuto umano."

    n "Il sole non è ancora tramontato, ma questi balordi sono già pieni all'orlo di alcol. Esattamente come li ho lasciati."

    friendA "Hey Houjou sta finendo il sakè!"

    tep "Si si lo so. {w}Ma che sta facendo Satoko, l'ho mandata a comprarlo un ora fa. {w}Sempre a perdere tempo."

    friendB """Che poi questa roba è troppo debole. Non è che la mocciosa ci mette l’acqua dentro? {w} Guarda non sono neanche un po' *hic*
     {w}neanche un po' ubriaco ti dico."""

    tep "Se tu sei sobrio io non mi faccio di niente."

    n "WHA HA HA HA HA HA!"

    scene black with fade
    scene satokhome with fade
    n """
        Non capisco come il capo può pensare di difenderlo.

        La burocrazia di questa città fa pena. Non possiamo fidarci delle autorità locali e abbiamo le mani legate,
        perché non capisce che sono necessarie misure drastiche?

        Non è solo questa volta. {w}Hinamizawa è piena di misteri, e noi dall’inizio non abbiamo fatto altro che seguire dei bambini.

        So che il capo non è uno stupido, nè tantomeno uno sprovveduto, è evidente che mi nasconde qualcosa. {w}
        A volte sa cose che non avrebbe modo di sapere, conosceva già i profili di alcuni cittadini. E poi c\'è la trasmittente...

        Da quando siamo arrivati dice che non funziona... ma non è vero.
    """

    play music "audio/vibration.mp3"
    n "*vrrrr - vrrrr - vrrrr*"

    n "Puntuale come un orologio svizzero, arriva la chiamata che stavo aspettanto."

    n "Lascio passare i quattro squilli concordati, e al quinto rispondo."

    stop music

    n "Dallo speaker del marchingegno esce una voce a me familiare."

    operator "Comunicazione regolare programmata. Perfavore esibire ID e nome in codice."

    la "ID numero XXX-XX {w}Larry a rapporto signora."



    operator "Qui Terry del quartier generale..."
    play music "audio/dawn.mp3"
    extend " va tutto bene?"

    ter "Mi dispiace, ieri non ho potuto dirti molto della situazione. Devi essere andato nel panico."

    la "No Terry, scusami tu. Avrei dovuto accorgermene prima.{w} I segnali d'allarme erano evidenti."

    scene satokhome flashback with fade

    n """
        È successo ieri mentre stavo esaminando la trasmittente dal mio nascondiglio. Non ho trovato traccia di nessun guasto o manomessione se non per un dettaglio.

        I gadget importanti sono dotati di localizzatori per tracciarne la posizione, quello della trasmittente era messo male, ma in qualche modo sono riuscito a sistemarlo.

        Non mi sarei mai aspettato però che da lì a pochi minuti, all'improvviso, avrebbe captato una chiamata.

        Inutile dire che il cuore mi è saltato in gola, ma sentire la voce di Terry mi ha subito tranquillizzato.

        Era un pezzo che non la sentivo. Lei e Gerry sono i miei amici più cari.
        {w}Li ho conosciuti quando avevamo più o meno l’età di Keiichi, siamo stati insieme per tutte le medie e le superiori, e poi siamo entrati insieme nel BKG.

        Quando il primo giorno ci presentammo in tre, eravamo uno più nervoso dell’altro.

        Vedendoci sempre vicini, il nostro superiore ci assegnò questi nomi in codice abbinati quasi come scherzo, e da quel momento l’ansia iniziò a sparire.

        Terry adesso lavora come operatrice al quartier generale. Fa parte dell’efficiente rete di comunicazione senza la quale il BKG non potrebbe funzionare.

        Eppure ciò che mi ha detto con quella chiamata è stato talmente uno shock che non ho potuto crederle sul momento.
    """

    scene satokhome with fade
    ter """Purtroppo è vero. Come ti ho accennato anche ieri, Check ha perso ufficialmente la sua posizione di comandante.

    Al momento è sospettato per tradimento, sembra stia cercando di supportare la stessa minaccia che era stato inviato a prevenire.
    """

    la "Ti prego, dimmi di più. Di che minaccia si parla? Ha a che fare con il Watanagashi? Chi è stato a corrompere Check? A me non hanno mai spiegato niente."

    ter """Mi dispiace, non ne so più di te, non ho mai visto nulla di così top secret.

    Gerry ed io abbiamo messo la nostra buona parola, ma i piani alti stanno ancora discutendo se fidarsi di te.

    Però sei fortunato, Lambdadelta è dalla tua parte."""

    la "Lambdachi? Chi è dalla mia parte?"

    ter """Il nuovo comandante che è subentrato in sostituzione di Check. Il suo nome in codice è Lambdadelta.

    Ha ottenuvo velocemente il supporto degli altri comandanti, e adesso sta attuanto delle pesanti riforme.

    Vista la situazione del quartier generale in questo periodo sarebbe difficile mandare un nuovo team di investigazione a Hinamizawa.
    {w}Per questo motivo il fatto che un agente sia già sul posto fa sicuramente comodo.

    Ecco perchè Lambdadelta era favorevole a chiedere il tuo aiuto.

    Perfavore abbiamo bisogno della tua collaborazione.
    """

    n """La trasmittente non era guasta, semplicemente al suo proprietario era stato revocato il diritto di fare chiamate. {w}Anche io posso solo aspettare di riceverne.

    Ma il BKG ha contattato me e non lui, questo è un fatto.

    Non posso più negarlo, devo farmente una ragione. {w}Il capo non è ciò che credevo. E io sono l'unico ad averlo osservato in queste ultime settimane.

    In poche parole solo io in tutto il BKG posso svolgere questa missione.
    """

    la "Si Terry, ti prometto che farò tutto il possibile."

    ter "Hey, è così che si parla in una comunicazione ufficiale?"

    la "Vero. Siamo entrambi sul posto di lavoro. La formalità prima di tutto."

    n "Dalla trasmittente proviene una lieve risata."

    ter "Assistente sul campo Larry. Può iniziare il suo resoconto riguardo il comportamento dell'ex comandante Check."

    la "Signorsi signora."

    n """Con la stessa meticolosità che metto nei miei appunti, riassumo ciò che è successo da quando si sono interrotti i contatti.
    {w}Dove Check è stato, chi ha incontrato, cosa ha indagato."""

    scene black with fade
    scene satokhome sunset with fade

    ter """Per finire ho un messaggio lasciato dal comandante Lambdadelta in persona, nel caso avessi deciso di aiutare.

    \"In lei nutriamo grandi aspettative, porti a compimento questa missione nella massima segretezza, e le assicuriamo
    la più rosea delle carriere, ma se dovesse fallire si prepari alle conseguenze.\"

    Con questo si conclude la comunicazione giornaliera. Continueremo a contattarla secondo le modalità discusse in precedenza.
    """

    la "Roger."

    scene black with fade
    scene satokhome sunset with fade

    n """Mi chiedo se sarebbe stato meglio chiedere consiglio per la questione di Satoko e Keiichi... {w}no, probabilmente non cambierebbe nulla.

    Non che non mi fidi del BKG, sicuramente loro capirebbero qual\'è la cosa giusta da fare. Ma anche se riuscissi a convincerli non sarebbero in grado di intervenire abbastanza in fretta.

    Sono felice di poter parlare con Terry, ma solo perchè sono in contatto col quartier generale non significa che accorreranno ad aiutarmi quando sarò in pericolo.

    Alla fine dei conti sono comunque da solo. {w}Io e il mio senso di giustizia."""


    scene black with longDiss


    return