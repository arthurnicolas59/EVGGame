import pygame
import random

class PixelAnimation(pygame.sprite.Sprite):
    def __init__(self, max_w, max_h, image_path, image_w, image_h):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image_path).convert_alpha(), (image_w, image_h))  # Replace "image.jpg" with the path to your image file
        self.image.set_colorkey((255, 255, 255))  # Set white color as transparent
        self.rect = self.image.get_rect()

        #screen info
        self.max_w, self.max_h = max_w, max_h

        # Set random position along the screen boundaries
        side = random.randint(0, 3)  # Selects a random side of the screen (0: top, 1: right, 2: bottom, 3: left)
        if side == 0:  # Top side
            self.rect.x = random.randint(0, self.max_w - self.rect.width)
            self.rect.y = 0
            self.speed_x = random.randint(-5, 5)  # Adjust the range based on your desired horizontal speed
            self.speed_y = random.randint(1, 5)  # Adjust the range based on your desired vertical speed
        elif side == 1:  # Right side
            self.rect.x = 800 - self.rect.width
            self.rect.y = random.randint(0, self.max_h - self.rect.height)
            self.speed_x = random.randint(-5, -1)  # Adjust the range based on your desired horizontal speed
            self.speed_y = random.randint(-5, 5)  # Adjust the range based on your desired vertical speed
        elif side == 2:  # Bottom side
            self.rect.x = random.randint(0, self.max_w - self.rect.width)
            self.rect.y = 600 - self.rect.height
            self.speed_x = random.randint(-5, 5)  # Adjust the range based on your desired horizontal speed
            self.speed_y = random.randint(-5, -1)  # Adjust the range based on your desired vertical speed
        else:  # Left side
            self.rect.x = 0
            self.rect.y = random.randint(0, self.max_h - self.rect.height)
            self.speed_x = random.randint(1, 5)  # Adjust the range based on your desired horizontal speed
            self.speed_y = random.randint(-5, 5)  # Adjust the range based on your desired vertical speed

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Check if the image has hit the screen boundaries
        if self.rect.x <= 0 or self.rect.x >= self.max_w - self.rect.width:
            self.speed_x *= -1
        if self.rect.y <= 0 or self.rect.y >= self.max_h - self.rect.height:
            self.speed_y *= -1




