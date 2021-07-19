import sys
import pygame


class AlienInvasion:
    """Класс для управления ресурсами и воведением игры"""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            # Отслеживание событий миши и клавиатуры
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # отображение последнегого прорисованого экрана
            pygame.display.flip()

if __name__ == "__main__":
    #Создание екземпляра создания игры
    ai = AlienInvasion
    ai.run_game()