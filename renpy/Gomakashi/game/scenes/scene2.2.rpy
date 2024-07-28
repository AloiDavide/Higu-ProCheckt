label scene2_2:
    n "2_2"

    stop music fadeout 4

    scene black with Dissolve(3)



    scene bern_fancy with Dissolve(3)

    play sound "audio/sfx/teleport.wav"
    show bern close at left
    show lamb unhappy smirk at right
    with squares

    play music "audio/umi/golden sneer.mp3" fadein 4



    bk "Ho perso. Concedo la partita."

    ld "Tutto qui? ti arrendi così facilmente? Non giochi nemmeno fino alla fine?"

    ld "Che peccato. Proprio quando stavo preparando la mossa finale per farti cadere nella disperazione una volta per tutte."
    show bern yoko
    bk "Non farmelo ripetere."

    show lamb smugclose pout
    ld "Lo sai? La tua {i}poker face{/i} sarà anche perfetta, ma dopo aver visto le tue mosse anche un idiota capirebbe cosa stai pensando..."

    show lamb defa cat
    ld "Quindi è super ovvio per un super genio come me!"

    show bern chira
    bk "..."
    show bern yoko

    show lamb unhappy pout
    ld "Dal momento in cui Shion si è sostituita a Mion hai smesso di giocare per vincere, e invece stavi già pensando alla prossima partita.{w} Che perdente!"

    bk "C'è differenza tra il coraggio e la stupidità. Non ha senso continuare a giocare da una posizione dove puoi contare le mosse allo scacco matto."

    show lamb defa smirk
    ld "Sei molto spericolata se pensi di poterti permettere di lasciarti scappare una qualsiasi occasione... {w}Quante partite ti mancano? Quanto ancora può resistere il tuo re? "

    bk "Lambda... Se devo dirti la verità sono confusa. {w}Sai, non è da te lasciarti scappare un vantaggio. {p}È molto fuori personaggio."

    show lamb worried
    pause 2

    ld "Mph!  ...D'altronde ho già vinto giusto? perchè dovrei preoccuparmi?"

    bk "Lambda, nella tua fretta ti sei forse dimenticata che il nostro non era l'unico gioco in ballo?"

    show lamb defa yep
    ld "Ahahahahahaha! Davvero?{w} Non è facile preoccuparsi di lui quando è così incompetente."


    ld "Non ho mai visto nessuno cadere in una trappola dopo l' altra in quel modo! {w}Non riuscirebbe a centrarle così efficienemente neanche provandoci! {w}Se fossi in te esploderei per l'imbarazzo."

    ld "E questo sarebbe il tuo asso nella manica Bern? La tua pedina? {w}È per colpa sua che mi sarei dovuta preoccupare?"

    ld "Bern, è questo il massimo che sai fare?"

    show bern chira
    bk "Non nego la sua totale incompetenza..."

    show bern yoko
    bk "Ma chissà, non è impossibile che tirando 100 dadi tutte le facce finiscano sul 6... Arrendendosi prima di tirare, invece, non si vince mai."

    bk "Lambda, tu non riesci ancora a comprendere il suo ruolo indiscutibile nella mia vittoria. {w}Anche se, devo dire, Hanabi è tutt'altro che scarso. Ci sa fare il ragazzo."

    ld "Vero? è tanto utile quanto arrogante! Tutto quello che deve fare è continuare a vincere!"

    stop music fadeout 4

    bk "Quasi mi dispiace per lui...{w} Sapevo che eri crudele, ma non pensavo che avresti preparato per i tuoi alleati un destino peggiore dei tuoi avversari. {w}Sai che di questo passo resterai senza amici, vero?"

    show lamb psycho mad
    pause 3

    scene black with longFade
    $persistent.third = True

    return