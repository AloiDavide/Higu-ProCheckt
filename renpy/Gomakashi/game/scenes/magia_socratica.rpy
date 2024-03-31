init:
    $ renpy.add_layer('overlayer', above='master')
    $ renpy.add_layer('underlayer', below='master')
    define masterFade = { "master" : Fade(2,0,2) }

label chessboard0:
    $notes=False
    play music "audio/higu/short dawn at the end of time.mp3" fadein(8)

    hide layer screens

    scene black
    with longFade

    show sepia onlayer overlayer
    #show layer overlayer
    show clinic_room
    show larry behind sepia

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
    show larry tilt cry at left
    show larry at flip
    show check plain yep at right
    with masterFade
    pause(6)

    ''

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
    show larry
    #with flash
    with Pixellate(2.5,5)
    $notes=True


    play music "audio/higu/time of rest.mp3" fadein 10
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

    la "Parlavo delle leggende che ci ha raccontato l'infermiera. {p}Vorrei sapere la sua opinione, pensa che vale la pena indagare a fondo?"

    show check yep
    ck "Se è solo una trovata pubblicitaria, è veramente pessima. {w}Potrebbe attirare al massimo qualche fanatico dell'occulto."


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

    show check yep
    n "Chiaramente si sono dimenticati di scrivere che la tradizione prevede fare a pezzi gli stranieri e darli in pasto ai demoni."


    show check at flip:
        ease 2 offscreenleft
    show larry:
        ease 2 center

    pause 2

    n "Questo è Larry, mio assistente e compagno in questa missione. Se dovessi evidenziare una sua qualità, beh, sicuramente vanta la penna più veloce del BKG."

    n "Quanto al resto, è ancora giovane e maldestro, ma so che ha del vero potenziale."

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
    ck "Ufficialmente il progetto per la diga è andato in stallo a tempo indeterminato. {w}Se non hanno ancora fatto smantellare tutto è solo per provare a salvare la faccia."

    la "Menomale. Un posto come questo non meritava di finire in fondo a un lago."

    la "Dopo che ho visto quel panorama, non mi sorprende che i cittadini abbiano fatto di tutto per salvare le loro case."

    show check nope
    ck "Tuttavia, il silenzio in questo cantiere si basa sul sangue versato di un civile."

    ck "....O almeno così sembrerebbe a giudicare dalle fonti ufficiali."

    la "Vuole dire che non è così?"

    ck "Pare che la decisione di fermare i lavori fosse già stata presa prima dell'omicidio del capocantiere."

    ck "Dopo avere ignorato le proteste per mesi, il ministro delle costruzioni ha semplicemente fatto dietro front, senza fornire una spiegazione, e cercando di attirare meno attenzione possibile."

    ck "Non è difficile immaginare che tipo di \"argomentazione\" gli sia stata mossa contro."

    la "Ma allora come si spiega il caso del capocantiere?"

    ck "Potrebbe trattarsi di semplice vendetta, o dell'inizio di un disegno più complesso.{w} Fatto sta che non è giustificabile neanche come ultimo atto di disperazione."

    la "Chiaro, ma certo, la serie di omicidi non prova niente, pure la polizia li sta trattando come casi separati."

    show check angry
    ck "Larry, pensi davvero che per {b}pura coincidenza{/b} ci possano essere un omicidio e una sparizione lo stesso giorno per quattro anni di fila?"

    ck "Tutte le vittime erano riconducibili a dei nemici del villaggio o potenziali ficcacaso."

    ck "Qualcuno con {b}MOLTA{/b} influenza sta tirando le fila, non c'è altra spiegazione."

    show check -angry


    la "Capito...."

    show larry worried
    la "Un momento. {w}Non siamo in pericolo anche noi allora?"

    ck "Frena l'ansia ragazzo. {w}Credimi, sono stato in situazioni ben peggiori."

    show check calling smile

    ck "Una volta che avremo smascherato il marcio di questo villaggio e ristabilito i contatti con il quartier generale, potremo richiedere un intervento diretto."

    ck "Fino ad allora basterà mantenere un basso profilo."



    la "Ma certo, mi scusi stavo per dubitare di lei."

    la "Non riusciranno mai ad accorgersi di noi, non con lei al capo della missione. {w}Non abbiamo di che preoccuparsi."

    ck "Ben detto Larry, assolutamente nulla di che preoccuparci."

    stop music
    play sound "audio/sfx/glass crack.mp3"
    show frag_overlay
    pause 1.5

label chessboard1:

    scene dam onlayer underlayer
    scene witch_flowers
    with purple_flash
    play music "audio/umi/the candles dance.mp3" #oppure scorpion entrails
    play sound "audio/sfx/teleport.wav"
    show check sor fp worried at left
    show check at flip
    show hnb yep at right
    with squares




    hb "NULLA DI CHE PREOCCUPARVI EH?"
    show hnb nope
    hb "Guarda quanta sicurezza dal nostro {b}EX{/b} comandante del BKG."
    play sound "audio/sfx/laugh.mp3"
    show hnb nopper
    hb "HANANANANANA. {w}Sei proprio sicuro che vuoi ancora vantarti quando a breve anche il tuo caro assistente ti pugnalerà alle spalle?"


    show check nope
    ck "Hanabi... cominciavo a pensare che non saresti più uscito da quella buca."

    show hnb nope
    hb "Uggh. "
    show hnb -fury sneer
    extend "Allora Check, sei pronto a subire la sconfitta più devastante che ti abbia mai inflitto?"


    show check sus

    ck "Non ancora sciagurato! Sto raccogliendo i miei pensieri, raffinando le mie teorie, affilando le mie tattiche..."

    show hnb yep
    show hnb grin
    hb "Costruendo castelli di carte?"

    hb "Senti, io ti conosco, e non te lo dico per cattiveria. {w}Non c'è possibilità al mondo che tu non fallisca!"

    ck "Se sei così certo di vincere, allora perchè non {nw}"

    show check angry shout:
        linear 0.2 zoom 1.8 ypos 1.7

    show hnb nope ohno:
        linear 0.2 zoom 0.6

    camera at sshake


    extend "STAI ZITTO DUE MINUTI e mi lasci riflettere!?"


    hide hnb with squares

    #Check to center stage
    show check nope -angry:
        ypos 1.7
        ease 1 center zoom 1

    pause 1



    menu:
        'vento':
            play music "audio/sfx/wind.mp3"
        'musica':
            play music "audio/umi/suspicion.mp3"
        'entrambi':
            play music "audio/umi/suspicion.mp3"
            play sound "audio/sfx/wind.mp3"



    show check think

    n "E quindi... questa volta sono finito a seguire capelli verdi..."

    show mion_doll onlayer underlayer
    show layer underlayer:
        zoom 1.5
        yalign 0.0 xalign 1.0
    with dissolve


    n "No, non questa capelli verdi."


    scene shion_bento onlayer underlayer with dissolve

    "Ecco si, lei!"



    n "Sinceramente avrei preferito la prospettiva di Mion... Possibile che abbia fatto confusione all'entrata?"

    n "DIAMINE che errore da dilettante, sarà perchè continuo a chiamare tutte e due con lo stesso nomignolo?"

    show check -think
    n "Ma non tutto il male vien per nuocere, anche Shion si sta rivelando una manna dal cielo. {w}Finalmente ho una finestra lucida su quello che sta succedendo, e soprattutto sulla famiglia Sonozaki."

    scene hinamizawa onlayer underlayer with dissolve
    n "Nonostante le provocazioni di Hanabi mi sento molto più sicuro di me stesso{w}, ma ancora non ho chiaro al 100\% nè il reale svolgimento degli eventi, nè come funzioni la cospirazione davvero."

    n "Forse è ancora presto per fare teorie... {p}No. {w}Non posso più essere passivo come prima."

    show check:
        ease 1 left
    show hnb:
        offscreenright
        ease 1 right

    play music "audio/umi/fishy aroma.mp3"

    hb "Con calma grande detective. Vuoi anche una tazza di tè? {w}In fondo quelli con un limite di tempo siete tu e la tua strega, non noi."

    show hnb cigar
    hb "Ma fammi almeno il favore di non annoiarmi a morte."

    ck "Ti dirò cosa penso di quello che abbiamo visto fin ora. {w}Nonostante l'orribile tortura che ha subito Shion, Satoshi è comunque scomparso."

    ck "Il modo per quadrare il cerchio è ovvio, è inutile girarci attorno. Si tratta della famiglia Sonozaki."

    hb "Un complotto? Ma davvero Check? {w}Penso che tu abbia visto troppi film, il mondo non è così conveniente..."

    show hnb -cigar
    show check angry

    ck "Conveniente un corno! Tutto torna."

    #Sound design bam bam bam
    ck "Mantengono il controllo sulla popolazione del villaggio e dintorni per propagare le antiche usanze religiose di Hinamizawa!"

    scene shrine onlayer underlayer with dissolve
    ck "Sfruttano le credenze locali per creare un clima di oppressione, dove chiunque metta in dubbio la loro autorità e quella di Oyashiro-sama è il nemico."

    ck "Adesso sappiamo anche quanto siano spietati persino con i membri della stessa famiglia, e quanto ci tengono alla segretezza!"

    scene police onlayer underlayer with dissolve
    ck "E non è tutto. Hanno infiltrato la polizia, e perfino la politica! Sono riusciti a opporsi al governo con minacce e rapimenti per contrastare il progetto della diga!"

    show check think
    ck "Questa non è speculazione, ho vissuto in prima persona delle indagini per quel caso."

    show check -think
    ck "Per un'organizzazione criminale come la loro, un complotto sarebbe tutt'altro che impossiblile."


    scene sonozroom onlayer underlayer with dissolve
    show hnb cigar
    hb "Senza prove concrete non puoi dimostrare niente, tutte le tue teorie sono come fumo al vento."

    hb "Parli del rapimento come un dato di fatto, ma puoi essere certo che I Sonozaki fossero veramente convolti?"

    stop music fadeout 3

    ck "........."

    play music "audio/umi/core.mp3" fadein 5

    show check -angry smile

    ck "Hahaheheha. Bel tentativo, Hanabi."

    show hnb nope -cigar
    ck "Puoi tentare di ingannarmi quanto vuoi, ma non funzionerà..."

    ck "Ci sono dei dettagli di quell'indagine che ti sfuggono."

    show check yep
    ck "Quando i rapitori sono stati costretti alla fuga, sai di chi hanno fatto il nome? "
    play sound "audio/sfx/damage2.mp3"
    camera at sshake
    extend "Nientemeno che i Sonozaki!"

    show oryou onlayer underlayer with dissolve:
        zoom 0.6
        truecenter

    ck "In più, secondo le parole di un informatore fidato, Oryou stessa ha implicato che il ragazzo rapito fosse stato liberato per suo ordine!"

    ck "E so cosa mi dirai adesso. {p}\"Tutto questo è successo prima di qualsiasi omicidio, non abbiamo prove che collegano i Sonozaki ai delitti annuali del Watanagashi.\""


    ck "Ed è quì che arriva la prova più schiacciante di tutte..."


    scene sonoztearoom onlayer underlayer
    show evil_mion onlayer underlayer:
        zoom 0.6
        truecenter
    with dissolve

    pause 0.5


    play sound "audio/sfx/strike.mp3"
    show check smile objection at pointing

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

    'let the music fade out'

    hb "......"



    menu:
        'system zero':
            play music "audio/umi/system zero.mp3" fadein 7
        'nighteyes':
            play music "audio/umi/nighteyes.mp3"
        'miragecoordinator':
            play music "audio/umi/miragecoordinator.mp3"

    show hnb yep -cigar
    show check nope
    hb "Hanananana! Hai un idea di prova davvero debole. Quell'argomentazione è piena di buchi."

    hb "Usa un attimo il cervello e immagina... E se qualcuno avesse tentato di incastrare I Sonozaki? {w}E se l'informatore avesse malinterpretato le parole di Oryou?"

    hb "E se mion stesse mentendo sotto minaccia? {w}Magari c'era un cecchino appostato fuori tutto il tempo pronto a sparare."

    ck "E hai il coraggio di chiamare la mia una teoria del complotto? {w}Penso che tu abbia visto troppi film Hanabi. Il mondo non è così conveniente."

    hb "Mhhhhhhh. Aspetta, ho io una bella spiegazione per te..."


    hb "E se Mion fosse posseduta..."
    show hnb fury grin fist
    show check angry
    play sound "audio/sfx/zbiin.ogg"
    extend "COME LEI STESSA HA CONFESSATO DI ESSERE??????!!!!!!!"

    hb "HANANANANA. Che succede, adesso non prendiamo più per buona la sua parola?"


    show hnb -fist grin fury
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
        linear 1 xalign 0.3
        linear 0.5 left
        linear 1 xalign 0.3
        linear 0.3 offscreenleft

    extend ''

    hide hnb
    show basement2 onlayer underlayer
    with PushMove(0.5, 'pushright')

    show check sor fp angry worried at offscreenright
    show check at flip
    show check:
        zoom 1
        linear 0.3 center

    ck "Haaarrg!"

    n "No! Non può essere questa la risposta! {w}Se viene fuori che è tutto davvero opera dei demoni non avremo modo per controbattere. {w}Ci DEVE essere un altra spiegazione!"

    show check -angry nope
    stop music fadeout 5

    n "Aspetta... Capelli verdi, possessione..."

    show check think
    play music "audio/umi/haruka.mp3" fadein 4
    n "Se la memoria non mi inganna... Ricordo di avere già discusso quella scena."

    n "Si, fu quella volta che ho ricevuto degli indizi da Bern, le chiesi delle parole di Mion!"

    n "Devo solo ricordare quello che mi ha risposto!"

    menu:
        "Capelli verdi era posseduta.":
            'a'
        "Capelli verdi non era posseduta, ha mentito.":
            'b'
        "Capelli verdi non era posseduta, ma non mentiva.":
            'c'

    show check -think yep
    n "Ma certo. Ricordo perfettamente!"


    show fragplane with Dissolve(2)
    play sound "audio/sfx/truth.mp3"
    bk "\"La ragazza battezzata Mion Sonozaki non era vittima di alcuna possessione demoniaca{w}, tuttavia era convinta di quel che diceva.\""

    n "Ancora non so che cazzo vuol dire, ma vuol dire che l'attacco di Hanabi è soltanto un modo per distrarmi e impedirmi di venire al fondo della questione."

    'check torna da hanabi che si sorprende che è fresco e confident. Se ne frega perchè tanto lo vedremo.'
    #confident
    ck "Secondo te Mion è posseduta heh? Beh, staremo a vedere."

    ck "Ti devo ricordare in che frammento siamo entrati? Qualsiasi cosa sia successa quella volta con capelli verdi si ripeterà anche quì, ma stavolta avremo dei posti in prima fila dalla prospettiva di sua sorella."

    ck "A differenza di chiunque altro, quella ragazza ha sia la lucidità che i mezzi per venire a capo dei misteri dei Sonozaki. {w}E di sicuro non le manca la motivazione, dopo che per colpa loro è scomparso Satoshi!"

    hb "Ancora ad insinuare che sia stato fatto sparire da qualcuno."

    hb "È la stessa storia con Satoshi, solo congetture e nulla di concreto. Questi ipocriti continuano a dire che era un bravo ragazzo, amava così tanto la sorella che non la avrebbe mai abbandonata."

    hb "Ti dirò io, anche senza i Sonozaki di mezzo è più che probabile che se la sia semplicemente svignata per non essere catturato dalla polizia."

    hb "Oppure, beh è posseduto anche lui! Non che tu possa saperlo finchè non andiamo a controllare la prospettiva sua."



    "Non penso che ci sia lo zampino dei Sonozaki... c'è una spiegazione più semplice. Per quanto non mi piaccia per niente."

    ck "Molto probabilmente, Satoko è la persona che ha complottato per causare la morte della zia. Sapendo che Satoshi è estremamente protettivo nei suoi confronti, ha escalato la situazione, finche lo stress del fratello non è esploso."
    ck "ha essenzialmente reso la situazione insopportabile, litigando quanto più possibile per non lasciare alcun momento di pace... Lasciando aperta un ovvia soluzione. La scomparsa della principale causa delle loro disgrazie."

    #pensa

    ck "... Per quanto sia doloroso criticarla... era naturale che questo comportamento avrebbe causato un disastro. Naturalmente era estremamente giovane, ma, probablimente senza rendersene conto... ha sacrificato il futuro di suo fratello."

    hb "Hai così poca fiducia in lei? Check, sei diventato spietato."

    ck "spietato? I sentimenti non sono null' altro che un impiccio durante un indagine. Non mi piace e non mi deve piacere, ma è un errore farsi distrarre dalle proprie emozioni."

    hb "Check. Tu ti stai facendo distrarre dalla tua paranoia. Stai dubitando un innocente perchè non sei in grado di accettare la spiegazione più semplice."

    ck "Questo lo dici tu!"

    'Check pensa'

    ck "...Non solo Satoshi. Persino Rena sembra essere stata ingannata quando viveva nel Kanto. Anche se non posso essere sicuro che siano stati I Sonozaki, chi altro potrebbe essere stato? chi altro ha interesse nel perpetuare Oyashiro-sama?"







label chessboard2:
    scene hinamizawa
    show check plain at center




    "come zooming out from the previous scene, one of the transparent fragment props overlays over it and it zooms into Bern's room"

    play sound "audio/sfx/teleport.wav"
    play music "audio/umi/golden sneer.mp3"

    scene bern_fancy

    show check_prop at truecenter:
        zoom 0.2

    camera:
        zoom 7
        xalign 0.498 yalign 0.496


    with ImageDissolve(im.Scale("mask_center.png", 1920, 1080), time=1)

    bk "\"Il metodo socratico.\""
    bk "Un metodo dialettico d'indagine filosofica basato sul dialogo..."


    camera:
        easeout_quad 1.5 zoom 1
    with None
    pause 1.5


    play sound "audio/sfx/teleport.wav"
    show bern at left
    show lamb cat at right

    with squares


    bk "Un dibattito volto a stabilire chi tra loro due può sostenere le sue asserzioni su cosa spiega gli eventi di Hinamizawa... Non proprio adatto a Check, devo dire."

    ld "Come un pesce fuor d'acqua, il suo fallimento sarà inevitabile! {w}Hey che ne dici, prepariamo del sushi stasera?"

    show bern yoko

    bk "Lambdadelta, non trovi che interrompere qualcuno con bisogni così terreni quali il cibo sia un pelo inappropriato? {w}Specialmente mentre stanno richiamando i saggi come Socrate?"

    show lamb pout frown

    ld "Socrachi? Che c'entra adesso? Non cercare di cambiare argomento."

    ld "Fatto sta che Check è spacciato."

    show lamb mad evil

    ld "Le mie tre barriere sono inattaccabili!"

    ld "Tu che sei al corrente delle prime due dovresti capire meglio di chiunque quanto siano fuori dalla sua portata."

    ld "Abbiamo la barriera numero 1:"
    play sound "audio/sfx/truth.mp3"
    ld "{color=#ffe674}{b}L'inganno dei Sonozaki!{/b}{/color}"

    ld "Anche se questa dovesse fallire, si troverebbe davanti la barriera numero 2:"
    play sound "audio/sfx/truth.mp3"
    ld "{color=#ffe674}{b}La maledizione di Oyashiro-sama!{/b}{/color}"

    show lamb smugclose
    ld "Non che conoscerle ti abbia aiutato più di tanto."
    bk "Che nomi inutilmente complicati."


    show lamb evil
    ld "E per finire, anche se per un miracolo riuscisse a passare oltre, ad aspettarlo sarà le barriera più possente di tutte."
    ld "Quella che ancora costringe perfino te a brancolare nel buio!"

    play sound "audio/sfx/truth.mp3"
    ld "{color=#ffe674}{b}La certezza di Lambdadelta!{/b}{/color}, Ahahahahahahahaha!"

    show lamb fury smirk
    ld "Allora Bern, riesci a sentire la tua sconfitta? La tua pedina ti è stata strappata di mano, e il tuo re è quasi esausto."
    ld "Ormai è incredibilmente distante da te, l' unica similitudine rimane alla radice. Siete praticamente due persone diverse."

    n "Bernkastel bevve l'ennesimo sorso dalla sua tazza di tè dalla capienza apparentemente illimitata."
    bk "Devo ammetterlo, ora come ora Check farà ancora fatica a districarsi tra le regole di questo mondo."

    bk "{size=16}Almeno fino a che non si renderà conto di cosa è capace...{/size}"

    show lamb yep defa
    ld "Mhh? Che cosa hai detto? Ripeti non ho sentito."

    bk "Chissà, magari sono estremamente fiduciosa della vittoria di Check. Incredibilmente scaltro come è, non potrebbe mai fallire."

    show lamb close
    ld "Oh beh, non che mi importi. Il vincitore di quel gioco ormai per me è irrilevante."

    show lamb frown pout
    ld "Piuttosto Bern... non pensi forse che io non me ne sia accorta vero?"


    ld "Ormai da un pò di tempo, ho un dubbio... Sembra che Rika sappia molto di più di quello che dovrebbe, non trovi?"
    ld "Che Ragazza intelligente! Certo, non intelligente quanto me!"
    bk "È davvero una ragazza intelligente. Non intelligente quanto te, si intende."

    show lamb worried

    ld "Che ti prende, non è normale ricevere un tuo complimento."

    show lamb lookaway
    ld "Ma grazie, lo accetto..... "
    pause 0.5
    show lamb unhappy nag
    extend "Hey! Non cambiare discorso."

    ld "Quindi Rika sarebbe talmente intelligente da essere a conoscenza, alla giovane età di 5 anni, di tutto quello che sarebbe accaduto in futuro, in dettagli estrememente precisi?"

    show lamb pout frown
    ld "Qualcuno potrebbe sospettare che ci sia una ragione, un qualche trucco meschino, grazie al quale lei riesce ad appropriarsi di informazioni che non le appartengono!"

    bk "Che pensiero curioso da avere."

    show lamb nag unhappy
    ld "Vuota il sacco! stai barando! Come mai Rika sa tutte quelle cose!? Mi devi rispondere hai capito!?"

    bk "Lambda, nel tuo stesso gioco non sai come mai una pedina si comporti in un certo modo? Un bel fallimento da parte tua. Per non parlare del fatto che, immediatamente, difendi la tua reputazione dando la colpa ad altri."

    show lamb evil pout

    bk "Non c' è bisogno di prendersela. Sarò onesta con te, non ci sono io di mezzo."

    ld "Ed io dovrei crederti? Se sei tanto sicura perchè non lo ripeti in blu Bern?"

    bk "Non so Lambda. Forse mi piace tenerti nel dubbio."

    bk "Detto chiaro e tondo, perché mai, anche se io sapessi la risposta, dovrei riferirla a te? {w}SIAMO AVVERSARI DOPO TUTTO."

    bk "E, d' altronde... tu stai già vincendo in maniera così schiacciante... Detto tra noi, nonostante io tenti di ribellarmi, ho già praticamente perso. Tu non hai alcun bisogno di questa informazione che potrei avere o no."

    show lamb yep unhappy

    ld "Humpf! Ben detto!"

    ld "Allora sei pronta? Le preparazioni sono complete. {w}Lasciamo quei due sguazzare nel loro acquario e iniziamo il prossimo round!"

    bk "Sarò il tuo avversario ancora una volta."

    ld "Vedremo per quanto ancora avrai la volontà di continuare."

    stop music fadeout(1)
    hide bern
    hide lamb
    with squares


    #alternatively sunrise
    play music "audio/higu/shadow.mp3" fadein(3)
    n "E così, Bernkastel, nonostante sappia di non avere alcuna chanche di fronte alle magnificenza di Lambdadelta, rifiuta ancora di arrendersi con grazia."

    camera:
        ease 3 zoom 7

    pause 3

    play sound "audio/sfx/teleport.wav"
    scene hinamizawa_sunset
    show check plain fp at left
    show check at flip
    show larry at right
    show frag_overlay
    show stop_time

    camera:
        zoom 1

    with ImageDissolve(im.Scale("mask_center.png", 1920, 1080), time=1, reverse =True)
    pause 2

    play sound "audio/sfx/teleport.wav"
    hide stop_time with Dissolve(1.5)

    hide frag_overlay with Dissolve(1.5)




    ck "Il sole sta calando Larry, torniamo al nascondiglio e riposiamo. {w}Ti voglio sveglio domani."

    scene sky_sunset with PushMove(2,'pushdown')

    ck "Dopotutto domani, {w}è il fantomatico giorno del Watanagashi."

    show black with Dissolve(10)

    return
