init:
    $ renpy.add_layer('overlayer', above='master')
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
    ''

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


    scene red with masterFade
    pause(4)
    #play sound "audio/sfx/chishibuki.ogg"
    ""

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


    #check meno sorriso
    stop music fadeout(2)
    scene forest_path
    show larry
    #with flash
    with Pixellate(2.5,5)

    $notes=True
    la "Allora, mi sta ascoltando o no? {w}Che succede? Non l'ho mai vista sovrappensiero."

    play music "audio/higu/time of rest.mp3" fadein 5

    show check plain fp at left
    show check at flip:
        offscreenleft
        ease 1 left
    show larry:
        ease 1 right

    pause 1

    ck "Scusa ragazzo, ragionavo sulla missione e non ti ho sentito. Cosa stavi dicendo?"

    la "Parlavo delle leggende che ci ha raccontato l'infermiera. {p}Vorrei sapere la sua impressione, pensa che valga la pena indagare a fondo?"

    ck "Se è solo una trovata pubblicitaria, è veramente pessima. {w}Potrebbe attirare al massimo qualche fanatico dell'occulto."

    show check worried
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

    n "Quanto al resto, è ancora giovane e maldestro, ma so che ha del vero potenziale. Posso vederlo in lui"

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

    ck "Frena l'ansia ragazzo. {w}Credimi, sono stato in situazioni ben peggiori."

    " check trasmittente "

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

    scene dam
    show frag_overlay
    show stop_time
    with purple_flash
    play music "audio/umi/golden sneer.mp3"
    play sound "audio/sfx/teleport.wav"
    show check sor fp worried at left
    show check at flip
    show hnb sneer fury at right
    with squares




    hb "NULLA DI CHE PREOCCUPARVI?? HANANANANANA!!!!"

    play sound "audio/sfx/laugh.mp3"
    hb "Sentitelo {w}\"Ci sono io quindi andrà tutto bene\" HANANANANANA! Guarda quanta sicurezza dal nostro {b}EX{/b} comandante del BKG."

    hb "Sei proprio sicuro che puoi ancora vantarti quando a breve anche il tuo caro assistente ti pugnalerà alle spalle?"
    play sound "audio/sfx/laugh.mp3"
    extend "HANANANANANA."

    n "Venefico come al solito... {w}Eppure ci ha dato un grande aiuto durante il processo. Non oso immaginare come sarebbe finita se Lambdadelta non si fosse convinta."

    hb "Hanabi... cominciavo a pensare che non saresti più uscito da quella buca."

    hb "Non farti strane, volevo solo l'occasione di distruggerti lealmente uno contro uno."

    hb "Allora Check? Tutto pronto per la sconfitta più devastante di sempre?"

    show check nope

    ck "Non ancora sciagurato! Sto raccogliendo i miei pensieri, raffinando le mie teorie, affilando le mie tattiche..."

    hb "Innalzando la torre di stronzate dalla quale cadrai! Guarda, io ti conosco, non c'è possibilità al mondo che tu non fallisca miseramente!"

    show check angry
    ck "Se sei così certo di vincere, allora perchè non STAI ZITTO DUE MINUTI e mi lasci riflettere!?"

    'He blows Hanabi out of the frame with some screen shake.'
    'he gets bigger Trigger style?'

    #Check to center stage
    show check -angry:
        ease 1 center

    ck "Non nego che avrei preferito la prospettiva di Mion. DIAMINE, sarà perchè continuo a chiamare tutte e due capelli verdi?"

    ck "Ma non è un problema, anche Shion si sta rivelando una manna dal cielo. Finalmente sono riuscito ad avere una finestra più lucida su quello che sta succedendo, e soprattutto sulla famiglia Sonozaki."

    ck "Ora sono molto più sicuro di me stesso. Ma ancora non ho chiaro al 100 PERCENTO quello che è accaduto, ne come funzioni la cospirazione davvero."

    ck "Forse è ancora presto per fare teorie... {w}No non ho più tanto tempo."

    show check:
        ease 1 left
    show hnb:
        ease 1 right

    hb "Con calma Signor pensatore. Vuoi una tazza di tè?"

    ck "Nonostante l' orribile trattamento di Shion, Satoshi è comunque scomparso. C'è un ovvio modo per quadrare il cerchio."

    ck "Non mi piace girarci intorno visto che è così evidente, si tratta della famiglia Sonozaki."

    hb "Un complotto? Ma davvero Check? {w}Penso che tu abbia visto troppi film, il mondo non è così conveniente..."

    show check angry


    ck "Conveniente un corno! Tutto torna."

    'Qua cambio lo sfondo in sottofondo e ci metto dei background topici: sonozaki estate - shrine - police'
    #sonoz house

    ck "Mantengono il controllo sulla popolazione di Hinamizawa ed Okinomiya per soddisfare il loro desiderio di propagare le antiche usanze religiose di Hinamizawa!"
    #shrine
    ck "Creano un clima di oppressione, dove chiunque metta in dubbio la loro autorità ed Oyashiro-sama è il nemico, mantnendo un controllo schiacciante sulla popolazione."
    #police


    ck "Hanno infiltrato la polizia, e perfino la politica! Sono riusciti a opporsi al governo con minacce e rapimenti per contrastare il progetto della diga!"

    ck "Questa non è speculazione, ho vissuto in prima persona le indagini di un poliziotto di nome Akasaka che si occupava del caso."

    ck "Per un'organizzazione come la loro, un complotto sarebbe tutt'altro che impossiblile."


    hb "Eppure, senza alcuna prova le tue teorie non sono altro che fumo. E la logica non torna non trovi? Non abbiamo alcuna prova che I Sonozaki fossero convolti in alcun rapimento, ad esempio"

    ck "...Puoi tentare di ingannarmi quanto vuoi, ma non funzionerà... per caso devo ricordarti la solida base di prove che abbiamo?"



    ck "Ora conosciamo quanto siano spietati persino con la loro stessa famiglia, ed il loro incredibile desiderio di segretezza!"

    ck "I rapitori hanno nominato una famiglia quando sono stati costretti a scappare!"

    ck "Oryou stessa ha implicato che il ragazzo rapito fosse stato liberato per suo ordine!"

    ck "Ed infine, la prova più schiacciante di tutte..."

    'finger point, fitting sound effect'

    ck "Mion stessa ha confessato! Quando confrontata da Keichi ha completamente vuotato il sacco!"

    hb "Hanananana! Hai un idea di prova davvero debole. Posso pensare almeno a 10 scenari che invalidano il tuo ragionamento."

    ck "Sentiamo."

    hb "E se qualcuno avesse tentato di incastrare I Sonozaki? Se l'informatose avesse malinterpretato le parole di Oryou? {w} E se mion stesse mentendo per tornaconto personale o semplicemente sotto minaccia? Con tanto di cecchino appostato fuori. , e costretta a mentire con la sua spiegazione?"

    ck "Un complotto? Penso che tu abbia visto troppi film Hanabi. Non mi aspettavo di vederti arrampicarti sugli specchi così presto."

    hb "Che ne pensi di questa..."

    'Cattivissimo, music change, oni mion.'
    ck "E se semplicemente Mion fosse posseduta COME LEI STESSA HA CONFESSATO?! HANANANANA. Che succede, adesso non prendiamo più per buona la sua parola?"

    'qui gioco di regia, voglio una scena agitata puntuata da scene chiave con tonfi e/o spatter che ti fanno capire come scandisce le parole'

    ck "Ammettilo, non ha senso. {w} Perchè \"Mion Sonozaki\" {w} Si comporta {w} in questo modo."


    #confident
    ck "Ed è quì che ti sbagli. Ti devo ricordare in che frammento siamo entrati? Bern mi ha assicurato che il corso degli eventi sarà pressochè uguale a Watanagashi, qualsiasi cosa sia successa con capelli verdi, seguire sua sorella ci porterà senza dubbio alla verità."

    ck "Dopotutto quella ragazza ha sia i mezzi che il sangue freddo per venire a capo della questione. E di sicuro non le manca la motivazione, dopo che per colpa loro è sparito il suo ragazzo!"

    'e da qua mi ricollego alla fase satoshi di Crunter'

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
