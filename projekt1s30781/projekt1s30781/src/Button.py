"""
Nie ukrywam że do robienia guzika wzorowalem sie na poradniku na yt
https://www.youtube.com/watch?v=al_V4OGSvFU
"""
import pygame

class Button:
    def __init__(self, screen, x, y, width, height, color=(200, 0, 0), text='', font=None, text_color='white', action=None, image=None):
        """
        konstruktor przyjmuje dane i ustawia je
        """
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.font = font or pygame.font.SysFont("Arial", 20)
        self.text_color = text_color
        self.action = action
        self.image = image


    def draw(self):
        """
        jeśli został podany obrazek to jest on rysowany i skalowany do rozmiaru przycisku
        dodatkowo zawsze rysuje tekst na guizku (jak nie chemy tekstu to dajemy pusy string)
        """
        if self.image:
            scaled_image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
            self.screen.blit(scaled_image, self.rect.topleft)

        if self.text:
            text_surf = self.font.render(self.text, True, self.text_color)
            text_rect = text_surf.get_rect(center=self.rect.center)
            self.screen.blit(text_surf, text_rect)


    def check_click(self, event):
        """
        Sprawdza czy użytkownik klikną myszką.
        Jeśli kliknięcie było i jest w guziku to wywołujemy metoda
        która to została przekazana przy towrzniu guzika
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if self.action:
                    self.action()
