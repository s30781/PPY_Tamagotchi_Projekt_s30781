import pygame
from src.const import *

class Animal:
    def __init__(self):
        self.hunger = 100
        self.energy = 100
        self.happiness = 100
        self.alive = True
        self.health = 100


    def feed(self):
        """
        Metoda feed sluzy do karmienia zwierzaka, zwiekszamy głód o ustaloną wartość
        """
        if self.alive:
            self.hunger = min(100, self.hunger + settings["hungerValueForButton"])
            self.regenerate_health()
            return "Your pet has been fed!"
        return ""

    def sleep(self):
        """
        Metoda sleep sluzy do kzwiekzania wyspania zwierzaka o ustaloną wartość
        """
        if self.alive:
            self.energy = min(100, self.energy + settings["energyValueForButton"])
            self.hunger = max(0, self.hunger - 5)
            self.regenerate_health()

    def play(self):
        """
        Metoda play zwieksz poziom fun zwierzaka o ustaloną wartość
        """
        if self.alive:
            if self.happiness < 100:
                self.happiness = min(100, self.happiness + settings["funValueForButton"])
                self.regenerate_health()
                return "Your pet is happier now!"
            else:
                return "Your pet is already very happy!"
        return ""

    def decay_factor(self, value):
        """
        Metoda oblicza współczynnik spadku na podstawie wartości statystyki.
        Przy 100 współczynnik = 1 (normalny spadek),
        przy 0 współczynnik = 3 (3x szybszy spadek).
        """
        return 1 + (1 - value / 100) * 2

    def update(self):
        """
        Metoda update symuluje upływ czasu i pogarszanie się stanu zwierzaka
        zmienia sie głód, energia, szczęście, zdrowie
        Spadek zdrowia zwierzaka zaley od tego jakie sa wartosci zmiennych zwierzaka obecnie

        hunger_factor = self.decay_factor(self.hunger)
        energy_factor = self.decay_factor(self.energy)
        happiness_factor = self.decay_factor(self.happiness)
        Im gorszy stan (np. głód blisko 0), tym szybsze pogarszanie się innych statystyk.
        decay_factor() zwraca wartość między 1 (dla 100%) a 3 (dla 0%).

        self.energy = max(0, self.energy - int(5 * hunger_factor))
        Im bardziej głodny zwierzak, tym szybciej traci energię

        self.hunger = max(0, self.hunger - int(3 * energy_factor))
        Im mniej energii, tym szybciej robi się głodny.

        happiness_decay = int(2 * (hunger_factor + energy_factor) / 2)
        self.happiness = max(0, self.happiness - happiness_decay)
        Średnia z głodu i energii wpływa na tempo utraty szczęścia.

        min_stat = min(self.hunger, self.energy, self.happiness)
        health_decay = int(5 * self.decay_factor(min_stat) / 3)
        self.health = max(0, self.health - health_decay)
        Najgorsza statystyka (np. hunger = 0) powoduje największy spadek zdrowia.
        Zdrowie spada wolniej (dzielone przez 3), żeby zwierzak nie umierał zbyt szybko
        """
        if not self.alive:
            return

        hunger_factor = self.decay_factor(self.hunger)
        energy_factor = self.decay_factor(self.energy)
        happiness_factor = self.decay_factor(self.happiness)

        """
        Spadek energii zależny od poziomu głodu (im głodniejszy, tym szybciej energia spada)
        """
        self.energy = max(0, self.energy - int(5 * hunger_factor))

        """
        Spadek głodu zależny od poziomu energii (im mniej energii, tym szybciej głód rośnie)
        """
        self.hunger = max(0, self.hunger - int(3 * energy_factor))

        """
        Spadek szczęścia zależny od głodu i energii (średnia z tych dwóch czynników)
        """
        happiness_decay = int(2 * (hunger_factor + energy_factor) / 2)
        self.happiness = max(0, self.happiness - happiness_decay)

        """
        Zdrowie spada, ale wolniej niż wcześniej - dzielimy przez 3
        """
        min_stat = min(self.hunger, self.energy, self.happiness)
        health_decay = int(5 * self.decay_factor(min_stat) / 3)
        self.health = max(0, self.health - health_decay)

        self.check_alive()

    def regenerate_health(self):
        """
        Regeneruje zdrowie, ale tylko jeśli zwierzak żyje i zdrowie poniżej 100
        """
        if self.alive and self.health < 100:
            self.health = min(100, self.health + 10)

    def check_alive(self):
        """
        Sprawdza czy zwierzak żyje
        """
        if self.health <= 0:
            self.alive = False
            return "Your pet has passed away..."
        else:
            return ""

    def show_stats(self, screen, font, x, y):
        """
        Zbieraz strtystyki zwierzaka i nastepni wypisuje je przeentując je graficznym paskiem
        którego rozmiar zmienia się w zależnośic od wartości zmiennej
        """
        stats = {
            "Hunger": self.hunger,
            "Energy": self.energy,
            "Happiness": self.happiness,
            "Health": self.health
        }

        bar_width = 200
        bar_height = 15
        spacing = 30

        for i, (label, value) in enumerate(stats.items()):
            """
            Wypisanie tekstu
            """
            label_surface = font.render(f"{label}: ", True, "white")
            screen.blit(label_surface, (x, y + i * spacing))
            """
            Rysowanie tła paska
            """
            pygame.draw.rect(screen, "gray", (x + 200, y + i * spacing, bar_width, bar_height))
            """
            Rysowanie prostokątu, w zależności od wartości zmienia sie kolor paska
            """
            bar_color = "green" if value > 60 else "orange" if value > 30 else "red"
            pygame.draw.rect(screen, bar_color, (x + 200, y + i * spacing, int(bar_width * value / 100), bar_height))
        """
        Wyświetlanie komunikatu o śmierci
        """
        if not self.alive:
            dead_msg = font.render("Your pet is no longer with us...", True, "white")
            screen.blit(dead_msg, (100, 38))
