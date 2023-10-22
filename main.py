from funcion import *
#створення вікна
window = pygame.display.set_mode((setting_win["WIDTH"], setting_win["HEIGHT"]))
pygame.display.set_caption("КОСМІЧНИЙ ШУТЕР")

def run():
    game = True
    which_window = 1    #змінна для виведення різних вікон(гра, меню, магазин)
    start_time = 0
    end_time = 0

    hero = Hero(setting_win["WIDTH"] // 2 - setting_hero["WIDTH"] // 2, #x
                setting_win["HEIGHT"] - setting_hero["HEIGHT"] - 20,    #y
                setting_hero["WIDTH"],                                  #width
                setting_hero["HEIGHT"],                                 #height
                image= hero_image_list)

    clock = pygame.time.Clock()

    while game:
        events = pygame.event.get() #події з зовнішнього світу

        if which_window == 1:
            window.fill((20, 200,40))

            #HERO
            hero.move(window)
            for bullet in hero.BULLET_LIST:
                bullet.move_hero(hero, window )

            #BOT
            end_time = pygame.time.get_ticks()
            if end_time - start_time > 2000:
                bot_list.append(Bot(randint(0, setting_win["WIDTH"] - setting_bot["WIDTH"]),
                                            - setting_bot["HEIGHT"],
                                            setting_bot["WIDTH"],
                                            setting_bot["HEIGHT"], 
                                            image= bot_image_list))
                start_time = end_time
            for bot in bot_list:
                bot.move(window, hero)
            for bullet in bullet_bot_boss_list:
                bullet.move_bot_boss(hero, window)
            
            for event in events:    #перебираємо події
                if event.type == pygame.KEYDOWN:    #перевіряємо чи клавіші нажаті
                    if event.key == pygame.K_a:
                        hero.MOVE["LEFT"] = True
                    if event.key == pygame.K_d:
                        hero.MOVE["RIGHT"] = True
                    if event.key == pygame.K_SPACE:
                        hero.BULLET_LIST.append(Bullet(hero.centerx - 20, hero.y, 10, 20, color= (255, 20, 20)))
                if event.type == pygame.KEYUP:  #перевіряємо чи клавіші отпущені
                    if event.key == pygame.K_a:
                        hero.MOVE["LEFT"] = False
                    if event.key == pygame.K_d:
                        hero.MOVE["RIGHT"] = False

        for event in events:
            if event.type == pygame.QUIT:
                game = False
        
        clock.tick(setting_win["FPS"])
        pygame.display.flip()       #оновлюємо екран

run()
