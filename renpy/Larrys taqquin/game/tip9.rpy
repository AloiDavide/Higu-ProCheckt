label tip9:
    stop music

    scene telephone with fade
    play music "audio/lies lies.mp3"

    la "Che cosa..."

    la "...diamine..."
    la "...è successo..."
    la "...a Hinamizawa?"

    n """Secondo i media, il gas ha riempito la vallata durante la notte.

    Dopo una mattinata a perlustrare il villaggio hanno trovato ancora solo un sopravvissuto.

    Non importa, è troppo presto per avere un identikit delle vittime.{w} Inoltre nessuno sarebbe in grado di identificare il capo.

    È improbabile che stesse dormendo, non durante un operazione del genere. {w}Non può essere stato colto di sorpresa.

    Sicuramente è riuscito a fuggire e sarà qui a momenti.

    Si è tirato fuori illeso dalla guerra in Vietnam e dal deserto dei Gobi. Non sarà una piccola eruzione a fermarlo... {w}Voglio sperare.

    Quando finalmente metto la preoccupazione a tacere per un momento, mi colpisce una realizzazione."""

    la "Ma... quante persone..."

    la "...sono appena morte?"

    n """

    Hinamizawa è un villaggio sperduto, un buco di campagna, un piccolo comune di appena 2000 abitanti.

    Solo adesso mi rendo conto di quanto sia grande veramente quel numero.

    Fino a ieri migliaia di persone erano vive.

    E ora sono scomparse tutte. Buone e cattive."""

    scene streets with fade
    n "Tutti i residenti e i turisti."

    scene building with fade
    n "I vecchi e i giovani."

    scene classroom with fade
    n "Tutti gli studenti della scuola."


    scene clinic room with fade
    n "I dottori che ci hanno soccorso."


    scene satokhome with fade
    n "Pure Teppei e i suoi amici."
    n "E ovviamente Satoko insieme a loro."

    scene hinamizawa with fade
    n "La quasi totalità di un centro abitato."
    n "Perfino Lambda..."

    scene telephone with fade
    la "Aspetta! Anche Lambdadelta era là!"

    la "Potrebbe essere tra le vittime. {w}No, è molto probabile che lo sia."

    la "Gli sta bene! Fa tanto il genio e poi finisce vittima di un disastro naturale. {w}Hah haha."

    n """Per qualche motivo non riesco a essere genuinamente contento.

    No, il motivo é ovvio.

    Anche se il fato avesse ucciso il nostro nemico giurato. Per quanto conveniente possa essere.

    Se riesci a gioire di una cosa del genere non sei umano."""

    n "Non riesco ancora a credere a quello che è successo, ma ora ho un solo desiderio."

    n "Fa che il capo sia sano e salvo."

    play sound "audio/vibration.mp3"

    stop music fadeout(5)
    n "*vrrrr - vrrrr - vrrrr - vrrrr*"


    n "Terry deve essere scioccata quanto me."

    #---------------------------------------------------------
    stop sound
    play music "audio/fascism.ogg"
    pause (1)
    ltk "Parla Lambdadelta. Recluta Larry, buon giorno."

    la "MACCHE... {w}piacere sentirla. Comandante."

    n "Se avessi avuto dell'acqua in bocca mi sarei fatto una doccia."

    n "Quindi non ha beccato il gas. Dannazione."

    n "Va bene, devo solo mantenere la calma e agire secondo il piano."


    n "Lambda mi vede ancora come un suo sottoposto spaventato ma leale, e deve continuare a farlo."

    la """Con tutto il rispetto egregio comandante. {w}Vorrei contribuire a giustiziare Check il prima possibile. {w}
    Ma come posso svolgere la missione in queste condizioni?

    Avrà senz'altro avuto notizia del disastro naturale che ha colpito Hinamizawa. {w}
    Diamine, se non mi fossi trovato fuori dal villaggio adesso sarei morto anche io!"""

    ltk "Non deve essere facile per te, per cui voglio almeno dare una risposta ai tuoi dubbi."

    ltk "Check {b}non{/b} è stato ucciso dalla catastrofe."

    n "Lo sapevo! Non poteva essere altrimenti!"

    ltk "Non avrebbe potuto morire per via del gas. {w}D'altronde..."
    play sound "audio/wake up.ogg"
    ltk "Quando il gas è arrivato era già morto da ore."

    la "CHE CO..."

    la "...Che conveniente notizia."

    n "Dev'essere un test, sta bluffando perchè sospetta di me. Si deve essere così."

    la "Significa che il mio aiuto non è più necessario?"

    ltk "Precisamente, ho solo voluto mostrare un po' di considerazione nei tuoi confronti."


    ltk "Pensavo che avresti voluto conoscere le ultime parole del tuo amato capo."

    scene eyes
    play sound "audio/wake up.ogg"
    n "Sa tutto."

    n "Anche attraverso la trasmittente, anche con la voce fortemente alterata. Capisco che ai suoi occhi le mie bugie sono trasparenti come l'aria."

    ltk """Aaah, forse non mi credi. {w}Ma fortunatamente ho pensato a questa possibilità. {w}E l'ho registrato!

    Ma devi sapere che ho sempre odiato gli spoiler.

    Dato che sei così determinato ad espormi. Non sarebbe noioso se le risposte arrivassero senza che te le sei guadagnate?

    Quindi ho preso la libertà di censurare tutte le parti con informazioni di valore.
    """

    la "Smettila! Stai vaneggiando! Il capo non perderebbe mai! Non contro di te!"

    ltk "Non devi credermi sulla parola, ascolta con le tue orecchie."


    scene red with fade


    define dyingCK = Character("???", who_color = "#480000", what_style= "wide", who_style = "border")

    dyingCK "Grr gnn aah..."

    n "Che succede? Cosa sono quei lamenti?"

    n "Non è Lambda. Sta riproducendo un audio?"

    dyingCK "La... La pagherete... haah! Specialmente tu {nw}"

    play sound "audio/truth.mp3"
    extend "{color=#ffe674}*beeep*{/color}, la pagherai!"

    ltk "Lo senti Larry? Questo è il suono di Check che si gratta la gola."

    ltk "Ha battuto da solo 10 dei miei uomini, ma infine è caduto in trappola e adesso è solo un cane rabbioso."

    ck "Larry? Larry! Si c'era ancora Larry! *coff coff*"

    ck "Non pensare di aver vinto. Larry scoprirà la verità!"

    ck "E Terry e tutti gli altri!"

    ck "Le nostre reclute hanno qualcosa di speciale. {w}...Anche se adesso si piegano a te! ..Presto!.."

    ck "...Si, presto il tuo regno cadrà!"

    ck "E poi Oyashiro ti punirà. Aghh. Si, come nelle leggende. *bleargh* Scenderà dal cielo per punire i demoni che sgorgano dal sottosuolo."

    ltk "Ha hah"

    ltk "Ancora non ti è chiaro?"

    ltk "Non vi è dio senza maledizioni. {w}Gli uomini mi temono poichè li maledico. {w}Mi riveriscono poichè mi temono."

    ltk "Dio è già sceso in terra. {b}IO{/b} sono Oyashiro-sama.{w}\nHAAAHAHAHAHAHAHAHAHA HAAAHAHAHAHAHAHAHAHAHAHA HAAAAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA"


    scene telephone with longFade

    ltk "Larry questo Larry quello. {w}Doveva proprio fidarsi di te."

    ltk "Sfortunatamente, le persone in quello stato tendono a nascondere male i segreti."

    ltk "Sinceramente non pensavo che avresti avuto la lucidità di tornare dalla parte di Check."

    ltk "Ma adesso che lui non c'è non hai più nessun obbligo."

    ltk "Che cosa pensi di fare adesso???"

    la "......"

    la "Che cosa farò?"

    la "Dopo aver sentito questo, che cosa altro posso fare?..."

    la "...Dopo che il capo mi ha affidato una missione con il suo ultimo respiro. Come posso ignorarla e fuggire?"

    la "Giuro sul suo onore di portarla a termine. {w}Ti troverò Lambdadelta! Costi quel che costi. E ti porterò alla giustizia!"

    ltk "Ho hoo. Ammirevole."

    ltk "Se ne sei convinto allora vai e provaci."

    ltk "Ma risalire a me non sarà facile, dovrai prima svelare tutte le verità su Hinamizawa."

    ltk "Le altre persone potranno dimenticare con il tempo. {w}Ma tu vivrai il resto dei tuoi giorni incapace di uscire da questo incubo."

    ltk "Finchè ci saranno persone come te, il ricordo di Hinamizawa non cadrà mai nell'oblio."

    ltk "Che aspetti allora? Vienimi a cercare."

    ltk "HAHAHAHAHAHAHAHAHAHAHAHAHAHA."

    stop music fadeout(5)

    scene control room with longFade
    play music "audio/forfeit.mp3"
    true_n """Come Check aveva previsto, il tempo del BKG come regime totalitario non durò a lungo. {w}Il motivo, tuttavia, è lungi da quello
    che avrebbe sperato.

    A causa del malcontento diffuso, presto l'organizzazione un tempo unita si divise in fazioni.

    Mentre essa si trovara sul ciglio di una guerra civile, il nome Lambdadelta scomparve nel nulla
    tanto in fretta quanto era comparso.

    Ormai stanco e spezzettato, il BKG cessò ufficialmente di esistere sei mesi dopo la catastrofe.

    Le forze politiche che fino ad allora lo avevano supportato si pentirono di aver sprecato tempo su un esperimento fallito,
    e i tentativi di alcuni ex membri di ricostruirlo da zero furono ostacolati.

    Alla fine tutti continuarono con la propria vita.

    Quasi tutti..."""


    scene notes closed with fade
    # TODO no data
    true_n """

    In parallelo a tutto ciò, Larry si immerse nelle indagini, dedicando anima e corpo alla scoperta della verità.

    Tutti i contatti da parte di Terry cessarono in una questione di giorni. Ma egli non poteva demordere.

    Il villaggio era ormai completamente inaccessibile, e l'unico sopravvissuto, un tale Keiichi Maebara, è morto poco
    tempo dopo lasciando solo un intervista di dubbia autenticità.

    Nonostante tutti gli impedimenti. Per anni Larry investigò il disastro di Hinamizawa, e le numerose contraddizioni che lo circondavano.

    Credendo di trovarvi le motivazioni di Lambdadelta, Larry iniziò ad approfondire il folclore della regione e la sua storia.

    Nel farlo venne a conoscenza di un fantomatico quaderno di appunti che girava tra gli appassionati di occulto.

    Il cosiddetto 'Documento No.34'.

    Si diceva che fosse stato scritto da un'infermiera che lavoravava a Hinamizawa, e che al suo interno vi fosse una profezia che prevedeva un grande disastro.

    Stando a chi lo ha avuto tra le mani, a prima vista sembra una lettura erratica e senza senso.

    Ma i sostenitori di questa teoria sono convinti della sua validità come prova a favore di una cospirazione.

    Il fatto che l'autrice originale sia stata uccisa poco prima della catastrofe rende credibilità alla storia.

    Forse aveva tentato di mettere in guardia gli abitanti, e per questo era stata cancellata.

    """

    la "Col senno di poi, può darsi che Takano-san fosse in una situazione simile alla mia."

    la "Anche lei rincorreva un fantasma con il nome Oyashiro. {w}La differenza è che io sono ancora quà a combattere."

    la "A volte ripenso alle ultime frasi che mi ha detto Lambdadelta."

    la "Se quell'essere ha veramente l'abilità di maledire le persone. Allora quelle parole erano senza dubbio una maledizione nei miei confronti."

    la "Ma anche se fosse non posso smettere adesso. {w}Vorrebbe dire tradire la fiducia che il capo ha riposto in me."

    dyingCK "m..di.p.c...."

    dyingCK "mi.di.pi.ce..."

    dyingCK "...mi dispiace, mi dispiace, mi dispiace, mi dispiace..."

    la """Di nuovo questa voce.

    È lei capo, non è vero?

    Non si scusi. è stata tutta colpa mia.

    Lo so, dopo tutti questi anni non ho ancora svolto la sua ultima missione.

    Lambdadelta è ancora la fuori da qualche parte e sta ridendo di noi.

    Ma non si preoccupi. Non mi hanno creduto fino ad ora, ma questa volta. {w}Oh questa volta vedrà capo.

    Ho finalmente messo le mani sul documento 34.

    Aggiungerò il mio resoconto degli eventi, e li pubblicherò insieme.

    Serve un nome accattivante. {w}Lo chiamerò: Gli indizi perduti di Hinamizawa.

    Porterò alla luce la verità, così che un giorno, qualcuno possa venire a fondo di tutti i misteri.

    Questo è l'ultimo pezzo del puzzle, adesso finalmente saprò cosa ha scoperto Takano-san......"""

    scene notes

    la "...."

    la "Assurdo..."

    la "Non credo ai miei occhi. {w}Come può tutto questo essere la verità??????"

    stop music fadeout 10
    scene black with longerDiss

    return