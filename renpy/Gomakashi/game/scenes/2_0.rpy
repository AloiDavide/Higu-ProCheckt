label scene2_0:

    stop music fadeout 4

    scene night_hinamizawa with longFade


    n "Hinamizawa è in subbuglio per la seconda notte di fila."

    play sound "audio/sfx/cri cri.mp3"

    n "Con la scomparsa del sindaco ieri sera, e di quelle due ragazzine oggi, i residenti stanno rivoltando il villaggio come un calzino."


    n "Che diamine sta succedendo? Non doveva essere una morte e una sparizione all'anno? Abbiamo più che raddoppiato quelle cifre."



    play music "audio/higu/rainy days.mp3"


    anon "R k -  a  !"


    n "Sento una voce avvicinarsi"

    play sound 'audio/sfx/bushes2.mp3'

    scene night_road with Dissolve(1)

    old1 "Rika-chamaaa!!!"

    old2 "Il bosco di notte è pericoloso! Vieni fuori! {w}Rika-chama!"

    n "A prima vista sono solo due anziani che cercano Rika... {w}Ma non lo posso dare per scontato adesso."

    play sound "sfx/down.ogg"

    pause 0.5

    n "Si sono fermati in modo sospetto... uno dei due è caduto in ginocchio. {w}Che stanno facendo?"

    old1 "O grande Oyashiro-sama. Ti prego calma la tua ira."

    old2 "Idiota! Non lo devi neanche pensare. {w}Oyashiro-sama non può maledire un membro delle stimate tre famiglie. È semplicemente impossibile!"

    old1 "Ah si? E allora il prete Furude come me lo spieghi? Non è stato maledetto anche lui due anni fa?"

    old2 "Tu non capisci proprio niente però. Lui non era un vero membro della famiglia quindi non conta."

    old2 "Te lo dico io. Questo è un modo per mettere alla prova la nostra fede. {w}Sia Kimiyoshi che Rika-chama sono al sicuro, ne sono convinto!"

    old2 "E poi i trasgressori sono già stati puniti tutti, no?"

    old1 "Ma no, ma che dici. Dov'eri ieri quando Mion ha parlato a nome dei Sonozaki?"

    old1 "Nel magazzino rituale era entrato anche il figlio dei Maebara. Se qualcun altro merita di essere rapito dai demoni è quello screanzato."

    play sound "sfx/down.ogg"

    pause 0.5

    old1 "Oyashiro-sama. Abbi pietà per loro."

    n "......."

    n "Non hanno tutti i torti."

    n "Capisco \"maledire\" gli stranieri che hanno rotto il taboo, ma queste sparizioni sono troppo strane."

    n "Ammesso che li abbiano giudicati responsabili del cambio del lucchetto. Perchè loro prima di Keiichi?"

    n "E poi c'è Satoko. {w}È scomparsa anche lei ma non sembra importare a nessuno."

    n "Oltre ai ragazzi non ho sentito un solo abitante chiamarla. È come se tutti accettassero la sua sparizione come qualcosa di ovvio."

    play sound 'audio/sfx/bushes1.mp3'

    pause 2

    old2 "Ehi! Ho sentito qualcosa. Veniva da di là."

    old2 "Rika-chamaaaaa!"

    n "Dannazione mi hanno sentito."

    play sound 'audio/sfx/bushes3.mp3'
    scene night_small_shrine with Dissolve(2)

    n "Qua dovrei essere al sicuro per ora."

    n "È un sentiero sterrato in salita ed è notte fonda.{w} Non possono avermi seguito alla loro età."

    n "Ma potrebbero tornare con dei rinforzi."

    n "E se dovessero setacciare questo lato della montagna troverebbero il nostro nascondiglio...... {w}Il nascondiglio dove ora sta riposando il capo."

    show larry evil nope with dissolve

    stop music fadeout 4

    n "........{p}Ho bisogno di raccogliere i miei pensieri. Devo fare mente locale."

    play music 'audio/higu/ancient times.mp3' fadein 4
    play sound 'audio/sfx/multiple pageflips.mp3'
    show larry notes tilt with dissolve

        
    pause 1

    lan """
    Per riassumere in poche parole la mia situazione: Non mi posso fidare di Check in questo momento.

    Lo so, sembra assurdo. Eppure ho parlato sia con Terry che con un comandante in persona, e adesso devo fare i conti con la realtà davanti ai miei occhi.

    Sicuramente sapeva bene anche lui che il fondatore stesso del BKG è l'ultima persona da cui ci saremmo aspettati un'insubordinazione.

    Tante cose si spiegano nel momento in cui accettiamo un coinvolgimento del capo. Ad esempio il fatto che mi ha mentito sulla trasmittente.

    Da quando siamo partiti non siamo venuti in contatto con nessun altro capace di manometterla.
    Deve aver finto un guasto, così che non interferisse con le sue \"altre\" comunicazioni.
    """
    nvl clear

    play sound 'audio/sfx/pageflip.mp3'

    lan """
    Non è tutto quì.
    A distanza di minuti da quando quei quattro sono entrati nel magazzino rituale, Mion ne era già al corrente.
    {w}Lo so perchè l'abbiamo sentita incalzare Keiichi.

    Difatto anche i due anziani di prima lo avevano sentito dalla bocca di Mion. Non può essere una coincidenza.

    Secondo la nostra ricostruzione nessun altro si trovava nei paraggi in quel momento.{w}
    A meno che uno di loro non abbia vuotato il sacco di sua spontanea volontà, soltanto il capo avrebbe potuto diffondere l'informazione.

    E adesso abbiamo questa serie di omicidi e sparizioni su una scala completamente diversa da quelle degli altri anni...

    Possibile che la missione fosse una copertura, e che in realtà Check è venuto quì in qualità di spia e sicario per conto dei Sonozaki?

    """
    nvl clear
    "{nw}"
    show larry worried cry -tilt -notes

    la "Questa è tutta colpa sua capo. {w}Perchè non mi ha detto niente? Io di lei mi fidavo."

    show larry evil
    n "No, basta lamentele, devo concentrarmi. Non sono al sicuro quì."

    show larry nope notes tilt

    play sound 'audio/sfx/pageflip.mp3'



    lan """
    Oggi come ieri, il capo mi ha incaricato di fare da vedetta, e di avvisarlo qualora si avvicinassero troppo al nascondiglio. {w}
    Questo sembrerebbe indicare che non si è ancora accorto della mia presa di coscienza. {w}

    Mi chiedo che effetto avrebbe se lo facessi sgamare dagli abitanti del villaggio. {w}Sarebbe abbastanza per fermarlo?

    A meno che...

    Se Check è dalla loro parte significa che gli apici sono già al corrente della sua sua presenza, e per loro dovrebbe essere
    facile dirigere le ricerche lontano dalla sua posizione.

    Ma allora perchè assegnarmi questo ruolo? {w}Potrebbe essere un modo per distrarmi mentre porta a termine i suoi piani, o nel peggiore dei casi una trappola...
    """

    nvl clear

    "{nw}"

    show larry -tilt

    pause 0.5

    show larry at flip

    pause 1

    show larry at unflip

    pause 1

    play sound 'audio/sfx/pageflip.mp3'
    show larry tilt

    lan """
    A dire il vero.... {w}È da ieri sera che mi sento osservato...

    La ragione mi dice che non è possibile.
    Ho applicato tutte le precauzioni che conosco contro l'essere pedinato, e sono abbastanza sicuro di non avere telecamere addosso.

    So che tendo a panicare in queste situazioni, ma adesso sono sorprendentemente calmo. {w}
    I miei sensi oggi sono più acuti che mai. Posso dire con sicurezza che se qualcuno si avvicinasse lo noterei. {w}
    Credo che lo noterei....

    Ma allora perchè questa sensazione?
    """
    play music "audio/sfx/vibration.mp3"
    play sound "audio/higu/festivals_start.mp3"
    pause 0.7
    show larry -tilt


    n "{b}BZZZZZ BZZZZZ BZZZZZ{/b}"

    n "La trasmittente... è già l'orario stabilito?"

    n "Chi sarà questa volta? Sarà Terry? Oppure..."

    n "Mi faccio coraggio, e dopo aver controllo ancora una volta di non essere ascoltato, rispondo."

    stop music

    la "Agente semplice F32, nome in codice Larry."

    stop sound
    play music "audio/higu/festivals_main.mp3"

    show larry -notes worried


    ltk "Comandante 001, nome in condice Lambdadelta."

    n "È lui... {w}Il misterioso comandante designato al posto di Check per sventare i suoi piani. {w}dicono che la sua rete di informazioni sia senza paralleli."

    n "Questa è la seconda volta che mi contatta direttamente, il che non fa altro che riconfermare la serietà della situazione."

    show larry nope
    la "Al momento non ho ancora prove schiaccianti per incriminare Check, ma ormai sono sicuro che nasconde qualcosa."

    ltk "*bzz* Rispondimi Larry."

    ltk "Dove... Dove si trova? *bzz*"

    n "La trasmissione è disturbata... Sarà per via della montagna? Oppure ho sbagliato qualcosa nelle riparazioni?{w} Se solo Gerry fosse qua al mio posto..."

    la "Se sta chiedendo dov'è Check adesso, dovrebbe trovarsi ancora nel rifugio. {w}L'intero villaggio è sull'attenti per la scomparsa di altre due persone, è improbabile che si sia mosso."

    la "Per non destare sospetti sto seguendo il suo ordine di pattugliare la montagna, perciò non posso esserne certo. {w}Dovrei andare a verificare?"

    show larry scared

    ltk "Lascia perdere e rispondi alla mia domanda!"

    ltk "Voglio bzz sapere dov'è *bzzzzz*."

    la "Mi-m-m-mi perdoni. Non ho sentito bene a causa di interferenze. L-le chiedo umilmente di ripetere."

    camera at sshake

    play sound "audio/sfx/wake up.ogg"

    ltk "{cps=*0.5}DOVE È RIKA FURUDE?!{/cps}"


    n """Cosa? Rika? Come dovrei fare a sapere che fine ha fatto Rika Furude?

    Se lo chiede a me... vuol dire che Check è veramente responsabile per le sparizioni?

    È stato lui a rapire tutti? Quando è successo?

    Perchè solo Rika è così importante??"""

    "get some fitting image"
    show mion_jumpscare_phone

    ltk "Acolta bene questa è la tua nuova missione. Voglio che la trovi al più presto. Devo sapere con assoluta {b}CERTEZZA{/b} se è viva o morta o sarà tutto finito."

    la "Ma la mia copertura... {w}Cosa devo fare con Check?"

    ltk "Non importa! Se hai il tempo di rispondere esegui i miei ordini. MUOVITI!"

    ltk "Trova Rika! Fallo come se la tua vita dipendesse da questo."

    ltk "Trovala senza perdere tempo o non te la caverai con un espulsione. {w}La mia maledizione si abbatterà su di te. HAI CAPITO?"



    n "Che succede al comandante Lambdadelta? {w}Riesco a capire anche attraverso i filtri che sta parlando con voce spettata... sembra in preda al panico."

    show larry worried scared

    play sound "audio/sfx/wake up.ogg"

    "CAMBIA SFONDO E POI BOSCHI UPON BOSCHI"

    la "Chi va la!!!"

    n "Un momento fa... Posso giurare di aver sentito il rumore di un passo dietro di me. -swipe camera to another angle?-"

    n "Ma appena mi giro non c'è nessuno."

    n "Non c'è verso, DEVE essere lui. Nessun altro si sarebbe avvicinato così tanto prima di percepirlo."

    la "Capo? è lei? Non mi faccia spaventare, esca fuori."

    la "Sto sorvegliando le strade come mi ha detto."

    n "Nessuna risposta... Ha visto attraverso la mia facciata."

    n "L'unica cosa sensata in questo momento è correre."

    la "Comandante Lambdadelta! {W}È Check! Mi ha scoperto. Deve aver sentito tutto! Che devo fare?"

    n "Appoggio l'orecchio alla trasmittente in attesa di istruzioni, ma quello che sento è tutt'altro."

    ltk "TROVA RIKA TROVA RIKA TROVA RIKA TROVA RI A TR VA RIKA  ROVA  IKA TRO A RIKA T O A RI A"

    la "Comandante! Ho bisogno di rinforzi. Non posso farcela da solo."

    ltk "MALEDIZIONEMALEDIZIONEMALEDIZIONEALEIZIOEMLEDIONLEDIZONEMLEDIZEZIONZIODIZINE"

    n "Ahhh! Sento i suoi passi subito dietro di me. {w}È così vicino, ma per qualche miracolo non è ancora riuscito ad attaccarmi."

    anon "Heeeey! Venite qua. Ho visto qualcuno che corre sul fianco della montagna!"


    "larry slips and falls with the swamp in background"
    show larry cry worried

    la "DANNAZZIONE!"
    n "Lo sento avvicinarsi ma non ho più dove correre."
    show larry evil
    la "Non ho scelta."

    "ciaffff"

    "fade to black"



    return