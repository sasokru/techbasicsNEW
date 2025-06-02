import pygame
import random
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (255, 245, 250)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bouncing Hearts")
clock = pygame.time.Clock()

img_path = os.path.join("imagesource", "heart.png")
base_img = pygame.image.load(img_path).convert_alpha()
base_img = pygame.transform.scale(base_img, (60, 60))

class Heart:
    def __init__(self):
        self.image = base_img.copy()


        tint = random.randint(150, 255)
        self.image.fill((255, tint, tint, 0), special_flags=pygame.BLEND_RGBA_MULT)

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)

        self.speed_x = random.choice([-1, 1]) * random.uniform(2, 5)
        self.speed_y = random.choice([-1, 1]) * random.uniform(2, 5)

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y


        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.speed_x *= -1
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.speed_y *= -1

    def draw(self, surface):
        surface.blit(self.image, self.rect)


hearts = [Heart() for _ in range(12)]

running = True
while running:
    clock.tick(60)
    screen.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    for heart in hearts:
        heart.update()
        heart.draw(screen)

    pygame.display.flip()

pygame.quit()