import os

from src.Button import *
from src.animal import *
from src.const import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
folder_path = os.path.join(BASE_DIR, "..", "assets", "animals", "animal1")
pygame.init()

Screen_width = 600
Screen_height = 600
myScreen = pygame.display.set_mode((Screen_width, Screen_height))


def load_animation_frames(folder_path):
    """
    funkcja load_animation_frames służy do wczyania zdjęć zwierzątka które zostaną wykorzystane do animacji.
    Funkcja zbiera pliki png i wpisuje je do tablicy frames. Pliki są zebrane z folderu assets/animals
    W środku znajduje się oddzielny folder dla każdego zwierzaka.
    """
    frames = []
    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            path = os.path.join(folder_path, filename)
            image = pygame.image.load(path).convert_alpha()
            frames.append(image)
    return frames


def get_font(size):
    """
    prosta funkcja zbierające czcionkę.
    Cziconka znajduje się w folderze assets/fonts
    """
    return pygame.font.Font("../assets/fonts/Daydream.ttf", size)


def info():
    """
    Funkcja info odpowiada za ekran opisujący gre.
    Jest to Prosty ekran gdize nazwa okna została zmianiona na info.
    Do tego tło zebrane jest z fodleru asstets gdzie jest plik bg.png
    Dodatkowo na ekranie pojawia sie przycisk back który odpowiada za wywołanie funkcji menu co wraca grę do menu głównego.
    Tło do przycisku wczytane jest równeż z foldeu assets gdzie plik nazwany jest buttonMenuNuBG.png
    """
    pygame.display.set_caption("Info")

    """
    wczytanie zdjęć tła i tła przycisku
    """
    bg_image = pygame.image.load("../assets/bg.png").convert()
    bg_image = pygame.transform.scale(bg_image, (Screen_width, Screen_height))
    button_bg_image = pygame.image.load("../assets/buttonMenuNuBG.png").convert_alpha()
    button_bg_image = pygame.transform.scale(button_bg_image, (200, 60))

    """
    Teskt wyświetlany na ekranie, (podzielony na części by sie mieścił)
    """
    text1 = "Tamagotchi  is  a  basic  game  that"
    text2 = "simulates  pet  ownership."
    text3 = "The  goal  of  the  game  is  to  keep"
    text4 = "the  pet  healthy  and  happy"
    text5 = "This  project  was  made  by  s30781"

    """
    Deklaracja guzika, podajemy do jakiego ekranu przypiasć.
    podajemy współrzędne, kolor, tekst oraz czcionke na guzik
    dodatkowo podajemy jaka funkcja ma zostać wywołana po kliknięciu
    jeszcze podajemy zdjęcie które ma być tłem dla tego guzika
    """
    backButton = Button(
        screen=myScreen,
        x=200, y=400,
        width=200, height=60,
        color=(0, 100, 200),
        text="BACK",
        font=get_font(30),
        action=mainMenu,
        image=button_bg_image
    )

    """
    Główna pętla która obsługuje informacje. Zaczyna od rysowania tła.
    Następnie czy guzik został kliknięty.
    """
    running = True
    while running:
        myScreen.blit(bg_image, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            backButton.check_click(event)

        """
        Deklaracja tekstu (tekstów bo podzielony na części)
        """
        text_surf1 = get_font(15).render(text1, True, "White")
        text_surf2 = get_font(15).render(text2, True, "White")
        text_surf3 = get_font(15).render(text3, True, "White")
        text_surf4 = get_font(15).render(text4, True, "White")
        text_surf5 = get_font(15).render(text5, True, "White")

        myScreen.blit(text_surf1, (80, 200))
        myScreen.blit(text_surf2, (80, 220))
        myScreen.blit(text_surf3, (80, 240))
        myScreen.blit(text_surf4, (80, 260))
        myScreen.blit(text_surf5, (80, 280))

        """
        Wywołanie rysowania guzika
        """
        backButton.draw()
        pygame.display.update()


def optionsSelecLevel():
    """
    funkcja optionSelectLevel odpowiada za zmiane okna
    """

    def increaseHungerlevelByOne():
        """
        Funkcja ta jest wywoływana podczas zmianiania wartości w menu opcji.
        Jest to metoda wywoływana po wciśnięciu guzika ">"
        i służy do zwiększenia wartości głodu o jeden.
        If sprawdza czy obecna wartośc nie jest poza dozwolonym obszarem od 0-100.
        """
        if outOfRange(settings["hungerValueForButton"]):
            settings["hungerValueForButton"] = 100
        else:
            settings["hungerValueForButton"] = settings["hungerValueForButton"] + 1

    def decreaseHungerlevelByOne():
        """
        Funkcja ta jest wywoływana podczas zmianiania wartości w menu opcji.
        Jest to metoda wywoływana po wciśnięciu guzika "<"
        i służy do zmiejszenie wartości głodu o jeden.
        If sprawdza czy obecna wartośc nie jest poza dozwolonym obszarem od 0-100.
        """
        if outOfRange(settings["hungerValueForButton"]):
            settings["hungerValueForButton"] = 0
        else:
            settings["hungerValueForButton"] = settings["hungerValueForButton"] - 1

    def increaseFunlevelByOne():
        """
        Funkcja ta jest wywoływana podczas zmianiania wartości w menu opcji.
        Jest to metoda wywoływana po wciśnięciu guzika ">"
        i służy do zwiększenia wartości fun o jeden.
        If sprawdza czy obecna wartośc nie jest poza dozwolonym obszarem od 0-100.
        """
        if outOfRange(settings["funValueForButton"]):
            settings["funValueForButton"] = 100
        else:
            settings["funValueForButton"] = settings["funValueForButton"] + 1

    def decreaseFunlevelByOne():
        """
        Funkcja ta jest wywoływana podczas zmianiania wartości w menu opcji.
        Jest to metoda wywoływana po wciśnięciu guzika "<"
        i służy do zmiejszenie wartości fun o jeden.
        If sprawdza czy obecna wartośc nie jest poza dozwolonym obszarem od 0-100.
        """
        if outOfRange(settings["funValueForButton"]):
            settings["funValueForButton"] = 0
        else:
            settings["funValueForButton"] = settings["funValueForButton"] - 1

    def increaseEnergylevelByOne():
        """
        Funkcja ta jest wywoływana podczas zmianiania wartości w menu opcji.
        Jest to metoda wywoływana po wciśnięciu guzika ">"
        i służy do zwiększenia wartości energy o jeden.
        If sprawdza czy obecna wartośc nie jest poza dozwolonym obszarem od 0-100.
        """
        if outOfRange(settings["energyValueForButton"]):
            settings["energyValueForButton"] = 100
        else:
            settings["energyValueForButton"] = settings["energyValueForButton"] + 1

    def decreaseEnergylevelByOne():
        """
        Funkcja ta jest wywoływana podczas zmianiania wartości w menu opcji.
        Jest to metoda wywoływana po wciśnięciu guzika "<"
        i służy do zmiejszenie wartości energy o jeden.
        If sprawdza czy obecna wartośc nie jest poza dozwolonym obszarem od 0-100.
        """
        if outOfRange(settings["energyValueForButton"]):
            settings["energyValueForButton"] = 0
        else:
            settings["energyValueForButton"] = settings["energyValueForButton"] - 1

    pygame.display.set_caption("Options")

    """
    Część odpowiedzialna za wczytanie zdjęć tła i przycisku
    """
    bg_image = pygame.image.load("../assets/bg.png").convert()
    bg_image = pygame.transform.scale(bg_image, (Screen_width, Screen_height))
    button_bg_image = pygame.image.load("../assets/buttonMenuNuBG.png").convert_alpha()
    button_bg_image = pygame.transform.scale(button_bg_image, (200, 60))

    text1 = "Please alter the values"
    text2 = "to your liking. (hunger,fun,energy)"

    """"
    Ustawienie jednolitych rozmiarów dla guzików
    """
    wysokoscGuzikiHunger = 250
    wysokoscGuzikiFun = 320
    wysokoscGuzikiEnergy = 390

    """
    Deklarowanie obiektów guzików
    """
    backButton = Button(
        screen=myScreen,
        x=200, y=450,
        width=200, height=60,
        color=(0, 100, 200),
        text="BACK",
        font=get_font(30),
        action=mainMenu,
        image=button_bg_image
    )
    increaseHungerButton = Button(
        screen=myScreen,
        x=myScreen.get_width() - 200, y=wysokoscGuzikiHunger,
        width=200, height=60,
        color=(0, 100, 200),
        text=">",
        font=get_font(30),
        action=increaseHungerlevelByOne,
        image=button_bg_image
    )
    decreaseHungerButton = Button(
        screen=myScreen,
        x=0, y=wysokoscGuzikiHunger,
        width=200, height=60,
        color=(0, 100, 200),
        text="<",
        font=get_font(30),
        action=decreaseHungerlevelByOne,
        image=button_bg_image
    )
    increaseFunButton = Button(
        screen=myScreen,
        x=myScreen.get_width() - 200, y=wysokoscGuzikiFun,
        width=200, height=60,
        color=(0, 100, 200),
        text=">",
        font=get_font(30),
        action=increaseFunlevelByOne,
        image=button_bg_image
    )
    decreaseFunButton = Button(
        screen=myScreen,
        x=0, y=wysokoscGuzikiFun,
        width=200, height=60,
        color=(0, 100, 200),
        text="<",
        font=get_font(30),
        action=decreaseFunlevelByOne,
        image=button_bg_image
    )
    increaseEnergyButton = Button(
        screen=myScreen,
        x=myScreen.get_width() - 200, y=wysokoscGuzikiEnergy,
        width=200, height=60,
        color=(0, 100, 200),
        text=">",
        font=get_font(30),
        action=increaseEnergylevelByOne,
        image=button_bg_image
    )
    decreaseEnergyButton = Button(
        screen=myScreen,
        x=0, y=wysokoscGuzikiEnergy,
        width=200, height=60,
        color=(0, 100, 200),
        text="<",
        font=get_font(30),
        action=decreaseEnergylevelByOne,
        image=button_bg_image
    )

    running = True
    while running:
        """
        Główna pętla dla tej funkcji. Zaczynamy od ustawienia tła
        """
        myScreen.blit(bg_image, (0, 0))
        """
        A tu sprawdzamy eventy kliknięcia w guziki
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            backButton.check_click(event)
            increaseHungerButton.check_click(event)
            decreaseHungerButton.check_click(event)
            increaseFunButton.check_click(event)
            decreaseFunButton.check_click(event)
            increaseEnergyButton.check_click(event)
            decreaseEnergyButton.check_click(event)

        """
        Deklaracja i wyświetlenie tekstów
        """
        text_surf1 = get_font(15).render(text1, True, "White")
        text_surf2 = get_font(15).render(text2, True, "White")
        textHunger = get_font(15).render(str(settings["hungerValueForButton"]), True, "White")
        textFun = get_font(15).render(str(settings["funValueForButton"]), True, "White")
        textEnergy = get_font(15).render(str(settings["energyValueForButton"]), True, "White")

        myScreen.blit(text_surf1, (80, 200))
        myScreen.blit(text_surf2, (80, 220))
        """
        Wyswietlany tekst który sie zmienia
        """
        myScreen.blit(textHunger, (myScreen.get_width() / 2 - 10, wysokoscGuzikiHunger + 15))
        myScreen.blit(textFun, (myScreen.get_width() / 2 - 10, wysokoscGuzikiFun + 15))
        myScreen.blit(textEnergy, (myScreen.get_width() / 2 - 10, wysokoscGuzikiEnergy + 15))

        """
        Rysowanie guzików "<" oraz ">" które służą do zmiany zmiennych
        """
        increaseHungerButton.draw()
        decreaseHungerButton.draw()

        increaseFunButton.draw()
        decreaseFunButton.draw()

        increaseEnergyButton.draw()
        decreaseEnergyButton.draw()

        backButton.draw()
        pygame.display.update()


def mainMenu():
    """
    Funkcja mainMenu która służy do pokaznia ekranu gdzie uzytkownik wrzucony jest po odpaleniu aplikacji.
    Zaczynamy od wczytania tła do menu oraz zdjęcia używanego do guzików.

    Nie ukrywam że wzorowalem sie na poradniku na yt:
    https://www.youtube.com/watch?v=GMBqjxcKogA
    (uważem że niebyłoby ok gdybym nie wspomniał o tym)
    """
    pygame.display.set_caption("Main Menu")

    bg_image = pygame.image.load("../assets/bg.png").convert()
    bg_image = pygame.transform.scale(bg_image, (Screen_width, Screen_height))

    button_bg_image = pygame.image.load("../assets/buttonMenuNuBG.png").convert_alpha()
    button_bg_image = pygame.transform.scale(button_bg_image, (200, 60))

    """
    Deklaracja przycisków. Podajemy ekran w któym mają być podpięte.
    Podejmy współrzędne oraz szerokość i wysokość.
    Mimo podania zdjęcia tła dla guzika to podajemy kolor na wszelki wypadek.
    Podajemy jeszcze tekst który ma sie pojawić na guziku.
    """
    infoButton = Button(
        screen=myScreen,
        x=Screen_width / 2 - 250 / 2,
        y=Screen_height / 2,
        width=250, height=80,
        color=(0, 100, 200),
        text="INFO",
        font=get_font(30),
        action=info,
        image=button_bg_image
    )

    startButton = Button(
        screen=myScreen,
        x=Screen_width / 2 - 250 / 2,
        y=Screen_height / 2 - 100,
        width=250, height=80,
        color=(0, 100, 200),
        text="START",
        font=get_font(30),
        action=chooseEgg,
        image=button_bg_image
    )

    optionsButton = Button(
        screen=myScreen,
        x=Screen_width / 2 - 250 / 2,
        y=Screen_height / 2 + 100,
        width=250, height=80,
        color=(200, 50, 50),
        text="Options",
        font=get_font(30),
        action=optionsSelecLevel,
        image=button_bg_image
    )

    exitButton = Button(
        screen=myScreen,
        x=Screen_width / 2 - 250 / 2,
        y=Screen_height / 2 + 100 + 100,
        width=250, height=80,
        color=(200, 50, 50),
        text="EXIT",
        font=get_font(30),
        action=lambda: (pygame.quit(), exit()),
        image=button_bg_image
    )

    running = True
    """
    Główna pętla która działa do momentu wciśnięcia guzika exit np.
    Zaczynamy od rysowania tła i sprawdzanie eventu wciesniecia exit oraz wszystkich przycisków.
    A potem rysujemy przyciski które azdeklarowaliśmy już wcześniej
    """
    while running:
        myScreen.blit(bg_image, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            infoButton.check_click(event)
            startButton.check_click(event)
            exitButton.check_click(event)
            optionsButton.check_click(event)

        startButton.draw()
        infoButton.draw()
        exitButton.draw()
        optionsButton.draw()

        pygame.display.update()


def chooseEgg():
    """"
    Funckaj choose egg pokazuje na ekranie 4 ptzyciski.
    Ich zdjęcia to są konkretne zdjęcia jajek potworków.
    Po kliknięciu wywoływana jest odpowiednia funkcja która ustala jakie zwierzątko pokazać
    """

    """
    Setup tło i tekstu na oknie
    """
    pygame.display.set_caption("TAMAGOTCHI")
    bg_image = pygame.image.load("../assets/bg.png").convert()
    bg_image = pygame.transform.scale(bg_image, (Screen_width, Screen_height))

    """
    Wczytanie obrazków
    """
    egg1img = pygame.image.load("../assets/eggs/egg1.png")
    egg2img = pygame.image.load("../assets/eggs/egg2.png")
    egg3img = pygame.image.load("../assets/eggs/egg3.png")
    egg4img = pygame.image.load("../assets/eggs/egg4.png")

    """
    metoda wybrano1 ustawia którego zwierzaka pokazać
    """

    def wybrano1():
        global selected_animal_folder
        selected_animal_folder = os.path.join(BASE_DIR, "..", "assets", "animals", "animal1")
        selected_animal_folder = os.path.abspath(selected_animal_folder)
        takingCare()

    def wybrano2():
        global selected_animal_folder
        selected_animal_folder = os.path.join(BASE_DIR, "..", "assets", "animals", "animal2")
        selected_animal_folder = os.path.abspath(selected_animal_folder)
        takingCare()

    def wybrano3():
        global selected_animal_folder
        selected_animal_folder = os.path.join(BASE_DIR, "..", "assets", "animals", "animal3")
        selected_animal_folder = os.path.abspath(selected_animal_folder)
        takingCare()

    def wybrano4():
        global selected_animal_folder
        selected_animal_folder = os.path.join(BASE_DIR, "..", "assets", "animals", "animal4")
        selected_animal_folder = os.path.abspath(selected_animal_folder)
        takingCare()

    """
    Ustawienie jednokrotnych rozmiarów dla przycisków jajek.
    Deklarowanie guzików jajek podajć ich ekran do któego przypisać guzik
    Wpiasnie rozmierów i pozycji, Ustawienie koloru (dalej przyjmujemy na wszelki wypadek)
    podanie pustego tekstu i czcionki 
    (równiez podajemy tekst na wszelki wypadek bo tak wyglada moja kasla button)
    oraz jaką funkcje należy wykonac i jakie zdjęcie ustawić
    """
    eggWith = 150
    eggHeight = 150

    egg1 = Button(
        screen=myScreen,
        x=(myScreen.get_width() / 2) - 2 * eggWith,
        y=myScreen.get_height() / 2,
        width=eggWith,
        height=eggHeight,
        color=(200, 100, 100),
        text="",
        font=get_font(20),
        action=wybrano1,
        image=egg1img
    )

    egg2 = Button(
        screen=myScreen,
        x=(myScreen.get_width() / 2) - eggWith,
        y=myScreen.get_height() / 2,
        width=eggWith,
        height=eggHeight,
        color=(100, 100, 200),
        text="",
        font=get_font(20),
        action=wybrano2,
        image=egg2img
    )

    egg3 = Button(
        screen=myScreen,
        x=(myScreen.get_width() / 2),
        y=myScreen.get_height() / 2,
        width=eggWith,
        height=eggHeight,
        color=(100, 100, 200),
        text="",
        font=get_font(20),
        action=wybrano3,
        image=egg3img
    )

    egg4 = Button(
        screen=myScreen,
        x=(myScreen.get_width() / 2) + eggWith,
        y=myScreen.get_height() / 2,
        width=eggWith,
        height=eggHeight,
        color=(100, 100, 200),
        text="",
        font=get_font(20),
        action=wybrano4,
        image=egg4img
    )

    running = True
    while running:
        """
        Główna pętla, zaczyna od rysowania tła.
        Potem sprawdzamy eventy dla wszystkich przycisków.
        """
        myScreen.blit(bg_image, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            egg1.check_click(event)
            egg2.check_click(event)
            egg3.check_click(event)
            egg4.check_click(event)

        """
        Wypisanie napisu informacyjnego
        """
        chooseText = get_font(20).render("CHOOSE YOUR TAMAGOTCHI", True, "White")
        chooseRect = chooseText.get_rect(center=(Screen_width // 2, 250))
        myScreen.blit(chooseText, chooseRect)
        """
        Rywsoanwie jajko-guzików
        """
        egg1.draw()
        egg2.draw()
        egg3.draw()
        egg4.draw()

        pygame.display.update()


def takingCare():
    """
    Najbardziej obszerna funkcja która to jest odpowiedzialna za mian game loop podczas opieki na dzwierzakiem.
    Zmianiamy tytuło kna i odpalamy głowną pętle.
    W środku zaczynamy od wczytania tła (z folderu assets)
    Potem robimy obiekt animal A1
    Potem ładujemy animacje z danego folderu
    """
    pygame.display.set_caption("TAMAGOTCHI")
    running = True

    # Wczytanie tła
    bg_image = pygame.image.load("../assets/gbbg.png").convert()
    bg_image = pygame.transform.scale(bg_image, (Screen_width, Screen_height))

    """
    Deklaruje obiekt zwierzaka i potem ładujemy animacje.
    """
    a1 = Animal()
    global selected_animal_folder
    raw_frames = load_animation_frames(selected_animal_folder)
    animal_frames = [pygame.transform.scale(frame, (275, 275)) for frame in raw_frames]

    """
    current_frame to aktualny numer klatki animacji
    frame_delay co ile milisekund ma się zmieniać klatka 200 ms = 5 fps
    last_frame_switch zapisuje czas ostatniej zmiany klatki sluzy do kontrolowania tempa animacji
    """
    current_frame = 0
    frame_delay = 200
    last_frame_switch = pygame.time.get_ticks()
    """
    update_interval opisuje co ilemilisekund beda aktualizowane statystyki zwierzaka
    last_update_time to tez zapisny ostatki cas aktualizacji bo pomaga kontrolowac animacje
    """
    update_interval = 2000
    last_update_time = pygame.time.get_ticks()

    """
    Mesage co bedzie wypisywany jak klikamy guizk. Na poczatku wiadomosc jest pusta
    """
    message = ""
    sleeping = False
    sleep_start_time = 0
    sleep_duration = 5000

    """
    Wczytanie obrazków śpiącego zwierzaka (ifologia w zależności jakie jajko wybrano)
    """
    sleeping_img_path = selected_animal_folder.replace("animal1", "stills") + "/animal1sleeping.png"
    if "animal2" in selected_animal_folder:
        sleeping_img_path = selected_animal_folder.replace("animal2", "stills") + "/animal2sleeping.png"
    if "animal3" in selected_animal_folder:
        sleeping_img_path = selected_animal_folder.replace("animal3", "stills") + "/animal3sleeping.png"
    if "animal4" in selected_animal_folder:
        sleeping_img_path = selected_animal_folder.replace("animal4", "stills") + "/animal4sleeping.png"

    """
    Skalowanie zdjec
    """
    sleeping_image = pygame.image.load(sleeping_img_path).convert_alpha()
    sleeping_image = pygame.transform.scale(sleeping_image, (275, 275))

    """
    Aktualizowanie wiadomosci wyswietlanej jak wcisniety guzik.
    Ponieważ znienna jest poza funkcja używamy nonlocal
    """

    def update_message(new_msg):
        nonlocal message
        message = new_msg

    def feed_action():
        """
        Funkja która ma nakarmić zwierzaka, sprawdza czy postać nie śpi.
        Jak nie śpi to wywołuje a1.feed i przekazuje
        zwrócony tekst do update_message.
        Jak śpi to wiadomość o tym że śpi.
        """
        nonlocal sleeping
        if not sleeping:
            update_message(a1.feed())
        else:
            update_message("Your pet is sleeping and cannot eat now.")

    def sleep_action():
        """
        Funkja która ma zregenerować zwierzaka
        Jak nie śpi to wywołuje a1.sleep i przekazuje
        zwrócony tekst do update_message.
        Jak śpi to wiadomość o tym że śpi.
        """
        nonlocal sleeping, sleep_start_time
        if not sleeping:
            sleeping = True
            sleep_start_time = pygame.time.get_ticks()
            update_message("Your pet started sleeping...")

    def play_action():
        """
        Funkja która ma bawić zwierzaka, sprawdza czy postać nie śpi.
        Jak nie śpi to wywołuje a1.play_action i przekazuje
        zwrócony tekst do update_message.
        Jak śpi to wiadomość o tym że śpi.
        """
        nonlocal sleeping
        if not sleeping:
            update_message(a1.play())
        else:
            update_message("Your pet is sleeping and cannot play now.")

    """
    Robimy nasze guziki deklarując tak jak wcześniej pozycje, rozmiar,
    kolor, bez zdjęcia bo guzik jest na tle i tekst.
    """
    feedButton = Button(
        screen=myScreen,
        x=80, y=500,
        width=150, height=50,
        color=(0, 0, 0),
        text="Feed",
        font=get_font(25),
        action=feed_action,
        text_color="white"
    )
    sleepButton = Button(
        screen=myScreen,
        x=370, y=500,
        width=150, height=50,
        color=(0, 0, 0),
        text="Sleep",
        font=get_font(25),
        action=sleep_action,
        text_color="white"
    )
    playButton = Button(
        screen=myScreen,
        x=225, y=500,
        width=150, height=50,
        color=(200, 150, 50),
        text="Play",
        font=get_font(25),
        action=play_action,
        text_color="white"
    )
    backButton = Button(
        screen=myScreen,
        x=Screen_width // 2 - 200,
        y=Screen_height / 2 - 200,
        width=400,
        height=50,
        color=(200, 50, 50),
        text="BACK",
        font=get_font(70),
        action=mainMenu,
        text_color="white"
    )

    while running:
        """
        Główna pętla naszej metody. Game loop zaczyna od rysowani tła.
        Potem sprawdza eventy czy coś jest wciśnięte to wywołuje odpowiednią funkcje.
        
        """
        myScreen.blit(bg_image, (0, 0))

        """
        Sprawdzanie czy wciśnięte quit
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            backButton.check_click(event)

            """
            Guziki reagują na kliknięcia tylko gdy zwierzak żyje
            """
            if a1.alive:
                feedButton.check_click(event)
                sleepButton.check_click(event)
                playButton.check_click(event)

        """
        Spradzanie czy minęło wystarczająco dużo czasu,
        aby np. zmienić stan zwierzaka czy też jego klatke animacji
        """
        current_time = pygame.time.get_ticks()

        if a1.alive:
            """
            Jak zwierzaczek nie śpi i minelo ponad 2000 ms od ostatniej aktualizacji to 
            wywołujemy metode update która zmniejsza statystyki zwierzaka
            aktualizowany jest last_update_time  
            """
            if not sleeping and current_time - last_update_time > update_interval:
                a1.update()
                last_update_time = current_time

            """
            Obudzenie zwierzaka po odpowienim czasie.
            Zmiana jesgo stanu i wysłanie wiadomości
            Dodanie mu energii metodą sleep
            """
            if sleeping and current_time - sleep_start_time > sleep_duration:
                sleeping = False
                a1.sleep()
                update_message("Your pet woke up!")
        else:
            """
            Jak zwierzak nie żyje to usuwamy wiadmość
            """
            message = ""

        if message:
            msg_surf = get_font(10).render(message, True, (255, 255, 255))
            myScreen.blit(msg_surf, (100, 38))

        if a1.alive:
            if sleeping:
                """
                Jak zwierzak żyje i śpi wyświetla grafike śpiacego zwierzaka
                """
                image_rect = sleeping_image.get_rect(center=(Screen_width // 2, 200))
                myScreen.blit(sleeping_image, image_rect)
            else:
                """
                jak zwierzak nie spi to pokazujemy kolejna klatke animacji
                co frame_delay (200 ms) pzmieniamyt klastke animacji
                """
                if current_time - last_frame_switch > frame_delay:
                    current_frame = (current_frame + 1) % len(animal_frames)
                    last_frame_switch = current_time
                animal_image = animal_frames[current_frame]
                image_rect = animal_image.get_rect(center=(Screen_width // 2, 200))
                myScreen.blit(animal_image, image_rect)

        a1.show_stats(myScreen, get_font(15), 100, 350)

        """
        Rysowanie guzików karmienia snu i zabawy
        """
        feedButton.draw()
        sleepButton.draw()
        playButton.draw()

        """
        Rysowanie guzika back jak zwierzak umiera
        """
        if not a1.alive:
            backButton.draw()

        pygame.display.update()


def outOfRange(wartosc):
    """
    Funckja sprawdzająca czy nasza przekazan liczba jest w przedziale od 0 do 100.
    Pewnie dałoby sie to zrobić łatiwej bo to python ale ja miałem taki pomysł.
    """
    if (wartosc <= 0) or (wartosc >= 100):
        return True


def main():
    """
    Main function to run program.
    """
    mainMenu()


if __name__ == "__main__":
    main()
