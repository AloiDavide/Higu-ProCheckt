label scene2_1:
    call hide_menu

    scene sonozakitchen with Dissolve(4)
    show witch_flowers with purple_flash
    play music "audio/umi/scorpion entrails.mp3"
    play sound "audio/sfx/teleport.wav"
    show check sor fp worried at left
    show check at flip
    show hnb fury at right
    with squares

    show hnb grin
    hb "HANANANANANA! CHECK! È TUTTO QUI QUELLO CHE SAI FARE?"

    show hnb -fury yepper
    hb "Che dire, la tua teoria faceva schifo. Come ci si sente?"

    ck "Nghhhhhh..."

    hb "O forse dovrei farti i complimenti? Visto che la colpevole di tutto era Mion... "

    show hnb fury evilgrin
    extend "Peccato che non fosse la Mion che pensavi! HANANANANANANA!"

    ck "Allora... Non avevo sbagliato obiettivo... Non era un errore."

    show hnb taunt yepper
    pause 1

    hb "Esatto Check! La risposta era nelle tue mani dal momento in cui hai toccato quel frammento, e tu l'hai completamente ignorata!"

    show hnb close
    hb "È un vero spreco che una abilità così potente sia finita in delle mani così incompetenti."

    show sky_frag onlayer underlayer2
    scene mion_jumpscare onlayer underlayer:
        zoom 0.5
        xalign 0.5
        yalign 0.3
    hide sonozakitchen
    show witch_flowers

    show check sor fp worried at left
    show check at flip
    show hnb yepper -taunt -close at right

    with purple_flash




    hb "Credevi di trovare la conferma dei tuoi complotti, e invece hai trovato solo un'altra pazza assassina senza un briciolo di contesto."

    hb "Non puoi fidarti di una parola che dice... A meno che non vuoi credere ai demoni e alle possessioni."

    show hnb close
    hb "Questa battaglia era praticamente decisa prima di iniziare! "

    show hnb -close grin
    show check angry
    hide mion_jumpscare
    show sonozakitchen onlayer underlayer with purple_flash
    ck "Non è ancora finita, ho una nuova teoria! Questa volta ci sono!"
    
    hb "Avanti, sentiamo!"

    show check think nope
    ck "Come già stabilito, I Sonozaki sono in larga parte legati a molti omicidi del passato di Hinamizawa!{w} Ma c'è un altra sconosciuta organizazione che sta ordendo un complotto, e loro sono la causa degli eventi che non tornano!"

    ck "Ecco, così ha senso."
    show check angry worried

    hb "HANANANANANA! Ovvio Check, quando qualcosa non riesci ad inquadrarlo, è stato un misterioso complotto! Ma certo!"

    hb "Non hai imparato niente? La lezione non ti è bastata? Non puoi supplire la tua incompetenza con teorie campate per aria!"

    ck "Uuuugh....... Silenzio!"

    hide sonozakitchen
    show rika_moon onlayer underlayer:
        zoom 0.5
        xalign 0.5
        yalign 0.3

    with purple_flash
    ck "Rika è in combutta con questa misteriosa organizazione! Trae vantaggio dalle informazioni ottenute dalle riunioni dei Sonozaki a cui ha assistito per tramare i suoi loschi piani."

    show rika_moon:
        linear 0.5 zoom 0.3 xalign 0.1

    pause 1

    show rena_shion onlayer underlayer:
        zoom 0.5
        xalign 0.5
        yalign 0.3

    with purple_flash

    ck "Rena è fanatica della maledizione di Oyashiro-Sama, e convince Shion a crederci! A causare il disastro ogni volta è Shion, suggestionata dalle parole di Rena! Sempre Rena ha suggestionato Keichi nel terzo frammento e lo ha fatto impazzire!"

    ck "Palesemente, Rena è stata manipolata fin da bambina da questa organizzazione segreta per essere un pedone nel loro piano!"

    show rena_shion:
        linear 0.5 zoom 0.3 xalign 0.9

    pause 1

    show rika_shion onlayer underlayer:
        zoom 0.5
        xalign 0.5
        yalign 0.3

    with purple_flash
    ck "Rika intanto, ha rubato loro una siringa con una droga che fa impazzire la vittima e l'ha usata per attaccare Shion. Voleva difendere Keiichi come ha difeso Satoko in passato!"

    ck "Se Satoko è una manipolatrice come penso potrebbe essere anche lei una parte importante del piano, dopo tutto quelle due erano inseparabili."

    scene sonozakitchen onlayer underlayer with purple_flash

    hb "Si! Forza! Continua a sparare alla cieca come un pivellino che non ha mai tenuto un fucile in mano. {p}Questi anni lontato dal fronte ti hanno rammollito. Nemmeno tu hai idea di cosa stai dicendo."

    hb "Sei sull'orlo della sconfitta. Non vedo l'ora che tu perda e scompaia definitivamente, è l'unica cosa che ti meriti."

    stop music fadeout 3
    ck "......."

    play music "audio/higu/lies lies.mp3" fadein 3

    show hnb smug nope
    ck "Sei cambiato Hanabi, non sei sempre stato così acido... che ti è successo?"
    
    hb "...Sono cambiate molte cose. Ma a te che importa Check? Tanto ti sei lasciato tutto alle spalle, no?"
    
    ck "..."

    show hnb nopper fist
    hb "Non hai il diritto di criticarmi quando sei stato tu il primo a cambiare. Quando hai abbandonando il tuo dovere!"
    show hnb -fist
    ck "Credevo che un giorno avresti capito le mie motivazioni."

    ck "Tu che sei più giovane eri ancora soddisfatto dal diventare più forte, ma io no... Non volevo vivere seguendo gli ordini ciecamente fino alla mia morte."

    ck "Prima o poi un uomo ha bisogno di un posto dove è libero di seguire i propri ideali, e il campo di battaglia non era il posto adatto. Questo è tutto."

    hb "E questo sarebbe tutto? Tsk..."

    show hnb smug2 nope
    hb "Check... la vita intera è una guerra, non si può sfuggire alla realtà delle proprie responsabilità. {w}Altrimenti stai solo scaricando sugli altri il peso dei tuoi problemi."


    hb "Dovresti saperlo. Non è esattamente di questo che stai accusando Satoko?"

    show check shout
    ck "Quello che ho fatto io è stato scegliere un dovere rispetto a un altro.{w} Non devo delle scuse a NESSUNO."

    show hnb fury nopper fist
    hb "Hai costruito un'organizzazione sugli ideali e guarda il risultato! Un castello di carte sarebbe crollato meno facilmente!"


    ck "E tu invece? Sei andato in Afghanistan e ci hai lasciato le PENNE! {w}Vuoi dirmi che era quella la morte che volevi?"

    show hnb yepper
    hb "Se credi che basterà una conversazione per farmi sparire come un fantasma hai letto troppe storie. {w}Non ho mai avuto rimpianti. Nè in vita nè dopo."

    show hnb nopper
    hb "Sono qua per un solo motivo. {w}Impedire a {i}TE{/i} di evadere di nuovo la tua condanna."

    hb "Il tuo destino è morire ad Hinamizawa con il BKG in frantumi. {w}Non lascerò che tu abbia la possibilità di cambiarlo, fosse anche una in un millione."

    show check sus nope
    ck "Hanabi... davvero, cosa diavolo è successo in Afghanistan..."

    stop music fadeout 3

    hb"....."
    
    pause 2

    show hnb -fist smug grin

    play music "audio/umi/the candles dance.mp3"

    hb "Senti, ti concedo una pausa.  {w}Vai a sfregare quei tre neuroni, non si sa mai che facciano una scintilla."

    hb "Magari questa volta tornerai con una teoria lontanamente plausibile. Hanananana."

    show check -sus
    ck "Non mi lasci altra scelta che batterti. Molto bene allora, non ho motivo di rifiutare."

    show hnb fury
    hb "Farò a pezzi tutte le tue teorie una per una."

    hb "Forse comincerò proprio dimostrando l'innocenza di Satoko. Visto che detesti così tanto dubitare di lei posso sollevarti da quel peso."

    ck "Fai del tuo peggio Hanabi."

    hb "Non serve che me lo dici. "
    play sound "audio/sfx/laugh.mp3"
    extend "Hananananana!"

    play sound "audio/sfx/teleport.wav"
    hide check
    hide hnb
    with squares

    stop music fadeout 10
    scene black with Dissolve(8)

    $persistent.second = True

    jump start

    return