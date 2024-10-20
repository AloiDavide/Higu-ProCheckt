init:
    $ lambdadelta = "Lambdadelta"


label returnal:
    stop music fadeout 2
    scene bus with Dissolve(2)
    play music "audio/cicadas.ogg" fadein 2
    play sound "audio/teleport.wav"
    show stop_time with Dissolve(2)
    show check nope p with squares


    ck "Grazie Akasaka, so che non puoi sentirmi, ma mi hai dato delle informazioni indispensabili."
    scene sonozroom with fade
    show oryou with dissolve:
        xpos -550
        yalign 1.0
        zoom 0.75

    show chibimion with dissolve:
        xpos 550
        yalign 1.0
        zoom 0.75

    ck "Tutta la faccenda del rapimento da solidità alla teoria Sonozaki."

    ck "Dopotutto, se ci fidiamo di quell'informatore, la loro matriarca ha dato dei chiari ordini al riguardo."

    scene police2 with fade
    show ooishi with dissolve:
        yalign 1.0
        zoom 0.75

    ck "Anche Ooishi sostiene questa teoria."

    ck "Lui ha lavorato nei dintorni di Hinamizawa per tutta la sua carriera. Quindi è molto familiare con le sue dinamiche."

    ck "Ma se davvero sono riusciti a organizzare un crimine del genere, non sono solo un semplice gruppo di yakuzari..."

    scene bus with fade
    show stop_time with dissolve
    show check p nope

    ck "Volevo continuare a investigare questo frammento, ma dopo che Akasaka lascia il villaggio la mia connessione con lui si disperde."

    ck "Con questa mia abilità nè lo spazio nè il tempo sono degli ostacoli. {w}Tuttavia sembra che io possa vedere solo eventi che riguardano Hinamizawa."

    play music "audio/shadow.mp3" fadein 5
    scene airport with fade
    ck "Infatti, sono riuscito a ristabilire la connessione con Akasaka in occasione della sua riunione con Ooishi, diversi anni dopo."

    ck "E lì ho scoperto qualcosa di cruciale."

    scene swamp with fade
    ck "Un'eruzione di gas (o chiunque sta usando questa copertura) ha sterminato la popolazione di Hinamizawa poco dopo la mia uccisione."

    ck "Larry... posso solo immaginare la tua preoccupazione."

    ck "Questo mi porta all'ultima informazione che ho ottenuto da questa escursione, la più cruciale di tutte. {w}Non sono l'unico a venire sempre ucciso nei giorni successivi al festival."

    scene sonozroom with fade
    show rika defa with dissolve:
        yalign 1.0
        zoom 0.75

    ck "Capelli blu, detta Rika, è senza dubbio una chiave di volta del mistero."

    show rika niya:
        yalign 1.0
        zoom 0.75

    ck "La bimba ha dei momenti in cui cambia completamente voce e personalità, come se fosse posseduta, o come se volesse farcelo credere."

    scene rikacg with fade
    ck "Un anno prima che iniziasse la serie di omicidi, conosceva per filo e per segno tutte le vittime{w}, e sapeva che l'ultima sarebbe stata lei."

    play sound "audio/voice/a.ogg"
    rika "Voglio soltanto vivere felice."

    play sound "audio/voice/b.ogg"
    rika "Non voglio morire."

    ck "Fossi stato al posto di Akasaka, non so se avrei saputo fidarmi di lei. {w}Anche di fronte ad una rischiesta di aiuto così chiara, probabilmente i miei sospetti avrebbero avuto la meglio."
    stop music fadeout 2
    scene bus with fade
    show stop_time with dissolve
    show check p yep
    play music "audio/core.mp3" fadein 3
    ck "Ma quando avrò risolto tutti i misteri, giuro sull'onore del BKG che salverò anche lei! Non ci saranno vittime nel mio lieto fine."

    ck "Grazie al mio potere ho ottenuto una abilità di spionaggio impareggiabile. {w}Quando riuscirò a padroneggiarla potrò vedere tutto, e nessuno potrà vedere me."
    show check smile

    ck "Si, questa è la mia {nw}"
    play sound "audio/truth.mp3"
    extend "{color=#480000}{b}prospettiva fantasma.{/b}{/color}"

    show check think nope
    ck "Quando stavo monitorando Keiichi mi è capitato alle volte di sentire i suoi pensieri e di sapere cose che solo lui saprebbe."

    ck "Adesso so il motivo, ma da lui non avrò altre informazioni, è troppo scollegato dalla verità."

    show check -think
    ck "Devo assolutamente riuscire a sintonizzarmi con qualcuno che che sa. Non una vittima, ma il colpevole stesso. {w}Un ottimo punto di inizio sarebbe capelli verdi, dopotutto in Wata ha praticamente confessato di avere organizzato gli omicidi."

    ck "Ma prima di tutto, torniamo da Bern per fare rapporto."

    stop music fadeout 2
    hide check with squares
    pause 1

    play music "audio/beat.mp3" fadein 2
    show fragplane with Dissolve(4)

    n """Ormai per quattro volte, lo spirito di Check era stato trascinato da frammento in frammento,
    costretto ogni volta ad assistere a tragedie e orrori senza una via di fuga in vista.

    Eppure lui sapeva che il peggio doveva ancora venire.

    Fù allora che Check pensò tra se e se, che forse forse, sarebbe meglio finirla quì. {w}Rinunciare ai richiami della strega, e tornare ad essere un semplice essere umano.

    Sarebbe tanto semplice quanto lasciarsi andare alla deriva in questo immenso mare.

    Qualcun altro scoprirà la verità, un altro detective arriverà prima o poi a risolvere tutti i misteri. {w}Non è certo una sua responsabilità.

    Ecco perchè in quel momento Check scelse la resa."""
    $prima_resa=False

label scelta:

    menu:
        "Mi arrendo":
            call resa from _call_resa
        "Non mi arrendo":

            n "Hehem... Ripeto. {w}Check scelse la resa perchè aveva perso la voglia di combattere."
            menu:
                "Mi arrendo":
                    call resa from _call_resa_1
                "Non mi arrendo":
                    n "{i}{size=20}Come ti dicevo, con lui non sarà così facile.{w}\n\nShhh! Zitta e stai a vedere.{/size}{/i}"
                    n "Ormai perso nei suoi dubbi, Check {b}non riusciva più a trovare{/b} la determinazione per andare avanti... {w}Letteralmente."
                    python:
                        import random
                        options = 6
                        while options>2:
                            choices = [("Mi arrendo", "resa") for n in range(options)]
                            choices[random.randint(0, options-1)] = ("Non mi arrendo","continue")
                            result = renpy.display_menu(choices)
                            if result == "resa": renpy.call("resa")
                            else: options -= 1

                    menu:
                        "Mi arrendo":
                            call resa from _call_resa_2
                        "ECCHEDDIAMINE ho detto che non mi arrendo!":
                            n "..."
                            play sound "audio/ahaha.wav"

                            show bern_kekkai with Dissolve(4)
                                #xalign 0.5
                                #yalign 0.5
                                #zoom 0.01
                                #ease 1.5 zoom 1.0
                            #pause 1.5
    call turnabout from _call_turnabout
    $ MainMenu(confirm=False)()

label resa:
    $ if prima_resa: renpy.call('resa_repeat')

    define c07 = Character("???", who_prefix="{color=#00D915}", who_suffix="{/color}")
    define h07 = Character("???", who_prefix="{color=#E29F00}", who_suffix="{/color}")
    default o7_color = "#00D915"

    play music "audio/determination.mp3"

    c07 "Ti arrendi cosi facilmente? getti la spugna alla prima avvisaglia? Patetico.{w} Ridicolo.{w} Dilettante."
    h07 "Non c'è bisogno di rimproverarlo così tanto, anche se... fermarsi proprio al giro di boa è davvero anticlimatico."
    h07 "Sinceramente pensavo che fossi all'altezza. Ho perso la scommessa."
    c07 "Ehehe! Check, sei patetico e debole, e se devo essere onesto anche un pò imbarazzante... ma non sarebbe divertente se finisse tutto qua, giusto?"
    h07 "Mi trovo d'accordo, per questa volta ti diamo noi una mano, ma non farti ingannare di nuovo."

    stop music fadeout 2
    $ prima_resa = True
    with Dissolve(2)
    play music "audio/beat.mp3" fadein 2
    jump scelta
    return



label resa_repeat:
    play music "audio/determination.mp3"
    h07 "Check, non vedi che ti stanno fregando? Clicca qualcos'altro."
    c07 "Se te lo devo spiegare a prova di idiota, Lambdadelta ti sta manipolando... sta interferendo con il framing per spingerti a prendere una decisione che non prenderesti."
    h07 "Insomma, resta determinato!"

    play music "audio/beat.mp3"

    jump scelta
    return


label turnabout:

    $lambdadelta = "λ¿¿¿δ"

    transform munch(rep=10000):
        linear 0.2 yoffset 30
        linear 0.2 yoffset 0
        repeat rep

    play music "audio/haruka.mp3" fadein 6

    scene bern_kekkai
    play sound "audio/teleport.wav"
    show check sor p at center with squares


    ck "Hey Bern senti che ho scoperto su capelli blu...."

    show check sus nope

    play sound "audio/munching.mp3"
    ld "Munch munch - nom nom - munch munch"
    pause 0.2
    show check fp at flip
    pause 1
    show check p at unflip

    ck "Cos'è questo chiasso! Chi è che mastica?"

    hide check


    image tnb = im.FactorScale("overlay/tea and biscuits.png",0.08)
    show table
    show tnb:
        yalign 0.7
        xalign 0.47
    show lamb pout behind table with dissolve:
        zoom 0.5
        xalign 0.5
        ypos 250

    n "Al tuo ritorno trovi una ragazzina bionda vestita di rosa seduta al tavolo di Bernkastel."

    ck "Capelli gialli!?"

    #play sound "audio/munching.mp3"
    show lamb nag unhappy
    ld "Chi hai chiamato... nom nom... capelli gialli."
    stop sound
    n "Non smette di ingozzarsi di biscotti neanche per risponderti, mentre li manda giù bevendo tè a fiumi."


    show check p at right


    show bern yoko at left

    ck "Ehm Bern... e questa chi diamine sarebbe? Una tua amica?"

    bk "Mentre non c'eri è venuta a fare visita... o forse è meglio dire che si è autoinvitata."

    bk "Le ho offerto la minima ospitalità fino a che non saresti tornato."

    ck "E questo è il risultato..."

    n "A te i biscotti non li ha mai offerti... ma a giudicare dalla scena devono essere fantastici."

    ck "Beh, piacere, puoi chiamarmi Check... E tu saresti?"

    play sound "audio/munching.mp3"

    ld "Lumhaheta."
    stop sound

    show check angry
    ck "Ehi mocciosa, nessuno ti ha insegnato a non parlare con la bocca piena?"

    play sound "audio/munching.mp3"

    ld "Nom nom - munch munch - ...Gulp!"
    stop sound

    ld "Che insolente! Osi chiamarmi mocciosa quando dal mio punto di vista sei tu il neonato."

    ld "E poi non è colpa mia se i biscotti sono così buoni! {w}Più ne mangio e più ne compaiono di nuovi."

    ld "Così non posso finirli al {b}100\%{/b}!"

    play sound "audio/munching.mp3"
    show lamb tantrum at munch

    ld "Dannati dolciumi, non avrete la meglio su di me! *Munch Munch Munch - Gulp*"

    bk "Sembra essere entrata in una qualche competizione con la sua stessa merenda."


    show lamb surprise at munch(0)
    stop sound

    ld "AAAAAH!"

    hide lamb with dissolve
    show lamb surprise pout with dissolve

    n "Improvvisamente si alza in piedi come se avesse ricordato qualcosa di importante."
    show check -angry
    ld "È vero! Non sono venuta quì per fare merenda!"

    ck "Ma davvero?"


    hide check
    hide bern
    with dissolve

    $ lambdadelta = "Lambdadelta"

    show lamb smugclose yep

    play music "audio/fishy aroma.mp3"
    hide tnb

    ld "Ehem. Check e Bernkastel! Quest'oggi mi rivolgo alla vostra attenzione per annunciare che io, Lambdadelta la strega della certezza, trovo la vostra collaborazione totalmente antisportiva e di cattivo gusto."
    show lamb unhappy nag
    ld "Questa sfida era tra me e Bern, ma quando lei stava per perdere ha portato dentro un elemento imprevisto come te. {w}Non sa proprio perdere, farebbe di tutto per arrampicarsi sugli specchi un po' più a lungo."
    show bern at left


    bk "Non ricordo di averti autorizzata ad accorciare il mio no---{nw}"
    show bern:
        linear 0.2 xalign -0.5
    show lamb:
        linear 0.2 xalign 0.1
        linear 0.2 xalign 0.5
    show lamb tantrum
    ld "E quando giustamente metto degli ostacoli per limitare la tua influenza, tu li ignori!!"

    ld "Che significa che puoi guardare i frammenti dalle teste degli altri? Non vale non vale non vale!!!"


    show check angry fp at flip, left
    show lamb unhappy at right



    ck "Hai frainteso qualcosa scricciolo, non è stata Bern a coinvolgermi. "

    show check shout
    extend"Sono quì di mia volontà perchè ho un conto in sospeso giù a Hinamizawa con un certo tuo omonimo."

    show lamb yep defa
    ld "Se è per quello puoi anche rinunciarci, tanto è una battaglia impossibile da vincere."

    ld "Una volta su 100 forse riusciresti a sopravvivere, ma anche in quel caso il tuo BKG sarebbe spacciato. {w}Fa parte della rete di certezza che io e quella persona abbiamo tessuto attorno a Hinamizawa."
    hide check
    show bern at left

    bk "Un lavoro magistrale, vorrei sapere il nome di questa altra persona per poterle dare una medaglia."

    show lamb close cat
    ld "Ma certo, si chiama.... "

    show lamb tantrum nag
    play sound "audio/boing.mp3"
    extend "HEY non vale! Ci sono quasi cascata!"

    show lamb -tantrum -nag

    ld "Ma ormai non funziona più, non avrete così facilmente il nome del colpevole."

    hide bern
    show check fp angry nope at flip, left
    ck "Non so quale sia il vostro obiettivo, ma il BKG non si abbasserà a vostro stumento. {w}Lo difenderò a tutti i costi."

    ld "Sai come negli scacchi esistono delle configurazioni di pezzi da cui è impossibile per uno dei due giocatori vincere?"

    ld "Vedi Check, il nostro gioco ha raggiunto quel punto di non ritorno, ecco perchè persino io non posso più farti riavere il BKG. {w}Al {b}100\%{/b}! Hahahahahaha!"
    hide check
    show bern at left
    bk "Allora non dovrebbero esserci problemi nel fare quello che vogliamo, tanto non porterebbe a nulla, o sbaglio?"

    show lamb worried
    ld "Eh? Ah, però dobbiamo comunque essere leali fino alla fine."

    hide bern
    show check fp at flip, left

    ck "Ci stai dicendo che anche se ora andassi a rivedere tutti i frammenti da dieci punti di vista diversi non cambierebbe il risultato del tuo piano perfetto."

    ck "Allora ci possiamo salutare Lambda, la festa è finita."

    ck "Sai, visto che non ho niente da fare mi sa che andrò anch'io a fare un pò di turismo come Akasaka. {w}Turismo mentale, si intende."

    show lamb tantrum nag at munch(5)
    ld "AAAAH! Eddai eddai eddai seguite le regole! Waaah."

    hide check
    show bern at left
    bk "Oh cielo, l'hai fatta piangere."

label turnabout2:
    scene bern_kekkai
    stop music fadeout(4)
    show lamb tantrum nag at right
    show check fp sus nope at flip, left
    ck "Puoi anche smettere di comportarti come una bambina viziata."
    ck "Non mi puoi fregare con la carineria, so che sotto la maschera sei più subdola di come sembri."

    ld "......."
    play music "audio/nighteyes.mp3"

    show check angry worried
    show lamb mal evil
    ld "*cackle cackle cackle*"

    ld "Sembra che non hai ancora capito il messaggio quindi sarò più chiara."

    show lamb mad fury
    ld "Abbassa la cresta, intruso! {w}Sparisci dalla mia vista prima che ti cancello dalla faccia della terra."


    show lamb smugclose smirk
    ld "Questo gioco che io ho organizzato sta per volgere al termine."

    ld "Il re di Bern è con le spalle al muro, e ormai cadrà nel giro di due o tre frammenti. {w}Mentre il mio re è ancora solidamente arroccato dietro tre impenetrabili difese."

    ld "Nessuno può sfuggire al destino scelto. {w}Ormai solo un miracolo ribalterebbe il risultato."
    show lamb mal evil
    ld "Per miracolo si intende un fattore oltre ogni previsione che trasforma la certezza in incertezza."

    show lamb mad fury

    ld "Una cosa del genere non può essere tollerata nel mio mondo."

    show check neutral smile
    ck """Hehehahaha. Hai sentito Bern?

    La mocciosa pensa che io faccia miracoli, deve avermi scambiato per Gesù o per il Buddha.
    """
    show check angry shout

    ck "Ma sfortunatamente per te Lambda... non sono un pacifista nè ho nessuna intenzione di porgere l'altra guancia."

    show check angry nope
    ck "Visto che sei venuta di persona a farti pestare ci penserò io a rimandare i tuoi resti al frammento da cui vieni."


    n """Ti prepari a sferrare un attacco contro Lambdadelta. {w}Strega o no, l'avversario è molto più basso e gracile di te, non c'è motivo di esitare.

    Durante il tuo tempo da militare si stato addestrato al combattimento corpo a corpo, e da allora non hai mai trascurato l'allenamento.

    La distanza, la differenza di altezza, la disposizione dei mobili. {w}In una frazione di secondo valuti tutti i fattori dell'ambiente e selezioni la mossa più efficace dal tuo repertorio."""


    show lamb:
        xalign 1.0
        linear 0.4 xalign 0.5

    show check fp at flip:
        xalign 0.0
        linear 0.2 xalign 0.4

    pause 0.2

    show check behind lamb:
        xalign 1.2
        linear 0.2 xalign 0.7

    pause 0.3
    n "Approcci il nemico dalla sinistra, ma è soltanto una finta, e un attimo dopo ti ritrovi alla sua destra. {w}Ormai è fatta, il tuo attacco non può più mancare."

    show frag_lines
    show lamb scary psycho with vpunch

    play sound "audio/zbiin.ogg"
    queue sound "audio/ahaha.wav"

    show red with Dissolve(5)

    hide frag_lines

    n """Il tuo campo visivo è compromesso... deve aver fatto qualcosa.

    Nonostante l'inconveniente cerchi di mandare a termine la presa.

    Ma ti accorgi che le tue braccia non sono dove dovrebbero essere. {w}No, nessun pezzo del tuo corpo è più nella posizione giusta."""

    play sound "audio/chishibuki.ogg"
    show red with vpunch
    n "Incapace di reggerti in piedi ti accasci sul pavimento, ormai poco più che un mucchio di poltiglia. {w}Decisamente un cadavere ma ancora del tutto cosciente."


    bk "Check, per quanto hai intenzione di rimanere in quello stato? {w}Non dirmi che ti credi ancora un essere umano."

    bk "Alle esistenze come noi non si applica il concetto di vita e di morte. Non è possibile per una strega sottomettere un'altra strega con la violenza."

    bk "...Vedo che stai avendo qualche problema. D'accordo, per questa volta ti darò una mano io."

    show bern behind red at flip, right
    show lamb mal evil behind red at center
    show check worried behind red at flip, left
    hide red with Dissolve(4)


    pause 1

    ck "Haah, uff, haah."

    show check nope

    ck "Hai sentito? Le tue minacce sono vuote. {w}Non puoi eliminarmi, e quindi cerchi farmi rinunciare per vie traverse."

    ck "Anche prima, eri tu la voce che ho sentito mentre tornavo vero?"

    ld "Ma che bel passo in dietro, ho sentito male o un momento fa hai dichiarato che mi avresti rimandata indietro a pezzi?{w} E ora invece sei completamente sulla difensiva."

    ck "Dì quello che vuoi, ma anche se puoi imporre regole su quello che faccio ma non mi puoi cacciare via."
    show check yep
    ck "Vuol dire che nonstante tutto non puoi fare nulla contro la nostra superiorità numerica."

    show lamb psycho scary
    show check worried
    ld "Se solo lo volessi potrei potrei farti assaggiare una tortura tale da convincerti ad abbandonare la partita in un secondo."

    show lamb cat defa
    play sound "audio/boing.mp3"
    stop music fadeout 4

    ld "Ma c'è una soluzione di gran lunga più interessante."


    ld "Se lei può avere un servo aiutante, non vedo perchè non possa averne uno io."
    show lamb yep close
    ld "Abracabula magicadabra. {w}Palesati mia pedina."

    play sound "audio/thunder.wav"
    scene bern_kekkai with dissolve
    n "Sul tavolo del salotto si materializza un cerchio magico, e l'energia che ne fuoriesce fa cadere l'intero servizio da tè."

    n "Infine, dal cerchio magico fuoriesce un losco figuro."
    play music "audio/black liliana.mp3"
    $Hanabi = "???"
    show hnb smirk at center with squares

    hb "HANANANANA! Finalmente un po d'aria fresca."
    show hnb at right
    show check fp at flip, left

    ck "Ci mancava solo un trap."

    ck "E tu chi saresti, sentiamo?"

    hb "Per farla semplice, sono te ma più forte, Check. {w}Come tu lavori per la goth apatica, io lavoro per la Mussololi quì presente."

    show hnb ohno nope
    show lamb unhappy nag at center
    play sound "audio/bzz.mp3"
    n "bzzzz"

    ld "{cps=*0.2}LA-M-B-DA{/cps}!"

    show hnb smug nope
    hb "Ho capito, ho capito. {w}Non ti stanchi proprio mai eh?"

    hide lamb

    show hnb yep
    hb "Beh, sentita la notizia? Pare che io e te ci scontreremo."
    show hnb fury fist
    hb "Naturalmente, è inutile dire che la mia entrata in scena marcherà la tua fine."

    ck "Vedo che le minacce vuote sono un vostro vizio.{w} Hey, ti hanno mai detto che la mimetica non aiuta quando la tua testa arancione risalta più di un cono stradale?"
    show hnb -fury -fist smirk
    hb "Hah, e tu invece ti sei visto con quel cappotto {i}cringe{/i}? Credi di essere in Matrix? {w}Evidentemente non hai il taste minimo necessario per capire quanto questo outfit sia {b}CHAD{/b}."

    ck "Si come no. Non si capisce neanche se sei uomo o donna."

    show hnb taunt
    hb "Vuoi davvero scoprirlo?"

    show check angry shout
    ck "HNNOOOOH!"

    show check sus nope
    ck "...Aspetta{w}, questa conversazione ha un qualcosa di familiare..."
    ck "Chi sei?"
    show hnb -taunt
    hb "Non mi dire che è bastato un cambio di acconciatura per farti dimenticare di me."
    show hnb -fist cigar smug yep

    hb "Dopo tutto quello che abbiamo passato. {w}Ricordo ancora come ieri quando mi chiamavi {b}Sir{/b}."
    show check worried -sus
    ck "Impossibile.....{w} Hanabi???"
    $Hanabi = "Hanabi"


    hb "Ce ne hai messo per capirlo, hanananana."
    hide check
    show bern at left
    bk "Check, è per caso un tuo amico?"
    hide bern
    show check fp nope at flip, left
    ck """Lo è stato... {w}o almeno è quello che credevo un tempo.

    Siamo stati compagni nell'esercito, nonostante fossimo entrambi giovani riuscimmo a ottenere dei posti in una squadra di anti terrorismo d'elite."""

    show hnb nope fury fist -cigar

    hb """Tanta fatica sprecata. Visto che al punto di svolta della nostra carriera hai voluto a tutti i costi abbandonare la tua posizione nell'esercito.

    Dicevi di volere fondare la tua organizzazione. {w}Che dovevi adoperarti per proteggere il pudore e la morale."""

    show hnb sneer -fist

    hb """Io ti ho avvertito di quanto cringe e patetica fosse la tua idea, ma tu niente, come al solito non mi hai dato retta.

    Ed ecco il risultato, ancora peggio del previsto. Hananananananana."""

    ck "Non mi pento minimamente delle mie scelte. {w}E tu invece, mi sorprende che sei ancora vivo."

    hb "Non sono quì per i ricordi, è il momento di fare i conti una volta per tutte."

    show check yep angry
    ck "Ora che ci penso, il nostro ultimo scontro è finito in pareggio.{w} Non sono il tipo che si tira indietro davanti a una sfida, fatti sotto."

    show blue_aura at left:
        xoffset 0
        yoffset 30
    show yellow_aura at right:
        xoffset 90
        yoffset 30
    play sound "audio/super saiyan.mp3"
    play music "audio/aura.mp3"

    show debris behind check, hnb:
        ypos 1080
        linear 1 ypos 0

    pause 1
    with Shake((0, 0, 0, 0),6.0, dist=4)

    hide blue_aura
    hide yellow_aura
    hide debris
    hide hnb
    hide check

    show bern at left
    show lamb frown pout at right
    play sound "audio/zbiin.ogg"
    play music "audio/umineko organ.mp3"
    with vpunch

    ld "Ma allora siete veramente sordi."

    bk "Come stabilito pochi minuti fa, il combattimento corpo a corpo non ha nessuna utilità in questo contesto."
    show lamb cat

    show lamb smugclose
    ld "Rimane il fatto che anche io adesso ho un servitore, ed è molto più forte del tuo Bern."

    ld "Con i suoi mirabolanti poteri ostacolerà ogni vostra mossa fino alla mia vittoria."

    bk "Devo prendere il fatto che hai creato un'imitazione come dimostrazione che stai accettando Check?"

    show lamb pout frown

    ld "Mi sono soltanto adattata ai tuoi trucchi. Non farti strane idee."

    bk "Molto bene, e ora che la cosiddetta inguistizia dalla nostra parte è risolta possiamo procedere con le nostre condizioni."

    bk "Ovvero bandire la creazione di regole con il tuo potere."

    show lamb worried
    ld "Ueh? E perchè?"

    bk "Non dovrebbero servirti a nulla ora che non abbiamo più un vantaggio scorretto."

    bk "O hai di nuovo intenzione di fare una mossa all'ultimo minuto fuori dal tuo turno?"

    show lamb lookaway
    ld "P-perchè mai dovrei barare quando so di vincere?"

    ld "Il giallo è più una sorta di arbitro, ecco..."

    hide lamb
    show check p sus nope at right
    ck "Pensavo di chiederlo da un po', ma cosa significa il testo colorato?"

    bk "Detto in modo semplice, le frasi che contengono il potere di una strega appaiono di un colore specifico a chi le ascolta."

    bk "Gli specifici esiti e limitazioni cambiano da strega a strega, ma gli effetti tendono a essere permanenti, quindi è bene non farne un uso spropositato."

    show check at center with move
    show check fp at flip
    show bern yoko
    show lamb frown nag at right with dissolve
    n "..........."
    ld "Hey non guardatemi in quel modo! Io uso sempre i miei poteri in modo responsabile!"
    hide bern
    show lamb smugclose mal
    show check at left

    ld "In quanto strega della certezza, ciò che dico in giallo diventa verità inconfutabile. Posso prendere qualsiasi probabilità che non sia 0\% e renderla {b}100\%{/b}!"

    show lamb surprise yep
    ld "Ci sono! Mi basta fare una regola che mi da il diritto di fare regole. {w}Come ho fatto a non pensarci prima!"

    show lamb at center
    show hnb at right

    hb "La classica decisione all'araba."

    ck "......"


    stop music fadeout(4)
    hide hnb
    show check think nope
    show lamb unhappy pout at right


    ck "Adesso ho capito. {w}Si, ho capito benissimo come ragioni."
    show check -think
    ck "Tu arrivi dal nulla e ci accusi di non stare alle regole che hai deciso da sola.{w} Quando le cose non ti vanno a genio le cambi, e quanto non le puoi cambiare fai appello alla sportività."
    ck "\"La palla è mia quindi decido io.\" Questo è il tuo motto."
    ld "E cosa ci sarebbe di male?"


    show check think
    n "............................."


    ld "Hey, non zittirti all'improvviso. Che cosa hai in mente?"

    with Shake((0, 0, 0, 0), 4.0, dist=5)
    show check angry
    pause 0.2

label turnabout3:
    $Hanabi = "Hanabi"
    play sound "audio/attorney/take that.mp3"
    play music "audio/attorney/cornered_sudden.mp3"
    scene black
    call defence from _call_defence
    show check shout with sshake

    ck "Sei tu Lambda a non avere la mencheminima sportività!"

    call witness from _call_witness
    with sshake
    ld "Gaah! {w}Come.. come ti permetti!"


    call berndef from _call_berndef
    bk "Per fortuna l'hai fermata, ma... {i}era veramente necessario evocare un intero tribunale?{/i}"


    call defence from _call_defence_1
    ck """

    Tu dici di avere tutto sotto controllo! Ma io non me la bevo!

    La verità è che sai di poter perdere. Per questo hai iniziato a metterci i bastoni tra le ruote, prendendo pure il rischio di annunciare la tua presenza!

    In realtà sei nel panico in questo stesso momento!
    """


    call prosecution from _call_prosecution
    play sound "audio/attorney/objection sound.mp3"
    show hnb smug yep with sshake

    hb "OBIEZIONE!"
    show hnb close
    hb "Le accuse sono infondate vostro onore. L'imputata è innocente!"

    call defence from _call_defence_2
    show check shout
    ck "Eppure il suo comportamento non si spiega altrimenti!"

    call prosecution from _call_prosecution_1
    show hnb smirk


    hb "Non capisci? È logico Check. La mia padrona ha un potere assoluto capace letteralmente di rendere inevitabile qualsiasi evento lei voglia."

    hb "Che motivo avrebbe di scendere a patti con elementi patetici come voi?"

    hb "Ciò che lei prova nei vostri confronti non è timore, ma indignazione."

    show hnb fury sneer
    hb "Schiacciare ogni vostra fonte di speranza sul nascere serve a punire l'arroganza che dimostrate nel pensare di poter combattere alla pari."

    hb "Perchè non provate a eguagliarci in forza prima di chiedere dei diritti?"

    call defence from _call_defence_3

    ck "Se credete di essere gli unici con delle armi vi sbagliate alla grande."

    ck "Avevo pensato di tenerlo segreto, ma vedo che le notizie viaggiano in fretta."

    show check shout
    ck "Ebbene si Lambda, col la mia {nw}"
    play sound "audio/truth.mp3"
    extend "{color=#480000}{b}prospettiva fantasma{/b}{/color} non ho più nessun limite alle informazioni che posso raccogliere."

    ck "È questo che temevi più di ogni altra cosa, non è vero?"

    call witness from _call_witness_1
    show lamb pout with sshake
    show lamb yep
    ld "Hahahahahahaha. Ammetterò che mi ha sorpreso, ma non penserai veramente che basti quello per raggiungere la vittoria, vero?"

    call defence from _call_defence_4
    ck "Qualcuno in quel dannato villaggio deve pur sapere cosa succede veramente. Mi basterà seguire lui!"

    call witness from _call_witness_2
    show lamb mad fury
    ld "Hinamizawa è piena di illusioni. Potresti seguire una pista fino alla fine solo per scoprire che il filo conduceva ancora più a fondo nel labirinto."

    call berndef from _call_berndef_1
    bk "Pensa un po' non me ne ero mai accorta.{w} Ci puoi fare un esempio?"

    call witness from _call_witness_3
    show lamb smugclose yep
    ld "Beh, il finale di Watangashi può sembrare ovvio quando in realtà...{nw}"

    call prosecution from _call_prosecution_2
    show hnb ohno nope
    play sound "audio/attorney/objection sound.mp3"
    hb "Stop all'interrogatorio! La mia cliente eserciterà il diritto di restare in silenzio."

    call witness from _call_witness_4
    show lamb tantrum nag
    ld "Waaaa! Non è vero! Non ci stavo cascando di nuovo!"

    call prosecution from _call_prosecution_3
    show hnb nope
    hb "Ammesso che Lambda la smetta di regalarvi informazioni."

    show hnb yep
    hb"Cosa ti fa pensare che riuscirai a risolvere questo mistero?"

    call defence from _call_defence_5
    ck "Sai benissimo che non ti conviene sottovalutare le mie capacità."

    call prosecution from _call_prosecution_4
    hb "Riformulo la domanda."

    show hnb sneer fury
    hb "Anche con tutte le informazioni davanti a te, cosa ti fa pensare che una soluzione ci sia?"

    show hnb smirk -fury
    hb "Hai mai pensato che la spiegazione possa davvero essere sovrannaturale?"

    hb "Dopotutto esistono le streghe e il multiverso, a questo punto un dio che maledice non è poi così assurdo."

    call witness from _call_witness_5
    show lamb evil smirk
    ld "Specialmente se è la strega della certezza a renderlo verità."


    call prosecution from _call_prosecution_5

    hb "Non siamo in un romanzo giallo, nessuno ha preparato ad arte gli indizi per farli trovare al detective e al lettore. "
    play sound "audio/attorney/take that.mp3"
    extend "Questo è il mondo reale."

    call witness from _call_witness_6
    show lamb defa cat
    ld "Ma con giusto un pizzico di magia."

    call defence from _call_defence_6
    show check angry shout with sshake

    ck "Sarai anche capace come militare, ma di investigazioni non ne sai niente Hanabi."

    ck "So bene che nel mondo reale non avrai mai tutti gli indizi. Ecco perchè In ultimo é l'intuito a portarti alla soluzione."

    call prosecution from _call_prosecution_6

    hb "Il che rende la tua abilità non più così assoluta."

    play sound "audio/attorney/take that.mp3"
    show hnb fury sneer with sshake
    hb "Colpito e affondato."


    call defence from _call_defence_7
    show check nope
    ck "Grrrrr.{w} Hey Bern, digliene quattro anche tu!"



    call berndef from _call_berndef_2

    bk "Esistono delle verità che neanche una strega può sopraffare. {w}Un gioco senza condizione di sconfitta non è un gioco."

    play sound "audio/truth.mp3"
    bk "Per quanto improbabile, {color=#0000cf}una soluzione esiste{/color}."
    bk "Se questa sia naturale o sovrannaturale non ci è ancora dato sapere."

    call defence from _call_defence_8
    ck "Ha ragione! Che senso avrebbe giocare un gioco che non si può perdere?"

    call prosecution from _call_prosecution_7
    show hnb smirk
    hb "Oh, ma la possibilità di perdere esiste. "
    show hnb fury smirk
    extend "Solo che è pari a ZERO!"
    show hnb yep -fury
    hb "È la stessa filosofia del presidente di un certo club a Hinamizawa. Vittoria a tutti i costi."
    hb "Qualche problema?"

    call berndef from _call_berndef_3
    play sound "audio/truth.mp3"
    bk "Per quando difficile, {color=#0000cf}la soluzione può essere raggiunta{/color}."
    bk "Lo garantisco nel nome di Bernkastel, strega dei frammenti."


    call defence from _call_defence_9
    show check yep
    ck "Capisco, quando parla in blu non puoi controbattere."

    play sound "audio/attorney/take that.mp3"
    ck"Che cosa hai da dire adesso, Hanabi?!"


    call prosecution from _call_prosecution_8
    play sound "audio/attorney/objection sound.mp3"
    show hnb fury sneer with sshake
    hb "Avvocato, lei è un incompetente!"

    call defence from _call_defence_10
    play sound "audio/attorney/take that.mp3"
    show check shout with sshake
    ck "Signore, lei è un deficiente!"
    ck "Perchè devo discutere con questo clown?"

    call prosecution from _call_prosecution_9
    play sound "audio/attorney/objection sound.mp3"
    show hnb fury sneer with sshake
    hb "Tu non sei un clown, sei l'intero circo."


    call defence from _call_defence_11
    play sound "audio/attorney/objection sound.mp3"
    show check angry shout with sshake

    ck "Vostro onore dica qualcosa, gli argomenti della difesa non hanno nessun senso!"

    call judge from _call_judge
    show lamb smirk

    ld "Ha abbastanza senso per me. {w}Obiezione rifiutata!"

    call defence from _call_defence_12
    show check shout
    ck "COSA? Ora sei anche il giudice?"

    call judge from _call_judge_1
    show lamb bent b_yep

    play sound "audio/gavel.mp3"
    bent_ld "*bam* *bam* Silenzio in aula!"


    call prosecution from _call_prosecution_10
    hb "Hai capito adesso? Sei ancora convinto di avere una scelta oltre che stare al nostro gioco?"

    call judge from _call_judge_2
    show lamb frown pout
    ld "Mhh. Questo gioco di ruolo era divertente all'inizio ma ora mi sto annoiando, non potete fare più in fretta?"

    call defence from _call_defence_13
    ck "Che c'è, non ti basta dire la parola magica per vincere?"

    ck "Forse il tuo potere non è così assoluto come vuoi farci credere."

    ck "Cosa ti rende davvero tanto superiore?"

    call berndef from _call_berndef_4
    stop music fadeout 2
    bk "Asp..."


    call judge from _call_judge_3
    show lamb evil smirk
    play music "audio/gallery of madness.mp3"
    ld "Proprio non vuoi capire lo stato della situazione in cui sei heh."
    show lamb psycho
    ld "Molto bene {w}se è il giallo che vuoi, è il giallo che avrai. {w}Delle parole che non si limitano a riflettere la realtà come le vostre, ma capaci di plasmarla......."

    play sound "audio/truth.mp3"
    ld "{i}{color=#ffe674}Per il resto del processo l'accusa non può controbatere.{/color}{/i}"

    call defence from _call_defence_14
    show check nope
    ck "{color=#ffe674}......................{/color}"

    call berndef from _call_berndef_5
    bk "{color=#ffe674}......................{/color}"

    call judge from _call_judge_4
    show lamb bent b_yep
    bent_ld "Che c'è, la strega vi ha mangiato la lingua?"

    call prosecution from _call_prosecution_11
    show hnb smirk
    hb "Hanananana. Vostro onore, l'accusa non sembra avere ulteriori commenti."

    call judge from _call_judge_5
    show lamb close
    ld "Proceda pure con la replica conclusiva, avvocato Hanabi."
    stop music fadeout 3


    call prosecution from _call_prosecution_12
    show hnb close
    hb "Con piacere."
    play music "audio/attorney/telling the truth.mp3" fadein 4
    show hnb -close

    hb """Onorevoli giurati, quanto è emerso da questo processo indica la chiara innocenza della mia cliente.

    Delle inguste calunnie sono state mosse nei suoi confronti. {w}Accuse di non sportività, e tentativi di limitare la sua assoluta influenza."""

    call judge from _call_judge_6
    show lamb smirk
    with Dissolve(1)

    hb "Chi ha bisogno regole condivise? {w}Anche quando le fondamenta stesse del gioco vengono mutate a suo proprio piacimento, non è forse una dimostrazione di genio strategico?"
    hb "Dopo tutto, chi può competere con la mente illuminata della signora Mussololi? È un'innovatrice, una visionaria, maestra del capriccio."
    show lamb frown pout
    hb "Con la grazia di un calciatore che fa gol a porta vuota e poi si porta via il pallone. {w}Con la caparbietà del bambino che batte in una sola mossa sasso carta e forbice facendo una pistola con le dita."

    hb "E i comuni mortali possono solo immaginare quale possa essere la sensazione provata da chi ha raggiunto simili vette di eccelsa meschinità."
    show lamb worried
    hb "Il perchè è presto detto. {w}Le persone inferiori portano con se una zavorra chiamata coscienza, ma lei è libera da tali pesi, e si libra nel cielo come un leggiadro avvoltoio."

    scene def_stand
    show check fp angry at flip:
        ypos -40
    show bern:
        xalign 0.5
        ypos -90
    show lawyer_table
    with Dissolve(1)

    hb "Il concetto stesso di morale è banale per una persona così incapace di attenervi, come un castello di sabbia da schiacciare con i propri piedi nudi."

    hb "Con l'astuzia di Caligola ed il genio strategico di Luigi XVI, niente può frapporsi tra Lambda ed il suo obiettivo."

    hb "Come l'araba fenice che brucia nelle fiamme della rinascita, ogni minuscolo taglietto la spingerà a creare un'altra regola."

    hb "Martin Luther King jr, Mahatma Gandhi, Nelson Mandela. {w}Tutti loro sarebbero fieri di come evita il benchè minimo conflitto ad ogni costo."

    call prosecution from _call_prosecution_13
    with Dissolve(1)
    hb "Una luce di ispirazione per ogni persona che aspiri alla grandezza! {p}Il genio del gioco! {w}La strega della certezza!"


    stop music fadeout 2
    hb "Sia lodata Mussololi nei secoli dei secoli amen."

    show hnb close


    hb "Vostro onore, non ho niente da aggiungere........"

    play sound "audio/cri cri.mp3"

    show hnb nope
    pause 3
    stop sound

    call judge from _call_judge_7
    show lamb bent b_yep b_psycho

    n "............................................................................................................."

    call prosecution from _call_prosecution_14
    show hnb ohno nope
    n '.................'


    call berndef from _call_berndef_6
    play sound "audio/truth.mp3"
    bk "{color=#0000cf}Codarda.{/color}"

    play music "audio/attorney/cornered_sudden.mp3"
    call judge from _call_judge_8
    show lamb tantrum nag

    with sshake

    ld "Perchè sono sempre tutti contro di meeeeeeeeee!"

    show lamb psycho pout
    ld "Ascolta attentamente pedina, ti darò solo una possibilità. {w}Fallisci nel fermare Check e sarai smantellato all'istante!"

    ld "A differenza di loro ti ho creato io, non pensare per un istante che non possa distruggerti."

    show lamb tantrum nag
    ld "E adesso fuori dal mio tribunaleeeeeeeee!!!"

    call prosecution from _call_prosecution_15
    show hnb ohno
    n "In un'istante, esattamente sotto Hanabi si apre una botola senza fondo dove prima c'era solo il pavimento."

    play sound "audio/goofy yell.mp3"
    show hnb:
        easeout 1 ypos 2000

    hb "HANNAAAAAAAaaaaaaaa..."

    stop music fadeout 4

    play sound "audio/glass crack.mp3"
    show frag_lines with dissolve


    scene bern_kekkai with Fade(3, 0, 3, color='#a26ccc')


    play music "audio/attorney/maya fey.mp3"

    show lamb worried nag with dissolve
    ld "E voi due, che sia chiaro, niente di quello che ha detto è vero."

    show lamb lookaway pout

    ld "Non è che avessi paura di perdere, ecco si, stavo solo testando come avreste reagito."

    ld "Tranquilli, ho finito di aggiungere regole, tanto non ne avrò più bisogno."
    show lamb -lookaway
    ld "Potete gioire."

    show lamb at right
    show bern at left
    bk "Una promessa lascia il tempo che trova, se davvero accetti le nostre condizioni usa il tuo stesso potere per rendere l'accordo vincolante."

    ld "Mmmh. E sia."
    play sound "audio/truth.mp3"
    ld "{i}{color=#ffe674}Ogni futuro cambio alle regole dovrà essere di comune accordo tra Lambdadelta e Bernkastel.{/color}{/i}"

    ld "Ecco, contenti? Fate come vi pare, tanto il mistero è al {b}100\%{/b} irrisolvibile. Chiaro?!"

    hide bern
    show check fp nope at flip, left
    ck "Aspetta, hai dimenticato di annullare le regole già presenti."

    show lamb frown pout
    ld "Te l'ho già detto, una volta che rendo certo un fatto nemmeno io lo posso revocare."

    show lamb -frown -pout
    ld "Altrimenti con che faccia potrei chiamarmi la strega della certezza?"

    play sound "audio/truth.mp3"
    ld "{i}{color=#ffe674}Il giallo non può contraddire se stesso.{/color}{/i} {w}E questo è un fatto."

    show check angry
    ck "Hey! Ma allora come..."

    hide lamb
    show check -angry
    show bern at flip, right

    bk "Per quella questione lascia fare a me. {w}Ho un'idea che voglio testare, ma ci vorrà del tempo."

    ck "Come al solito, se si tratta di stregoneria lascio fare a te."

    ck "Inoltre pare che avrò altro di cui occuparmi."

    hide bern
    show lamb at right
    ck "Lambda, parliamo chiaro, cosa hai intenzione di far fare ad Hanabi?"

    ld "Non essere nervoso, non credo che la mia proposta sarà così cattiva per voi."

    hide check
    show bern at left
    bk "Penso di sapere dove vuoi andare a parare. {w}Il tuo problema era la presenza di Check come elemento esterno, ma se venisse integrato nel gioco sotto regole condivise nessuno avrebbe motivo di lamentarsi."


    ld "Ebbene si Check, visto che se sei così ostinato a intrometterti in una lotta tra streghe, ti ho portato un rivale per tenerti compagnia."

    show lamb smugclose
    ld "Ma quando sei a Roma fai come i romani, non duellerete a pugni, ma a deduzioni e dibattiti!"



    show lamb smirk defa
    ld "Così saremo di nuovo solo io e te, Bernkastel."

    ld "Il tuo zuccone se la vedrà faccia a faccia con il mio zuccone, nessuno ci potrà disturbare."

    ld "E per quando torneranno avrò già vinto da un pezzo! Hahahahaha."

    bk "Lasciando da parte il modo in cui è posta, penso che questa proposta sia la prima cosa ragionevole che ti sento dire."

    hide lamb
    show bern at flip, right
    show check fp sus nope at flip, left
    ck "Insomma, volete che io e Hanabi facciamo un altro processo?"


    show check -sus
    bk "Hai dimenticato il nostro obiettivo? Risolvere i misteri di Hinamizawa."


    show lamb at center
    ld "E il nostro è fare in modo che non succeda."


    ld "Avrai la libertà di esaminare un frammento come più preferisci, e alla fine dovrai formulare una teoria."

    ck "Niente trucchi e rimangiamenti?"

    bk "Sarò io ad assicurarmente personalmente."

    ld "Ma il tuo avversario non starà di certo a guardare, cercherà di seminare rumore e confusione nelle tue deduzioni."

    show lamb psycho mad
    ld "Altrimenti sa bene cosa lo aspetta."

    hide bern
    show lamb fury smirk at right
    ld "Dopo quanto mi ha dato sui nervi quel clown impertinente, ho quasi voglia di tifare per te."

    show lamb -fury cat
    ld "Mhhhhhh. {w}No, ora che ci penso mi stai abbanzanza antipatico anche tu."

    show check angry
    ck "Ricambio il sentimento in pieno."

    ld "Quantomeno ti lascerò scegliere per primo il campo di battaglia. {w}Scegli il frammento che vuoi."

    play music "audio/core.mp3"

    show check -angry shout
    ck "Non ho il minimo dubbio. Partirò da Watanagashi."

    ck "Non so ancora come mai capelli verdi sia sbroccata alla fine. {w}Lei dice di essere posseduta, ma quella storia non mi convince per diversi motivi."

    ck "Il modo più semplice di scoprire la verità è andare a osservare tutto il processo direttamente dalla sua testa."

    ld "Beh, buona fortuna a ritrovarlo in mezzo al mare di frammenti."

    show lamb worried

    show wata_prop with dissolve:
        yalign 0.5
        xalign 0.5
        zoom .25

    bk "Ecco un frammento quasi identico a Watanagashi."

    ck "Inizio a capire il perchè del tuo titolo Bern."

    ld "Dannazione! Lo avevi preparato in anticipo!"

    show lamb mal evil
    ld "Poco male."

    ld "Sembri sicuro di te. {w}Ma prima ancora delle abilità deduttive, mi chiedo se avrai il coraggio di osservare l'altro lato di quel frammento fino alla fine."

    ld "Non hai idea di quali scene orribili scoverai scavando troppo a fondo. Praticamente è una scatola di Pandora."

    show lamb close -mal
    ld "Per me ovviamente è dolce come un cofanetto di biscotti alla cannella."

    ck "Ormai ne ho viste di cotte e di crude, chi si spaventa più. Da quì!"

    show lamb -close

    show check yep fp at flip:
        xalign 0.0
        linear 0.5 xalign 0.5

    pause 0.5

    show check p at unflip, center
    show bern at left with dissolve

    bk "Spero che non deluderai le mie aspettative."

    ck "Alla prossima Bern, non essere troppo sbalordita quando tornerò con tutte le risposte."

    show lamb frown
    ld "Ok ok, scaduto il tempo per i saluti. {w}Partenza!!!"

    hide bern
    hide lamb
    with dissolve

    show check shout angry
    pause 1

    show sky_frag behind bern_kekkai



    show bern_kekkai:
        ypos 1080
        easeout 0.3 ypos 0


    image sky_frag_2 = im.Scale("bg/sky of frag.png", 1924, 1080)
    pause 0.3



    #----tentativi in corso di fare una cosa figa con lo sfondo che loopa mentre cade----

    define pushup = PushMove(1.0, "pushup")
    #show sky_frag:
        #ypos 1080
        #linear 1 ypos 0
        #repeat 4


    ck "UN ALTRA BOTOLAAAAAAAAAA?!"




    hide check with squares
    window hide
    show wata_prop:
        ease 2 zoom 1
    pause(2)
    hide wata_prop

    scene wata_prop
    show wata_frag behind wata_prop
    with Dissolve(1)
    show meakashi_frag with Dissolve(5)

    pause 1

    play sound "audio/doon.mp3"

    stop music fadeout 13
    $renpy.transition(vpunch)
    $renpy.call_screen('welcome_meakashi')

    return