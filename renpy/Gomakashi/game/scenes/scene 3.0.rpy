label scene3_0:
    call hide_menu
    stop music fadeout 4

    play music("audio/sfx/cicadas.ogg")

    scene koya with longFade
    scene torakku with Dissolve(5)
    play music("audio/higu/lies lies.mp3")
    show larry evil at left
    show check at right
    show larry direct at flip

    ""
    window hide dissolve
    show larry:
        ease 1 center
    show check:
        ease 1 offscreenright

    "start"
    ""
    show larry evil
    ""
    show larry directevil
    ""
    show larry hide_arm tilt with dissolve
    ""
    show larry evil
    ""
    show larry direct

    "------------Crazy larry-------------"
    play music "audio/higu/forfeit.mp3"

    "Ho trovato l'ospedale dove è ricoverato capelli chiari. Dobbiamo interrogarlo su cosa è successo."

    la "Non muova un muscolo capo!"

    la "Ho fatto qualche modifica all'attrezzatura, con questo telecomando posso causare un cortocircuito abbastanza potente da far saltare in aria la baracca. Questa stanza esploderà al mio segnale."

    ck "Idiota, non vedi che così morirai anche tu?"

    la "NON TESTARE LA MIA PAZIENZA!"

    "-instant flashback to larry being crazy in watanagashi, it only lasts a moment-"

    la "Da quando va avanti il complotto?"

    la "Non mi puo fregare adesso. Era evidente che foste in combutta."

    la "D'altronde tutto il villaggio sapeva che quei quattro erano entrati nel magazzino... E gli unici testimoni erano loro, io e lei."

    la "Ha continuato ha commettere atrocità sotto il mio naso"

    "LARRY ASPETTA"

    la "Ma io credo ancora in lei capo... il capo che conosco non farebbe mai una cosa simile anche lei è una vittima vero? Si siamo tutti vittime... io, lei, Mion e i Sonozaki, Lambdadelta e il BKG..."

    ck "Di cosa DIAMINE stai parlando!"

    la "È LA MALEDIZIONE DI OYASHIRO-SAMA."

    la "LUI PRENDE IL CONTROLLO DELLE PERSONE E LE TRASFORMA IN DEMONI SPIETATI."

    la "E DOPO CHE HANNO DISTRUTTO CON LE LORO MANI CIò A CUI TENGONO DI PIù, LE PORTA A UNA MORTE VIOLENTA E SADICA."

    la "Ma non si preoccupi, sono quì per liberarci dal suo controllo."



label sc302:

    "------------The flashback-------------"

    "bg soffitto"
    la "Un soffitto sconosciuto"

    show larry at right
    show check at left
    show check at flip
    la "O cazzo c'è il capo"

    ck "Se non ti fidi di me perchè non parli con lei?"

    "Terry?!"

    te "Chi altri"

    show larry with longFade

    ck "Allora, adesso mi credi?"

    la "Ma allora... da cosa stavo scappando?"

    te "Pensi davvero che riusciresti ad attraversare un intero versante della montagna con Check alle calcagna senza essere preso?"

    "look at check"

    la "Effettivamente..."

    la "Ma una cospirazione per usurpare il controllo del BKG. Chi può aver fatto una cosa del genere e perchè?"

    ck "Questo \"Lambdadelta\" non può sicuramente aver fatto tutto di sua iniziativa. Ci dev'essere qualcuno dall'alto lo sponsorizza."

    "Momento kojima cutscene"

    ck "Il BKG è una cellula antiterroristica paramilitare che gode di una certa autonomia, ma non si sostiene certamente da solo."

    ck "Il Giappone non ha più avuto un esercito dalla seconda guerra mondiale, ma quanto a servizi segreti non scherza. {w}Come pensi che un giapponese come me si sia ritrovato a combattere per tutta l'asia e il medio oriente?"

    ck "Dopo che mi sono distinto come militare all'estero mi è stata data l'occasione di creare la mia organizzazione. {w}Sinceramente non ne potevo più di vedere compagni morire combattendo sul campo di battaglia per cause in cui non credevano."

    ck "L'unico rimpianto che ho è non essere stato al fianco del mio compagno più fidato nei suoi ultimi momenti. {w}È morto durante una missione in Afghanistan poco dopo la mia dipartita."

    ck "Questa mia filosofia ha senza dubbio reso il BKG una pedina scomoda da muovere, e questa volta una qualche fazione deve aver deciso che la mia presenza era più un contro che un pro."

    "back to hideout"

    ck "Per questo motivo non basterà tornare a casa base e spiegare la situazione per liberarci dell'impostore."

    te "Ecco perchè dobbiamo cogliere questa occasione."

    te "Come spiegavo a Check, il BKG al momento è in uno stato caotico. {w}Abbiamo perso ogni contatto con il nuovo comandante, e l'organizzazione è divisa sul da farsi."

    te "La mia teoria è che sia successo un imprevisto che nessuno si aspettava, neanche i nostri avversari."

    te "In mezzo a a questo scompiglio, chi di noi credeva ancora in Check ha formato una fazione autonoma. {w}Il nostro obiettivo è scoprire cosa è successo davvero dietro le quinte e ri-leggittimare il BKG."

    te "Non siete soli Larry. Avete ancora degli alleati."




    n "C'è un pensiero fastidioso da qualche parte nei meandri del mio cervello che cerca di venire a galla contro la mia volontà."

    n "\"Che prove hai che stanno dicendo la verità?\" ... mi sussurra."

    n "\"È così che suonava la voce di Terry?\" ... \"Quando è l'ultima volta che l'hai sentita?\" ... \"Riusciresti a sopportare un altro inganno?\""



    n "Respingo quel presentimento in fondo alla palude da cui è uscito. {w}Ho sbagliato, niente di nuovo..."

    show larry cry
    n "Eppure non sono mai stato così sollevato di essere in errore."

    ck "Hey Larry che ti è preso?"

    la "Sono veramente inutile... non ne combino mai una giusta. {w}Anche in una crisi come questa non sono stato altro che un ostacolo per voi."

    ck "Quel tuo fraintendimento ci tornerà estremamente utile."

    ck "Vedi, mi hai dato un ottima idea per far perdere le nostre tracce e confondere il nemico allo stesso tempo. Andrà più o meno così..."


label sc303:
    "------------The escape-------------"

    play sound "audio/sfx/BANG.ogg"
    pause 1

    play sound "audio/sfx/office.mp3" fadein 6 volume 0.8 loop
    scene monitor_room with longFade

    # BGM options: silver mirror
    play music "audio/higu/silver mirror.mp3" fadein 2






    "L'ultimo suono a uscire dall'altoparlante fu il botto di un esplosione, mentre due messaggi di errore a schermo notificavano tutti i presenti dell'improvvisa perdita di segnale, sia del canale audio, sia della geolocalizzazione."

    "Nello sgomento generale dei presenti, una sola figura rimase ferma davanti al suo monitor."
    "Comandante, cosa facciamo adesso?"

    "back to the hideout"

    ck "Una performance degna di un oscar ragazzo mio. Ora basterà dare fuoco al nascondiglio."

    la "Il merito è suo per aver concepito questo piano."

    la "Le trasmittenti in dotazione al BKG saranno anche impermeabili e ignifughe, peccato che non siano anche a prova di martello. Ahahahahaha!"

    la "Vorrei vedere le loro facce in questo momento! {w}Chiunque ci darebbe per morti dopo questa messinscena."

    ck "Quello sarebbe l'ideale, ma non ci contare.{w} Anche loro sono professionisti, tra non molto verranno quì a indagare."

    ck "Ricorda che il vero obiettivo di questa operazione è confonderli abbastanza da guadagnare il tempo per nasconderci e unire le forze con la fazione di Terry."

    ck "...O almeno è quello che penseranno..."

    ck "Se davvero il nuovo comandante si trova a Hinamizawa, questa è l'occasione perfetta per scoprire la sua identità. Mi aspetto che abbia con se una piccola cellula (check sa che i mountain dogs have no actual combat training?), sarà senza dubbio il suo gruppo a investigare. E io sarò"


label sc304:
    "------------Hanabi reveal-------------"

    ck "Oshit pensavo che eri morto fra"

    hb "I'm a ghost and I'm back to haunt you"

    "------------Kojima moment-------------"

    hb "Si signore. Quì Hanabi... {w}anzi... quì Lambdadelta."

    hb "Check è stato neutralizzato insieme al suo assistente."

    hb "No signore, non abbiamo tracce degli altri disertori del BKG. {w}La trasmittente di Check è andata distrutta e il loro hacker ha rimosso dai server ogni traccia delle loro comunicazioni."

    hb "..... Si signore farò rapporto a TOKYO tempestivamente.."

    hb ".... Ricevuto."

    show black with longFade
    jump mid_start

    return