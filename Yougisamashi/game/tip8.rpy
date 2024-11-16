image larleft = im.Scale(im.Flip("sprites/lar1 scared shout.png", horizontal ="True"),681, 1080)
image ckright = im.Scale(im.Flip("sprites/check1 angry dissatisfied.png", horizontal ="True"),681, 1080)
image larleft focus straight = im.Scale(im.Flip("sprites/lar1 focus straight.png", horizontal ="True"),681, 1080)
image larleft neutral straight = im.Scale(im.Flip("sprites/lar1 neutral straight.png", horizontal ="True"),681, 1080)
image supplex:
    animation
    size(681, 1080)
    "sprites/check1 angry dissatisfied.png"
    xalign 1.0
    yalign 1.0
    linear 0.5 xalign 0.3

    "sprites/check1 angry shout.png"
    pause 0.5
    linear 0.5 yalign 0.5
    linear 0.5 yalign 1.0
    repeat

image runup:
    animation
    size(681, 1080)
    im.Flip("sprites/check1 angry dissatisfied.png", horizontal ="True")

    xalign 0.0
    linear 0.5 xalign 1.0
    "sprites/check1 angry dissatisfied.png"


transform walkupRight:
    xalign 0.0
    yalign 0.0
    linear 0.8 xalign 0.6

transform walkbackLeft:
    xalign 0.6
    yalign 0.0
    linear 1.3 xalign 0.0

transform leap:
    xalign 1.0
    yalign 0.0
    linear 0.6 ypos -400
    linear 0.3 ypos 0

transform spin:
    parallel:
        yalign 0.0
        linear 0.6 ypos -400

        easein (0.5) rotate 450.0
        linear 0.3 ypos 400

    parallel:
        xalign 0.85
        pause 0.5
        linear 0.5 xalign -0.2

transform spinOld:
    parallel:
        yalign 0.0
        linear 0.6 ypos -400

        easein (0.5) rotate 180.0
        linear 0.3 ypos 300

    parallel:
        xalign 0.85
        pause 0.5
        linear 0.5 xalign 0.0

transform getup:
    parallel:
        xpos -550
        size(681, 1080)
        "sprites/lar1 scared straight.png"
        easein (0.5) rotate 360.0
        linear 0.3 ypos -100








label tip8:
    play music "audio/cicadas.ogg"
    scene koya with longFade
    show larleft:
        xalign 0.85
    show ckright at left


    play music "audio/dancers7.mp3"
    ck "Con che coraggio ti ripresenti al mio cospetto?"

    la "Sono successe tante cose, ma è tempo di mettere tutto in chiaro e far quadrare i conti."

    ck "Ah vuoi fare i conti? E allora preparati a subire la mia ira!"

    la "Cosa? No non in quel senso!"


    hide ckright
    show runup


    ck "Yaaaaaaahhh."


    hide runup
    show larleft at spin
    show check1 angry shout at leap



    pause(1.5)
    la "Ouch."

    n "Devo aggiungere questo alla lista di motivi per cui non farsi nemico Check."

    n "Mi ha lanciato così forte che non mi sento più le gambe."

    n "Guardando verso l'alto dal terreno dove sono stato scaraventato vedo un volto collerico, ma non è quello di un mostro."

    n "É la tipica faccia del capo quando faccio qualche cazzata."

    n "E stavolta l'ho fatta davvero grossa."

    show check1 angry unhappy

    ck "Forza rialzati."

    ck "Non hai la faccia di uno che è tornato per tendere una trappola. Ed evidentemente non sei qui per sfidarmi a duello. {w}Deduco tu abbia qualcosa da dire."

    show check1 angry shout
    ck "MA TIENI LE MANI DOVE LE POSSO VEDERE!"


    show larleft at getup
    pause(1)
    hide larleft

    show lar1 neutral pleased at left
    show check1 angry unhappy

    la "A lei non posso nascondere proprio nulla, eh capo?"

    la "Non sono venuto per farmi perdonare. Ma in questo momento è cruciale che lei conosca il mio lato della storia."

    ck "E sia, ti starò a sentire prima di decidere cosa fare con te."

    stop music fadeout 4

    scene woods1 with longFade

    play sound "audio/vibration.mp3"

    n "*vrrrr - vrrrr - vrrrr*"

    play music "audio/silence.mp3"

    n """Non adesso. Non sono pronto.

    Non dovrebbero richiamare così presto.

    Io non ho niente da dire al quartier generale. Non sono capace a fare nulla.

    Entrare nel BKG non ha cambiato niente, è sempre stato così.

    Sono solo un buono a nulla che per pura fortuna è diventato l'assistente di un comandante. E ora non sono neanche quello.

    Smettetela di aspettarvi risultati da me. Anche volendo non posso battere Check. Non sono all'altezza.

    Questa dannata trasmittente. Se solo non l'avessi mai presa."""

    play sound "audio/vibration.mp3"
    n"""*VRRRR - VRRRR - VRRRR*

    La vuoi smettere di vibrare?!

    Perchè le vibrazioni si fanno più forti?

    *VRRRR - VRRRR - VRRRR - VRRRR - VRRRR*

    Ho capito. Rispondo. {w}Basta che fai finire questo chiasso assordante.
    """

    stop sound

    play music "audio/words of atonement.mp3"

    ter "...Larry?"

    la "Terry!"

    ter "Grazie al cielo sei tu."

    la "Ma il nuovo capo aveva detto..."

    n "A questo punto non sopporterei un altro inganno. Me ne devo accertare."

    la "Scusa la domanda ma...{w} Sei veramente Terry... vero?"

    ter "Mhhhhh. Chi lo sa."

    la "Dì qualcosa che solo Terry saprebbe! Allora forse ti starò a sentire."

    ter "Hohoho, che paura."

    ter "Vediamo..."

    ter "Vuoi che ti reciti la top 10 battute orribili di Gerry? {w}Guarda che ci sono stati dei movimenti nella classifica mentre non c'eri."

    la "....Grazie, ma faccio volentieri a meno."

    ter "Sicuro? Ne vale la pena."

    la "Ho capito ho capito ti credo. {w}Sicuramente avrai cose più importanti da dirmi. O sbaglio?"

    ter "Conoscendoti ho pensato che a quest'ora saresti finito a piangere da solo in un angolino, e ho pensato di venirti a consolare."

    la """Non hai tutti i torti, sinceramente mi sento aggrappato alla sanità mentale per un filo. {w}Ma non farmi preoccupare e vieni al punto.

    Cosa è successo? {w}Perchè mi hanno detto che eri stata rimossa dal tuo ruolo?"""

    ter """....{w}Hai ragione. {w}È solo questione di tempo prima che si accorgano di questa chiamata, quindi la farò breve.

    Il BKG ha perso di vista se stesso. {w}Non è più l’organizzazione che ci ha accolti. {w}Non da quando quel comandante è arrivato.

    Usare un nome falso è la norma da noi, ma Lambdadelta da un nuovo significato alla parola top secret.

    Nessuno che conosco ne ha mai visto l’aspetto, o sentito la vera voce. {w}Non abbiamo idea se sia uomo o donna, niente di niente.

    La sua ascesa al potere è stata spinta fortemente dai finanziatori del BKG, nessuno degli altri comandanti avrebbe potuto rifiutare un’offerta del genere.

    Non sapevano in che guaio si erano infilati.

    Pur non essendosi mai presentato al quartier generale, in poco tempo è stato in grado di prendere tutta la nostra infrastruttura sotto il suo controllo.{w}
    Gli è bastato dirigere i pochi sottoposti con cui è in contatto diretto.

    Abbiamo a che fare con qualcuno di incredibilmente astuto.

    E hanno mirato di proposito al periodo in cui Check non era presente. Sapevano che lui non l’avremme mai lasciato succedere.

    Capisci dove voglio andare a parare, vero Larry?

    Lambdadelta ha presentato una grossa quantità di materiale incriminante contro Check.

    È chiaro, una tale accusa non sarebbe mai presa sul serio senza nulla a supporto.

    L'accusatore farebbe la figura dell’idiota, o al peggio del traditore.

    Sotto normali circostanze mi verrebbe da dire che non c’è modo di forgiare una tale quantità di prove, ma una cosa è certa.

    Quella persona non è normale.

    Non è forse possibile che fosse tutto falso dall'inizio?

    È vero, le azioni di Check possono sembrare strane in confronto al suo solito modus operandi.

    Poi sei arrivato tu a confermare il tutto con la tua testimonianza, e anche io stavo per convincermi dell’evidenza.

    Ma non riuscivo a non pensarci. Ci sono dei punti di questa storia che proprio non mi tornano.

    Tanto per cominciare, dopo voi due non si è più parlato di inviare nessuno a Hinamizawa. {w}Né per catturare Check, nè per proseguire la vostra missione originale. {w}Sembra che la questione abbia perso completamente priorità.


    Inoltre, come mai i piani alti erano così sicuri che avessi tu la trasmittente?

    Il fatto che il tracker sia tornato operativo non è minimamente abbastanza evidenza. Eppure giorno dopo giorno sapevano esattamente quando chiamare.

    Neanche io mi fiderei di te fino a quel punto."""

    la "Hey!"

    ter"Senza offesa compare."

    la "Aspetta. Mi stai dicendo che il BKG non ha svolto nessuna investigazione supplementare?"

    ter "No, non da quando siamo riusciti a contattare te."

    la "Ma allora. Come faceva a sapere tutte quelle cose?"

    ter "Anche tu inizi a nutrire il sospetto vedo. {w}Lascia che ti dia la conferma."

    ter "Non sono riuscita a scoprirne l’identità, ma so da dove provenivano tutte le comunicazioni del nostro nuovo comandante."

    ter "Senza ombra di dubbio, Lambdadelta è a Hinamizawa."

    ter "Sia nelle scorse settimane che in questo stesso momento."

    la "E cosa vuoi che faccia al rigurado?"

    ter """Ecco quello che penso. {w}Non posso affermare con assoluta certezza che Check sia innocente, ma una cosa la so.

    Se qualcuno può risanare il BKG quello è lui, e tu sei il suo assistente. {w}Nessun altro può portargli le informazioni di cui ha bisogno in questo momento."""

    la "Ma.. i passi. Sono due giorni interi che mi segue."

    ter "Lo hai visto seguirti?"

    la "Beh no, non direttamente, ma chi altro poteva essere?"

    ter "Pensala così. Se Check volesse veramente farti del male, credi davvero che gli saresti sfuggito così a lungo?"

    la "...No{w}, lui non pedinerebbe in un modo così evidente."

    n "Ripensandoci era impossibile che fossi migliorato a tal punto."

    la "Si però"

    ter "Senti, non so bene cosa è successo tra voi due. Ma ripeto, è qualcosa che posso chiedere soltanto a te."

    scene black
    show moon
    show lar1 focus talk
    la "Ancora questa storia?"

    ter "Larry?"

    la """Ancora con i \"solo tu puoi\".

    Io non sono un agente segreto, non ho nervi saldi o abilità fuori dal comune.

    Io sono solo quello che scrive le cose sul taccuino{w}, non ho nessun desiderio di essere l'eroe della situazione."""

    show lar1 focus smile
    la "Insomma, per una volta ho provato a combinare qualcosa per conto mio, ed ecco il risultato!"

    show lar1 focus worried
    la "Non voglio più cadere vittima di gente che fa appello all'ego."

    show lar1 focus pleased
    la "Hey Terry rispondimi, tu che hai sempre avuto le idee chiare."

    la "Davvero posso fidarmi di te?"

    la "Davvero Check non è impazzito o posseduto?"

    la "Davvero posso finalmente smettere di correre?"

    la "Se faccio quello che dici tu andrà tutto bene questa volta, vero?"

    ter "Oh ma certo che..."

    show lar1 focus straight
    ter """No...

    Non posso farmi carico io di tutte le tue scelte. {w}Non ha alcun senso se tu stesso non hai fiducia nelle direzioni che segui. {w}
    Questo vale tanto nei miei confronti quanto in quelli di Check.

    Lo so che hai paura di sbagliare, dimostra quanto ti sta a cuore quello che fai. {w}Ma se prenderai ordini da qualcuno, devi farlo sulla base del rispetto.{w}
    Altrimenti non sei altro che una pedina."""

    show lar1 focus pleased
    la "Severa come al solito. {w}Ancora una volta mi impedisci di fuggire dai miei problemi."

    show lar1 closed straight
    la ".........................................................................."

    show lar1 focus talk
    la "....Un'ultima volta."

    ter "Mhh?"

    la "Sinceramente vorrei tirarmene fuori in questo momento."

    show lar1 closed talk
    la "Ma se penso a Lambdadelta che se la ride mentre guarda tutti noi danzare nel palmo della sua mano, il sangue mi ribolle nelle vene."

    show lar1 focus smile
    la "Non sono adatto al ruolo dell'eroe... ma posso almeno fare la spalla fino alla fine."

    la "Voglio provare a fidarmi di Check un'ultima volta. {w}Questa sarà la mia ultima missione per il BKG. {w}Il {b}vero{/b} BKG."

    ter "Larry..."

    ter "È così che ti voglio! Ora prepara quel tuo taccuino."

    ter "È il momento di segnare tutti gli ultimi succosi scoop su Lambdadelta. {w}Appena sfornati da Terry la super hacker, solo per voi."

    hide lar1
    show lar2 focus pleased

    la "Se si tratta di scrivere, quello almeno mi riesce ancora bene."

    stop music fadeout 5.0

    scene koya with longFade
    play music "audio/gear.mp3" #oppure gear

    show check1 angry unhappy at right

    show lar1 closed straight at left

    ck """Mi stai dicendo che tu, convinto dalle storie di un pazzo che va in giro a rubare il lavoro degli altri, avresti sabotato la mia operazione e divulgato le mie informazioni dietro le mie spalle...

    Ci vuole coraggio.

    Cosa hai da dire a tua discolpa?"""

    show lar1 closed talk
    la "Nulla capo, non merito scusanti{w}, ma dovevo a tutti i costi riferirle ciò che so."

    show lar1 closed straight

    ck "Questa è l’ennesima volta che la tua inesperienza ci mette in pericolo."

    ck "Larry! Sei licenziato per doppiogioco e sabotaggio, oltre che per enorme stupidità."

    show lar1 closed pleased

    n "C'era da aspettarselo, ma è giusto così. {w}Con questo il mio ruolo è finalmente giunto al termine."

    n "Non correrò più il rischio di rovinare tutto."




    show lar1 focus pleased

    la "Capisco perfettamente. Ecco a lei taccuino e trasmittente."

    show lar1 at walkupRight
    pause(1)

    stop music fadeout 2.0

    show lar1 focus talk
    la "Addio capo..."

    hide lar1
    show larleft focus straight at walkbackLeft

    pause(1.3)
    show check1 neutral talk

    ck "Hey Larry!"

    hide larleft
    show lar1 neutral straight at left

    play music "audio/sisters.mp3"

    ck "Ah è vero, non ti chiami più Larry. {w}Qual’era il tuo vero nome?"

    show check1 closed shout

    ck "Aspetta non me lo dire... Davvero cel'ho sulla punta della lingua."

    show check1 closed straight
    ck "Mhhhhhhhh..."

    show check1 neutral talk

    ck """Comunque! {w}Il fatto che tu sia riuscito a raggirarmi dimostra se non altro una differenza di abilità abissale rispetto a quando hai cominciato questo lavoro.

    Quando avrò ripulito il BKG dalla corruzione e riscattato il mio posto avrò bisogno di giovani talenti per rifocillare i ranghi. {w}E tu, a quanto mi risulta, sei disoccupato.

    Che ne diresti di mettere le tue abilità a protezione della morale e del pudore?"""

    show check1 neutral straight
    show lar1 closed straight

    n "Impossibile."

    n "Mi sta davvero dando un'altra possibilità. {w}Dopo tutto quello che ho fatto."

    n "Suvvia Larry. Quel mondo non fa per te e lo hai capito benissimo."

    n "Devi rifiutare."

    n "Se resti al loro fianco continuerai a deluderli."

    show lar1 cry straight

    n "Ma allora perchè... {w}le parole escono da sole?"

    show lar1 cry smile

    la "Ne sarei onorato. {w}Mio comandante."

    show check1 neutral smile
    ck "Bentornato ragazzo."

    ck "Bentornato."

    stop music fadeout 8.0
    scene hinamizawa with longerFade

    play music "audio/cicadas.ogg"
    show check1 neutral unhappy at right
    show lar1 neutral straight at left
    ck """Che tu ci sia cascato non mi sorprende, ma dire che pure Terry era finita per sospettare di me. {w}Quel bastardo deve essersi proprio impegnato per infamarmi.

    Non solo ha deragliato la nostra investigazione con l’inganno, ma si è divertito nel farlo. {w}Giuro che non la passerà liscia."""

    show check1 neutral straight
    show lar1 neutral worried
    la """Terry ha lasciato un avvertimento. {w}Dice di fare attenzione perchè sta per succedere qualcosa di grosso ad Hinamizawa.

    Forse ci conviene lasciare momentaneamente il villaggio e tornare più preparati.

    Intanto lei cercherà di sistematizzare le sue attività di spionaggio. {w}Non è molto ma alcune reclute non contente del nuovo BKG sono già dalla nostra parte."""

    play music "audio/core.mp3"
    show check1 neutral talk
    show lar1 neutral straight
    ck "Più preparati? {w}Più di così?"

    la "Cosa intende?"

    ck "Intendo che grazie alle informazioni che mi hai dato ho capito esattamente dove si trova il covo del nemico."
    hide check1
    show check2 neutral worried at right
    ck "Pensaci, Se veramente il controllo del nostro nemico sul BKG si basa sulla comunicazione remota, deve avere molto più che una trasmittente come questa."
    hide check2
    show check1 neutral talk at right

    ck """C'è un solo posto in questo buco di campagna dove sarebbe possibile nascondere tutta l'attrezzatura! {w} Oltre al mio nascondiglio, si intende.

    Sarebbe da pazzi fermarsi ora che sono a tanto così da risolvere il mistero.

    Devo soltanto scoprire l'identità del comandante ladro, anche solo il volto mi basterebbe per ottenere un vantaggio."""

    show lar1 neutral pleased
    la "Capisco, vuole coglierli con le mani nel sacco."
    show lar1 neutral straight
    la "Ma non sarà pericoloso? Siamo praticamente nella tana del nemico."

    ck "Hinamizawa sarà anche la sua tana. {w}Ma un nemico che sta per giocare la mossa vincente è nel suo stato più vulnerabile."

    show lar1 neutral talk
    la "Ma capo, per colpa mia non ha neanche il suo equipaggiamento."

    show check1 neutral smile
    ck "Quella roba? Mi è bastato un pomeriggio per rimetterla in sesto."

    show lar1 neutral worried
    la "...dovevo immaginarlo."

    n "E dire che mi ero impegnato per rallentarlo almeno 24 ore."

    ck "Stai a vedere."

    ck "Il BKG è la mia casa. Per proteggerlo combatterò come un esercito di nani."

    show lar1 neutral talk
    la "A colpi di piccone?"

    show check1 angry talk
    ck "NOO! {w}Fino alla vittoria o alla morte."

    show lar1 neutral shout
    la "Capo! Non lo dica neanche, quando fa sul serio lei è imbattibile!"

    show check1 neutral talk
    ck "Tu aspettami nella città accanto e cerca di stabilire un contatto stabile con Terry. {w}Avrò bisogno di entrambi una volta scoperta l’identità del nemico."

    #stop music fadeout 2

    show lar1 neutral straight
    ck "Prendi questa."

    #play music

    n "La trasmittente è il simbolo del mio tradimento, eppure Il capo me la porge con grandissima naturalezza."

    n "Pensavo che averla portata con me fosse stata una maledizione{w}, ma alla fine è lei che ci ha portati alla verità."

    n "Non ho più motivo di esitare."

    la "Non la deluderò questa volta, promesso."

    ck "Hey, ti prendo sulla parola. Mi servirà tutto quello che hai da offrire."

    ck "Siamo pochi, ma non per questo meno agguerriti."

    ck "Dichiaro quì l'inizio dell'operazione per reclamare il BKG da Lambdadelta."

    ck "Dopodichè porteremo alla luce tutti i misteri che ricoprono Hinamizawa. Uno per uno."

    ck "Ieri il calunniatore ti ha detto di chiamarlo Oyashiro, vero?"

    ck "Che provocazione di pessimo gusto."

    ck "Ma se è questo che vuole, dimostreremo di essere più forti delle sue maledizioni."

    ck "Tutto può essere spiegato dall'intervento umano."

    ck "Ecco perchè chiameremo questa operazione: {w}{b}Hinamizawa Ghostbusters.{/b}"

    stop music fadeout 10
    scene black with longerDiss


    return