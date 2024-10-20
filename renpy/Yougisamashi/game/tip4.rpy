image koya = im.Scale("koya.png", 1920, 1080)
image basement = im.Scale("basement.png", 1920, 1080)
image torakku = im.Scale("torakku.png", 1920, 1080)
image small shrine = im.Scale("small shrine.png", 1920, 1080)
image hinamizawa = im.Scale("hinamizawa.png", 1920, 1080)
image fragment = im.Scale("fragment80.png", 1920, 1080)

label tip4:
    #$persistent.route = "none" #this needs to go away
    play music "audio/cicadas.ogg"

    scene hinamizawa with fade
    pause 1.5
    scene small shrine with fade
    pause 1.5
    scene koya with fade


    scene basement with fade

    pause 1.5

    scene torakku with fade

    show check1 closed worried at right

    n """Il tuo è un lavoro duro e solitario. {w}Ultimamente hai lavorato senza sosta, e sebbene questo sia il tuo habitat naturale,
     la stanchezza comincia a farsi sentire.

    Larry non è ancora tornato dalla sorveglianza... forse faresti meglio a prendere un momento di riposo, accompagnato dalle cicale.

    ....{w} ....{w} ...."""

    show lar1 neutral straight at left


    play sound "audio/door.mp3"
    la "Larry a rapporto sir."

    show check1 angry unhappy
    show lar1 scared worried

    ck "Chi va la!"

    show check1 neutral unhappy
    ck "Ah, sei tu ragazzo, bentornato..."

    ck "Qua le cose stanno prendendo una brutta piega."


    show lar1 neutral talk
    la "Esattamente, dopo il........{w} il........................."
    play music "audio/boy in the windmill.mp3"

    show lar1 neutral shout
    extend " capo ma cosa diavolo è successo al nascondiglio?!"

    la "Fino a ieri non era altro che una stazione radio abbandonata!"

    show check1 neutral smile
    show lar1 neutral pleased
    ck "MA CHE DIAMINE Larry che domande sono, naturalmente l'ho sistemato in modo che fosse più adeguato al nostro compito!"
    show lar1 neutral talk
    la "Wow! da quando in qua è in grado di fare tutto questo? {w}Ci abbiamo trovato giusto una manciata di lampadine, qualche cavo elettrico e l'impianto radio!"
    show check1 neutral talk
    ck "Per diamine, è INDISPENSABILE avere almeno questo livello di competenza per un agente del BKG, secondo te come ho fatto a contattare i soccorsi quando sono rimasto intrappolato nel mezzo del deserto del Gobi?"
    show check1 neutral smile
    show lar1 neutral pleased
    la "Beh, l'ho sempre detto che lei è proprio il migliore...{w} A che serve quello?"
    show check1 neutral straight
    ck "Serve ad agganciarsi alle linee telefoniche della cittadina, ma a meno che non lo colleghiamo a qualcosa di specifico non sarà molto utile."

    show lar1 neutral talk
    la "E tutte quelle luci attaccate a quel sistema di fili? A cosa servono?"

    ck "Mostrano la frequenza di onde radio che stiamo captando in codice binario."

    show lar1 neutral talk
    la "..... per quale scopo?"

    ck "Ho usato tutti i display per le nostre telecamere nascoste." #"E dove diavolo trovo un computer?"

    la "Oh! Certo! ....."

    la "Questo invece?"

    show lar1 neutral pleased
    ck "Ti faccio sentire, avvicina l'orecchio....."

    n "Larry ci è cascato in pieno naturalmente."

    play sound "audio/screee.mp3" volume 0.05
    show lar1 scared unhappy
    pause 2

    play music "audio/bright sun.mp3"
    show check1 neutral smile

    show lar1 closed talk
    la "Capoooooooo! Non è giusto!"

    n "Larry sembra massaggiarsi l'orecchio in preda al dolore."

    ck "Cosi impari a fare tutte quelle domande! Mica sono qui per rispondere ai tuoi... ai tuoi..."
    show check1 angry unhappy
    extend " ECCO DOVE ERA FINITA LA DIAVOLO DI TRASMITTENTE!"

    show lar1 scared unhappy
    la "Pensavo fosse guasta."

    ck "Non importa! Avresti potuto perderla."

    la """Non sarò bravo come Gerry, ma anche io ho qualche conoscenza di elettronica. {w}Quindi ecco. {w}Ho pensato
        che durante i tempi morti della sorveglianza avrei potuto...
        """

    la "Ma capo, lei è così competente, perchè non la sistema lei?"

    ck "Non ho avuto tempo, e poi dove pensi che lo trovi il diamine di silicio?"

    show lar1 scared unhappy
    show check1 neutral unhappy


    ck "Bando alle ciance. {w}E dunque? Risolto nulla?"

    show lar1 neutral worried

    show lar1 scared worried
    show check1 neutral straight



    show lar1 scared talk
    la "No capo, purtroppo niente, ma posso continuare a provare."

    show lar1 neutral straight
    ck "Mhh… D’accordo, la lascio in tua custodia. {w}Ma fa in modo di non perderla e non farla trovare a nessuno."

    show lar1 neutral worried
    la "Certo… non mi permetterei mai."

    play music "audio/seijaku.mp3"
    ck "Veniamo ai fatti, qual'è la situazione a casa Houjou? {w}Come si comportano capelli biondi e suo zio quando sono da soli?"
    show check1 neutral straight

    show lar1 neutral talk
    la """Da quello che ho visto, quella bambina non ha quasi mai un momento di riposo. {w}Quando non è a scuola obbedisce
    gli ordini di Teppei e dei suoi amici senza fiatare. {w}Neanche una lamentela."""

    show lar1 neutral unhappy
    la """Anche quando sono arrivati gli addetti dal centro di assistenza minorile, zio e nipote hanno negato insieme le accuse, e
    lui sel'è cavata con un rimprovero e dei volantini.

    Non hanno nemmeno provato a ispezionare la casa..."""

    show lar1 neutral pleased
    la "A quel punto ho sperato di poter fare un'ispezione io personalmente."
    show lar1 neutral talk

    la """Però purtroppo non c'è mai un momento in cui la casa è vuota.

    Nei rari momenti in cui sia Satoko che Teppei erano fuori c'era sempre qualcuno dei suoi compari a fare i propri comodi. {w}
    Per cui non sono potuto entrare a cercare prove.
    """

    show lar1 neutral unhappy
    show check1 neutral unhappy
    ck "E dimmi... hai assistito anche ad abusi... {i}di quel tipo{/i}?"

    show lar1 scared unhappy
    la "..."

    show lar1 scared shout
    show check1 neutral straight
    la "Se una cosa del genere dovesse succedere davanti ai miei occhi giuro che lo fermerò! Costi quel che costi!!"

    show check1 neutral unhappy
    show lar1 scared straight
    ck """Si ti capisco{w}, persino io non garantisco che manterrei la calma.

    Ma sta attento, è proprio in queste situazioni che non possiamo permetterci errori.

    Come ti dicevo, la situazione continua a peggiorare. Guarda che scenata è successa stamani a scuola."""



    hide lar1
    hide check1

    n """Procedi mostrando a Larry tutto ciò che è successo da quando i ragazzi si sono riuniti per il pranzo.

     Satoko apparentemente in salute, la gentilezza dei suoi compagni, e poi il punto di rottura.

     Non era una scena che avresti voluto rivedere, ma in questo momento non hai scelta.

     Quanto al tuo assistente, lo trovi alquanto pallido e sconvolto."""

    play music "audio/dancers7.mp3"

    show lar1 scared shout at left
    show check1 neutral unhappy at right

    la "C.c.capo! {w}Cosa facciamo? È peggio del previsto."

    ck """E datti una calmata. Non posso escludere del tutto che Satoko stia esagerando le cose. {w}Ma se così non
    fosse, vuol dire che la la sua psiche ha raggiunto definitivamente il limite.

    E non è tutto, Keiichi ha iniziato a mostrare dei movimenti sospetti. {w}Sono quasi sicuro che stia pianificando
    l’omicidio di Teppei per proteggere capelli biondi."""


    show lar1 closed shout

    la """Capo! Io lo capisco benissimo che dobbiamo essere cauti. Che la missione viene prima di tutto.

    Ma se non facciamo qualcosa adesso, che ne sarà della nostra dignità da BKG?

    No, forse è già troppo tardi...
    """

    witch "...Il ragazzo non ha tutti I torti."

    hide lar1
    hide check1

    play sound "audio/teleport.wav"
    show fragment with fade

    n """Improvvisamente la voce di Larry si fa lontana.

     In questo momento due versioni di te sono sovrapposte. Un panorama familiare, è evidente che la tua memoria sia tornata."""

    witch """Oh oh. So cosa stai pensando. {w}Sii rassicurato, non è ancora il momento di tornare...
    {w}Anche se volessi fuggire prima di arrivare al peggio, non ti sarebbe concesso.

    Tuttavia, devi renderti senz'altro conto del privilegio che hai.

    Di norma gli esseri umani non possono vedere fuori dal proprio frammento... Tu però, sei l’eccezione...

    Se la mia teoria è corretta, a te che sei capitato nel mare di frammenti è stato concesso il lusso della scelta.

    Check, questo è un esperimento. Mostrami come con la tua volontà spingerai questo frammento nell'una o nell'altra direzione.

    """

    n """In questo momento sei a cavallo tra sbocchi del fato, e senti che l'autorità di scegliere il futuro risiede soltanto in te.

    Non è più il momento di essere uno spettatore passivo. {w}Consapevole della tua responsabilità, esamini le tue opzioni."""

    call screen fragment_choice

    return

label tip4P:
            if persistent.route == "genocide":
                call no_regrets
                call screen fragment_choice

            $ persistent.route = "pacifist"

            play sound "audio/teleport.wav"
            scene torakku with fade
            show check1 neutral talk at right
            show lar1 closed straight at left
            ck "Ben detto Larry. É finito il tempo di stare con le mani in mano."

            show lar1 neutral straight

            ck"""
            Al momento noi due siamo gli unici a conoscere il piano di capelli chiari.

            Quel ragazzo si merita tanto ma non l'ergastolo.{w} Ecco perchè, non abbiamo altra scelta che fermarlo.

            Nello stato in cui è capelli biondi non sarà difficile incriminare quel rifiuto umano del suo tutore.
            {w}Daremo anche noi una mano ovviamente. {w}Ma dobbiamo prima porre fine a questo insulso tentativo di eroismo.
            """

            stop music fadeout 2.0

            show lar1 neutral talk

            la "......{w}Ne è davvero sicuro?"

            play music "audio/gear.mp3" fadein 3.0

            ck "Obiezioni?"

            show check1 neutral straight
            la """Ecco, è solo che.. ci pensi. {w}Denunciare gli abusi a chi di ruolo non è servito a nulla. {w}Anche se trovassimo
            delle prove schiaccianti, significherebbe lasciarla nelle grinfie di Teppei ancora per alcuni giorni, nel migliore dei casi.

            Se invece Keiichi riuscisse nel suo piano non sarebbero tutti più felici?"""

            show check1 neutral unhappy
            ck "Larry. Di che stai parlando."

            show check1 neutral straight
            show lar1 neutral pleased
            la """Lo ha appena detto lei. Siamo gli unici a conoscere il suo piano. {w}Anche se da solo fallirebbe,
            sicuramente sarebbe un'altra storia con noi a coprire le sue tracce."""

            ck """........{w}  ........

            È fuori questione, non diventeremo complici di un'assassino."""

            show lar1 neutral smile
            la """Quella pausa significa che ci ha pensato.

            Che le prende? Il Check che conosco non esita mai a usare la forza quando è convinto di essere nel giusto.
            {w}Non è forse la stessa cosa che sta facendo Keiichi In questo momento?"""

            show lar1 neutral unhappy
            show check1 angry unhappy
            ck """Ascolta! Neanche io voglio starmene a guardare mentre una ragazzina viene sfruttata, picchiata.. O PEGGIO.

            Ma il BKG non serve per aiutare la gente ad ammazzare le persone che odiano. {w}A quello ci sta già pensando chiunque sia dietro gli omicidi annuali.

            È chiaro che in questi casi mobilitare le autorità locali sia la cosa migliore."""

            show lar1 closed talk
            show check1 angry straight
            la """Si ma questo è un caso di emergenza. Le autorità hanno dimostrato di essere inaffidabili, e persino i Sonozaki
            se ne sono tirati fuori.

            Non c'è una persona in questo villaggio oltre a Keiichi che si stia mettendo veramente
            d'impegno per risolvere il problema."""

            show check1 angry unhappy
            ck "E Ooishi? Almeno a lui fregherà qualcosa di tutta sta faccenda! O SBAGLIO!?"
            show check1 angry straight
            show lar1 evil shout
            la """Ooishi era sul caso anche l’anno scorso, sicuramente era al corrente degli abusi anche allora.{w}
            Eppure non ha fatto nulla. Quel vecchio non vuole altro che una golosa esca per Oyashiro-sama."""

            show check1 angry unhappy
            show lar1 evil unhappy
            ck """Non so se hai capito. Quell'idiota sta per commettere un omicidio durante il WATANAGASHI, quando gli occhi della polizia saranno puntati senza dubbio sul villaggio.

            Non abbiamo idea di cosa combinerà Keiichi, rischieremmo di venire indagati al minimo errore sia suo che nostro. E allora addio missione."""

            show check1 angry straight
            show lar1 evil shout
            la """Beh ma allora contattare Ooishi o chiunque altro dal lato nostro non manda allo sbaraglio la segretezza della missione istantaneamente?

            Non importa come la mettiamo, una soffiata di quel tipo sarebbe sospetta. Almeno la mia idea ci permette di restare anonimi fintanto che lavoriamo bene.

            Che c'è? Non mi dica che un \"comandante\" del BKG ha paura delle indagini di qualche poliziotto di campagna."""

            show check1 angry shout
            show lar1 scared worried
            ck """Attento Larry stai testando i limiti della mia pazienza!

            Sono stato chiaro. Non permetterò a capelli chiari di ammazzare nessuno! Nel bene e nel male!

            ORA TORNA AL TUO CAZZO DI LAVORO!"""

            show check1 angry straight

            n """Larry non controbatte. Forse si è finalmente rassegnato alla tua decisione.

            Senza elaborare ulteriormente, prende la trasmittente e si volta per uscire dal nascondiglio."""

            show lar1 scared talk

            stop music fadeout 4

            la "Capo..."

            ck "Che altro c’è?!"

            play music "audio/cicadas.ogg" fadein 2

            la "Non ha proprio idea di quale sia il problema con la trasmittente... vero?"

            show check1 angry unhappy
            ck "Come ti ho già detto, o è rotta o ci hanno sabotato, che altro dovrei sapere? Basta sprecare il mio tempo!"

            la "..."

            la "Ho capito..."

            play sound "audio/door.mp3"

            scene black with longDiss

            return

label tip4G:
            if persistent.route == "pacifist":
                call no_regrets
                call screen fragment_choice
            $ persistent.route = "genocide"

            play sound "audio/teleport.wav"
            scene torakku with fade
            show check1 neutral talk at right
            show lar1 closed straight at left
            ck "Ben detto Larry. É finito il tempo di stare con le mani in mano."

            show lar1 neutral straight

            ck"""
            Al momento noi due siamo gli unici a conoscere il piano di capelli chiari.

            Quel ragazzo si merita tanto ma non l'ergastolo.{w} Ecco perchè non abbiamo altra scelta che aiutarlo.

            In tutta questa storia lui è l'unico disposto a sporcarsi le mani per fare la cosa giusta.

            Ciò è ammirevole, ma è chiaro che non ne ha l'abilità. Preparato o meno resta un amatoriale, ed è questione di tempo prima che lasci delle tracce.

            Per altro pianifica di farlo il giorno del Watanagashi.

            Dobbiamo necessariamente intervenire noi se vogliamo che la storia ottenga un lieto fine.
            """

            stop music fadeout 2.0

            show lar1 neutral unhappy

            la "......{w}Ne è davvero sicuro?"

            play music "audio/gear.mp3" fadein 3.0


            ck "Obiezioni?"

            show lar1 neutral talk
            show check1 neutral straight
            la "Cioè... se ho capito bene. {w}Sta dicendo che non faremo niente mentre un civile uccide un altro civile?"
            show lar1 neutral unhappy

            ck "No Larry, non hai sentito? Sto dicendo che gli copriremo le spalle attivamente."

            show lar1 scared talk
            la "Ma.. ma siamo alla vigilia del festival, gli occhi di Ooishi e compagnia saranno puntati sul villaggio."
            show lar1 scared unhappy

            show check1 neutral unhappy
            ck """Dalle informazioni che ho recuperato, Ooishi è l'unico a credere ancora che gli omicidi abbiano un filo conduttore.
            Inoltre stavo già tenendo traccia dei movimenti della polizia.

            Certo, la sicurezza sarà più stretta del solito, ma non è nulla di insormontabile per Check, comandante del BKG.
            """

            show lar1 scared talk
            la "Va bene, non lo metto in dubbio. Ma che succede se Keiichi sbaglia e veniamo indagati per colpa sua?"
            show lar1 scared unhappy

            ck """Ovviamente non mi sognerei mai di riporre fiducia in capelli chiari, ma dopotutto il villaggio è circondato da boschi inabitati.
            {w}Anche un'idiota capirebbe il vantaggio che ciò offre."""

            show check1 neutral straight

            pause 1

            show lar1 scared talk
            la """Forse ha ragione... Satoko è in pericolo e forse non c'è davvero altro modo per salvarla.{w}
            Ma cosa racconteremo al resto del BKG quando lo verranno a sapere? Non verremo puniti?"""
            show lar1 scared unhappy

            ck "Farò quello che ho sempre fatto quando gli altri comandanti avevano da ridire sui miei metodi"
            show check1 neutral unhappy
            extend ": mostrare i risultati."

            show lar1 scared worried
            la "Però.... però........"



            show check1 neutral unhappy
            ck """Lo so. Non è una scelta facile! Non ti voglio costringere a collaborare se sei assolutamente contrario.
            Ma per come la vedo io, è in queste situazioni che un BKG deve tirare fuori il coraggio."""

            show lar1 scared worried
            la "Se devo essere sincero ho ancora i miei dubbi. {w}Ma ho detto che l'avrei seguita in questa missione. E non mi voglio tirare indietro adesso."

            show check1 neutral unhappy
            ck "Bravo ragazzo, è così che ti voglio. Adesso torna a sorvegliare la casa, avremo bisogno di conoscere i movimenti di Teppei. {w}Io continuerò a seguire Keiichi mentre mette insieme il suo piano."

            show lar1 neutral unhappy
            la "...."

            n "Larry prende la trasmittente e si dirige in silenzio verso l'uscita."

            ck "Dove è finita la risposta?"

            show check1 neutral straight

            la "Sissignore"

            stop music fadeout 5


            play sound "audio/door.mp3"

            scene black with longDiss

            return

label no_regrets:
    witch "Credevo di averti detto di scegliere. Perchè cerchi di tornare sui tuoi passi adesso?"
    return