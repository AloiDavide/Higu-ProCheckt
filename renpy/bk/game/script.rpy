
define bk = Character("???", color="#0000cf")
define c = Character("Check", color="4e1212")
image bg1 = im.Scale("bg1.png", 1920, 1080)
image bg1 = im.Scale("bg1.png", 1920, 1080)
image bg2 = im.Scale("bg2.png", 1920, 1080)
image bg3 = im.Scale("bg3.webp", 1920, 1080)
image bg4 = im.Scale("bg4.png", 1920, 1080)
image tatarifrag = im.Scale("tatari fragment.webp", 1920, 1080)
image tatari = im.Scale("tatari.png", 1920, 1080)

image dis = "disembodied.png"




label start:

    scene bg1

    play music "audio/beat.mp3"

    pause 0



    "La prima volta eri sconcertato, {w} la seconda eri spaesato,{w} ma gia alla terza questo vuoto comincia a sembrarti confortante."

    "Un momento di quiete e tranquillità in mezzo alla follia…{w} Subito interrotto da una risata acuta e meno che dignitosa. "

    play sound "audio/laugh.mp3"
    bk "Ahahahahaahahah. {p}Il tuo aspetto. {w} Troppo ridicolo hehehehahaa."

    bk "Ahem"

    pause .7

    "Una volta calmatasi, la voce femminile si aggiusta su un tono più grave e nobile."

    bk """
    Pardon. Scusa la mia reazione fuori luogo, ma attendevo da tempo di vedere come tu fossi fatto.

    Sembra che dovrai abituarti ancora un po’ a questo piano prima di poter materializzare una forma fisica completa.{w} Pff.

    Ma è comico in vero. É così forte il tuo desiderio di sapere di più che pur non essendo capace di manifestare un corpo intero,{w} per prima cosa hai creato una bocca per domandare e delle orecchie per decifrare ogni risposta.
    """


    show dis:
        xalign 0.5
        yalign 0.5

    "In quel momento ti rendi conto che il tuo udito e la tua voce sono funzionanti."

    "Ti rendi conto anche del fatto che in questo momento sei una bocca e delle orecchie incorporee.{w} Questo spiega la reazione della donna."

    "Incidentalmente non hai ancora gli occhi, non sei quindi in grado di vedere il tuo interlocutore nè lo spazio circostante, ma le costellazioni di gemme che lei chiama frammenti adornano il tuo “campo visivo” ciò nonostante."

    hide dis

    show dis

    menu:
        "Macche diamine!":
            pass
        "Sono ANCORA PIÙ CONFUSO di prima!":
            pass
        "QUANDO RIVEDO LARRY LO LICENZIO!!!":
            bk "Placati, ciò che è successo non è interamente colpa del ragazzo.{w} É il fato che ti riporta inevitabilmente qui."

    hide dis

    bk "Capisco la tua confusione.{w} Stai pur certo, ciò che hai visto non è un altro mondo. Hai semplicemente potuto osservare l’unica e sola Hinamizawa da due prospettive diverse."

    scene bg2 with dissolve

    pause 1

    scene bg3 with dissolve

    pause 1

    scene bg4 with dissolve

    bk """
        Sii onorato, non è un’esperienza normalmente permessa ad un comune essere umano, limitato per tutta la vita ad uno degli infiniti frammenti di realtà.

        E nonostante questo privilegio vedo che una cosa resta uguale...{w} La tua mancanza di conoscenza è a dir poco sconcertante.

        Allora, sei stufo di annegare nella tua stessa frustrazione?{w} Stufo di conoscere così poco?{w} La tua sete di conoscenza è accesa?
    """

    show dis

    menu:
        "Sissignora.":
            call sissignora from _call_sissignora

        "Si però parlami con rispetto":
            bk "Sei 100 anni in anticipo per meritare la mia cortesia, giovanotto. Ora rispondi come si conviene."

            menu:
                "Sissignora.":
                    call sissignora from _call_sissignora_1

                "Non mi piace la tua attitudine.":
                    bk "Mhhh. proviamo in questo modo."

                    menu:
                        "Sissignora":
                            bk """
                                Come puoi vedere, usando i miei poteri sono in grado di controllare le tue risposte.

                                Però riconosco che infringere sul tuo libero arbitrio sarebbe contraddittorio alla proposta della quale voglio renderti partecipe.

                                Per cui...{w} come dire...{w} hai le mie scuse, per il momento.
                            """
                            call sissignora from _call_sissignora_2


        "Naah":
            bk "Uuuhm. Capito..."
            play sound "audio/boing.mp3"
            bk "Addio!"

            return

    pause 2

    bk "Allora, come ti senti dopo esser stato investito da cotanta saggezza?"

    show dis

    menu:
        "Grazie delle dritte, voce incorporea senza nome.":
            hide dis
            show dis:
                xalign 0.5
                yalign 0.5

            bk "Guarda un po' tu chi parla..."
            bk "Se per la prossima volta che farai ritorno qui avrai anche degli occhi, potrei pure decidere di mostrare a te la mia forma, lasciamo le presentazioni per allora."
            hide dis

        "Sinceramente... sono ancora confuso.":
            hide dis
            bk "Abbiamo stretto un patto, cerca di non deludermi.{w} Credevo che nessuna richiesta fosse troppo per il capo del BKG.{w} Mi sbaglio?"

    bk "Ordunque, qualunque sia il destino che ti attende è arrivato il momento di andargli in contro."

    hide dis

    play sound "audio/chimes.ogg"

    "Percepisci un frammento avvicinarsi alla tua posizione. Sembrerebbe simile agli altri, se non per il fatto che da esso fuoriesce un soverchiante senso di tristezza e rassegnazione."

    scene tatarifrag with dissolve

    bk """
        Che succede, non sarai forse intimorito.

        È arrivato il momento di mostrarti tra gli infiniti frammenti uno dei più ostici in assoluto.{w} Perfino io, tutt’ora, lo comprendo solo in parte.

        Dovrai essere estremamente perspicace per decifrarne il contenuto, ma è un passo necessario.
    """

    menu:
        "-Tocca il frammento-":
            pass

    bk "Va adesso piccola serpe nel pozzo, mettiti in gioco e lasciami scoprire,{w} se sarai solo un altro pedone{w}.{w}.{w}."

    stop music

    play sound "audio/zbiin.ogg"

    bk "O se sarai colui che fa girare la scacchiera."

    window hide

    play sound "audio/doon.mp3"

    show tatari with zoomin

    pause 15

    return



label sissignora:
    hide dis

    bk """
            Tu desideri sapere di più, io ho bisogno di alleati, i nostri interessi coincidono.{p}E sia, ti concederò di attingere ai miei secoli di esperienza.

            Tuttavia non posso semplicemente chiarire ogni tuo dubbio.{p}Un alleato incapace di ragionare da se è solo un peso.{w} Che ne diresti piuttosto di un gioco?{w} Perfetto per combattere la noia.

            Le regole sono le seguenti.
        """
    play sound "audio/truth.mp3"

    bk "Da adesso {i}{color=#0000cf}Tutto ciò che dirò in blu sarà una verità che trascende i frammenti.{/color}{/i}"

    bk """
            Tuttavia utilizzerò questo potere solo in risposta ai tuoi interrogativi, e solo se li riterrò degni di essere esauditi.{w} Sta a te formulare delle domande su quanto hai visto durante i tuoi viaggi.

            Inoltre,{w} hai diritto a {b}tre{/b} risposte prima del prossimo frammento.{w} Non di più, non di meno.

            Non sei felice?{w} Grazie a me potresti perfino confermare o confutare quei quesiti che la mancanza di informazioni ti ha portato ad abbandonare.

            Ebbene forza. Chiedi pure.
        """

    #creo una lista delle tre domande in modo da potervi accedere facilmente
    default domande = ["Quando capelli chiari ha rotto il mobile, c'era effettivamente qualcuno o qualcosa dietro di lui?",
                "Il \"demone\" da cui Mion dice di essere posseduta è reale?",
                "Sei tu Oyashiro-sama?"]

    #creo un dizionario che associa a ogni domanda il nome del blocco di codice da eseguire per la risposta
    default risposte = {
        domande[0] : 'keiichi_question',
        domande[1] : 'mion_question',
        domande[2] : 'oyashiro_question'
    }

    #fino a che c'è almeno una domanda in lista continua a mostrare le domande restanti e cancella dalla lista quella che viene scelta
    while len(domande) > 0:
        menu:
            "[domande[2]]" if len(domande) > 2:
                $ renpy.call(risposte[domande[2]])
                $ del domande[2]

            "[domande[1]]" if len(domande) > 1:
                $ renpy.call(risposte[domande[1]])
                $ del domande[1]

            "[domande[0]]":
                $ renpy.call(risposte[domande[0]])
                $ del domande[0]



    pause 2
    bk """Tre domande e tre incontrovertibili verità, queste erano le regole. Non dirmi che non sei soddisfatto.

            Però beh, devo dire che parlare con te non mi dispiace.

            Come premio per l'intrattenimento ti concedo un ultima domanda. Risponderò se mi sarà lieta.
            """
    menu:
        "Chi era il \"responsabile\" chiamato a casa di Keiichi da Mion e Rena?":
            pass
    bk "Non hai prestato attenzione? Lo hanno detto pure le ragazze{w}: il responsabile è il responsabile, come il regista di un film."

    play sound "audio/truth.mp3"
    bk "In ogni caso... {i}{color=#0000cf}Lo incontrerai presto.{/color}{/i} Questo te lo posso garantire."

    return




label oyashiro_question:
    bk "Sapevo che lo avresti chiesto, è una teoria più che lecita.{w} Quasi mi dispiace doverla frantumare."
    play sound "audio/truth.mp3"
    bk "{i}{color=#0000cf}Non rispondo a quel nome, nè sono mai stata chiamata con esso fino ad ora.{/color}{/i}"
    bk "Che peccato, la risposta più semplice non è necessariamente quella giusta."
    bk "Se avessi detto di si mi avresti incolpata per tutte le tragedie come il resto di voi umani fa con quell'essere?"
    return

label mion_question:
    bk "Haha, scelta interessante, allora ascolta con attenzione il significato di queste parole."
    play sound "audio/truth.mp3"
    bk "{i}{color=#0000cf}La ragazza battezzata Mion Sonozaki non era vittima di alcuna possessione demoniaca{w}, tuttavia ella era convinta di quel che diceva.{/color}{/i}"
    play sound "audio/laugh.mp3"
    pause 1
    return

label keiichi_question:
    bk "Capelli chiari?{w} ...oh, giusto, è come tu e il tuo assistente chiamate Maebara Keiichi."
    play sound "audio/truth.mp3"
    bk "{i}{color=#0000cf}Nonostante Keiichi non abbia visto o colpito nulla, c'era senza dubbio qualcuno o qualcosa immediatamente dietro di lui.{/color}{/i}"
    bk "Mentre per quanto riguarda il resto delle sue sventure... huhu chissà."
    return










    # Questo finisce il gioco.



