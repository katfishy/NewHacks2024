import pygame

class CharacterStatus:
    def __init__(self, image_files, max_health, health_bar_size=(150, 20)):
        # Health attributes
        self.max_health = max_health
        self.current_health = max_health
        self.health_bar_width, self.health_bar_height = health_bar_size
        
        # Icon animation attributes
        self.frames = [pygame.image.load(img).convert_alpha() for img in image_files]
        self.current_frame = 0
        self.animation_speed = 0.5  # Default speed

    def take_damage(self, amount):
        self.current_health = max(0, self.current_health - amount)

    def increase_health(self, amount):
        self.current_health = min(self.max_health, self.current_health + amount)

    def get_health_percent(self):
        return (self.current_health / self.max_health) * 100

    def update(self):
        # Adjust animation speed based on health percentage
        health_percent = self.get_health_percent()
        self.animation_speed = 5 + (health_percent * 0.01)

        # Update frame progression based on animation speed
        self.current_frame += self.animation_speed * 0.01
        if health_percent >= 75:
            self.current_frame += self.animation_speed * 0.04
        elif health_percent >= 50:
            self.current_frame += self.animation_speed * 0.03
        elif health_percent >= 30:
            self.current_frame += self.animation_speed * 0.02
        if self.current_frame >= len(self.frames):
            self.current_frame = 0  # Reset to the first frame

    def draw(self, surface, icon_pos, health_bar_pos):
        # Draw the icon animation
        frame = self.frames[int(self.current_frame)]
        surface.blit(frame, icon_pos)

        # Draw the health bar
        health_ratio = self.current_health / self.max_health
        pygame.draw.rect(surface, 'white', (*health_bar_pos, self.health_bar_width, self.health_bar_height), 2)
        pygame.draw.rect(surface, 'brown', (*health_bar_pos, self.health_bar_width * health_ratio, self.health_bar_height))
