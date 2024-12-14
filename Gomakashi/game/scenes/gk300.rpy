label gk300:
    call hide_menu
    stop music fadeout 4

    play music("audio/sfx/cicadas.ogg") fadein 4


    scene koya with longFade
    pause 2
    stop music fadeout 8
    scene torakku with Dissolve(5)

    show check plain sus worried at left

    play music "audio/higu/forfeit.mp3"
    "------------scene 300 Larry explodes-------------"

    ck "DIAMINE! Stiamo perdendo tutti i testimoni. {w}Ora che anche Shion ci ha lasciato le penne rimane solo capelli chiari."

    show larry hide_arm nope directevil:
        offscreenright
        ease 2 right

    ck "Larry preparati! Dobbiamo vestirci da reporter e convincere a tutti i costi l'ospedale a lasciarci avere un intervista."

    show check nope -sus fp at flip
    ck "Muoviti, partiamo tra.... Larry?"

    show larry worried

    la "Non così in fretta capo! {w}Anzi..."

    show check angry shout
    la "Traditore!"

    ck "QUESTO NON È IL MOMENTO PER GLI SCHERZI RAGAZZO!"


    la "Per quanto ancora credeva di potermi ingannare? Le sembro davvero così stupido?"

    ck "....La pianti ora o hai bisogno di un riassestamento della spina dorsale?"


    window hide
    show check:
        linear 0.3 offscreenleft
    show larry:
        linear 0.3 center
    camera:
        xalign 0.5 yalign 0.95
        ease 0.6 zoom 2

    pause 0.6

    show larry -worried transmitter with dissolve
    pause 0.8

    camera:
        ease 1 zoom 1

    pause 1

    la "Non lo farei se fossi in lei."

    la "Ho fatto qualche modifica all'attrezzatura a sua insaputa. {w}Alla pressione di questo bottone posso causare un cortocircuito abbastanza potente da far saltare in aria questa baracca."

    ck "Sapevo che eri un idiota, ma questa volta l'hai fatta grossa. {w}Ti aspetti che ti creda? Non vedi che così morirai anche tu?"

    play sound "audio/sfx/wake up.ogg" volume 1.5
    show larry close nope
    camera at sshake
    la "NON TESTI LA MIA PAZIENZA!"

    show larry directevil
    la "Non mi frega più ormai. Era evidente che foste in combutta dall'inizio. {w} Intervistare Keiichi? È ovvio che sta cercando un metodo per liberarsi anche di lui."

    show larry evil  tilt
    la"Sentiamo, da quando va avanti il complotto? {w}Dal giorno del festival?... Dal nostro arrivo a Hinamizawa?... O magari dal primo incidente 5 anni fa."

    la "Quanto meno gli omicidi di quest'anno non possono che essere opera sua. {w}D'altronde tutto il villaggio sapeva che quei quattro erano entrati nel magazzino... E gli unici testimoni erano loro, io e lei."

    la "Ha continuato ha commettere atrocità sotto il mio naso pensando che fossi troppo ottuso per rendermene conto."

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


    show check:
        linear 0.5 left
    show larry:
        linear 0.5 right

    ck "VIA LE MANI DA QUEL PULSANTE!"

    la "Se c'è un prossimo mondo mi ringrazierà."

    show check:
        easeout 0.7 xalign 0.4
    ck "ASPETTA LARRY!...{nw}"


    play sound "audio/sfx/BANG.ogg"


    scene black with Dissolve(0.4)
    stop music fadeout 10

    pause 7

    jump gk320