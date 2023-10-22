import pygame
from random import randint

#ініціалізуємо всі модулі пайгейма
pygame.init()

setting_win = {
    "WIDTH": 1000,
    "HEIGHT": 600,
    "FPS": 60
}
setting_hero = {
    "WIDTH": 130,
    "HEIGHT": 85
}
setting_bot = {
    "WIDTH": 80,
    "HEIGHT": 100
}

bot_list = list()
bullet_bot_boss_list = list()

hero_image_list = [
    pygame.transform.scale(pygame.image.load("image\\hero_fly_1.png"), (setting_hero["WIDTH"], setting_hero["HEIGHT"])),
    pygame.transform.scale(pygame.image.load("image\\hero_fly_2.png"), (setting_hero["WIDTH"], setting_hero["HEIGHT"]))
]
bot_image_list = [
    pygame.transform.scale(pygame.image.load("image\\bot_1_1.png"), (setting_bot["WIDTH"], setting_bot["HEIGHT"])),
    pygame.transform.scale(pygame.image.load("image\\bot_1_2.png"), (setting_bot["WIDTH"], setting_bot["HEIGHT"]))
]
