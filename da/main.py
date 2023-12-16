import pygame
import random

clock = pygame.time.Clock()
health = 100
health2 = 100  
health_bar_width = 400  
health_bar_height = 20  
health_bar_back_color = (0, 0, 0)  
health_bar_color = (153,0,0)
pygame.init()
screen = pygame.display.set_mode((1600,900))
pygame.display.set_caption("Death Battle")
bg = pygame.image.load("da/icons/win.jpg")
bg = pygame.transform.scale(bg, (1600, 900))
pygame.display.set_icon(pygame.image.load("da/icons/icon.PNG"))
blackass = pygame.transform.scale(pygame.image.load("da/icons/black.jpg"), (1600, 900)).convert_alpha()

title_font = pygame.font.Font("da/fonts/Mortal-Kombat-MK11.otf",350)
button_font = pygame.font.Font("da/fonts/Mortal-Kombat-MK11.otf",50)
button_font1 = pygame.font.Font("da/fonts/Mortal-Kombat-MK11.otf",90)
you_lose_title = title_font.render("YOU LOSE", False, (153, 0, 0))
you_win_title = title_font.render("YOU WIN", False, (153, 0, 0))
play_again = button_font.render("PLAY AGAIN", False, (102, 0, 0))
exit_botton = button_font.render("EXIT", False, (102, 0, 0))
exit_rect = exit_botton.get_rect(topleft = (780,780))
back = button_font.render("BACK TO MENU", False, (102, 0, 0))
back_rect = back.get_rect(topleft = (650,800))
restart_rect = play_again.get_rect(topleft = (700,650))
bg_sound = pygame.mixer.Sound("da/music/bgmusic.mp3")
bg_sound.set_volume(0.1)
bg_sound.play(-1)

icon = pygame.transform.scale(pygame.image.load("da/icons/icon.PNG"), (360, 360)).convert_alpha()
ninja = pygame.transform.scale(pygame.image.load("da/icons/anim/IMG_0565.PNG"), (360, 640))

movement1 = [
    pygame.transform.scale(pygame.image.load("da/icons/anim/IMG_0565.PNG"), (360, 640)),
    pygame.transform.scale(pygame.image.load("da/icons/anim/IMG_0566.PNG"), (360, 640)),
    pygame.transform.scale(pygame.image.load("da/icons/anim/IMG_0565.PNG"), (360, 640)),
    pygame.transform.scale(pygame.image.load("da/icons/anim/IMG_0564.PNG"), (360, 640))
   
]

bomber = pygame.transform.scale(pygame.image.load("da/icons/anim/IMG_0567.PNG"), (360, 640))
movement2 = [
    pygame.transform.scale(pygame.image.load("da/icons/anim/IMG_0567.PNG"), (360, 640)),
    pygame.transform.scale(pygame.image.load("da/icons/anim/IMG_0569.PNG"), (360, 640)),
    pygame.transform.scale(pygame.image.load("da/icons/anim/IMG_0567.PNG"), (360, 640)),
    pygame.transform.scale(pygame.image.load("da/icons/anim/IMG_0568.PNG"), (360, 640))
   
]
bomber_sounds = [pygame.mixer.Sound("da/music/hit1.mp3"),
                 pygame.mixer.Sound("da/music/hit2.mp3"),
                ]
hoos = [
            pygame.mixer.Sound("da/music/hoo1.mp3"),
            pygame.mixer.Sound("da/music/hoo2.mp3"),
            pygame.mixer.Sound("da/music/hoo3.mp3")
            ]
armhits = [
            pygame.mixer.Sound("da/music/hoo4.mp3"),
            pygame.mixer.Sound("da/music/hoo5.mp3"),
            pygame.mixer.Sound("da/music/hoo6.mp3")
            ]
leghits = [
            pygame.mixer.Sound("da/music/legninja.mp3"),
            pygame.mixer.Sound("da/music/legninja2.mp3")
            ]
damage = [
            pygame.mixer.Sound("da/music/oof.mp3"),
            pygame.mixer.Sound("da/music/oof1.mp3"),
            pygame.mixer.Sound("da/music/oof2.mp3"),
            pygame.mixer.Sound("da/music/oof3.mp3"),
            pygame.mixer.Sound("da/music/oof4.mp3"),
            ]
move_count = 0
ninja_speed = 65
bomber_speed = 65
ninja_x = 1000
ninja_y = 200
isJump = False
jumpCount = 4
jumpCount2 = 4
bomber_x = 300
bomber_y = 200
flag = True
hitted = False
hitted1 = False
bomber_hitted = False
bomber_hitted1 = False
var = [1,1,1,2,2,3,3,4,5,5,5,6,6,6]
t_flag = False
m_flag = True
t=0
n_flag = True
n1_flag = True
damaged = False
tickle = 0
menu_flag = True
pushed = 0
pushed2 = 0
l2 = 0
dyst = 0
l_2 = 0
dam = 1


while flag:

    mouse = pygame.mouse.get_pos()
    if pushed ==0:
        pushed2 = 0
        screen.blit(blackass, (0, 0))
        screen.blit(icon, (650,100))
        play_button = pygame.transform.scale(pygame.image.load("da/icons/playgame.jpg"), (360,70)).convert_alpha()
        play_rect = play_button.get_rect(topleft = (650, 500))
        screen.blit(play_button, play_rect)
        options = pygame.transform.scale(pygame.image.load("da/icons/options.jpg"), (360,70)).convert_alpha()
        opti_rect = options.get_rect(topleft = (650,600))
        screen.blit(options, opti_rect)
        insructions = pygame.transform.scale(pygame.image.load("da/icons/instructions.jpg"), (360,70)).convert_alpha()
        inst_rect = insructions.get_rect(topleft = (650,700))
        screen.blit(insructions, inst_rect)
        screen.blit(exit_botton, (exit_rect))
    if exit_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0] and pushed == 0:
            flag = False
    if opti_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0] and tickle<200 or pushed == 2:
        pushed = 2
        screen.blit(blackass, (0, 0))
        lev_botton = button_font1.render("DIFFICULTY LEVEL", False, (102, 0, 0))
        level = lev_botton.get_rect(topleft =  (450,300))
        screen.blit(lev_botton, (level))
        location = button_font1.render("CHOOSE LOCATION", False, (102, 0, 0))
        loc_rect = location.get_rect(topleft =  (450,450))
        screen.blit(location, (loc_rect))
        if level.collidepoint(mouse) and pygame.mouse.get_pressed()[0] or pushed2 == 2:
            pushed2 = 2
            screen.blit(blackass, (0, 0))
            lev1 = button_font1.render("EASY LEVEL", False, (102, 0, 0))
            lev1_rect = lev1.get_rect(topleft = (550,150))
            lev2 = button_font1.render("MID LEVEL", False, (102, 0, 0))
            lev2_rect = lev2.get_rect(topleft = (550,400))
            lev3 = button_font1.render("PRO LEVEL", False, (102, 0, 0))
            lev3_rect = lev3.get_rect(topleft = (550,650))
            screen.blit(lev1, (lev1_rect))
            screen.blit(lev2, (lev2_rect))
            screen.blit(lev3, (lev3_rect))
            if lev1_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                var = [1,1,1,2,2,3,3,4,5,5,5,6,6,6]
                pushed = 0 
                l2 = 0
                dyst = 0
                l_2 = 0
                dam = 1
            if lev2_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                var = [1,1,1,1,2,3,5,3,3,4,5,5,5,6,6,6,1,5,6,5,6]
                pushed = 0
                l2 = 10
                dyst = 300
                l_2 = 3
                dam = 1.5
            if lev3_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                var = [1,1,1,1,2,3,5,3,3,4,5,5,5,6,6,6,1,5,6,5,6,5,6,3,3,6,5,6,5]
                pushed = 0
                l2 = 10
                dyst = 300
                l_2 = 3
                dam = 2.5


        if loc_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0] and tickle<200 or pushed2 == 1:
            pushed2 = 1
            screen.blit(blackass, (0, 0))
            bg1 = pygame.transform.scale(pygame.image.load("da/icons/arena.png"), (400,300)).convert_alpha()
            bg1_rect = bg1.get_rect(topleft = (200, 300))
            bg2 = pygame.transform.scale(pygame.image.load("da/icons/win.jpg"), (400,300)).convert_alpha()
            bg2_rect = bg2.get_rect(topleft = (1000, 300))
            screen.blit(bg1, (bg1_rect))
            screen.blit(bg2, (bg2_rect))
            if bg1_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                bg = pygame.transform.scale(pygame.image.load("da/icons/arena.png"), (1600, 900))
                pushed = 0
            elif bg2_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                bg = pygame.transform.scale(pygame.image.load("da/icons/win.jpg"), (1600, 900))
                pushed  = 0

    if inst_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0] and tickle<200 or pushed == 3:
        pushed = 3
        screen.blit(blackass, (0, 0))
        screen.blit(button_font1.render("CHARACTER CONTROL", False, (102, 0, 0)), (450,120))
        screen.blit(button_font.render("LEFT and RIGHT - the movements of the fighter ", False,(102, 0, 0)), (150,300))
        screen.blit(button_font.render("E - kick ", False,(102, 0, 0)), (150,400))
        screen.blit(button_font.render("R - punch ", False,(102, 0, 0)), (150,500))
        screen.blit(button_font.render("E + R - block ", False,(102, 0, 0)), (150,600))
        screen.blit(button_font.render("SPACE - jump ", False,(102, 0, 0)), (150,700))
        screen.blit(back, (back_rect))
        if back_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            pushed = 0
    if play_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0] or pushed == 1:
        pushed = 1
        screen.blit(bg, (0, 0))
        ninja_rect = pygame.Rect(ninja_x+70, ninja_y+170, 150, 370)
        bomber_rect = pygame.Rect(bomber_x+100, bomber_y+170, 150, 370)

        pygame.draw.rect(screen, health_bar_back_color, (1100, 70, health_bar_width, health_bar_height))
        pygame.draw.rect(screen, health_bar_color, ((1500-health * 4), 70, health * 4, health_bar_height))
        pygame.draw.rect(screen, health_bar_back_color, (100, 70, health_bar_width, health_bar_height))
        pygame.draw.rect(screen, health_bar_color, (100, 70, health2 * 4, health_bar_height))
        
        if move_count == 3:
            move_count = 0
        else:
            move_count+=1
        if (health2>0 and health>0) or isJump or k == 4:
            if t<=0:
                k = random.choice(var)
                t_flag = True
                m_flag = True
                pic = 0
                damaged = False

            if (t>0 or k==2 or k==3) and k!=1 and k!=4 and k!=5 and k!=6 and pic == 0 and (health2>0 and health>0):
                screen.blit(movement2[move_count], (bomber_x, bomber_y)) 

            if k == 1:
                screen.blit( pygame.transform.scale(pygame.image.load("da/icons/anim/bomblock.PNG"), (360, 640)), (bomber_x, bomber_y))
                if t_flag == True:
                    t = random.randint(10,40-l2)
                t_flag = False

            elif k == 2 and bomber_x>0 and (ninja_x-bomber_x>=dyst or pic == 1):
                bomber_x -= bomber_speed
                if t_flag == True:
                    t = random.randint(4,16-l2)
                t_flag = False
                if pic == 1:
                    screen.blit( pygame.transform.scale(pygame.image.load("da/icons/anim/damaged.PNG"), (360, 640)), (bomber_x, bomber_y))
            if bomber_x == 0:
                    pic = 0
            elif k == 3 and ninja_x-bomber_x>= 200 + dyst:
                bomber_x += bomber_speed
                if t_flag == True:
                    t = random.randint(4,16-l2)
                t_flag = False

            elif (k == 4 and ninja_x-bomber_x>= dyst) or (k == 4 and t>0):
                screen.blit( pygame.transform.scale(pygame.image.load("da/icons/anim/bomJUMP.PNG"), (360, 640)), (bomber_x, bomber_y))
                if jumpCount2 >= -4:
                    if jumpCount2 > 0:
                        bomber_y -= (jumpCount2 ** 4)*0.7
                    else:
                        bomber_y += (jumpCount2 ** 4)*0.7
                    jumpCount2 -= 1
                else:
                    
                    jumpCount2 = 4
                if t_flag == True:
                    t = 30
                t_flag = False

            elif k ==5:
                bomber_rect = pygame.Rect(bomber_x+100,bomber_y+170, 250, 370 )
                if ninja_rect.colliderect(bomber_rect) and (t_flag == True) and not (keys[pygame.K_r] and keys[pygame.K_e]):
                    health-=10*dam
                    damaged = True
                    random.choice(damage).play()
                    t_flag = False
                    t=9-l_2
                    ninja_x+=65
                if m_flag == True:
                    pygame.mixer.Sound("da/music/leg.mp3").play()
                    m_flag = False
                screen.blit( pygame.transform.scale(pygame.image.load("da/icons/anim/bomberLEG.PNG"), (360, 640)), (bomber_x, bomber_y))
                
            elif k ==6:
                bomber_rect = pygame.Rect(bomber_x+100,bomber_y+170, 250, 370 )
                if ninja_rect.colliderect(bomber_rect) and (t_flag == True) and not (keys[pygame.K_r] and keys[pygame.K_e]):
                    health-=5*dam
                    damaged = True
                    random.choice(damage).play()
                    t_flag = False
                    t=6-l_2
                    ninja_x+=35
                if m_flag == True:
                    random.choice(hoos).play()
                    m_flag = False
                screen.blit( pygame.transform.scale(pygame.image.load("da/icons/anim/bomberARM.PNG"), (360, 640)), (bomber_x, bomber_y))
            t-=3

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and ninja_x-bomber_x>=200:
                ninja_x -= ninja_speed

            if (keys[pygame.K_RIGHT] or damaged) and ninja_x <1300:
                ninja_x += ninja_speed
                if damaged:
                    screen.blit( pygame.transform.scale(pygame.image.load("da/icons/anim/damagedn.PNG"), (360, 640)), (ninja_x, ninja_y))
            if keys[pygame.K_e] and (not keys[pygame.K_r]) and not damaged:
                if n1_flag==True:
                    random.choice(leghits).play()
                    n1_flag = False
                ninja_rect = pygame.Rect(ninja_x, ninja_y+170, 150, 370)
                if ninja_rect.colliderect(bomber_rect) and (not hitted) and k!=1:
                        hitted = True
                        health2-=10
                        if bomber_x > 0:
                            if k!=4:
                                k = 2
                                t = 9
                                t_flag = False
                                pic = 1
                        random.choice(bomber_sounds).play()
                screen.blit( pygame.transform.scale(pygame.image.load("da/icons/anim/leghit.PNG"), (360, 640)), (ninja_x, ninja_y))
            else:
                hitted = False
                n1_flag = True

            if keys[pygame.K_r] and (not keys[pygame.K_e]) and not damaged:
                if n_flag==True:
                    random.choice(armhits).play()
                    n_flag = False
                ninja_rect = pygame.Rect(ninja_x, ninja_y+170, 150, 370)
                if ninja_rect.colliderect(bomber_rect) and (not hitted1) and k!=1:
                        hitted1 = True
                        health2-=5
                        if bomber_x > 0:
                            if k!=4:
                                k = 2
                                t = 6
                                t_flag = False
                                pic = 1
                        random.choice(bomber_sounds).play()
                screen.blit( pygame.transform.scale(pygame.image.load("da/icons/anim/cross.PNG"), (360, 640)), (ninja_x, ninja_y))  
            else:
                hitted1 = False
                n_flag = True

            if keys[pygame.K_r] and keys[pygame.K_e] and not damaged:
                    screen.blit( pygame.transform.scale(pygame.image.load("da/icons/anim/block.PNG"), (360, 640)), (ninja_x, ninja_y)) 
                    
            if not isJump and (not keys[pygame.K_e]) and (not keys[pygame.K_r]) and (not damaged) and  ((health2>0 and health>0) or k ==4):
                screen.blit(movement1[move_count], (ninja_x, ninja_y))

            if not isJump:
                if keys[pygame.K_SPACE]:
                    isJump = True
            else:
                if (not keys[pygame.K_e]) and (not keys[pygame.K_r]) and (not damaged):
                    screen.blit( pygame.transform.scale(pygame.image.load("da/icons/anim/jump.PNG"), (360, 640)), (ninja_x, ninja_y))
                
                if jumpCount >= -4:
                    if jumpCount > 0:
                        ninja_y -= (jumpCount ** 4)*0.7
                    else:
                        ninja_y += (jumpCount ** 4)*0.7
                    jumpCount -= 1
                else:
                    isJump = False
                    jumpCount = 4
        
        


        if health <=0 and (not isJump) and (k!=4):
            screen.blit(movement2[move_count], (bomber_x, 200)) 
            screen.blit( pygame.transform.scale(pygame.image.load("da/icons/anim/dead.PNG"), (360, 640)), (ninja_x, ninja_y))
            blackass.set_alpha(tickle)
            screen.blit(blackass, (0, 0))
            if tickle >= 120:
                screen.blit(you_lose_title, (75,300))
            tickle+=5
            
        if health2 <=0 and (not isJump) and (k!=4):
            screen.blit(movement1[move_count], (ninja_x, 200))
            screen.blit( pygame.transform.scale(pygame.image.load("da/icons/anim/damaged.PNG"), (360, 640)), (bomber_x, bomber_y))
            blackass.set_alpha(tickle)
            screen.blit(blackass, (0, 0))
            if tickle >= 120:
                screen.blit(you_win_title, (150,300))
            tickle+=5
        mouse = pygame.mouse.get_pos()
        if tickle >= 200:
                screen.blit(play_again, (restart_rect))
                screen.blit(back, (back_rect))
                if restart_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                    health = health2 = 100
                    ninja_x = 1000
                    ninja_y = 200
                    isJump = False
                    jumpCount = 4
                    jumpCount2 = 4
                    bomber_x = 300
                    bomber_y = 200
                    flag = True
                    hitted = False
                    hitted1 = False
                    bomber_hitted = False
                    bomber_hitted1 = False
                    t_flag = False
                    m_flag = True
                    t=0
                    n_flag = True
                    n1_flag = True
                    damaged = False
                    tickle = 0
                    pushed = 1
                if back_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                    pushed = 0

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False

    pygame.display.update()
    clock.tick(8)
