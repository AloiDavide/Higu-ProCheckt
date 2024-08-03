label scene2_X:
    stop music
    call hide_menu
    scene fragplane with ImageDissolve("diagonal_crop.png", 2, ramplen=4)
#     scene fragplane with CropMove(
#         time=1.0,
#         mode='custom',
#         startcrop=(1.0, 0.0, 0.0, 0.0),
#         startpos=(1.0, 0.0),
#         endcrop=(0.0, 0.0, 1.0, 1.0),
#         endpos=(0.0, 0.0),
#         topnew=True
#     )

    pause 2

    play sound "audio/sfx/teleport.wav"
    show hnb smug2 nopper with squares
    hb "Che cringiata!"

    hb "Ancora a ripetere le stesse patetiche scuse. Pensa di meritare la vittoria dopo quello che ha fatto."

    show hnb fury fist
    hb "Pagherà con la distruzione di tutto ciò che ha costruito."

    n "In quel momento, sembrava che tutto stesse andando secondo i piani di Hanabi..."

    play music "audio/umi/fishy aroma.mp3" volume 1.2
    show hnb yep smug -fist
    hb "Già, tutto secondo i miei piani."

    n "Non è stato difficile per lui, d'altronde tutto quello che ha dovuto fare è ingannare Check, non un grande ostacolo dal momento che si inganna da solo."

    hb "Puoi dirlo forte!"

    n "Un lavoro facile, ma ben riuscito. Non gli resta che far scadere il tempo e tornare da Lambdadelta vittorioso."

    show hnb nope napalm_right at flip
    hb "Mmhh?"

    n "Ma stranamente, mentre si crogiolava nella sua gloria, cominciò a sentire delle strane voci."
    show hnb -napalm_right at unflip

    hb "Ehi in che senso..."
    play sound "audio/sfx/teleport.wav"
    show hnb:
        ease 1 xalign 0.9

    show fragplane greenflare with Dissolve(2)

    pause 1
    cr "Congratulazioni... Un piano ben riuscito, giusto? Una vittoria meritata."

    hb "Chi diamine è adesso? Sei qui per ribadire l'ovvio? Fatti vedere!"

    hd "Questa è una richiesta che non possiamo esaudire. {w}Per spiegarlo in modo che anche un principiante possa capire... ti stiamo parlando da dietro i punti ciechi di questo frammento. {w}Uscire allo scoperto sarebbe un rischio che non siamo disposti a correre."

    cr "Siamo solo venuti per farti I complimenti! Non badare a noi, non abbiamo alcuna intenzione, men che meno la capacità, di interferire in quello che stai facendo."

    hd "Apprezzeremmo se pensassi a noi come semplici voci nella tua testa. {w} O se preferisci delle allucinazioni."

    show hnb fury
    cr "Però vorrei chiederti... Cosa è la vittoria per te? Cosa significa vincere il gioco?"

    hd "Stiamo solo controllando se le regole ti sono chiare, non ti offendere."

    hb "Che domande... La mia vittoria è la sconfitta di Check. Non voglio nient'altro."



    show hnb smug2

    hd "Chiaro, chiaro... bene, abbiamo avuto la nostra risposta. Anche se devo dire, mi sembri un po' troppo rilassato."

    hb "Che intendi, stai cercando di confondermi?"

    hd "Certo che no... ma anche se tu stai vincendo in maniera schiacciante, c'è sempre una possibilità, per quanto infinitesimale, che Check possa risolvere il mistero... Ed in quel caso sai cosa farebbe di te Lambdadelta, non è vero?"

    show hnb grin smug
    hb "Non perderò! Non può battermi come è adesso, quindi non c'è niente da discutere."

    cr "Questo è lo spirito giusto! Ma se ti dicessi che, c'è un modo per scampare alle conseguenze? In caso un miracolo accadesse davvero."

    show hnb smug nope
    hb "Se avete qualcosa da dire smettete di girarci intorno e venite al punto."

    cr "Nonostante i suoi incredibili poteri, Lambdadelta non è completamente onnipotente."

    hd "Questo è un gioco tra te e Check, non più il suo. Siete fuori dalla sua giurisdizione, il suo campo di influenza."

    hd "Il suo obiettivo era allontanare Check, ma nel farlo ha creato una situazione dove qualunque cosa succeda non potrà agire subito."

    cr "Insomma, i suoi poteri quì non si applicano. Finchè non torni sul suo stesso livello non può farti niente. Capisci cosa voglio dire?"

    show hnb grin
    hb "Non c'è niente da capire, non ho alcuna possibilità di sconfitta! Hananananana!"

    hd "Molto bene. Non abbiamo intenzione di abusare ulteriormente del tuo tempo."

    cr "Arrivederci. Che I tuoi risultati siano proporzionali al tuo impegno."

    play sound "audio/sfx/teleport.wav"

    show fragplane
    with Dissolve(2)


    show hnb yep:
        linear 1 xalign 0.5

    pause 1

    hb "Chi credono di essere, ho tutto sotto controllo......."

    show hnb nope
    hb "Mmh? No davvero, chi diamine erano?"

    show hnb fury fist
    hb "Ci penserò con calma quando avrò distrutto Check."

    stop music fadeout 8
    scene black with longFade

    jump start

    return