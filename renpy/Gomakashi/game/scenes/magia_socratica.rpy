label chessboard0:
    $notes=False
    play music "audio/higu/short dawn at the end of time.mp3" fadein(5)

    hide layer screens

    scene black
    with Fade(3,0,1)

    show sepia onlayer overlayer
    #show layer overlayer
    show clinic_room
    show larry smile behind sepia

    with Dissolve(3)
    pause(4)


    scene satokoeat with masterFade
    pause(6)

    scene satokopat with masterFade
    pause(6)

    scene torakku
    show larry evil at right
    show check plain fp angry nope at left
    show check at flip
    with masterFade
    pause(6)

    scene koya
    show larry tilt worried cry at left
    show larry at flip
    show check plain yep at right
    with masterFade
    pause(6)

    scene red with masterFade
    pause 2
    play sound "audio/sfx/furu.ogg"
    pause 0.5
    play sound "audio/sfx/tataku.ogg"


    pause 2
    play sound "audio/sfx/chishibuki.ogg"
    pause 3

    scene purplenoise
    hide sepia onlayer overlayer
    with Pixellate(5,5)

    n "{cps=*0.3}Dove...{w} sono?{/cps}"

    n "{cps=*0.3}Sono stato catturato.{/cps}"

    n "{cps=*0.3}E poi...... cosa è successo?{/cps}"

    la "Capo...?"

    n "{cps=*0.3}Larry?{/cps}"

    la "Capo... mi sente?"

    n "{cps=*0.3}Io ho fallito. Quindi, almeno tu... {p}Promettimi che sarai...{/cps}"



    stop music fadeout(2)
    scene forest_path
    show larry nope
    #with flash
    with Pixellate(2.5,5)
    $notes=True



    la "Allora, mi sta ascoltando o no? {w}Che succede? Non l'ho mai vista sovrappensiero."



    show check plain fp at left
    show check worried at flip:
        offscreenleft
        ease 1 left
    show larry:
        ease 1 right

    pause 1

    ck "...."

    ck "Scusa ragazzo non è niente, ragionavo sulla missione e non ti ho sentito. Cosa stavi dicendo?"

    play music "audio/higu/time of rest.mp3" fadein 6
    show check yep
    la "Parlavo delle leggende che ci ha raccontato l'infermiera. {p}Vorrei sapere la sua opinione, pensa che vale la pena indagare a fondo?"

    show check yep
    ck "Se è solo una trovata pubblicitaria, è veramente TERRIBILE. {w}Potrebbe attirare AL MASSIMO qualche fanatico dell'occulto."


    ck "Il mio fiuto però mi dice che quì c'è sotto qualcos'altro.... {w}Per lo meno non è da ignorare."

    define to_center = MoveTransition(delay=1, enter=offscreenright, enter_time_warp=_warper.ease)
    show larry:
        ease 1 offscreenright
    show check at flip:
        ease 1 center

    pause 1

    n "Il mio nome in codice è Check, e sono un comandante del BKG."

    n "A causa della mia missione, sono giunto in un villaggio sperduto tra le montagne chiamato Hinamizawa."

    n "Ho letto una rivista per turisti prima di partire, a quanto pare questo villaggio è \"un paradiso rurale immerso nella tradizione\"."

    show check angry
    n "CHIARAMENTE si sono dimenticati di scrivere che la tradizione prevede fare A PEZZI gli stranieri e darli in pasto ai DEMONI."


    show check -angry at flip:
        ease 2 offscreenleft
    show larry yep:
        ease 2 center

    pause 2

    n "Questo è Larry, mio assistente e compagno in questa missione. Se dovessi evidenziare una sua qualità, beh, sicuramente vanta la penna più veloce del BKG."

    n "Quanto al resto, è ancora giovane e maldestro, ma so che ha del vero potenziale."

    show larry:
        ease 1 right
    show check at flip:
        ease 1 left

    ck "Mmhh? Il bosco sembra finire quì. {w}Mi sa che ci siamo. Dev'essere questo il posto."



    scene dam
    show check plain fp at left
    show check at flip
    show larry smile at right
    with Dissolve(1)

    la "Wow. {w}Non c'è anima viva, è veramente un cantiere abbandonato."

    show larry focus notes yep tilt
    la "Il sito è abbandonato da quasi 5 anni. Eppure I macchinari sono ancora posizione, come se dovessero riprendere i lavori a momenti."

    show larry -tilt -focus yep
    ck "Ufficialmente il progetto per la diga è andato in stallo a tempo indeterminato. {w}Se non hanno ancora fatto smantellare tutto è solo per salvare la faccia."

    la "L'ha visto anche lei quel panorama dalla collina. Un posto come questo non meritava di finire in fondo a un lago."

    la "È comprensibile che che i cittadini fossero disposti a tutto per salvare le loro case."

    show check nope
    show larry nope
    ck "Tuttavia, il silenzio in questo cantiere si basa sul sangue versato di un civile."

    show check yep
    ck "....O almeno così sembrerebbe a giudicare dalle fonti ufficiali."

    la "Vuole dire che non è così?"

    ck "Pare che la decisione di fermare i lavori fosse già stata presa prima dell'omicidio del capocantiere."

    ck "Dopo avere ignorato le proteste per mesi, il ministro delle costruzioni ha semplicemente fatto dietro front, senza fornire una spiegazione, e cercando di attirare meno attenzione possibile."

    ck "Non è difficile immaginare che tipo di \"argomentazione\" gli sia stata mossa contro."

    show check nope
    la "Ma allora come si spiega il caso del capocantiere?"

    ck "Potrebbe trattarsi di semplice vendetta, o dell'inizio di un disegno più complesso.{w} Fatto sta che non è giustificabile neanche come ultimo atto di disperazione."

    la "C'è una possibilità che questo omicidio e quelli successivi siano scollegati? {w}Voglio dire, pure la polizia li sta trattando come casi separati."

    show check angry
    show larry worried
    ck "Larry, pensi davvero che per PURA COINCIDENZA ci possano essere un omicidio e una sparizione lo STESSO giorno per quattro anni di fila?"

    ck "Tutte le vittime erano riconducibili a dei nemici del villaggio o potenziali ficcacaso."

    ck "È chiaro che qualcuno con MOLTA influenza sta tirando le fila."

    show check -angry


    la "Capito...."

    show larry scared
    stop music fadeout 10
    la "Un momento. {w}Non siamo in pericolo anche noi allora?"
    show check yep
    play music "audio/higu/sunrise.mp3" fadein 5 #or shadow or daily passing by
    ck "Frena l'ansia ragazzo. {w}Siamo stati in situazioni ben peggiori."
    show larry -scared

    ck "Ricordi quando ci siamo dovuti infiltrare in un gruppo di criminali che pianificavano una rapina? Quelli con i nomi in codice."

    show larry nope
    la "Quando sospettavano che ci fosse una talpa stavo per andare nel panico, ma lei ha tenuto il sangue freddo."

    ck "O quella volta che sulle tracce di uno scienziato pazzo siamo stati catturati dal suo ragno mutante?"

    show check sus
    ck "A ripensarci probabilmente era solo un automa molto realistico."

    show check -sus
    show larry yep
    la "Ho ancora gli incubi di quel giorno, non so come ne sarei uscito senza il suo aiuto."

    la "Però la missione più memorabile è stata quando una ragazza ha preso in ostaggio la sua classe minacciando di far saltare la scuola in aria."

    ck "Solo un pazzo penserebbe di rienpire i tubi dell'acqua di benzina. La puzza era insopportabile.{w} Ma anche quella volta abbiamo portato a termine l'incarico senza intoppi."

    show check smile

    ck "Perciò Larry, tu pensa soltanto a prendere gli appunti, in cambio io mi assicurerò di rendere la missione un successo."

    show check calling yep
    ck "Una volta che avremo smascherato il marcio di questo villaggio e ristabilito i contatti con il quartier generale, potremo richiedere un intervento diretto."

    ck "Fino ad allora basterà mantenere un basso profilo."

    show larry smile
    la "Ma certo, mi scusi stavo per dubitare di lei."

    la "Non riusciranno mai ad accorgersi di noi, non con lei sull'attenti. {w}Non c'è nulla di cui preoccuparsi."
    stop music fadeout 5
    ck "Ben detto Larry, assolutamente nulla di che preoccuparsi."

    stop music
    play sound "audio/sfx/glass crack.mp3"
    show frag_overlay
    pause 2.6

label chessboard1:

    scene dam onlayer underlayer
    scene witch_flowers
    with purple_flash
    play music "audio/umi/the candles dance.mp3" #oppure scorpion entrails
    play sound "audio/sfx/teleport.wav"
    show check sor fp worried at left
    show check at flip
    show hnb grin fury at right
    with squares




    hb "NULLA di cui preoccuparvi? Sul serio?!"


    hb "Guarda quanta sicurezza dal nostro {b}EX{/b} comandante del BKG."
    play sound "audio/sfx/laugh.mp3"

    hb "HANANANANANA. {p}Sei proprio sicuro che vuoi ancora vantarti quando a breve anche il tuo caro assistente ti pugnalerà alle spalle?"



    show check yep
    ck "Hanabi... cominciavo a pensare che non ti saresti più ripreso da quella caduta. Heheha."

    show hnb nope
    hb "Ugggh."

    show hnb -fury grin taunt
    hb "Allora Check, sei pronto a subire la sconfitta più devastante che ti abbia mai inflitto?"


    show check sus nope

    ck "Non ancora sciagurato! Sto raccogliendo i miei pensieri, raffinando le mie teorie, affinando le mie tattiche..."

    show hnb yep -taunt
    hb "Costruendo castelli per aria?"

    hb "Senti, io ti conosco, e non te lo dico per cattiveria. {w}Non c'è possibilità al mondo che tu non fallisca!"

    ck "Se sei così certo di vincere, allora perchè non {nw}"

    play sound "audio/sfx/damage2.mp3"
    show check angry shout:
        linear 0.2 zoom 1.8 ypos 1.7

    show hnb -finger grin:
        linear 0.2 zoom 0.6

    camera at sshake


    extend "STAI ZITTO DUE MINUTI e mi lasci riflettere!?"

    stop music fadeout 5
    play sound "audio/sfx/laugh.mp3"
    pause 1

    play sound "audio/sfx/teleport.wav"
    hide hnb with squares

    #Check to center stage
    show check nope -angry:
        ypos 1.7
        ease 2 center zoom 1

    pause 3



    play music "audio/sfx/wind.mp3" fadein 5 #or suspicion




    show check think

    n "E quindi... questa volta sono finito a seguire capelli verdi..."

    show mion_doll onlayer underlayer
    show layer underlayer:
        zoom 1.5
        yalign 0.0 xalign 1.0
    with dissolve


    n "...No, non questa capelli verdi."


    scene shion_bento onlayer underlayer with dissolve

    "Ecco si, lei!"



    n "Sinceramente avrei preferito la prospettiva di Mion... Possibile che abbia fatto confusione all'entrata?"

    n "DIAMINE che errore da dilettante, sarà perchè continuo a chiamare tutte e due con lo stesso nomignolo?"

    show check -think
    n "Ma non tutto il male vien per nuocere, anche Shion si sta rivelando una manna dal cielo."

    n "Non mi illudo che la sua sia una visione obiettiva, nessuna lo è."

    n "In passato ho fallito perchè mi sono fidato solo di ciò che avevo davanti agli occhi. {w}Ora so che l'unico modo per ottenere una visione d'insieme è mettere al confronto più prospettive da più frammenti."

    n "Fatto sta però, che la sua è di gran lunga la finestra più lucida fin ora, ed è in una posizione altamente favorevole per ottenere informazioni sui Sonozaki."

    scene hinamizawa onlayer underlayer with dissolve
    n "Nonostante le provocazioni di Hanabi mi sento molto più sicuro di me stesso{w}, ma ancora non ho chiaro al 100\% nè il reale svolgimento degli eventi, nè come funzioni la cospirazione davvero."

    show check think
    n "Forse è ancora presto per fare teorie..."
    show check -think
    n "No... {w}Sono stato fin troppo passivo fin ora, non vincerò mai aspettando solamente che la soluzione mi venga servita."



    stop music fadeout 3


    show check:
        ease 1.5 left
    show hnb:
        offscreenright
        ease 1.5 right

    pause 2.5
    play music "audio/umi/suspicion.mp3" fadein 4
    hb "Con calma grande detective. Vuoi anche una tazza di tè? {w}In fondo quelli con un limite di tempo siete tu e la tua strega, non noi."

    show hnb cigar
    hb "Ma fammi almeno il favore di non annoiarmi a morte."

    ck "Ti dirò cosa penso di quello che abbiamo visto fin ora. {w}Nonostante l'orribile tortura che ha subito Shion, Satoshi è comunque scomparso."

    ck "Il modo per quadrare il cerchio è ovvio, è inutile girarci attorno. Si tratta della famiglia Sonozaki."

    hb "Un complotto? Ma davvero Check? "


    extend "Penso che tu abbia visto troppi film, {b}il mondo non è così conveniente...{/b}"

    show hnb -cigar nope
    show check angry

    ck "Conveniente un CORNO! Tutto torna."




    #play sound "audio/sfx/damage.mp3"
    ck "Mantengono il controllo sulla popolazione del villaggio e dintorni per propagare le antiche usanze religiose di Hinamizawa!"

    scene shrine onlayer underlayer with dissolve
    #play sound "audio/sfx/damage2.mp3"
    ck "Sfruttano le credenze locali per creare un clima di oppressione, dove chiunque metta in dubbio la loro autorità e quella di Oyashiro-sama è il nemico."

    #play sound "audio/sfx/damage.mp3"
    ck "Adesso sappiamo anche quanto siano spietati persino con i membri della stessa famiglia, e quanto ci tengono alla segretezza!"

    scene police onlayer underlayer with dissolve
    #play sound "audio/sfx/damage2.mp3"
    ck "E non è tutto. Hanno infiltrato la polizia, e perfino la politica! Sono riusciti a opporsi al governo con minacce e rapimenti per contrastare il progetto della diga!"

    show hnb yep
    hb "Questa è solo una tua speculazione."


    show hnb -fury yep
    show check think
    ck "Non è speculazione, ho vissuto in prima persona le indagini di quel caso."

    show check -think
    ck "Per un'organizzazione criminale come la loro, mettere in atto un complotto sarebbe tutt'altro che impossiblile."


    scene sonozroom onlayer underlayer with dissolve
    show hnb cigar yep

    hb "Puoi basare le tue accuse sulle circostanze quanto vuoi. {w}Senza prove concrete tutte le tue teorie restano fumo al vento."

    hb "Parli del rapimento come un dato di fatto, ma puoi essere certo che I Sonozaki fossero veramente coinvolti?"

    stop music fadeout 3
    ck "........."

    show check -angry smile

    play music "audio/umi/core.mp3" fadein 5

    ck "Hahaheheha. Bel tentativo, Hanabi."

    show hnb nope -cigar
    ck "Ma per tua sfortuna, devi sapere che quella stessa indagine ha prodotto delle prove più che solide del loro coinvolgimento."

    show check yep
    ck "Quando i rapitori sono stati costretti alla fuga, sai di chi hanno fatto il nome? "
    play sound "audio/sfx/strike.mp3"
    camera at sshake
    show check angry objection at pointing with purple_quick
    extend "Nientemeno che i Sonozaki!"

    show check -angry -objection at reset
    show oryou onlayer underlayer with dissolve:
        zoom 0.6
        truecenter


    ck "In più, secondo un informatore fidato di Ooishi, Oryou stessa ha implicato che il ragazzo rapito fosse stato liberato per suo ordine!"

    ck "E so cosa mi dirai adesso. {p}\"Quel rapimento non c'entra niente con gli omicidi, non puoi usarlo per collegare i Sonozaki ai delitti annuali del Watanagashi.\""

    ck "Tuttavia, ho motivo di pensare che il piano fosse stato architettato già da allora."

    hb "Sentiamo con che scusa proverai a uscirtene adesso."

    ck "Si tratta di Rika. {w}Lei era già al corrente di tutti gli eventi che negli anni a venire sarebbero stati chiamati la maledizione di Oyashiro-sama."

    ck "Lei che sappiamo essere presente a tutti gli incontri dei vertici del villaggio, ma incapace di influenzarli."

    play sound "audio/sfx/strike.mp3"
    show check angry objection at pointing with purple_quick
    camera at sshake
    ck "Rika Furude è una prova vivente che qualcuno ha orchestrato gli omicidi!"

    show check -angry -objection at reset
    show oryou onlayer underlayer with dissolve:
        zoom 0.6
        truecenter


    ck "Ed è estremamente probabile che questo qualcuno siano i Sonozaki."

    ck "E se tutto questo non ti dovesse bastare, ho ancora la prova più schiacciante di tutte..."


    scene sonoztearoom onlayer underlayer
    show evil_mion onlayer underlayer:
        zoom 0.6
        truecenter
    with dissolve

    pause 0.5


    play sound "audio/sfx/strike.mp3"
    show check smile objection at pointing with purple_quick

    camera at sshake
    ck "Mion stessa ha confessato! {p}Si è seduta di fronte a Rena e Keichi e ha parlato con parole chiare!"

    camera at sshake
    play sound "audio/sfx/damage.mp3"
    pause 0.5
    play sound "audio/sfx/damage2.mp3"
    pause 0.5
    play sound "audio/sfx/strike.mp3"
    extend " Ha completamente vuotato il sacco!"

    show check sor at reset
    ck "Di che altra prova hai bisogno?!"

    stop music fadeout 6

    hb "........."


    show hnb grin -cigar
    show check nope

    hb "Hanananana! Hai un idea di prova davvero debole. Quell'argomentazione ha più buchi di un bersaglio al poligono di tiro."
    play music "audio/umi/suspicion.mp3" fadein 3
    show hnb yep
    hb "Usa un attimo il cervello e renditi conto di quante opzioni plausibili stai scartando."

    hb "E se qualcuno avesse tentato di incastrare i Sonozaki? {w}E se l'informatore avesse malinterpretato le parole di Oryou?"

    hb "E se mion stesse mentendo sotto minaccia? {w}Magari c'era un cecchino appostato fuori tutto il tempo pronto a sparare."

    show check yep
    ck "E hai il coraggio di chiamare la mia una teoria del complotto? "

    extend"Penso che tu abbia visto troppi film Hanabi. {b}Il mondo non è così conveniente.{/b}"


    hb "Mhhhhhhh. Aspetta, ho io una bella spiegazione per te..."

    play music "audio/umi/nighteyes.mp3" fadein 3

    show hnb grin
    hb "E se Mion fosse posseduta..."
    show hnb fury fist devil
    show check angry nope
    play sound "audio/sfx/zbiin.ogg"
    extend "COME LEI STESSA HA CONFESSATO DI ESSERE???!!!"

    hb "HANANANANA. Che succede, adesso non prendiamo più per buona la sua parola?"

    hb "Non dirmi che hai dimenticato tutti i suoi comportamenti incoerenti. {w}I cambi di personalità improvvisi! {w}I suoi episodi maniaci e impulsivi!"

    hb "Il tutto dopo che si è presentata da Shion in lacrime facendo tutta la pentita!"

    show hnb -fist sneer
    hb "Ammettilo, non lo puoi spiegare!"

    scene sisters onlayer underlayer


    play sound "audio/sfx/furu.ogg"
    show hnb:
        linear 0.1 zoom 1.3 ypos 1.3

    show check:
        linear 0.1 zoom 0.8

    pause 0.3
    play sound "audio/sfx/slam.mp3"
    camera at sshake
    hb "Perchè Mion..."

    scene mion_jumpscare onlayer underlayer

    play sound "audio/sfx/furu.ogg"
    show hnb:
        linear 0.1 zoom 1.6 ypos 1.5

    show check:
        linear 0.1 zoom 0.6

    pause 0.3
    play sound "audio/sfx/slam.mp3"
    camera at sshake
    extend " Si comporta..."


    scene mion_jumpscare_phone onlayer underlayer


    play sound "audio/sfx/wake up.ogg"
    show hnb:
        linear 0.1 zoom 1.9 ypos 1.7

    show check:
        linear 0.1 zoom 0.4



    camera at Shake((0, 0, 0, 0), 5.0, dist=25)
    extend " Da pazzoide indemoniata?!?!{nw}"


    show check:
        linear 0.3 xalign -0.1
        linear 0.6 xalign 0.1
        linear 0.5 left
        linear 0.5 xalign 0.1
        linear 0.3 offscreenleft


    extend "{nw}"
    pause 2.3

    hide hnb
    show basement2 onlayer underlayer
    with PushMove(0.5, 'pushright')

    show check sor fp angry worried at offscreenright
    show check at flip
    show check:
        zoom 1
        linear 0.3 center

    ck "Haaaaaarrrrrgh!"

    n "NO! Non può essere questa la risposta! {w}Se viene fuori che è tutto davvero opera dei demoni non avremo modo per controbattere. {w}Ci DEVE essere un altra spiegazione!"

    n "Quella è la soluzione che tutti cercano a palesemente di far passare per vera. {w}Mi RIFIUTO di darla per scontata!"

    show check -angry nope
    stop music fadeout 5

    n "Aspetta... Capelli verdi, possessione..."

    show check think
    play music "audio/umi/haruka.mp3" fadein 4
    n "Se la memoria non mi inganna... Ricordo di avere già discusso quel momento."

    n "Quella volta che ho ricevuto degli indizi da Bern le chiesi delle parole di Mion."

    n "Devo solo ricordare l'indizio che mi ha dato!"

label remember:
    menu:
        "Capelli verdi era posseduta.":
            n "Mhhh... no, non può aver detto questo, sarei spacciato."
            n "Devo ricordare."
            jump remember
        "Capelli verdi non era posseduta, ha mentito.":
            n "Era qualcosa del genere... ma non esattamente."
            n "Che cosa aveva detto di preciso?"
            jump remember
        "Capelli verdi non era posseduta, ma non mentiva.":
            show check -think yep
            n "Ma certo. Ora ricordo perfettamente!"


    show fragplane with Dissolve(1.5)
    play sound "audio/sfx/truth.mp3"
    bk "{color=#0000cf}\"La ragazza battezzata Mion Sonozaki non era vittima di alcuna possessione demoniaca, tuttavia era convinta di quel che diceva.\"{/color}"

    hide fragplane with Dissolve(1.5)

    n "Questa è una delle poche informazioni che posso dare per certe."

    n "Mion non era posseduta..."

    n "In altre parole l'attacco di Hanabi è soltanto una distrazione per tenermi lontano dalla verità."

    show check nope sus
    n "Ma allora come può essere che non mentisse........"

    show check smile -sus
    n "Ma certo! Ci sono!"
    stop music fadeout 4

    show check:
        ease 1 offscreenright
    pause 1

    show hinamizawa onlayer underlayer
    show hnb at right
    with PushMove(0.5, 'pushleft')

    show check:
        offscreenleft
        ease 1 left


    pause 1

    play music "audio/sfx/cicadas.ogg"
    ck "TORNA QUA non abbiamo ancora finito."

    n "Hanabi mi lancia uno sguardo sorpreso, probabilmente non si aspettava che mi riprendessi così in fretta."

    show hnb nope
    hb "Eh? Già.... Già pronto ad ammettere la tua cocente sconfitta?"

    hb "Avanti, prova a spiegare il comportamento di Mion se ne sei in grado."


    play music "audio/higu/theme of owner.mp3"
    show check nope
    ck "Sono d'accordo con te sul fatto che non sia per niente normale. {w}Ci sono momenti in cui le sue opinioni sembrano andare contro la tradizione, e ci sono momenti in cui sembra più pazza che calcolatrice."

    ck "Accetterei una spiegazione sovrannaturale se fosse l'unica possibile, ma non lo è."

    ck "La risposta più probabile è un severo indottrinamento."

    ck "Mion è stata cresciuta per essere l'erede della famiglia, probabilmente le è stato inculcato che in loro scorre sangue demoniaco da prima che imparasse a camminare."

    ck "Tuttavia, non è qualcosa che avrebbero potuto fare alla luce del sole. {w}Devono pur sempre mantenere un'apparenza di normalità. {p}Quindi capelli verdi ha sempre dovuto vivere una doppia vita."

    ck "Sappiamo bene che ha un talento naturale per l'inganno, e che farebbe di tutto pur di vincere. {w}Ma che succederebbe se qualcuno nella sua posizione iniziasse a sviluppare sentimenti di amicizia o affetto nei confronti dei nemici che sa che dovrà uccidere?"

    ck "La sua pazzia è scatenata dalla dissonanza cognitiva tra la se stessa capofamiglia, baluardo delle regole del villaggio, {w}e la se stessa normale adolescente, amica di Satoko e Satoshi."

    ck "In questa condizione estrema, deve essersi convinta di avere un demone dentro di se, con cui giustifica le azioni orribili che si aspettano da lei."

    ck "E quando verrà a sapere che Keiichi e Shion hanno commesso un sacrilegio entrando nel magazzino, raggiungerà il limite e smetterà di agire in modo razionale."

    ck "Forse si è inflitta le stesse ferite di Shion come forma di inganno, oppure è possibile che le dispiacesse veramente. Questo non lo so ancora per certo."

    ck "Tuttavia, quando sarà il momento non esiterà a imprigionare e torturare sia sua sorella che i suoi amici, perchè è il \"demone\" a farlo."

    stop music fadeout 8
    show hnb yep
    hb "Ma che bella fanfiction strappalacrime, sono quasi commosso. "

    hb "E va bene, se questa è la tua teoria staremo a vedere chi ha ragione."
    play music "audio/sfx/cicadas.ogg" fadein 5

    show check yep
    ck "C'è un motivo per cui ho scelto questo frammento."

    ck "Qualsiasi cosa sia successa quella volta con capelli verdi si ripeterà anche quì, ma stavolta avremo dei posti in prima fila dalla prospettiva di sua sorella."

    ck "A differenza di chiunque altro, quella ragazza ha sia la lucidità che i mezzi per venire a capo del mistero. {w}E di sicuro non le manca la motivazione, dopo che per colpa loro è scomparso Satoshi!"


    hb "Hanananana. {w}Mi vuoi dire che è tutta colpa dei Sonozaki se Satoshi ha bonkato sua zia e se l'è data a gambe?"

    ck "Mion lo ha negato ma io non me la bevo... {w}Non so se lo abbiamo aiutato a scappare o se se ne siano sbarazzati, ma è impossibile che non ne sappiano nulla."

    play music "audio/higu/dawn.mp3"

    show check nope
    ck "Mentre per il motivo del delitto... c'è una spiegazione più semplice. Per quanto non mi piaccia per niente."
    show hnb nope
    ck "Più probabilmente, la persona che ha complottato per causare la morte della zia è Satoko."

    ck "Sapendo che Satoshi fosse estremamente protettivo nei suoi confronti, ha escalato la situazione rendendola insopportabile, finche lo stress del fratello non è esploso."

    ck "Il povero ragazzo, privato di qualsivoglia momento di pace, si è fiondato sulla soluzione più diretta. La scomparsa della causa delle loro disgrazie."

    ck "Agendo in modo egoista, probablimente capelli biondi ha sacrificato il futuro di suo fratello senza rendersene conto..."

    show hnb sneer
    hb "Mammamia Check, non ti ricordavo così spietato. {w}Daresti la colpa a una povera bambina orfana e maltrattata?"

    show check angry
    show hnb nope -fury
    ck "Spietato?! {w}I sentimenti non sono null' altro che un impiccio durante un'indagine. {w}Non mi piace e non mi deve piacere, ma è un errore farsi distrarre dalle proprie emozioni."

    hb "L'unica cosa che ti distrae è la tua paranoia. Stai dubitando un innocente perchè non sei in grado di trovare altre spiegazioni."

    ck "Questo lo dici tu!"

    ck "In questo modo hanno un senso anche le visioni di Satoshi. {w}Se consideriamo il suo stato psicologico, non è impensabile che potesse venire suggestionato stando a contatto con Rena."

    hb "E sentiamo allora, chi a sua volta, avrebbe suggestionato Rena? {w}Per di più a distanza di decine di chilometri quando viveva nel Kanto?"

    ck "OK, in quel caso non posso essere sicuro che c'entrino i Sonozaki, ma chi altro DIAMINE può essere stato? {w}Chi altro ha interesse nel perpetuare la maledizione di Oyashiro-sama?"

    ck "Devono aver corrotto il suo psichiatra ad Ibaraki o qualcun altro vicino a lei."

    hb "Tanto lavoro per una bambina di una famiglia senza nessuna importanza? Ma fammi il piacere."

    stop music fadeout 3
    play music "audio/sfx/cicadas.ogg" fadein 5
    show check -angry

    ck "Vabene, allora quando avremo finito quì seguiremo anche Rena e vedremo chi ha ragione!"
    show hnb yepper
    hb "Accetto volentirei la sfida. Hananana. {w}Ma non prima di averti  mostrato quanto torto hai su Mion. {w}Vedrai, al prossimo round ti avrò in lacrime."

    show check angry
    ck "Ti aspetterò affilando le mie asce, Hanabi."

    play sound "audio/sfx/laugh.mp3"
    show hnb evilgrin
    hb "HANANANANANANANANANA!"
    hide hnb with squares
    show check:
        ease 1 center

    pause 1


label chessboard2:
    scene hinamizawa
    show check plain at center

    play sound "audio/sfx/teleport.wav"
    play music "audio/umi/golden sneer.mp3"

    scene bern_fancy

    #show check_prop at truecenter:
        #zoom 0.2

    #camera:
        #zoom 7
        #xalign 0.488 yalign 0.50


    show crystalball:
        xalign 0.28 yalign 0.66
        zoom 0.3

    camera:
        zoom 7
        xalign 0.28 yalign 0.64




    with ImageDissolve(im.Scale("mask_center.png", 1920, 1080), time=1)


    bk "Un metodo dialettico d'indagine filosofica basato sul dialogo..."
    n "Asserisce Bernkastel con tono colto, bevendo un altro sorso di tè."

    camera:
        easeout_quad 1.5 zoom 1
    with None
    pause 1.5


    play sound "audio/sfx/teleport.wav"
    show bern at left
    show lamb cat at right

    with squares


    bk "Un dibattito volto a stabilire la validità dell'interpretazione di Check riguardo gli eventi di Hinamizawa... Non proprio adatto a lui, devo dire."

    ld "Come un pesce fuor d'acqua, il suo fallimento sarà inevitabile! {w}Hey che ne dici, prepariamo del sushi stasera?"

    show bern yoko

    bk "Lambdadelta, non trovi che interrompere il prossimo con bisogni così terreni quali il cibo sia un pelo inappropriato? {w}Specialmente se intento a citare i saggi come Socrate."

    show lamb pout frown

    ld "Socrachi? Che c'entra adesso? Non cercare di cambiare argomento."

    show lamb cat -frown
    ld "Fatto sta che Check è spacciato. Cotto e mangiato! {w}Ahahahaha."

    ld "E vuoi sapere perchè? Vuoi saperlo? Vuoi saperlo?"

    show bern chira
    bk "...Sigh..."

    show bern yoko
    bk "...Si Lambda, voglio sapere perchè."

    show lamb unhappy smirk

    ld "Perchè le mie tre barriere sono inattaccabili!"

    ld "Tu che ne hai già individuate due dovresti capire meglio di chiunque altro quanto siano fuori dalla sua portata."

    show lamb surprise yep
    ld "Abbiamo la barriera numero {b}1{/b}:"
    play sound "audio/sfx/truth.mp3"
    ld "{color=#ffe674}{b}L'inganno dei Sonozaki!{/b}{/color}"

    ld "Anche se questa dovesse fallire, si troverebbe davanti la barriera numero {b}2{/b}:"
    play sound "audio/sfx/truth.mp3"
    ld "{color=#ffe674}{b}La maledizione di Oyashiro-sama!{/b}{/color}"

    show lamb smugclose
    ld "Non che conoscerle ti abbia aiutato più di tanto."
    bk "Che nomi inutilmente complicati."


    show lamb unhappy yep
    ld "E per finire, anche se per un miracolo riuscisse a passare oltre, ad aspettarlo sarà la barriera più possente di tutte."
    ld "Quella che ancora confonde persino te!"
    ld "Barriera numero {b}3{/b}:"

    play sound "audio/sfx/truth.mp3"
    show lamb surprise smirk
    ld "{color=#ffe674}{b}La certezza di Lambdadelta!{/b}{/color}, Ahahahahahahahaha!"


    ld "Allora Bern, riesci a sentire la tua sconfitta? La tua pedina ti è stata strappata di mano, e il tuo re è quasi esausto."
    ld "Ormai è incredibilmente distante da te. Siete praticamente due entità diverse, unite solo alla radice."


    n "Bernkastel solleva la tazzina verso le sue labbra per bere un ulteriore sorso."
    bk "Non posso negarlo, ora come ora Check fa ancora fatica a districarsi tra le regole di questo mondo. \n"

    show bern chira noflap
    extend "{size=24}Dopotutto non ha ancora notato la condizione di vittoria davanti ai suoi occhi...{/size}"

    show lamb frown pout
    show bern yoko -noflap
    ld "Se lo sai allora potresti anche disperarti un po di più, renderebbe il tutto più divertente."


    bk "Chissà, magari sono estremamente fiduciosa della vittoria di Check. Incredibilmente scaltro come è, non potrebbe mai fallire."

    show lamb close
    ld "Oh beh, non che mi importi. Il vincitore di quel gioco ormai per me è irrilevante."

    show lamb frown pout
    ld "Piuttosto Bern... non pensi forse che io non me ne sia accorta vero?"

    ld "Ormai da un pò di tempo, ho un dubbio... Sembra che Rika sappia molto di più di quello che dovrebbe, non trovi?"

    bk "È davvero una ragazza intelligente, non c'è che dire."

    show lamb smugclose yep
    ld "Non intelligente quanto me, è chiaro."

    show bern chira
    bk "Non oserei mai insinuarlo..."

    show bern yoko
    show lamb evil smirk
    play sound "audio/sfx/zbiin.ogg"

    ld "Non ci provare, non ti lascerò cambiare argomento questa volta."

    show lamb mad
    ld "Quindi Rika sarebbe talmente intelligente da essere al corrente, alla tenera età di 5 anni, di tutto quello che accadrà in futuro? {w}Persino gli elementi imprevedibili come l'omicidio della zia?"

    ld "Potrei quasi sospettare che ci sia una ragione, un qualche trucco meschino, grazie al quale lei riesce ad appropriarsi di informazioni che non le appartengono!"

    bk "Che pensiero curioso da avere. Hai mai pensato di fare la scrittrice?"

    show lamb nag tantrum
    ld "Vuota il sacco! stai barando! Come mai Rika sa tutte quelle cose!? Mi devi rispondere hai capito!?"

    show lamb worried
    bk "Lambda, nel tuo stesso gioco non sai come mai una pedina si comporti in un certo modo? Un bel fallimento da parte tua, per quanto mi riguarda."

    bk "Fammi questo favore, evita di dare a me la colpa delle tue mancanze."


    n "Bernkastel beve l'ennesimo sorso dalla sua tazza di tè dalla capienza apparentemente illimitata."

    bk "Non c' è bisogno di prendersela. {p}Sarò onesta con te, non ci sono io di mezzo."

    show lamb fury smirk
    ld "Ed io dovrei crederti? Se sei tanto sicura perchè non lo ripeti in blu Bern?"

    bk "Non so Lambda. Forse mi piace tenerti nel dubbio."


    bk "Detto chiaro e tondo, perché mai, anche se io sapessi la risposta, dovrei riferirla a te? {p}{b}{i}Siamo avversari dopo tutto.{/i}{/b}"

    show lamb unhappy yep
    show bern chira
    bk "E, d'altronde... tu stai già vincendo in maniera così schiacciante..."

    show bern yoko
    bk "In questo contesto dove nonostante io tenti di ribellarmi ho già praticamente perso, che bisogno avresti di questa informazione che potrei avere o no."

    ld "Humpf! Ben detto!"

    ld "Allora sei pronta? Le preparazioni sono complete. {w}Lasciamo quei due sguazzare nel loro acquario e iniziamo il prossimo round!"

    bk "Sarò il tuo avversario ancora una volta."

    ld "Vedremo per quanto ancora avrai la volontà di continuare."

    stop music fadeout(1)
    play sound "audio/sfx/teleport.wav"
    hide bern
    hide lamb
    with squares


    #alternatively sunrise
    play music "audio/higu/shadow.mp3" fadein(3)
    n "E così, Bernkastel, nonostante lei sappia di non avere alcuna chanche di fronte alle magnificenza di Lambdadelta, continua a rifiutarsi di arrendersi con grazia."

    camera:
        ease 3 zoom 7

    pause 3

    play sound "audio/sfx/teleport.wav"
    scene hinamizawa_sunset


    show check plain fp at left






    show check at flip

    show larry yep at right

    show stop_time

    show check nope fp at flip as sorcheck:
        center


    camera:
        zoom 1


    with ImageDissolve(im.Scale("mask_center.png", 1920, 1080), time=1, reverse =True)
    pause 1

    n "Buona fortuna voi due... ne avrete bisogno."

    n "Io ho la mia battaglia a cui pensare e al momento non posso aiutarvi, ma tenete duro."

    play sound "audio/sfx/teleport.wav"

    hide sorcheck
    hide stop_time
    with purple_flash

    pause 1


    ck "Il sole sta calando Larry, torniamo al nascondiglio e riposiamo."



    #please do a fade instead
    scene small_shrine with Dissolve(1.5)
    ck "Ti voglio sveglio domani."
    scene shrine_sunset with Dissolve(1.5)

    la "Signorsi signor comandante."
    scene road_sunset with Dissolve(1.5)

    ck "Non possiamo permetterci di abbassare la guardia."
    scene road_sunset2 with Dissolve(1.5)

    ck "Dopotutto domani..."
    scene sky_sunset with Dissolve(1.5)#PushMove(2,'pushdown')

    ck "È il famigerato giorno del Watanagashi."

    stop music fadeout(9)
    show black with Dissolve(10)

    return
