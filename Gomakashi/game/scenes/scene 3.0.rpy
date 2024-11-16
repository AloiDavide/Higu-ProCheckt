label scene3_0:
    call hide_menu
    stop music fadeout 4

    play music("audio/sfx/cicadas.ogg") fadein 4

    "------------sc300 Crazy larry-------------"
    scene koya with longFade
    pause 2
    stop music fadeout 8
    scene torakku with Dissolve(5)

    show check plain at right


    play music "audio/higu/forfeit.mp3"

    ck "Trovato! Ecco l'ospedale dove è ricoverato capelli chiari! Dobbiamo interrogarlo su cosa è successo."

    show larry hide_arm worried direct at flip
    show larry directevil at left
    show check angry shout
    la "Non muova un muscolo capo! {w}Anzi... TRADITORE!"

    ck "LARRY!? QUESTO NON È IL MOMENTO PER GLI SCHERZI!"


    la "Pensa ancora di potermi ingannare in questo modo?"

    ck "Brutto dannato... non mi lasci scelta!"

    window hide
    show larry -worried transmitter with dissolve
    pause 1
    la "Non lo farei se fossi in lei."

    la "Ho fatto qualche modifica all'attrezzatura a sua insaputa, alla pressione di questo bottone posso causare un cortocircuito abbastanza potente da far saltare in aria questa baracca."

    ck "Sapevo che eri un idiota, ma questa volta l'hai fatta grossa. {w}Ti aspetti che ti creda? Non vedi che così morirai anche tu?"

    play sound "audio/sfx/wake up.ogg" volume 1.5
    show larry nope
    camera at sshake
    la "NON TESTARE LA MIA PAZIENZA!"


    la "Non mi frega più ormai. Era evidente che foste in combutta dall'inizio. {w}Sentiamo, da quando va avanti il complotto?"

    show larry evil  tilt
    la "D'altronde tutto il villaggio sapeva che quei quattro erano entrati nel magazzino... E gli unici testimoni erano loro, io e lei."

    la "Ha continuato ha commettere atrocità sotto il mio naso pensando che fossi troppo stupido per rendermene conto."

    ck "Larry, posa quell'affare e datti una calmata."

    show larry yep close -tilt
    la "Ma io credo ancora in lei capo... il capo che conosco non farebbe mai una cosa simile."

    la "Anche lei è una vittima vero? {w}Si siamo tutti vittime... io, lei, Mion e i Sonozaki, Lambdadelta e il BKG..."

    ck "Di cosa DIAMINE stai parlando!"

    show larry directevil nope
    la "È la maledizione di Oyashiro-sama."

    la "Lui prende il controllo delle persone e le trasforma in demoni spietati."

    la "Ti spinge a distruggere con le tue mani tutto ciò a cui tieni di più, e poi ti porta a una morte violenta."

    show larry worried close
    la "Ma non si preoccupi, sono quì per liberarci dal suo controllo."

    la "Possiamo farla finita quì ed evitare ulteriori tragedie. Questa è la nostra unica salvezza."

    ck "VIA LE MANI DA QUEL PULSANTE!"

    la "Se c'è un prossimo mondo mi ringrazierà."

    show check:
        easeout 0.8 xalign 0.3
    ck "ASPETTA LARRY!...{nw}"


    play sound "audio/sfx/BANG.ogg"


    scene black with Dissolve(0.5)
    stop music fadeout 10

    pause 5

label sc301:
    call hide_menu

    scene tenjou with Dissolve(5)

    "------------sc301 The flashback-------------"
    play music "audio/higu/silence.mp3" fadein 3
    n "Un soffitto sconosciuto..."

    n "Sono spaesato... L'ultima cosa che ricordo è che stavo scappando. E poi mi sono gettato in quel fiume..."

    n "Come ho fatto a sopravvivere?"

    la "Dove sono...?"

    ck "Larry, sei sveglio? {w}Resta sdraiato, non sei messo granchè."

    show check direct yep plain with Dissolve(2)
    pause 1
    ck "Sei stato fortunato sai? Quando ti ho trovato eri già praticamente a valle. {w}Se la corrente non ti avesse spinto a riva saresti morto schiantato contro qualche roccia ancora prima di affogare."

    ck "Davvero, è un miracolo che tu non abbia neanche un osso rotto."

    la "Capo? Ma perchè..."

    show check direct calling
    ck "Perchè non ti ho fatto fuori come diceva Lambdadelta?"

    n "La trasmittente! Ho fallito, ha scoperto di Lambdadelta!"

    n "Ho dolori in tutto il corpo... come faccio a scappare in questo stato?"

    show check plain
    ck "Ho non poche domande da farti, ma forse prima è meglio che parli con lei."

    n "Check mi posa la trasmittente accanto alla testa... con chi vuole farmi parlare? Che sia la persona dietro tutto?"

    te "Buongiorno principessa."

    la "Terry?!"

    te "In persona."
    stop music fadeout 5

    scene torakku
    show check plain at left
    show check fp at flip
    show larry direct nope at right
    with longFade

#     play music "audio/higu/shadow.mp3"

    ck "Allora, adesso mi credi?"

    la "Ma i passi che ho sentito... da cosa stavo scappando?"

    te "Pensi davvero che riusciresti ad attraversare un intero versante con Check alle calcagna senza essere preso?"

    show larry -direct worried drop

    la "Effettivamente..."

    show larry -drop nope
    la "Ma una cospirazione per usurpare il BKG? Chi sarebbe in grado di prendere il controllo così semplicemente?"

    show check nope
    ck "Qualcuno con capacità fuori dal comune, e un potente sponsor ai piani alti."

    la "Piani alti? Vuole dire il governo?"

    ck "Non esattamente..."

    ck "Come ben sai, il BKG è una cellula antiterroristica paramilitare che gode di una certa autonomia, ma non si sostiene certamente da solo."

    "Momento kojima cutscene"
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
    te "Le possibilità che ci restano sono poche, ma non completamente assenti, specialmente se agiamo ora."

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



    n "C'è un pensiero fastidioso nei meandri della mia testa che cerca di venire a galla contro la mia volontà."

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
    show larry -tilt

    n "Respingo quel presentimento in fondo alla palude da cui è uscito. Ho sbagliato, niente di nuovo... Ma in confronto alle altre volte.{w}{nw}"

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

    te "Non è solo colpa tua, tutti noi all'inizio abbiamo dubitato. {w}Io ho perfino aiutato a convincerti di non fidarti di Check."

    te "Comandante, Larry. A nome di quel che resta del BKG, ci scusiamo profondamente."

    show check smile -angry

    ck "Ecchediamine, non pensavo di essere un superiore così antipatico. Ehehahaha."

    show larry direct

    ck "Larry, sappi che quel tuo fraintendimento ci tornerà estremamente utile."

    ck "Vedi, mi hai dato un ottima idea per far perdere le nostre tracce e confondere il nemico allo stesso tempo."

    ck "Ecco il piano....."

    scene black with Dissolve(5)
    stop music fadeout 5


label sc302:
    call hide_menu
    "------------sc302 The stakeout-------------"

    play sound "audio/sfx/BANG.ogg"
    pause 1

    play sound "audio/sfx/office.mp3" fadein 6 volume 0.8 loop
    scene monitor_room with Dissolve(5)

    # BGM options: silver mirror
    play music "audio/higu/silver mirror.mp3" fadein 2






    n "L'ultimo suono a uscire dall'altoparlante fu il botto di un esplosione, seguito da due messaggi di errore a schermo."

    n "{b}Errore canale audio:{/b} Segnale interrotto."

    n "{b}Errore Geolocalizazione:{/b} Segnale interrotto."

    anon "Assurdo."

    anon "Avete visto?"

    anon "Si è davvero fatto esplodere."

    anon "E ora?"

    n "Nello sgomento generale, una sola figura rimase ferma davanti al suo monitor."

    oko_anon "Maggiore, io e i miei uomini andiamo a verificare lo stato del luogo dell'esplosione."

    hb_anon "No, tu resta qua."

    n "Rispose senza distogliere gli occhi dai caratteri rossi a schermo."

    oko_anon "Signore, ci dobbiamo assicurare che non scoppi un incendio, sarebbe un incubo da infangare dopo."

    hb_anon "Non ti muovere da questa stanza.... "

    play music "audio/higu/gallery of madness.mp3" volume 1.5
    play sound "audio/sfx/zbiin.ogg"

    extend "Andrò io."

    n "Lo sguardo del maggiore in quel momento ammutolì tutti i presenti."

    n "Non uno di loro osò controbattere. Istintivamente sapevano che la sua calma apparente era come quella di una bomba che conta i secondi all'esplosione."

    stop music fadeout 10

    scene torakku with longFade
    show check plain at left
    show check fp yep at flip
    show larry direct yep at right

    play music "audio/higu/dancers5.mp3" volume 1.5

    ck "Una performance degna di un oscar ragazzo mio. {w}Ora non resta che dare fuoco al nascondiglio per aggiungere credibilità alla storia."

    la "Il merito è suo per avere ideato il piano."

    show larry smile
    la "Le trasmittenti in dotazione al BKG saranno anche impermeabili e ignifughe, peccato che non sono anche a prova di martello!"

    show check smile
    ck "Che dire, ora sappiamo cosa migliorare per il prossimo prototipo."

    la "Vorrei vedere le loro facce in questo momento! {w}Non solo non possono più tracciare i nostri movimenti e origliare le conversazioni, ma adesso ci daranno sicuramente per morti."

    show check yep
    show larry nope
    ck "Quello sarebbe l'ideale, ma non ci scommetterei.{w} Anche loro sono professionisti, tra non molto verranno quì a indagare e capiranno che qualcosa non va quando non troveranno i nostri corpi."

    ck "Il vero obiettivo di questa operazione è guadagnare abbastanza tempo per far perdere le nostre tracce e unire le forze con la fazione di Terry."

    show check smile
    show larry yep
    ck "...O almeno è quello che penseranno."

    ck "Se davvero Lambdadelta si trova a Hinamizawa, non avremo mai un'occasione migliore per scoprire la sua identità. {w}Per essere stanziati sotto copertura in questo villaggio la sua scorta non può essere poi così grande."

    scene koya
    "Check si apposta vicino per spioneggiare."



label sc303:
    call hide_menu

    "------------sc303 Hanabi reveal-------------"
    "------------sc303 Hanabi reveal-------------"

    "Hanabi ha previsto tutto e lo trova."

    ck "Pensavo che eri morto fra"

    hb "I'm a ghost and I'm back to haunt you"

    "Shooty shooty shoot"

    "------------Kojima moment-------------"

    hb "Si signore. Quì Hanabi... {w}anzi... quì Lambdadelta."

    hb "Check è stato neutralizzato insieme al suo assistente."

    hb "No signore, non abbiamo tracce degli altri disertori del BKG. {w}La trasmittente di Check è andata distrutta e il loro hacker ha rimosso dai server ogni traccia delle loro comunicazioni."

    hb "..... Si signore farò rapporto a TOKYO tempestivamente.."

    hb ".... Ricevuto."

    show black with longFade
    jump mid_start

    return