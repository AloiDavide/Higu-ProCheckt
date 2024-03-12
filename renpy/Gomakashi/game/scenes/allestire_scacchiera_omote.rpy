
label chess_layer0:
    play music "audio/higu/short dawn at the end of time.mp3" fadein(8)
    scene black with longFade

    scene clinic_room
    show larry
    show sepia
    with Dissolve(4)
    pause(4)

    scene satokoeat
    show sepia
    with Dissolve(4)
    pause(4)

    scene satokopat
    show sepia
    with Dissolve(4)
    pause(4)

    scene torakku
    show larry evil at right
    show check plain fp angry nope at left
    show check at flip
    show sepia

    with Dissolve(4)

    pause(4)

    scene koya
    show larry tilt cry at left
    show larry at flip
    show check plain yep at right
    show sepia
    with Dissolve(4)

    pause(4)
    show red behind sepia with Dissolve(4)
    play sound "audio/sfx/chishibuki.ogg"
    pause(4)
    ""

    scene purplenoise with Pixellate(5,5)

    n "{cps=*0.3}Dove...{w} sono?{/cps}"

    n "{cps=*0.3}Sono stato catturato.{/cps}"

    n "{cps=*0.3}E poi...... cosa è successo?{/cps}"

    la "Capo...?"

    n "{cps=*0.3}Larry?{/cps}"

    la "Capo... mi sente?"

    n "{cps=*0.3}Io ho fallito. Quindi, almeno tu... {p}Promettimi che sarai...{/cps}"


    stop music fadeout(2)
    scene forest_path
    show larry
    with Pixellate(2.5,5)

    la "Allora, mi sta ascoltando o no? {w}Che succede? Non l'ho mai vista sovrappensiero."

    play music "audio/higu/time of rest.mp3" fadein 5

    show check plain fp at left
    show check at flip:
        xalign -0.5
        ease 1 left
    show larry:
        ease 1 right

    pause 1

    ck "Scusa ragazzo, ragionavo sulla missione e non ti ho sentito. Cosa stavi dicendo?"

    la "Parlavo delle leggende che ci ha raccontato l'infermiera. {p}Vorrei sapere la sua impressione, pensa che valga la pena indagare a fondo?"

    ck "Se è solo una trovata pubblicitaria, è veramente pessima. {w}Potrebbe attirare al massimo qualche fanatico dell'occulto."

    show check worried
    ck "Il mio fiuto però mi dice che quì c'è sotto qualcos'altro.... {w}Per lo meno non è da ignorare."

    show larry:
        ease 1 xalign 1.5
    show check at flip:
        ease 1 center

    n "Il mio nome in codice è Check, e sono un comandante del BKG."

    n "A causa della mia missione, sono giunto in un villaggio sperduto tra le montagne chiamato Hinamizawa."

    n "Ho letto una rivista per turisti prima di partire, a quanto pare questo villaggio è \"un paradiso rurale immerso nella tradizione\"."

    show check yep
    n "Chiaramente si sono dimenticati di scrivere che la tradizione prevede fare a pezzi gli stranieri e darli in pasto ai demoni."


    show check at flip:
        ease 2 xalign -0.5
    show larry:
        ease 2 center

    pause 2

    n "Questo è Larry, mio assistente e compagno in questa missione. Se dovessi evidenziare una sua qualità, beh, sicuramente vanta la penna più veloce del BKG."

    n "Quanto al resto, è ancora giovane e maldestro, ma in lui vedo del vero potenziale."

    show larry:
        ease 1 right
    show check at flip:
        ease 1 left

    ck "Mmhh? Il bosco sembra finire quì."

    ck "Mi sa che ci siamo. Dev'essere questo il posto."

    scene dam
    show check plain fp at left
    show check at flip
    show larry at right
    with Dissolve(1)

    la "Wow. {w}Non c'è anima viva, è veramente un cantiere abbandonato."

    show larry focus notes tilt
    la "Il sito è abbandonato da quasi 5 anni. Eppure I macchinari sono ancora posizione, come se dovessero riprendere i lavori a momenti."

    show larry -tilt -focus
    la "Se non ricordo male il progetto per la diga è andato in stallo a tempo indeterminato."

    la "Un posto come questo non merita di finire in fondo a un lago. {w}Non mi sorprende che i cittadini abbiano fatto di tutto per salvare le loro case."

    show check nope
    ck "Tuttavia, il silenzio in questo cantiere si basa sul sangue versato di un civile."

    ck "...O almeno così sembrerebbe a giudicare dalle fonti ufficiali."

    la "Vuole dire che non è così?"

    ck "Pare che la decisione di fermare i lavori fosse già stata presa prima dell'omicidio del capocantiere."

    ck "Dopo avere ignorato le proteste per mesi, il ministro delle costruzioni ha semplicemente fatto dietro front senza fornire una spiegazione e cercando di attirare meno attenzione possibile."

    ck "Non è difficile immaginare che tipo di \"argomentazione\" gli sia stata mossa contro."

    la "Ma allora come si spiega il caso del capocantiere?"

    ck "Potrebbe trattarsi di semplice vendetta, o dell'inizio di un piano più grande.{w} Fatto sta che non è giustificabile neanche come un ultimo atto di disperazione."

    la "Chiaro, ma certo, la serie di omicidi non prova niente, pure la polizia li sta trattando come casi separati."

    ck "Ragazzo, pensi davvero che per {b}pura coincidenza{/b} ci possano essere un omicidio e una sparizione lo stesso giorno per quattro anni di fila?"

    ck "Qualcuno con {b}MOLTA{/b} influenza sta tirando le fila, non c'è altra spiegazione."

    la "Non siamo in pericolo anche noi allora?"

    ck "Credimi, sono stato in situazioni ben peggiori."

    " check trasmittente "

    ck "Non devi preoccuparti. Una volta che avremo smascherato il marcio di questo villaggio e ristabilito i contatti con il quartier generale, potremo richiedere un intervento diretto. Fino ad allora basterà mantenere un basso profilo."

    la "Ma certo. Non c'è da preoccuparsi, non quando Check è al capo della missione. Sono certo che andrà tutto alla grande."


    stop music
    play sound "audio/sfx/glass crack.mp3"
    show frag_overlay
    pause 2

    scene dam
    show frag_overlay
    play sound "audio/sfx/teleport.wav"
    show stop_time with Dissolve(2)
    show check sor fp worried at left
    show check at flip
    show hnb sneer fury at right
    with squares

    play music "audio/umi/golden sneer.mp3"


    hb "MACCCERTO COME NOOOOO!"

    play sound "audio/sfx/laugh.mp3"
    hb "Sentitelo: \"Ci sono io quindi andrà tutto bene\" HANANANANANA! Guarda quanta sicurezza dal nostro {b}EX{/b} comandante del BKG."

    hb "Sicuro che puoi ancora vantarti quando a breve anche il tuo caro assistente ti pugnalerà alle spalle? "
    play sound "audio/sfx/laugh.mp3"
    extend "HANANANANANA."


    ""

    ""

    return



label chess_layer1:

    return

