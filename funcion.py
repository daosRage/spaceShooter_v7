from data import *


class Sprite(pygame.Rect):
    def __init__(self, x, y, width, height, image= None, speed= None, hp= None):
        super().__init__(x, y, width, height)
        self.IMAGE_LIST = image
        self.IMAGE = self.IMAGE_LIST[0]
        self.IMAGE_COUNT = 0
        self.SPEED = speed
        self.HP = hp

    def move_image(self):
        self.IMAGE_COUNT += 1
        if self.IMAGE_COUNT == len(self.IMAGE_LIST) * 10 - 1:
            self.IMAGE_COUNT = 0
        if self.IMAGE_COUNT % 10 == 0:
            self.IMAGE = self.IMAGE_LIST[self.IMAGE_COUNT // 10]

class Hero(Sprite):
    def __init__(self, x, y, width, height, image= None, speed= 5, hp= 3):
        super().__init__(x, y, width, height, image, speed, hp)
        self.MOVE = {"LEFT": False, "RIGHT": False}
        self.BULLET_LIST = list()
    
    def move(self, window):
        if self.MOVE["LEFT"] == True:
            self.x -= self.SPEED
        if self.MOVE["RIGHT"] == True:
            self.x += self.SPEED
        window.blit(self.IMAGE, (self.x, self.y))
        self.move_image()

class Bot(Sprite):
    def __init__(self, x, y, width, height, image= None, speed= 1, hp= 1, body_damage= 1):
        super().__init__(x, y, width, height, image, speed, hp)
        self.SHOT = 0
        self.BODY_DAMAGE = body_damage

    def move(self, window, hero):
        self.y += self.SPEED
        window.blit(self.IMAGE, (self.x, self.y))

        self.SHOT += 1
        if self.SHOT % (setting_win["FPS"] * 2) == 0:
            bullet_bot_boss_list.append(Bullet(self.centerx, self.bottom, 10, 20, color= (20,240,20)))
        
        if self.colliderect(hero):
            hero.HP -= self.BODY_DAMAGE
            bot_list.remove(self)
            return 0


class Bullet(pygame.Rect):
    def __init__(self, x, y, width, height, image= None, color= None, speed= 2):
        super().__init__(x, y, width, height)
        self.IMAGE = image
        self.COLOR = color
        self.SPEED = speed

    def move_hero(self, hero, window):
        if self.y < 0:
            hero.BULLET_LIST.remove(self)
            return 0
        index = self.collidelist(bot_list)
        if index != -1:
            bot_list[index].HP -= 1
            if bot_list[index].HP == 0:
                bot_list.pop(index)
            hero.BULLET_LIST.remove(self)
            return 0
        self.y -= self.SPEED
        pygame.draw.rect(window, self.COLOR, self)
    
    def move_bot_boss(self, hero, window):
        if self.y > setting_win["HEIGHT"]:
            bullet_bot_boss_list.remove(self)
            return 0
        if self.colliderect(hero):
            hero.HP -= 1
            bullet_bot_boss_list.remove(self)
            return 0
        self.y += self.SPEED
        pygame.draw.rect(window, self.COLOR, self)
