import pygame


class BulletEntity:
    def draw(self, surface, entity):
        width, height = pygame.display.get_window_size()
        x = self.x - entity.x + width/2
        y = self.y - entity.y + height/2
        pygame.draw.circle(surface, self.color, (x, y), self.radius)
