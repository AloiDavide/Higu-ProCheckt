label scene3_0:
    call hide_menu
    stop music fadeout 4

    scene torakku with longFade
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





    "------------The flashback-------------"

    ck "Quel tuo fraintendimento ci tornerà estremamente utile."

    ck "Vedi, mi hai dato un ottima idea per far perdere le nostre tracce e confondere il nemico allo stesso tempo. Andrà più o meno così..."

    "------------The escape-------------"

    "BANG"
    "Video room"

    "burstling call center ambience"
    # BGM optiond: silver mirror,

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


    "------------Hanabi reveal-------------"

    ck "Oshit pensavo che eri morto fra"

    "------------Kojima moment-------------"

    hb "Si signore. Quì Hanabi... {w}anzi... quì Lambdadelta."

    hb "Check è stato neutralizzato insieme al suo assistente disertore."

    hb "No signore, non abbiamo tracce degli altri disertori del BKG. {w}La trasmittente di Check è andata distrutta e il loro hacker ha rimosso ogni traccia delle loro comunicazioni dai nostri server."

    hb "..... Si signore."

    hb ".... Ricevuto, farò rapporto a TOKYO tempestivamente."

    jump mid_start

    return