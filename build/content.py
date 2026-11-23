# Teksten voor joszegers.nl, per taal. Na een wijziging: python3 build/build.py

SPOTIFY = "https://open.spotify.com/show/6qAP26fsxaBlMo9mdwS8JP"
APPLE = "https://podcasts.apple.com/nl/podcast/maestro-d%C3%A9-podcast-over-dirigeren/id6809125230"
PODIMO = "https://podimo.com/s/higsXTka"
INSTAGRAM = "https://www.instagram.com/demaestropodcast/"
MAESTRO_SITE = "https://www.maestropodcast.nl"
PIXIE = "https://open.spotify.com/artist/0kSqe2dBbt8rg07yfEBnjR"

ARTISTS = [
    "Amsterdam Klezmer Band", "Barry Hay", "Benjamin Herman", "Danny Vera", "De Maastreechter Staar",
    "Dinand Woesthoff", "Do", "Elske DeWall", "Eric Vloeimans", "Gé Reinders", "Guus Meeuwis",
    "Het Goede Doel", "Jack Poels", "Johan van Iersel", "John Helliwell", "Kraantje Pappie",
    "Lode Smeets", "Maan", "Miss Montreal", "Nederlands Blazers Ensemble", "Piter Wilkens", "S10",
    "Syb van der Ploeg", "The Rosenbergs", "Wolfram Schmitt-Leonardy",
]
BANDS = [
    "Jeugdorkest Philharmonie Bocholtz", "Harmonie Noorbeek", "Harmonie Nederweert",
    "Harmonie Nieuwenhagen", "Fanfare SDG Ommen", "Fanfare Akkrum", "Fanfare Eensgezindheid Maasbracht",
]

LANGS = {}

# ---------------------------------------------------------------- Nederlands
LANGS["nl"] = {
    "path": "/",
    "locale": "nl_NL",
    "job": "Dirigent",
    "title": "Jos Zegers, dirigent",
    "description": "Jos Zegers is dirigent van de Fanfare Bereden Wapens en hoofdvakdocent HaFaBra-directie aan Conservatorium Maastricht. Daarnaast is hij chef-dirigent van het Kerkraads Symfonie Orkest en dirigent van Philharmonie Sittard.",
    "ui": {"skip": "Naar de inhoud", "menu": "Menu", "nav": "Hoofdmenu", "dark": "Donkere weergave", "intro": "Introductie"},
    "sections": [("functies", "Functies"), ("biografie", "Biografie"), ("onderwijs", "Onderwijs"), ("maestro", "Maestro"),
                 ("projecten", "Projecten"), ("samenspel", "Samenspel"), ("contact", "Contact")],
    "lead": "Dirigent van de Fanfare Bereden Wapens en hoofdvakdocent HaFaBra-directie aan Conservatorium Maastricht. Daarnaast chef-dirigent van het Kerkraads Symfonie Orkest en dirigent van Philharmonie Sittard.",
    "hero_alt": "Jos Zegers dirigeert een symfonieorkest.",
    "positions": [
        {"name": "Fanfare Bereden Wapens", "role": "Dirigent sinds 2022",
         "text": "Beroepsfanfare van de Koninklijke Landmacht. Het orkest speelt bij militaire ceremonies en geeft concerten.",
         "photo": "fbw", "alt": "Jos Zegers dirigeert in militair tenue, in zijlicht tegen een donkere achtergrond."},
        {"name": "Conservatorium Maastricht", "role": "Hoofdvakdocent HaFaBra-directie sinds 2022",
         "text": "De opleiding voor dirigenten van harmonie, fanfare en brassband aan Conservatorium Maastricht, onderdeel van Zuyd Hogeschool.",
         "link": ("#onderwijs", "Meer over het onderwijs")},
        {"name": "Kerkraads Symfonie Orkest", "role": "Chef-dirigent sinds 2023", "cls": "is-wide",
         "text": "Symfonieorkest uit Kerkrade met bijna zeventig musici, amateurs en professionals samen. Het orkest speelt vaak in Parkstad Limburg Theaters. De nieuwjaars- en carnavalsconcerten zijn daar elk jaar uitverkocht.",
         "photo": "kso", "alt": "Applaus na een concert van het Kerkraads Symfonie Orkest. Jos Zegers staat rechts, naast de solist met bloemen.",
         "caption": "Slotapplaus met het Kerkraads Symfonie Orkest"},
        {"name": "Philharmonie Sittard", "role": "Dirigent sinds 2022",
         "text": "Harmonieorkest uit Sittard, met een gevarieerd repertoire voor blaasorkest: van originele werken tot bewerkingen."},
    ],
    "bio": {
        "lead": "Jos Zegers (1983) begon op zijn achtste met hobo. Inmiddels staat hij voor symfonieorkest, militaire fanfare en harmonie, en leidt hij aan Conservatorium Maastricht dirigenten op.",
        "early": [
            "Vanaf 2001 studeerde hij hobo aan Conservatorium Maastricht, naast een studie Business Economics aan de Universiteit Maastricht. In 2006 studeerde hij in Maastricht met onderscheiding af. Daarna ging hij naar het Koninklijk Conservatorium in Den Haag, voor hobo bij Hans Roerade, solohoboïst van het Residentie Orkest, en voor HaFaBra-directie. Die laatste opleiding rondde hij in 2011 cum laude af.",
            "In 2009 haalde hij als jongste deelnemer de halve finale van de internationale dirigentenwedstrijd van het World Music Contest in Kerkrade. In 2015 won hij de internationale dirigentenwedstrijd Con Brio in Innsbruck, opnieuw als jongste deelnemer.",
        ],
        "munich_title": "München, 2016–2022",
        "munich": [
            "Van 2016 tot 2022 was hij chef-dirigent van het Bundespolizeiorchester München, een beroepsorkest van 46 musici. Hij was er niet alleen dirigent, maar ook leidinggevende van het hele orkest.",
            "Het orkest gaf meer dan negentig optredens per seizoen: concerten, ceremonies van de Bundespolizei en benefietconcerten in Beieren.",
            "In die jaren werkte hij ook als gastdirigent, onder meer bij het Polizeiorchester Bayern, het Bundespolizeiorchester Hannover en de Münchener Symphoniker, waar hij in 2019 debuteerde.",
        ],
        "back_title": "Terug in Nederland",
        "back": [
            "In 2022 keerde hij terug naar Nederland. In september begon hij als hoofdvakdocent aan Conservatorium Maastricht, in oktober als dirigent van de Fanfare Bereden Wapens. Datzelfde jaar werd hij dirigent van Philharmonie Sittard, in 2023 volgde het Kerkraads Symfonie Orkest.",
            "Hij is jurylid bij concoursen voor blaasorkesten, in Nederland voor de KNMO en in Duitsland voor de Bayerischer Blasmusikverband.",
        ],
        "facts": [
            ("2006", "Hobo, Conservatorium Maastricht, met onderscheiding"),
            ("2009", "Jongste halvefinalist, dirigentenwedstrijd World Music Contest, Kerkrade"),
            ("2010", "Jongste halvefinalist, Con Brio, Innsbruck"),
            ("2011", "HaFaBra-directie cum laude, Koninklijk Conservatorium Den Haag"),
            ("2015", "Winnaar Con Brio, Innsbruck"),
            ("2016–2022", "Chef-dirigent Bundespolizeiorchester München"),
            ("2019", "Debuut bij de Münchener Symphoniker"),
            ("2022", "Hoofdvakdocent Conservatorium Maastricht, dirigent Fanfare Bereden Wapens en Philharmonie Sittard"),
            ("2023", "Chef-dirigent Kerkraads Symfonie Orkest"),
        ],
        "alt": "Portret van Jos Zegers tegen een donkere achtergrond.",
    },
    "teaching": {
        "lead": "Sinds september 2022 is Jos Zegers hoofdvakdocent HaFaBra-directie aan Conservatorium Maastricht (Zuyd Hogeschool). Eerder bekleedden Jan Cober en Yvan Meylemans die functie.",
        "text": [
            "Hij leidt dirigenten op voor harmonie, fanfare en brassband. In de lessen draait het om slagtechniek, partituurstudie en de repetitie zelf: hoe bereid je een werk voor, wat zeg je tegen een orkest en wat laat je weg. Sinds 2023 vertegenwoordigt hij de vakgroep directie en zit hij in de curriculumcommissie.",
            "Hij pleit voor structureel muziekonderwijs op de basisschool. Daar begint de leerlijn die uiteindelijk naar het conservatorium leidt, en die leerlijn is op veel plekken niet meer vanzelfsprekend.",
        ],
        "alt": "Jos Zegers tijdens een repetitie, in T-shirt, met de baton naar het orkest gericht.",
        "coach_title": "Coaching voor dirigenten",
        "coach": "Ook buiten het conservatorium begeleidt hij dirigenten, individueel en afgestemd op hun vraag. Dat kan een amateurdirigent zijn die verder wil, of een professional die aan één onderdeel wil werken: slagtechniek, de voorbereiding van een partituur of de opbouw van een repetitie.",
        "coach_link": "Vraag een kennismakingsgesprek aan",
    },
    "maestro": {
        "lead": "Maestro is een podcast over dirigeren, die Jos Zegers maakt met dirigent Sander Teepen.",
        "text": [
            "Twee dirigenten praten met elkaar en met gasten over het vak: repeteren, programmeren, concoursen en de wisselwerking tussen amateurs en beroepsmusici. Sinds februari 2026 verschijnen er regelmatig nieuwe afleveringen. Gasten waren onder anderen Dominic Seldis, Johan de Meij, Ab Nieuwdorp en Louis Buskens.",
        ],
        "invite": "Luister de afleveringen terug en volg Maestro, dan mis je geen nieuwe aflevering.",
        "links": [
            ("Spotify", "Luisteren en volgen", SPOTIFY),
            ("Apple Podcasts", "Luisteren en abonneren", APPLE),
            ("Podimo", "Luisteren", PODIMO),
            ("Instagram", "Volgen", INSTAGRAM),
            ("maestropodcast.nl", "Alle afleveringen", MAESTRO_SITE),
        ],
    },
    "projects": [
        {"name": "Pixie Dust", "meta": "Elektronische muziek",
         "text": "Onder de naam Pixie Dust produceert hij jazz-hop. De nummers zijn samen meer dan vijftig miljoen keer gestreamd. Live trad hij onder meer op tijdens het WMC 2022 in Kerkrade.",
         "link": (PIXIE, "Pixie Dust op Spotify"),
         "photo": "pixie", "alt": "Jos Zegers achter keyboard en computer in de studio, met een trompettist op de achtergrond."},
        {"name": "Mit d'r kop in de wolke", "meta": "Musical, 2026",
         "text": "Muzikale leiding van de dialectmusical rond de liedjes van de Kerkraadse band Ummer d'r Neaver, met een live orkest van twaalf musici. Vier voorstellingen in Theater Kerkrade, juni 2026."},
    ],
    "together": {
        "artists_title": "Solisten en artiesten",
        "artists_note": "Onder meer bij Vrienden van Amstel Live in Ahoy (2023).",
        "artists": ARTISTS + ["Thomas Acda en Paul de Munnik"],
        "bands_title": "Harmonie en fanfare",
        "bands": BANDS,
    },
    "contact": {
        "lead": "Voor concerten, gastdirecties, coaching en jurywerk.",
        "alt": "Zwart-witfoto van Jos Zegers en profil, de baton geheven.",
    },
}

# ---------------------------------------------------------------- English
LANGS["en"] = {
    "path": "/en/",
    "locale": "en_GB",
    "job": "Conductor",
    "title": "Jos Zegers, conductor",
    "description": "Jos Zegers is conductor of the Fanfare Bereden Wapens of the Royal Netherlands Army and principal lecturer in wind band conducting at Conservatorium Maastricht. He is also chief conductor of the Kerkraads Symfonie Orkest and conductor of Philharmonie Sittard.",
    "ui": {"skip": "Skip to content", "menu": "Menu", "nav": "Main menu", "dark": "Dark mode", "intro": "Introduction"},
    "sections": [("positions", "Positions"), ("biography", "Biography"), ("teaching", "Teaching"), ("maestro", "Maestro"),
                 ("projects", "Projects"), ("alongside", "Alongside"), ("contact", "Contact")],
    "lead": "Conductor of the Fanfare Bereden Wapens and principal lecturer in wind band conducting at Conservatorium Maastricht. Also chief conductor of the Kerkraads Symfonie Orkest and conductor of Philharmonie Sittard.",
    "hero_alt": "Jos Zegers conducting a symphony orchestra.",
    "positions": [
        {"name": "Fanfare Bereden Wapens", "role": "Conductor since 2022",
         "text": "Professional fanfare band of the Royal Netherlands Army. The band performs at military ceremonies and gives concerts.",
         "photo": "fbw", "alt": "Jos Zegers conducting in military uniform, side-lit against a dark background."},
        {"name": "Conservatorium Maastricht", "role": "Principal lecturer in wind band conducting since 2022",
         "text": "The training programme for conductors of wind orchestras, fanfare bands and brass bands at Conservatorium Maastricht, part of Zuyd University of Applied Sciences.",
         "link": ("#teaching", "More about teaching")},
        {"name": "Kerkraads Symfonie Orkest", "role": "Chief conductor since 2023", "cls": "is-wide",
         "text": "A symphony orchestra from Kerkrade with nearly seventy musicians, amateurs and professionals together. It performs regularly at Parkstad Limburg Theaters, where its New Year and carnival concerts sell out every year.",
         "photo": "kso", "alt": "Applause after a concert by the Kerkraads Symfonie Orkest. Jos Zegers stands on the right, next to the soloist holding flowers.",
         "caption": "Final applause with the Kerkraads Symfonie Orkest"},
        {"name": "Philharmonie Sittard", "role": "Conductor since 2022",
         "text": "A wind orchestra from Sittard with a varied repertoire, from original works for wind band to arrangements."},
    ],
    "bio": {
        "lead": "Jos Zegers (born 1983) took up the oboe at the age of eight. Today he conducts a symphony orchestra, a military fanfare band and a wind orchestra, and trains conductors at Conservatorium Maastricht.",
        "early": [
            "From 2001 he studied oboe at Conservatorium Maastricht alongside a degree in Business Economics at Maastricht University, graduating from the conservatoire with honours in 2006. He then went to the Royal Conservatoire in The Hague to study oboe with Hans Roerade, principal oboe of the Residentie Orkest, and wind band conducting. He completed his conducting studies cum laude in 2011.",
            "In 2009, as the youngest participant, he reached the semi-finals of the international conducting competition at the World Music Contest in Kerkrade. In 2015 he won the international conducting competition Con Brio in Innsbruck, again as the youngest participant.",
        ],
        "munich_title": "Munich, 2016–2022",
        "munich": [
            "From 2016 to 2022 he was chief conductor of the Bundespolizeiorchester München, a professional orchestra of 46 musicians. Besides conducting, he was in charge of the orchestra as a whole.",
            "The orchestra gave more than ninety performances a season: concerts, ceremonies of the German Federal Police and charity concerts in Bavaria.",
            "During those years he also worked as a guest conductor, with the Polizeiorchester Bayern, the Bundespolizeiorchester Hannover and the Münchener Symphoniker, with whom he made his debut in 2019, among others.",
        ],
        "back_title": "Back in the Netherlands",
        "back": [
            "He returned to the Netherlands in 2022. In September he started as principal lecturer at Conservatorium Maastricht, and in October as conductor of the Fanfare Bereden Wapens. The same year he became conductor of Philharmonie Sittard, followed in 2023 by the Kerkraads Symfonie Orkest.",
            "He adjudicates at wind band competitions, for the KNMO in the Netherlands and the Bayerischer Blasmusikverband in Germany.",
        ],
        "facts": [
            ("2006", "Oboe, Conservatorium Maastricht, with honours"),
            ("2009", "Youngest semi-finalist, conducting competition, World Music Contest, Kerkrade"),
            ("2010", "Youngest semi-finalist, Con Brio, Innsbruck"),
            ("2011", "Wind band conducting, cum laude, Royal Conservatoire The Hague"),
            ("2015", "Winner, Con Brio, Innsbruck"),
            ("2016–2022", "Chief conductor, Bundespolizeiorchester München"),
            ("2019", "Debut with the Münchener Symphoniker"),
            ("2022", "Principal lecturer, Conservatorium Maastricht; conductor of the Fanfare Bereden Wapens and Philharmonie Sittard"),
            ("2023", "Chief conductor, Kerkraads Symfonie Orkest"),
        ],
        "alt": "Portrait of Jos Zegers against a dark background.",
    },
    "teaching": {
        "lead": "Since September 2022 Jos Zegers has been principal lecturer in wind band conducting at Conservatorium Maastricht (Zuyd University of Applied Sciences), a post previously held by Jan Cober and Yvan Meylemans.",
        "text": [
            "He trains conductors for wind orchestra, fanfare band and brass band. Lessons focus on baton technique, score study and the rehearsal itself: how to prepare a work, what to tell an orchestra and what to leave out. Since 2023 he has represented the conducting department and sat on the curriculum committee.",
            "He argues for structural music education in primary schools. That is where the path towards the conservatoire begins, and in many places that path can no longer be taken for granted.",
        ],
        "alt": "Jos Zegers in rehearsal, wearing a T-shirt, pointing the baton towards the orchestra.",
        "coach_title": "Coaching for conductors",
        "coach": "He also coaches conductors outside the conservatoire, one to one and tailored to their questions. That might be an amateur conductor who wants to develop further, or a professional working on one specific area: baton technique, score preparation or the structure of a rehearsal.",
        "coach_link": "Request an introductory meeting",
    },
    "maestro": {
        "lead": "Maestro is a Dutch-language podcast about conducting, made by Jos Zegers and conductor Sander Teepen.",
        "text": [
            "Two conductors talk with each other and with guests about the craft: rehearsing, programming, competitions and the interplay between amateur and professional musicians. New episodes have appeared regularly since February 2026. Guests have included Dominic Seldis, Johan de Meij, Ab Nieuwdorp and Louis Buskens.",
        ],
        "invite": "Listen to past episodes and follow Maestro so you don't miss a new one.",
        "links": [
            ("Spotify", "Listen and follow", SPOTIFY),
            ("Apple Podcasts", "Listen and subscribe", APPLE),
            ("Podimo", "Listen", PODIMO),
            ("Instagram", "Follow", INSTAGRAM),
            ("maestropodcast.nl", "All episodes", MAESTRO_SITE),
        ],
    },
    "projects": [
        {"name": "Pixie Dust", "meta": "Electronic music",
         "text": "Under the name Pixie Dust he produces jazz-hop. His tracks have been streamed more than fifty million times. He has performed live at, among others, WMC 2022 in Kerkrade.",
         "link": (PIXIE, "Pixie Dust on Spotify"),
         "photo": "pixie", "alt": "Jos Zegers at the keyboard and computer in the studio, with a trumpeter in the background."},
        {"name": "Mit d'r kop in de wolke", "meta": "Musical, 2026",
         "text": "Musical director of the dialect musical built around the songs of the Kerkrade band Ummer d'r Neaver, with a live orchestra of twelve musicians. Four performances at Theater Kerkrade, June 2026."},
    ],
    "together": {
        "artists_title": "Soloists and artists",
        "artists_note": "Including at Vrienden van Amstel Live, Ahoy Rotterdam (2023).",
        "artists": ARTISTS + ["Thomas Acda and Paul de Munnik"],
        "bands_title": "Wind and fanfare bands",
        "bands": BANDS,
    },
    "contact": {
        "lead": "For concerts, guest conducting, coaching and adjudication.",
        "alt": "Black-and-white photo of Jos Zegers in profile, baton raised.",
    },
}

# ---------------------------------------------------------------- Deutsch
LANGS["de"] = {
    "path": "/de/",
    "locale": "de_DE",
    "job": "Dirigent",
    "title": "Jos Zegers, Dirigent",
    "description": "Jos Zegers ist Dirigent der Fanfare Bereden Wapens des Königlich Niederländischen Heeres und Hauptfachlehrer für Blasorchesterdirigieren am Conservatorium Maastricht. Außerdem ist er Chefdirigent des Kerkraads Symfonie Orkest und Dirigent der Philharmonie Sittard.",
    "ui": {"skip": "Zum Inhalt", "menu": "Menü", "nav": "Hauptmenü", "dark": "Dunkle Ansicht", "intro": "Einleitung"},
    "sections": [("positionen", "Positionen"), ("biografie", "Biografie"), ("unterricht", "Unterricht"), ("maestro", "Maestro"),
                 ("projekte", "Projekte"), ("gemeinsam", "Gemeinsam"), ("kontakt", "Kontakt")],
    "lead": "Dirigent der Fanfare Bereden Wapens und Hauptfachlehrer für Blasorchesterdirigieren am Conservatorium Maastricht. Außerdem Chefdirigent des Kerkraads Symfonie Orkest und Dirigent der Philharmonie Sittard.",
    "hero_alt": "Jos Zegers dirigiert ein Sinfonieorchester.",
    "positions": [
        {"name": "Fanfare Bereden Wapens", "role": "Dirigent seit 2022",
         "text": "Professionelle Fanfare des Königlich Niederländischen Heeres. Das Orchester spielt bei militärischen Zeremonien und gibt Konzerte.",
         "photo": "fbw", "alt": "Jos Zegers dirigiert in Uniform, im Seitenlicht vor dunklem Hintergrund."},
        {"name": "Conservatorium Maastricht", "role": "Hauptfachlehrer für Blasorchesterdirigieren seit 2022",
         "text": "Die Dirigierausbildung für Blasorchester, Fanfare und Brass Band am Conservatorium Maastricht, Teil der Zuyd Hogeschool.",
         "link": ("#unterricht", "Mehr zum Unterricht")},
        {"name": "Kerkraads Symfonie Orkest", "role": "Chefdirigent seit 2023", "cls": "is-wide",
         "text": "Sinfonieorchester aus Kerkrade mit knapp siebzig Musikerinnen und Musikern, Amateure und Profis gemeinsam. Das Orchester spielt regelmäßig in den Parkstad Limburg Theaters. Die Neujahrs- und Karnevalskonzerte sind dort jedes Jahr ausverkauft.",
         "photo": "kso", "alt": "Applaus nach einem Konzert des Kerkraads Symfonie Orkest. Jos Zegers steht rechts neben der Solistin mit Blumen.",
         "caption": "Schlussapplaus mit dem Kerkraads Symfonie Orkest"},
        {"name": "Philharmonie Sittard", "role": "Dirigent seit 2022",
         "text": "Blasorchester aus Sittard mit einem vielseitigen Repertoire, von Originalwerken bis zu Bearbeitungen."},
    ],
    "bio": {
        "lead": "Jos Zegers (geb. 1983) begann mit acht Jahren Oboe zu spielen. Heute dirigiert er ein Sinfonieorchester, eine Militärfanfare und ein Blasorchester und bildet am Conservatorium Maastricht Dirigentinnen und Dirigenten aus.",
        "early": [
            "Ab 2001 studierte er Oboe am Conservatorium Maastricht, parallel zu einem Studium der Business Economics an der Universität Maastricht. 2006 schloss er in Maastricht mit Auszeichnung ab. Danach ging er an das Königliche Konservatorium Den Haag, wo er Oboe bei Hans Roerade, Solooboist des Residentie Orkest, und Blasorchesterdirigieren studierte. Das Dirigierstudium schloss er 2011 mit Auszeichnung (cum laude) ab.",
            "2009 erreichte er als jüngster Teilnehmer das Halbfinale des internationalen Dirigierwettbewerbs beim World Music Contest in Kerkrade. 2015 gewann er den internationalen Dirigierwettbewerb Con Brio in Innsbruck, erneut als jüngster Teilnehmer.",
        ],
        "munich_title": "München, 2016–2022",
        "munich": [
            "Von 2016 bis 2022 war er Chefdirigent des Bundespolizeiorchesters München, eines Berufsorchesters mit 46 Musikerinnen und Musikern. Neben der künstlerischen Leitung war er für das Orchester als Ganzes verantwortlich.",
            "Das Orchester gab mehr als neunzig Auftritte pro Saison: Konzerte, Zeremonien der Bundespolizei und Benefizkonzerte in Bayern.",
            "In diesen Jahren war er auch als Gastdirigent tätig, unter anderem beim Polizeiorchester Bayern, beim Bundespolizeiorchester Hannover und bei den Münchener Symphonikern, wo er 2019 debütierte.",
        ],
        "back_title": "Zurück in den Niederlanden",
        "back": [
            "2022 kehrte er in die Niederlande zurück. Im September begann er als Hauptfachlehrer am Conservatorium Maastricht, im Oktober als Dirigent der Fanfare Bereden Wapens. Im selben Jahr übernahm er die Philharmonie Sittard, 2023 folgte das Kerkraads Symfonie Orkest.",
            "Er ist Juror bei Blasorchesterwettbewerben, in den Niederlanden für die KNMO und in Deutschland für den Bayerischen Blasmusikverband.",
        ],
        "facts": [
            ("2006", "Oboe, Conservatorium Maastricht, mit Auszeichnung"),
            ("2009", "Jüngster Halbfinalist, Dirigierwettbewerb World Music Contest, Kerkrade"),
            ("2010", "Jüngster Halbfinalist, Con Brio, Innsbruck"),
            ("2011", "Blasorchesterdirigieren mit Auszeichnung, Königliches Konservatorium Den Haag"),
            ("2015", "Sieger Con Brio, Innsbruck"),
            ("2016–2022", "Chefdirigent Bundespolizeiorchester München"),
            ("2019", "Debüt bei den Münchener Symphonikern"),
            ("2022", "Hauptfachlehrer Conservatorium Maastricht; Dirigent der Fanfare Bereden Wapens und der Philharmonie Sittard"),
            ("2023", "Chefdirigent Kerkraads Symfonie Orkest"),
        ],
        "alt": "Porträt von Jos Zegers vor dunklem Hintergrund.",
    },
    "teaching": {
        "lead": "Seit September 2022 ist Jos Zegers Hauptfachlehrer für Blasorchesterdirigieren am Conservatorium Maastricht (Zuyd Hogeschool). Vor ihm hatten Jan Cober und Yvan Meylemans diese Stelle inne.",
        "text": [
            "Er bildet Dirigentinnen und Dirigenten für Blasorchester, Fanfare und Brass Band aus. Im Unterricht geht es um Schlagtechnik, Partiturstudium und die Probe selbst: Wie bereitet man ein Werk vor, was sagt man einem Orchester und was lässt man weg? Seit 2023 vertritt er die Fachgruppe Dirigieren und gehört dem Curriculumausschuss an.",
            "Er setzt sich für festen Musikunterricht an Grundschulen ein. Dort beginnt der Weg, der am Ende zum Konservatorium führt, und dieser Weg ist vielerorts nicht mehr selbstverständlich.",
        ],
        "alt": "Jos Zegers bei einer Probe, im T-Shirt, den Taktstock zum Orchester gerichtet.",
        "coach_title": "Coaching für Dirigenten",
        "coach": "Auch außerhalb des Konservatoriums begleitet er Dirigentinnen und Dirigenten, einzeln und abgestimmt auf ihre Fragen. Das kann ein Amateurdirigent sein, der weiterkommen möchte, oder ein Profi, der an einem bestimmten Punkt arbeiten will: Schlagtechnik, Partiturvorbereitung oder der Aufbau einer Probe.",
        "coach_link": "Kennenlerngespräch anfragen",
    },
    "maestro": {
        "lead": "Maestro ist ein niederländischsprachiger Podcast über das Dirigieren, den Jos Zegers mit dem Dirigenten Sander Teepen macht.",
        "text": [
            "Zwei Dirigenten sprechen miteinander und mit Gästen über das Handwerk: Proben, Programmgestaltung, Wettbewerbe und das Zusammenspiel von Amateuren und Berufsmusikern. Seit Februar 2026 erscheinen regelmäßig neue Folgen. Zu Gast waren unter anderem Dominic Seldis, Johan de Meij, Ab Nieuwdorp und Louis Buskens.",
        ],
        "invite": "Hören Sie die bisherigen Folgen und folgen Sie Maestro, damit Sie keine neue Folge verpassen.",
        "links": [
            ("Spotify", "Hören und folgen", SPOTIFY),
            ("Apple Podcasts", "Hören und abonnieren", APPLE),
            ("Podimo", "Hören", PODIMO),
            ("Instagram", "Folgen", INSTAGRAM),
            ("maestropodcast.nl", "Alle Folgen", MAESTRO_SITE),
        ],
    },
    "projects": [
        {"name": "Pixie Dust", "meta": "Elektronische Musik",
         "text": "Unter dem Namen Pixie Dust produziert er Jazz-Hop. Seine Tracks wurden zusammen mehr als fünfzig Millionen Mal gestreamt. Live trat er unter anderem beim WMC 2022 in Kerkrade auf.",
         "link": (PIXIE, "Pixie Dust auf Spotify"),
         "photo": "pixie", "alt": "Jos Zegers an Keyboard und Computer im Studio, im Hintergrund ein Trompeter."},
        {"name": "Mit d'r kop in de wolke", "meta": "Musical, 2026",
         "text": "Musikalische Leitung des Mundartmusicals rund um die Lieder der Kerkrader Band Ummer d'r Neaver, mit einem Live-Orchester aus zwölf Musikern. Vier Vorstellungen im Theater Kerkrade, Juni 2026."},
    ],
    "together": {
        "artists_title": "Solisten und Künstler",
        "artists_note": "Unter anderem bei Vrienden van Amstel Live in Ahoy Rotterdam (2023).",
        "artists": ARTISTS + ["Thomas Acda und Paul de Munnik"],
        "bands_title": "Blasorchester und Fanfaren",
        "bands": BANDS,
    },
    "contact": {
        "lead": "Für Konzerte, Gastdirigate, Coaching und Jurytätigkeit.",
        "alt": "Schwarzweißfoto von Jos Zegers im Profil, den Taktstock erhoben.",
    },
}
