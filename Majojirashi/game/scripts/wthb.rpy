init:
    $ yellow_witch = "λ¿¿¿δ"

image hinamizawa = im.Scale("bg/hinamizawa.png", 1920, 1080)
define hnb = Character("¿¿¿", who_color = "#cc4f33", what_style= "wide", who_style = "border")

#alternative music

label wthnb:
    #scene hinamizawa
    #show check
    #" "

    scene black with longFade
    stop music
    play sound "audio/teleport.wav"
    show vortex with dissolve



    pause 3

    play music "audio/golden sneer.mp3"

    yw "Vediamo... un po' di questo, un po' di quello."

    yw "Le orecchie dovrebbero funzionare..."

    yw "Hey, se mi senti annuisci."

    show vortex:
        ypos 1080
        linear 0.3 ypos 1030
        linear 0.3 ypos 1080

    pause 1

    yw "Visto? Un lavoro perfetto! *giggle* *giggle*"

    yw "Mentre per gli occhi... {w}Aaah, questo è difficile."

    show lamb black with Pixellate(2,5)

    yw "Basterà così per adesso."

    yw "Per finire la bocca. Questo è facile..."


    yw "E la mia nuova pedina è....."

    play sound "audio/thunder.wav"

    extend " completa! Ahahahahaha"


    hnb "Eccomi quiiiiiiii! Hanananananana!"

    yw "Pieno di entusiasmo vedo... questo è l' atteggiamento giusto! Pronto a servirmi?"

    hnb "Servirti? SERVIRTI? E perchè dovrei servirti! Non vedo l' ora di..."
    play sound "audio/bzz.mp3"
    extend "AAAAAAAAGH"

    show lamb blackB

    yw "Dicevi?"

    hnb "Ahahaha tutto chiaro dittatore-chan."

    yw "Ma che zuccone eh? Ahaha, proprio come me d'altronde!"

    show lamb black

    yw "Bene, ascoltami. Tu sei qui per un motivo specifico."

    yw "Sono attualmente impegnata in una partita con Bernkastel. {w}Una partita dove lei si rifiuta di arrendersi nonostante venga sconfitta ripetutamente..."

    yw "Ma ciò sta per venire a termine. {w}Il suo re è quasi esausto, e secondo i miei calcoli non rimangono più di 3 partite prima che si arrenda. {w}"
    play sound "audio/laugh.mp3"
    extend"Ho quasi vinto, una VITTORIA ASSOLUTA."

    hnb "Hanananananana! Una vittoria schiacciante dici? Ne sei proprio sicura?"

    yw "..."

    hnb "Hai la vittoria in pugno? E allora perchè mi avresti evocato, sentiamo? {w}Eh no ditatore-chan, qui c' è qualcosa che non mi torna."

    hnb "Te lo dico io, IN REALTà SEI IN DIFFICOLTÀ! Ho indovinato vero? Ehehehe."

    play sound "audio/bzz.mp3"

    hnb "Gyaaaah."



    show lamb blackB

    yw "Quattro punti su dieci. Se solo finissi di ascoltare ti sarebbe tutto chiaro."

    yw "Hai parzialmente ragione, non lo nego."
    show lamb black
    yw """ Il punto è questo;{w} Bernkastel ha impiegato una pedina a me sconosciuta con incredibili abilità, al punto che ha una minima possibilità di battermi.

    Questo è ovviamente inaccettabile. {w}Un 1\% di possibilità di perdere è troppo alto. Devo schiacciare Check."""

    hnb "Check?"

    yw "Ma mi stai ascoltando?! È il nome della pedina di Bern."

    hnb "Proprio un nome del cazzo ehehehehe."

    yw "Vero?! {w}Un assoluto maleducato senza alcuna attenzione nè per il decoro NÈ PER LO STILE!"

    play sound  "audio/teleport.wav"

    show check_prop with dissolve:
        xalign 0.5
        yalign 0.5
        zoom .25
    pause .5

    show check_prop:
        linear 1 zoom 1

    pause 1.5

    yw "Non vedi come si veste? {w}Non vedi come si comporta? {w}Un assoluto debosciato!"

    hnb "Guardalo! Oddio che fissato, nessuno gli ha spiegato che in estate si può togliere la felpa? Sceeeeeeemo!"

    yw """Già già! Ma scemo e maleducato come è, lui è comunque in grado di mettere le mani sul nostro piano e frantumarlo!

    Nel precedente frammento HA CAPITO DOVE SI TROVA LA BASE OPERATIVA! Ma ti rendi conto?

    Fortunatamente ha perso la memoria delle ultime ore, e quindi non ha capito la parte più importante!

    MA CAPISCI LA SITUAZIONE?"""

    hide check_prop

    hnb "Huuuuuh... Dittatore-chan mi sa che non mi hai spiegato niente! Ehehehehe!"

    yw "Usa il mio nome zuccone, mi chiamo Lamdadelta."

    $ yellow_witch = "Lambdadelta"

    hnb "Certo Dittatore-chan! {w}Dunque aggiornami! Se è qualcosa che ha capito pure Check non può essere tanto difficile."

    yw "Mmmmh... ok intelligentone, non sarebbe divertente se ti spiegassi tutto, no?"

    play sound  "audio/teleport.wav"
    show oni_prop with dissolve:
        xalign 0.1
        yalign 0.4
        zoom .25

    show wata_prop behind oni_prop with dissolve:
        xalign 0.5
        ypos 0
        zoom .25

    show tatari_prop behind wata_prop with dissolve:
        xalign 0.9
        yalign 0.4
        zoom .25

    yw "Perchè non butti un occhio su questi tre frammenti e mi dici quello che pensi? Lascia stare Check per il momento."

    hnb "Mmmmh..."

    #zoom su Onikakushi

    show oni_prop:
        linear 1 xalign 0.5 zoom 1 yalign 0.5

    pause 1

    hnb """Secondo me qui è evidente che Keiichi non ci sia di testa.

    Guardalo, prende a mazzate la cassetta delle lettere! Si lancia nel fango!

    Detto questo c'è qualcosa che non mi torna sulla questione di Rena e Mion... {w}non è una questione di comportamenti... non è coerente!"""


    show oni_prop behind wata_prop, tatari_prop:
        linear 1 xalign 0.1 yalign 0.4 zoom .25
    pause 1
    yw "Non male zuccone, passiamo al prossimo."

    yw "Il primo era semplice, mentre il secondo frammento è.... {w}certamente più semplice in un senso, ma anche più intricato."

    #zoom su Watanagashi

    show wata_prop:

        linear 1 xalign 0.5 zoom 1 yalign 0.5
    pause 1
    hnb "Mmmmmmh.... quì gli eventi sembrano molto lineari... cosa c' è da capire?"

    hnb "Aspetta... {w}Ma la storia di Mion alla fine è completamente incoerente! {w}Niente di quello che ha detto torna!"

    hnb "la storia che racconta sulla famiglia Sonozaki va in conflitto con quello che sappiamo!"

    show wata_prop behind oni_prop, tatari_prop:
        linear 1 xalign 0.5 yalign 0 zoom .25
    pause 1

    yw "Vedo che un cervello lo hai! Sono contenta di averti fatto bene!"

    hnb "Hanananana! grazie Dittatore-chan!"

    yw ".... huuuuuuuh non ci siamo proprio eh? Almeno chiamami Lambda..."

    hnb "Non ho sentito perfavore."

    yw "Ecco qua il tuo perfavore."

    play sound "audio/bzz.mp3"

    hnb "AAAGYAGYAGYA!"

    hnb "Ehehehe! Ok diciamo che Lamda va bene..."

    yw "Insolente! {w}Bene, zuccone, allora adesso guarda questo frammento!"

    #zoom su Tatarigoroshi
    show tatari_prop:
        linear 1 xalign 0.5 zoom 1 yalign 0.5
    pause 1

    hnb "... E questo che minchia è! Non ci capisco un cazzo!"

    yw "Andiamo, proprio niente?"

    hnb "....Non mi bevo la storia del clone di Keiichi... c'è qualcosa che non mi torna..."

    yw "E allora come te lo spieghi che Keiichi fosse presente al festival? {w}Lo hanno detto tutti i suoi compagni."

    hnb "huuuuugh.... mnhhhhhhh forse... qualcuno si è travestito da Keiichi e lo ha sostituito durante il festival? Questo avrebbe perfettamente senso!"

    yw "Si certo, è arrivato Lupin terzo a Hinamizawa."

    yw "E come lo spieghi il fatto che al festival non ha piovuto? {w}Senza contare la parte più importante, Teppei è ancora vivo!!"

    hnb "Gsdbgkhskgndsnsgk non lo so! Ci deve essere per forza una spiegazione!"

    show tatari_prop:
        linear 1 xalign 0.9 yalign 0.4 zoom .25
    pause 1



    yw "Già ti fumano le orecchie?"
    show lamb blackB
    yw "Bene, pensaci quanto vuoi perchè la risposta non te la do!"

    hnb "Ghaaaaaaaaaa! NON È GIUSTO LAMBDA! NEMMENO MI SPIEGHI LA RISPOSTA DOPO AVERMI FATTO PENSARE COSì A FONDO?"

    yw "AHAHAHAHAHAHA VEDI? VEDI? {b}100\%{/b}POSSIBILITà DI VITTORIA, IL MISTERO DI HINAMIZAWA è IRRISOLVIBILE!"

    hnb "DAIIIII DIMMELOOOOO!"

    play sound  "audio/teleport.wav"
    hide tatari_prop with dissolve
    hide wata_prop with dissolve
    hide oni_prop with dissolve

    #Musica si ferma
    play music "audio/umineko organ.mp3"
    #una musica drammatica

    pause .5

    show lamb black
    yw "Proprio non capisci eh?"

    yw "Non c'è nessun bisogno di scervellarsi. {w}La risposta è che è stata la maledizione di Oyashiro sama."

    yw "Basta che accetti questa idea come buona e potrai giustificare anche gli eventi più assurdi e tragici."

    yw "È quello che continuano a fare Keiichi e gli altri. {w}Adesso mancano solo Check e Bern."

    yw "In altre parole, la risposta non è altrettanto importante quanto il fatto che sia irrisolvibile."

    hnb "Ma io sono dalla tua parte, oh Lambdadeltissima, almeno puoi dire a me chi è stato per davvero!"

    yw "No. Tu per sicurezza devi rimanere all'oscuro di ciò che succede."

    hnb "...."

    yw "Se ti può consolare, zuccone, nemmeno io so al {b}100\%{/b} cosa succede."

    yw "Ad esempio, dopo tutto questo tempo ancora mi sfugge come mai Rena torni ad Hinamizawa. {w}O come mai Rika sappia quello che sa."

    hnb "ughhhhh.."

    hnb "E mi vuoi dire che questo Check invece è sulla buona strada per capire tutto?"

    yw """No, non in generale. Ma guarda.

    Nel primo frammento Check non ha fatto niente di importante, è stato uno spettatore passivo senza il minimo appiglio come dovrebbe essere.

    Nel secondo frammento ha cominciato ad investigare futilmente, ma solo nel terzo rischiava di metterci seriamente in crisi!

    Ho dovuto inserire DUE NUOVE REGOLE!"""

    play sound "audio/truth.mp3"
    yw "{i}{color=#ffe674}Da ora in poi Bernkastel e Check non si possono scambiare informazioni inerenti alla partita.{p}Check non può riconoscere la mia pedina.{/color}{/i}"

    yw """Infine, grazie al mio intervento ha raggiunto il limite di tempo senza nulla di guadagnato.

    In più, adesso Bernkastel e Check non possono collaborare, e lui non può scoprire il mistero di Hinamizawa! Ahahahaha.

    Ma anche in questa situazione la sua probabilità di sconfitta non è {b}100\%{/b}.

    Ed ecco dove entri in scena tu.

    Devi assolutamente distrarlo ed impedirgli di ficcare il naso nel mio gioco. {w}Lo costringerai a giocare contro di te.

    Sono stata chiara al {b}100\%{/b}?? {w}La tua condizione di vittoria è convincerlo che Oyashiro sama 'esiste'."""

    hnb "...Certo che fai proprio paura quando ti impegni sul serio..."

    yw "Farai bene ad impararlo in fretta."

    hnb "E quel Larry invece? Di lui che mi dici?"

    yw "Chi?"

    yw "Ah, l'assistente buono a nulla...{w} Hahahaha. {w}Guarda un po'che fine ha fatto in Tatarigoroshi. Come se ossessionarsi in quel modo risolvesse qualcosa."

    yw "Una volta andato Check, Larry è assolutamente innocuo. Te lo dice Lambdadelta, strega della certezza."

    hnb "Bene, sembra interessante. {w}A Check ci penso io, parola di..."

    hnb "A proposito, come mi chiamo?"

    yw "Ora che ci penso non ti ho ancora dato un nome... Mmmh."

    yw "Ci penserò! Ora abbiamo altro da fare."

    hnb "Uno vale l'altro immagino... {w}Bene, che si fa di preciso?"

    yw "Prima ti troverò degli occhi che funzionano. {w}E poi andremo ufficialmente a lanciare il guanto di sfida."

    hnb "Vuoi presentarti adesso? {w}Non ti sarai mica offesa perchè Check ti ha dato della codarda vero?"

    play sound "audio/bzz.mp3"

    yw "Silenzio! Ho cambiato idea e quindi si fa come dico io."

    yw "Non abbiamo tempo da perdere. Tu resta fermo quì."
    play sound "audio/teleport.wav"
    hide lamb black with dissolve

    pause 1

    hnb """Uuuugh... si comporta come una bambina ma è spaventosa, quella è capace di eliminarmi in un istante se la faccio arrabbiare....

    Beh, non mi devo preoccupare, quel coglioncello di Check non ha alcuna speranza di sconfiggere il mio grande intelletto e i miei superiori poteri...

    HAANANANANA HAANANANANA!!!"""

    scene black with longFade

    return