label gk301:
    call hide_menu

    stop music fadeout 3
    hide hinamizawa
    scene monitor_room
    with longFade
    "------------sc301 The aftermath-------------"
    play sound "audio/sfx/BANG.ogg"
    pause 1

    play sound "audio/sfx/office.mp3" fadein 6 volume 0.8 loop

    play music "audio/higu/silver mirror.mp3" fadein 2


    n "L'ultimo suono a uscire dall'altoparlante fu il botto di un esplosione, seguito da due messaggi di errore a schermo."

    n "{i}Errore canale audio:{/i} Segnale interrotto.{p}{i}Errore geolocalizazione:{/i} Segnale interrotto."


    anon "Assurdo."

    anon "Avete sentito?"

    anon "Si è davvero fatto esplodere."

    anon "E ora?"

    n "Nello sgomento generale, l'attenzione di tutti si spostò verso la figura seduta davanti al monitor centrale, apparentemente l'unica persona ad accogliere la notizia senza stupore o preoccupazione."

    oko_anon "Maggiore, io e i miei uomini andiamo a verificare lo stato del luogo dell'esplosione."

    n "L'uomo dai capelli verde scuro, visibilmente agitato fu il primo a prendere l'iniziativa."

    hb_anon "No, tu resta qua."

    oko_anon "Signore, ci dobbiamo assicurare che non scoppi un incendio, sarebbe un incubo da infangare."

    hb_anon "Ho detto resta qua. {w}Mi serve qualcuno che risponda alle chiamate in mia assenza.{p}{nw}"

    play music "audio/higu/gallery of madness.mp3" volume 1.5
    play sound "audio/sfx/zbiin.ogg"

    extend "Vado io."

    n "Lo sguardo del maggiore in quel momento ammutolì tutti i presenti."

    n "Istintivamente sapevano che la calma che vedevano era come quella di una bomba mentre conta i secondi all'esplosione."

    stop music fadeout 10

label gk302:
    call hide_menu

    scene tenjou with Dissolve(5)

    "------------scene 302 The flashback-------------"
    show sepia onlayer overlayer at truecenter:
        zoom 1.2
        alpha 0.5

    play music "audio/higu/silence.mp3" fadein 3
    n "Un soffitto sconosciuto..."

    n "Sono spaesato... L'ultima cosa che ricordo è che stavo scappando. E poi mi sono gettato in quel fiume..."

    n "Come ho fatto a sopravvivere?"

    la "Dove sono...?"

    ck "Larry, sei sveglio? {w}Resta sdraiato, non sei messo granchè."

    show check kindirect yep plain with Dissolve(2)
    pause 1
    ck "Sei stato fortunato sai? Quando ti ho trovato eri già praticamente a valle. {w}Se la corrente non ti avesse spinto a riva saresti morto schiantato contro qualche roccia ancora prima di affogare."

    ck "Davvero, è un miracolo che tu non abbia neanche un osso rotto."

    la "Capo? Ma perchè..."

    show check calling
    ck "Perchè non ti ho fatto fuori come diceva Lambdadelta?"

    n "La trasmittente! Ho fallito, ha scoperto di Lambdadelta!"

    n "Ho dolori in tutto il corpo... come faccio a scappare in questo stato?"

    show check plain
    ck "Ho non poche domande da farti, ma forse prima è meglio che parli con lei."

    n "Check mi posa la trasmittente accanto all'orecchio..... con chi vuole che parli?{w} Sarà la persona dietro tutto?"

    te "Buongiorno principessa."

    la "Terry?!"

    te "In persona."
    stop music fadeout 5

    scene torakku
    show check plain at left
    show check fp at flip
    show larry direct nope at right
    hide sepia onlayer overlayer
    with longFade


    play music "audio/higu/shadow.mp3"
    ck "Allora, adesso mi credi?"

    la "Ma i passi che ho mi inseguivano... da cosa stavo scappando?"

    te "Pensi davvero che riusciresti ad attraversare un intero versante con Check alle calcagna senza essere preso?"

    show larry -direct worried drop

    la "Non hai tutti i torti..."

    show larry -drop nope
    la "Ma una cospirazione per usurpare il BKG? Neanche questo è tanto facile da credere... Chi sarebbe in grado di fare una cosa del genere?"

    show check nope
    ck "Qualcuno con capacità fuori dal comune, e un potente sponsor ai piani alti."



    la "Piani alti? Vuole dire il governo?"

    ck "Non esattamente..."

    ck "Come ben sai, il BKG è una cellula antiterroristica paramilitare che gode di una certa autonomia, ma non si sostiene certamente da solo."

    "Change the music"
    play music "audio/higu/lies lies.mp3" fadein 2
    scene war with fade

    ck "Il Giappone non ha più avuto un esercito dalla seconda guerra mondiale, ma quanto a servizi segreti non scherza. {w}Come pensi che un giapponese come me si sia ritrovato a combattere per tutta l'asia e il medio oriente?"

    ck "Dopo che mi sono distinto come militare all'estero mi è stata data l'occasione di creare la mia organizzazione. {w}Sinceramente non ne potevo più di vedere compagni morire combattendo sul campo di battaglia per cause in cui non credevano."

    ck "L'unico rimpianto che ho è non essere stato al fianco del mio compagno più fidato nei suoi ultimi momenti. {w}È morto durante una missione in Afghanistan poco dopo la mia dipartita."

    ck "Questa mia filosofia ha senza dubbio reso il BKG una pedina scomoda da muovere, e questa volta una qualche fazione deve aver deciso che la mia presenza era più un contro che un pro."



    scene torakku
    show check plain at left
    show check fp nope at flip
    show larry direct worried at right
    with longFade

    ck "Per questo motivo non basterà tornare a casa base e spiegare la situazione per liberarci dell'impostore."

    la "Vuole dire che è stato preso di mira dalla stessa istituzione da cui il BKG dipende?{w} Allora è la fine... come possiamo sperare di vincere?"

    show larry nope
    te "Le carte che ci restano da giocare sono poche ma non ancora zero, specialmente se agiamo ora."

    te "Come spiegavo a Check, il BKG al momento è in uno stato a dir poco caotico. {w}Abbiamo perso ogni contatto con il nuovo comandante, e l'organizzazione è totalmente divisa sul da farsi."

    te "La mia teoria è che sia successo un imprevisto che nessuno si aspettava, nemmeno chi sta tirando le fila."

    te "Approfittando dello scompiglio, chi di noi credeva ancora in Check ha formato una fazione autonoma. {w}Il nostro obiettivo è uguale al vostro."

    te "Scoprire cosa è successo davvero dietro le quinte e trovare un modo di ri-leggittimare il BKG."

    te "Non siete soli Larry. Avete ancora degli alleati."



    show larry:
        ease 1 center
    show check:
        ease 1 offscreenleft
    pause 1.5

    "maybe this song starts earlier"
    play music "audio/higu/words of atonement.mp3" fadein 3
    show larry tilt with Dissolve(0.01)
    show red:
        alpha 0.1
    show black behind larry
    with Dissolve(3)

    n "...... rieccolo"



    n "C'è un pensiero fastidioso nei meandri del mio cervello che cerca di venire a galla."

    show red behind larry:
        alpha 0.2
    with Dissolve(1)
    n "\"{i}Che prove hai che stanno dicendo la verità?{/i}\" ... mi sussurra."

    show red behind larry:
        alpha 0.3
    with Dissolve(1)
    n "\"{i}È così che suonava la voce di Terry?{/i}\" ... \"{i}Quando è l'ultima volta che l'hai sentita?{/i}\" ... \"{i}Cosa faresti se fosse un altro inganno?{/i}\""

    show red behind larry:
        alpha 0.4
    with Dissolve(1)


    n "\"{i}Oppure questa è un allucinazione che stai avendo in punto di morte.... {w}Non vedi che è troppo perfetto per essere vero?{/i}\" "

    show larry -tilt
    n "Basta così. {w}Rinnego quel presentimento in fondo alla palude da cui è uscito. {w}La verità è più semplice di così... {w}ho sbagliato, niente di nuovo per me."

    n "Solo che questa volta....."

    hide red with Dissolve(2)
    show larry cry
    n "Non sono mai stato così felice di essere in errore."

    hide black
    show larry:
        ease 1 right
    show check angry:
        ease 1 left
    pause 1



    ck "Che ti prende ragazzo? Si sono riaperte le ferite?"

    la "Sono veramente inutile... non ne combino mai una giusta. {w}Anche in una crisi come questa sono stato solo un ostacolo per voi."

    la "Ho continuato a dare informazioni al nemico quando avrei dovuto fare il contrario e alla fine sono quasi affogato per niente."

    te "Non è solo colpa tua, tutti noi all'inizio abbiamo dubitato. {w}Sono io che per prima ti ho detto di non fidarti di Check."

    te "Larry, comandante. A nome di quel che resta del BKG, ci scusiamo profondamente."

    show check smile -angry
    ck "Ecchediamine, non pensavo di essere un capo così antipatico. Ehehahaha."

    show larry direct

    ck "Larry, sappi che quel tuo fraintendimento ci tornerà estremamente utile."

    ck "Vedi, mi hai dato un ottima idea per far perdere le nostre tracce e confondere il nemico allo stesso tempo."

    ck "Ecco il piano....."
    show check with Fade(2,0.5,2)

    te "...."

    la "Mhhh...."

#     play music "audio/higu/spinning seesaw.mp3"
    play music "audio/higu/fearlessness.mp3"

    te "È un'idea così fuori di testa che può funzionare."

    te "Quella trasmittente è il loro principale punto di contatto. In questo modo perderanno le vostre tracce almeno temporaneamente."

    show larry worried
    la "Ma sarà abbastanza per convincerli che siamo morti?"

    ck "Naah, non dei professionisti come loro. Sicuramente ci verranno a cercare."

    te "Ma guadagnerete abbastanza tempo per far perdere le vostre tracce e unirvi alla nostra fazione!"

    show check smile
    show larry yep
    ck "...O almeno è quello che penseranno."

    ck "Se davvero Lambdadelta si trova a Hinamizawa, non avremo mai un'occasione migliore per scoprire la sua identità."

    show larry scared
    ck "Il successo dell'operazione dipenderà dalla tua performance Larry. Che ne dici?"

    la "Io... ehm."

    te "Eri nel club di teatro alle superiori, non è così diverso... tranne la parte in cui rischiate il fallimento della missione e la distruzione del BKG."

    la "Non stai aiutando Terry."

    la "Però avete ragione."

    show larry direct yep
    la "Ci posso riuscire. {w}No, ci DEVO riuscire! {w}È l'unico modo che ho per sdebitarmi."

    ck "Ben detto Larry. Tu prepara un copione, io invece... "
    show check sus
    extend "penserò all'esplosione."

    "transizione migliore"



label gk303:
    call hide_menu
    scene koya_fire with longFade
    "------------scene 303 Plan execution-------------"
    play music "audio/higu/fearlessness.mp3"

    sgherro1 "Team 1, veniamo da ovest, la capanna sta bruciando e non ci sono tracce di sopravvissuti."
    sgherro1 "Team 2, Anche da est tutto regolare, nessuna traccia di nessuno, la vettura è ancora parcheggiata fuori."
    sgherro1 "Team 3, La zona circostante è tutta pulita, non vi sono tracce di pneumatici sulle strade. Tutti tranne il Team 2 tornino alla base. Tra poco il tenente verrà a controllare di persona."

    "(Tutti se ne vanno tranne il team 2, composto da 2 persone.)"
    "(Assalto a sorpresa di Check e Larry, stelle a schermo.)"

    "(Da qui musica trionfale, non finisce fino a che non appare il mirino del fucile da cecchino.)"
    show check plain at left
    show check smile direct fp at flip
    show larry smile direct at right
    ck "Ragazzone, il tuo amico è ancora a nanna. Mettiamo le cose in chiaro, c'è in gioco la vita tua e del tuo compare qui. Abbiamo distrutto le radio e tornerete vivi solo se ci direte dove si trova il vostro capo."

    sgherro1 "Nnngh... Era tutta una messa in scena?!"


    ck "Una performance degna di un oscar ragazzo mio."

    la "Il merito è suo per avere ideato il piano capo."

    sgherro1 "Avete fatto saltare il aria la vostra base di proposito, siete pazzi!"

    show check calling
    la "Le trasmittenti in dotazione al BKG saranno anche impermeabili e ignifughe, peccato che non siano anche a prova di martello!"


    ck "E con quell'effetto sonoro... dal vostro lato dev'essere sembrata un esplosione abbastanza convincente."

    la "Infine è bastato dare fuoco alla baracca per farvi correre allo scoperto."

    show check plain
    ck "Senza più la possibilità di localizzare la trasmittente e origliare le nostre conversazioni, la vostra prossima mossa come professionisti poteva essere una sola... l'occasione perfetta per un agguato!"

    show check angry nope:
        parallel:
            ease 1 zoom 1.5
        parallel:
            ease 1 yalign 0.2
    ck "Avanti rispondi! Chi è Lambdadelta e dove si nasconde!?"
    play sound "audio/sfx/down.ogg"
    sgherro1 "Ahrg!{w} Lambdadelta? Vuoi dire il maggiore?{w} Hahahaha. Far arrabbiare quella persona è stato il vostro ultimo errore. Tra non molto ve la farà pagare {nw}"
    play sound ["audio/sfx/furu.ogg", "audio/sfx/down.ogg"]
    extend "GRAAAAGH!"


    ck "Interessante... perchè non ci dici di più su questo maggiore?"
    sgherro1 "Dovrete chiedere al mio cadavere."

    show check smile
    ck "Larry, ho un idea. Riempi la macchina con l'esplosivo plastico."

    show larry scared worried
    la "Con cosa scusi?"
    show check neutral nope
    n "..........."
    show larry smile evil
    la "....Ah si.... l'esplosivo che ci era avanzato! {w}Lo carico tutto nel bagagliaio."
    show larry at flip:
        linear 1 offscreenright

#     show check yep fire:
#         linear 1 xalign 0.5
    pause 1
    sgherro1 "Ma che diavolo..."

    show check yep fire
    ck "Attaccheremo i circuiti al contachilometri. E se scende sotto i 10 Km/h per troppo tempo... BOOM"
    sgherro1 "Non potete fare sul serio"
    ck "Possiamo eccome, serve una dimostrazione?"

    show larry at unflip:
        offscreenright
        linear 1 right

    la "Ecco fatto... adesso le manette"


    show larry directevil:
        parallel:
            ease 1 zoom 1.5
        parallel:
            ease 1 yalign 0.2

    sgherro1 "IIIIIIH State lontani!"

    ck "Bene, mettiamolo in macchina."
    show black with Dissolve(0.5)
    play sound ["audio/sfx/furu.ogg","audio/sfx/down.ogg","audio/sfx/doon.mp3"]
    pause 3

    scene car
    show embers
    show larry directevil smile at right
    show check plain at left
    show check smile fire fp at flip
    show car_fire_overlay
    with Dissolve(0.5)
    ck "Ecco il quanto, ora ti ammanettiamo al volante e tu guiderai verso est quanto più veloce possibile."

    show check:
        parallel:
            ease 1 zoom 1.5
        parallel:
            ease 1 yalign -0.1
    show larry:
        parallel:
            ease 1 zoom 1.5
        parallel:
            ease 1 yalign -0.1
    ck "Se la chiave gira... boom. {w}Se stai fermo troppo a lungo... boom. {w}Se finisce la benzina e la macchina si spegne da sola, hai vinto."
    ck "Ovviamente non è solo la tua vita che è in gioco. {w}Abbiamo legato e caricato il tuo compagno nel sedile di dietro."
    sgherro2 "MHHHH MMHHHHHHH MMMMMMMMMMMMMMMHHHHHHHHHHHHM!"
    la "Lo senti? Ti sta augurando buona fortuna."


    sgherro1 "IIIIIIIIIH!!! {w}ABBIATE PIETÀ!!!"
    sgherro1 "Volete sapere chi siamo? Ve lo dico io! Perciò smettetela con quegli esplosivi!"
    sgherro1 "Siamo i {color=#ffe674}________ ____{/color}... abbiamo circa 90 uomini stanziati a Hinamizawa{w} La nostra base operativa è {color=#ffe674}___ __________ _____ _______ ____{/color}!"
    sgherro1 "Il maggiore... Non so da dove viene esattamente o perchè è stato assegnato a questa operazione, ma so che è un veterano di guerra."

    ck "Hai sentito Larry? Abbiamo un luogo da investigare.{w} Ci serve soltanto una traccia per fargli pensare che siamo scappati con questa automobile."
    ck "Puoi attaccare il plastico."
    la "Signorsi signore."
    show larry:
        ease 1 yoffset 600
    pause 1

    sgherro1 "ASPETTA QUESTO È UN CRIMINE DI GUERRA!!!!{w} DOVE È IL VOSTRO ONORE!!!!{w} DEMONI!!!!!!"
    ck "Dovreste esserci abituati qua a Hinamizawa. Vedi almeno di non finire nella palude."
    show larry:
        ease 1 yoffset 0
    pause 1
    la "Tutto pronto capo, il timer sarà attivo tra 30 secondi."
    ck "Premi il pedale amico. Buona fortuna!"
    window hide
    play sound "audio/sfx/speeding car.mp3" volume 1.5
    pause 2.5

    scene road_sunset with fade
    sgherro1 "AAAAAAAAAAAAAAAAAAAAAAAAAaaaaaaaaaahhhhhhhhhhhhhhhhhhh!!!!!!!"
    pause 1
    show larry direct yep at right
    show check plain at left
    show check yep direct fp at flip
    with dissolve

    ck "Era uno scherzone! Non c'era nessun esplosivo!"

    la "Andiamo a fare il resto della scena in cui mi sparano."


    "Hanabi ha previsto tutto e lo trova."

    hb "Proprio come ai vecchi tempi."

    ck "Pensavo che eri morto fra"

    hb "I'm a ghost and I'm back to haunt you"

    "Shooty shooty shoot"

    "------------Kojima moment-------------"

    hb "Si signore. Quì Hanabi... {w}anzi... quì Lambdadelta."

    hb "Check è stato neutralizzato insieme al suo assistente."

    hb "No signore, non abbiamo tracce degli altri disertori del BKG. {w}La trasmittente di Check è andata distrutta e il loro hacker ha rimosso dai server ogni traccia delle loro comunicazioni."

    hb "Quanto al vostro obiettivo primario, se ha letto un giornale ultimamente saprà già che non è più raggiungibile. {w}Suppongo che il mio ruolo quì sia finito."

    hb "..... Si signore, farò ritorno a TOKYO tempestivamente."

    hb ".... Ricevuto."

    show black with longFade
    jump mid_start

    return