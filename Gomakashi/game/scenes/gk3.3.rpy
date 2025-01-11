label gk330:
    call hide_menu from _call_hide_menu_7

    stop music fadeout 3
    hide hinamizawa
    scene monitor_room
    with longFade
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

    hb_anon "No capitano, lei resta qua."

    oko_anon "Signore, ci dobbiamo assicurare che non scoppi un incendio, sarebbe un incubo da infangare."

    hb_anon "Le ho detto di restare qua. {w}Mi serve qualcuno che diriga l'operazione in mia assenza.{p}{nw}"

    play music "audio/higu/gallery of madness.mp3" volume 1.5
    play sound "audio/sfx/zbiin.ogg"

    extend "Vado io."

    n "Lo sguardo del maggiore in quel momento ammutolì tutti i presenti."

    n "Istintivamente sapevano che la calma che vedevano era come quella di una bomba mentre conta i secondi all'esplosione."

    stop music fadeout 10

label gk331:
    call hide_menu from _call_hide_menu_8

    scene tenjou with Dissolve(5)


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
    la "Ci posso riuscire. {w}No, CI RIUSCIRÒ! {w}È l'unico modo che ho per sdebitarmi."

    ck "Ben detto Larry. Tu prepara un copione, io invece... "
    show check sus
    extend "penserò a simulare l'esplosione."

    stop music fadeout 5
    show black with Dissolve(5)


label gk332:
    call hide_menu from _call_hide_menu_9
    play custom_audio "audio/sfx/fire.mp3" fadein 5 volume 0.1 loop
    scene koya_fire with Dissolve(5)

    play music "audio/higu/ancient times.mp3" fadein 3
#     lay music "audio/higu/silver mirror.mp3" fadein 3



    play sound "audio/sfx/bushes1.mp3"
    sgherro1 "Team 1, veniamo da ovest, la capanna sta bruciando e non ci sono tracce di sopravvissuti."
    sgherro2 "Team 2, Anche da est tutto regolare, nessuna traccia di nessuno, la loro vettura è ancora nascosta tra la vegetazione."
    sgherro3 "Team 3, La zona circostante è tutta pulita, non vi sono tracce di pneumatici sulle strade."
    play sound "audio/sfx/bushes1.mp3"
    sgherro3 "Il maggiore si sta dirigendo sul luogo con la sua scorta.{w} Team 2, restate pronti a riceverlo, tutti gli altri si adoperino immediatamente per arginare l'incendio, dobbiamo farlo sembrare un incidente."
    sgherro2 "Ricevuto."
    play sound "audio/sfx/bushes3.mp3"
    pause 2
    sgherro "Mhh?"
    window hide
    camera:
        xalign 1.0
        yalign 0.9
        ease 2 zoom 1.5

    pause 3

    camera:
        xalign 1.0
        yalign 0.9
        ease 1 zoom 2

    pause 1
    play sound "audio/sfx/bushes2.mp3"
    play music "audio/higu/fearlessness.mp3"
    ck "Adesso Larry!"

    sgherro "Che diavolo!?{w} AAAHH!"
    play sound ["audio/sfx/furu.ogg","audio/sfx/slam.mp3","audio/sfx/down.ogg"]
    show koya_fire at sshake
    pause 2

    show black with Dissolve(4)
    camera:
        xalign 0.5
        yalign 0.5
        zoom 1

    hide black
    show check plain at left
    show check shoutest direct fp at flip
    show larry yep direct at right
    with Dissolve(4)


    ck "Sveglia ragazzone!"
    la "Peccato che il tuo compare sia ancora a nanna."

    sgherro "Nnngh... Era tutta una messa in scena?!"
    play sound "audio/sfx/down.ogg"
    ck "Faccio io le domande!"

    ck "Mettiamo le cose in chiaro! L'unico modo che avete per uscirne vivi è dirci dove si trova il vostro capo!"

    la "È inutile che cerchi la tua radio, l'abbiamo presa noi."



    sgherro "Avete incendiato la vostra base di proposito!? siete pazzi!"


    show larry yep
    show check angry nope:
        parallel:
            ease 1 zoom 1.5
        parallel:
            ease 1 yalign 0.2

    ck "Se non hai voglia di scoprire quanto possiamo essere pazzi, rispondi!"
    ck "Chi è Lambdadelta e dove si nasconde!?"
    play sound "audio/sfx/down.ogg"
    sgherro "Ahrg!{w} Lambdadelta? Vuoi dire il maggiore?{w} Hahahaha. Far arrabbiare quella persona è stato il vostro ultimo errore... {nw}"
    play sound ["audio/sfx/furu.ogg", "audio/sfx/down.ogg"]
    extend "GRAAAAGH!"

    show check yep
    ck "Interessante... perchè non ci dici di più su questo maggiore?"
    sgherro "Dovrete chiedere al mio cadavere!"

    show check smile
    ck "Larry, ho un idea. Riempi la macchina con l'esplosivo al plastico."

    show larry scared worried
    la "Con cosa scusi?"
    show check neutral nope
    n "..........."
    show larry yep evil
    la "....Si, certo capo, l'esplosivo avanzato! {w}Lo carico tutto nel bagagliaio come al solito?"
    show check angry yep
    ck "Esatto, e passami anche le manette."
    show larry at flip:
        linear 1 offscreenright


    pause 1

    sgherro "Ma che diavolo..."


    ck "Forse essere ammanettato al volante di un'auto bomba ti scioglierà la lingua."
    sgherro "Non potete fare sul serio!"
    ck "Hai mai visto quel film in cui un terrorista pianta delle bombe su un autobus che esploderanno se l'autista rallenta?"

    show larry at unflip:
        offscreenright
        linear 1 right

    ck "Dammi una mano a caricare anche lui."

    show larry directevil:
        parallel:
            ease 1 zoom 1.5
        parallel:
            ease 1 yalign 0.2

    sgherro "IIIIIIH State lontani pazzoidi!"

    show black with Dissolve(0.5)

    play sound ["audio/sfx/furu.ogg","audio/sfx/down.ogg"]
    pause 3

    scene car
    show embers
    show larry directevil yep at right
    show check direct plain at left
    show check smile fp at flip
    show car_fire_overlay
    with Dissolve(0.5)

    ck "Ecco il quanto, attaccheremo i circuiti al contachilometri, e tu inizierai a guidare."

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

    ck "Se scende sotto i 15 Km/h per troppo tempo... BOOM."
    ck "Se il motore si spegne... BOOM."
    ck "Se finisce la benzina e la macchina si spegne da sola, hai vinto."
    la "Ovviamente non è solo la tua vita che è in gioco. {w}Il tuo compagno è legato nel sedile di dietro."
    sgherroImb "MHHHH MMHHHHHHH MMMMMMMMMMMMMMMHHHHHHHHHHHHM!"
    la "Lo senti? Ti sta augurando buona fortuna."

    sgherro "IIIIIIIIIH!!! {w}ABBIATE PIETÀ!!!"

    ck "Sei ancora in tempo per parlare."
    sgherro "Volete sapere chi siamo e da dove operiamo? Ve lo dico io! Perciò calma con quegli esplosivi!"
#     sgherro "Siamo i {color=#ffe674}________ ____{/color}... abbiamo circa 90 uomini stanziati a Hinamizawa{w} La nostra base operativa è {color=#ffe674}___ __________ _____ _______ ____{/color}!"
#     sgherro "Il maggiore... Non so da dove viene esattamente o perchè è stato assegnato a questa operazione, ma so che è un veterano di guerra."


    show check -direct nope
    show larry evil nope
    with Fade(2,1,2)

    ck "Avevo i miei sospetti. Era l'unico posto adatto ad un operazione del genere!"
    la "Chi lo avrebbe mai detto che si nascondevano ad Hinamizawa fin dall'inizio...."
    ck "Bene Larry, abbiamo un luogo da investigare.{w} Ci servirebbe soltanto un modo per depistare chi ci sta cercando."
#     ck "Un modo per, ad esempio, fargli pensare che siamo scappati con questa automobile...."

    show check smile direct
    show larry smile directevil
    with dissolve
#     sgherro "Oh no..."
    ck "Larry, puoi attaccare il plastico."
    la "Signorsi signore."

    show larry:
        ease 1 yoffset 600
    pause 1

    sgherro "ASPETTA QUESTO È UN CRIMINE DI GUERRA!!!!{w} È contro la convenzione di Ginevra!!!!"
    ck "Il suggerimento di Ginevra vorrai dire!"
    sgherro "SIETE DEI MOSTRI!!!!"
    show check yep
    ck "Mostri? "
    show larry:
        ease 1 yoffset 0
    pause 1
    show check smile
    extend "No... DEMONI!"

    la "Tutto pronto capo, il timer sarà attivo tra 30 secondi."
    ck "Premi il pedale amico. Buona fortuna!"
    window hide
    stop custom_audio fadeout 4
    play sound "audio/sfx/speeding car.mp3" volume 1.5
    pause 2.5

    scene rural_road with fade
    sgherro "AAAAAAAAAAAAAAAAAAAAAAAAAaaaaaaaaaahhhhhhhhhhhhhhhhhhh!!!!!!!"
    pause 1
    show larry direct yep at right
    show check plain at left
    show check yep direct fp at flip
    with dissolve


    ck "Una performance degna di un oscar ragazzo mio."

    la "Tutto merito del piano capo! È bastato simulare il suono di un'esplosione e dare fuoco al nascondiglio per farli correre allo scoperto."

    show check smile
    show larry smile
    ck "Le trasmittenti in dotazione al BKG saranno anche impermiabili ed ignifughe, ma non sono a prova di martello! Hahahahaha!"

    show larry yep
    la "Dopo quanto pensa che si accorgeranno che non c'è nessun esplosivo nella macchina?"

    show check yep
    ck "Abbastanza a lungo da depistarli..."


    show check calling
    ck "E ora che abbiamo le radio di quei due, le posizioni sono ribaltate.{w} Adesso siamo noi a sentire tutto quello che dicono."




#     play music "audio/higu/insanity.mp3"

    scene koya_fire with fade

    sgherro3 "Maggiore, stanno fuggendo, abbiamo avvistato la loro vettura allontanarsi e la strada è sbarrata."


    hb_anon "Razza di incompetenti..."


    play sound "audio/sfx/codec call.mp3"

    $ renpy.pause(3, hard=True)

    hb_anon "Capitano, voglio immediatamente una squadra a inseguire quell'auto. {w}Vanno fermati a tutti i costi."

    oko_anon "...... {w}Ricevuto..."

    hb_anon "Dovete anche circondare il perimetro della montagna."

    oko_anon "Cosa?! Perchè?"

    hb_anon "Non è detto che siano scappati, potrebbe essere un'esca.{w} Travestitevi da forestali, pompieri o quello che volete ma fate in modo che non vi passino sotto il naso."

    oko_anon "Maggiore! La deve smettere di fare di testa propria! {w}Abbiamo problemi più importanti di due fuggitivi adesso!"

    oko_anon "Non ho più uomini da assegnarle come scorta!"

    hb "Bah! Meglio così, dei dilettanti come voi mi rallenterebbero e basta."

    scene forest_path_open with fade

    play music "audio/higu/fearlessness.mp3"
    show check calling at left
    show larry direct yep at right

    ck "Pare che la nostra esca abbia funzionato.{w} Tra quella e l'emergenza incendio non hanno quasi più uomini a disposizione."

    la "Vuol dire che il quartier generale è quasi sguarnito?"

    show check fp at flip
    ck "Esatto, non avremo mai più un'occasione come questa."

    show larry nope

    la "Ma capo, anche se ci hanno detto il luogo non sappiamo come entrare."

    ck "Sappiamo il loro punto debole, una persona che conosce tutti i loro segreti."

    show check sus
    ck "Ci farà il \"GENTILE FAVORE\" di aprirci, e servirà anche come ostaggio se ne avremo bisogno."

    show larry yep
    la "Ma certo! Bella pensata capo!"

    show check plain
    show check -sus

    ck "Una volta che saremo entrati nel villaggio non potranno fare mosse avventate, anche la loro è un'operazione sotto copertura."

    show check nope
    show larry nope
    ck "Ma non abbassare la guardia, pare che uno dei loro leader sia ancora sulle nostre tracce. {w}Faremo il giro dall'altro versante passando per il bosco."

    show check angry
    ck "Muoviamoci. E SIA CHIARO, NON LASCIARE TRACCE."

    la "Chiaro."

    stop music fadeout 5

    scene forest_path_winding_sunset with longFade

    play music "audio/sfx/cicadas.ogg" fadein 2
    play sound "audio/sfx/bushes1.mp3"

#     $ renpy.pause(4, hard=True)

    show check plain nope:
        offscreenright
        ease 2 right


    $ renpy.pause(1, hard=True)

    ck "La strada è libera. Possiamo procedere."

    play sound "audio/sfx/bushes1.mp3"

    show larry worried:
        left
        flip
        yoffset 900
        pause 0.5
        ease 2.5 yoffset 0

    $ renpy.pause(3.5, hard=True)




    ck "Ascoltami bene Larry, appena il sole sarà tramontato scenderò da questo versante e metterò in atto il piano. {w}Voglio che tu ti nasconda, e cerchi un occasione per scappare dal lato opposto mentre saranno concentrati su di me."
    play music "audio/higu/silence.mp3" fadein 3
    show larry direct
    la "Ma capo... dev'esserci qualcosa che anche io posso fare."

    la "Lo so. Sono stato solo un peso in questa missione. {w}Ma almeno adesso.{w} Almeno stavolta."

    ck "Il tuo ruolo è cruciale. {w}Nel caso qualcosa andasse storto serve che almeno uno di noi riesca a portare fuori le informazioni che abbiamo."

    ck "Ci sono! Inventati qualcosa per allertare la polizia, metterà ancora più alle strette i nostri avversari."

    la "Ma in quel caso sarebbe troppo tardi."

    show check think
    ck "Senti, non posso metterti in pericolo più di quanto non ho già fatto."

    show check fp at flip
    ck "Questi sono ordini, non seguirmi."

    la "Nnnnnnnnhhhhhhhh.........."

    show larry scared nope
    la "...............Capo..."


    ck "Larry, ho detto di no..."

    show check p -think at unflip
    ck "Non mi convincerai a...{w} Larry?"
    stop music fadeout 3
    show larry hide_arm b1 with Dissolve(2)

    show check angry shout
    show larry worried

    ck "La tua spalla!"
    play music "audio/higu/moon.mp3"

    show check shoutest
    ck "PRESTO AL RIPARO! SIAMO SOTTO TIRO"

    scene woods_sunset with PushMove(0.5, "pushleft")
    show check plain angry shout fp:
        flip
        offscreenleft
        parallel:
            ease 1 right
        parallel:
            pause 0.4
            ease 0.6 yoffset 350


    $ renpy.pause(1, hard=True)
    show check p at unflip
    n "Non ho sentito lo sparo... un silenziatore?"
    n "No! Nessuno era nelle vicinanze. Puo essere solo un cecchino!"

    ck "DA QUESTA PARTE! STA GIÙ E NON DARGLI VISUALE!!!"



    scene forest_path_winding_sunset
    show larry hide_arm scared worried b1 at left, flip

    with PushMove(0.5, "pushright")

    la "AAaaAaAAaaaaAAa!"

#     $ renpy.transition(Dissolve(1), layer="master")
    show larry:
        ease 1 offscreenright
    $ renpy.pause(0.7, hard=True)
    play sound ["audio/sfx/furu.ogg"]
    show rocky_wall_sunset behind larry with PushMove(0.5, "pushleft")
    play sound ["<silence 0.2>","audio/sfx/down.ogg"]
    show larry b2:
        offscreenleft
        parallel:
            ease 0.5 center
        parallel:
            pause 0.2
            linear 0.3 yoffset 100

    $ renpy.pause(0.5, hard=True)

    show larry close worried tilt
    $ renpy.pause(1, hard=True)
    la "Aaah... Aaah... Aaah..."

    scene woods_sunset with PushMove(0.5, "pushleft")
    show check plain angry shout:
        right
        yoffset 350

    ck "LARRY!"

    ck "DANNAZZIONE! Siamo in una FOTTUTA foresta! Come fa a prenderci di mira."

    show check sus
    play sound "audio/sfx/codec call.mp3"
    $ renpy.pause(3, hard=True)

    show check angry calling with dissolve
    hb_anon "Non muovere un muscolo.{w} Ho il ragazzo sotto tiro."



    scene rocky_wall_sunset
    show larry b1 b2 close worried tilt at center:
        yoffset 100
    show scope onlayer overlayer
    camera:
        zoom 0.7
        yalign 0.5
        xalign 0.8
    with Dissolve(2)

    camera:
        linear 3 xalign 0.2
        ease 1 zoom 1
        parallel:
            linear 2 yalign 0.3
        parallel:
            linear 2 xalign 0.5

    hb_anon "Se fai mosse sospette o provi a scappare, il prossimo colpo sarà in mezzo alla fronte."

    ck "Bastardo! Stai colpendo apposta i punti non letali!"

    hb_anon "Bingo, risposta esatta."

    hide scope
    scene woods_sunset
    show check angry shout calling:
        right
        yoffset 350

    with dissolve
    ck "Chi sei?! Sei tu Lambdadelta?!"

    hb_anon "Sai già il mio nome. Check."



    ck "Quella voce... e questa abilità col fucile... {w}No! non puoi essere lui!"

    hb "Bingo di nuovo."

    ck "Ma mi hanno detto che tu eri morto..."

    hb "Era una storia conveniente per il tipo di missioni di cui mi occupo."

    hb "Questo lavoro invece era un po'diverso... {w}Mi hanno scelto specificamente per tenere te sotto controllo."

    hb "E ora che sei uscito fuori controllo, non ti posso più permettere di scappare."

    scene rocky_wall_sunset
    show larry b1 b2 close worried tilt at center:
        yoffset 100
    show scope onlayer overlayer
    camera:
        zoom 1
        yalign 0.6
        xalign 0.5

    with Dissolve(2)

    camera:
        ease 1 zoom 1.5
        parallel:
            linear 2 xalign 0.25
        parallel:
            linear 2 yalign 1.05


    $ renpy.pause(4, hard=True)



    la "AAAAAAAHH!!"
    play sound "audio/sfx/chishibuki.ogg"
    show larry b3 with Dissolve(2)

    $ renpy.pause(1, hard=True)

    camera:
        zoom 1
        yalign 0.5
        xalign 0.5
    hide scope
    scene woods_sunset
    with dissolve
    show check plain angry shout:
        right
        yoffset 350

    hb "La tua vita per la sua."



    n "................"

    ck "Mi devi promettere di risparmiarlo."

    hb "Senza te non ho motivo di uccidere quell'incapace."
    stop music fadeout 3

    show check:
        linear 1 yoffset 0
    n "........................................"

    play music "audio/higu/requiem for the disaster.mp3" fadein 3

    show check:
        pause 2
        linear 4 offscreenleft

    $ renpy.pause(6, hard=True)

    scene rocky_wall_sunset
    show larry b1 b2 b3 close worried tilt at center:
        yoffset 200

    with PushMove(0.5, "pushright")

    show check plain angry shout:
        offscreenright
        ease 3 center
    $ renpy.pause(4, hard=True)

    ck "Molto bene. Accetto la proposta. {w}Dovrai passare sul mio cadavere!"


    show larry cry:
        ease 2 right


    la "Capo...."

    show scope onlayer overlayer with Dissolve(3)
    camera:
        xalign 0.4
        parallel:
            linear 2 zoom 1.7
        parallel:
            ease 2 yalign -0.2



    $ renpy.pause(3, hard=True)


    hb "Un vero idiota fino alla fine......"

    play sound "audio/sfx/BANG.ogg"
    camera:
        zoom 1
        yalign 0.5
        xalign 0.5
    hide scope
    show black

    pause 5


    scene mountain_sunset

    show hnb nope napalm_right at flip:
        xalign 0.7
    with Dissolve(5)

    play sound "audio/sfx/codec call.mp3"
    $ renpy.pause(3, hard=True)

    hb "È finita capitano."

    hb "Recuperate il corpo di Check."

    oko_anon ".... Roger.{w} Cosa dobbiamo fare con l'assistente?"

    hb "Fate come volete, non è più un mio problema."

    hb "Il mio ruolo in questa operazione si è esaurito, mi ricongiungerò a Tokyo già a partire da domani."

    oko_anon "Sissignore."

    pause 2

    show hnb cigar with Dissolve(2)

    hb "Niente di tutto ciò era era nei piani."

    hb "Se solo te ne fossi stato al tuo posto non sarebbe successo... {p}Sia ora che allora."

    stop music fadeout 13
    show black with Fade(10,2,5)
    jump gk34

    return