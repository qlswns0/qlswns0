import pygame
import os
pygame.init()
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("20202060 이예준")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GRAY = (200, 200, 200)

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT) # 보이지 않는 경계

current_path = os.path.dirname(__file__)

pygame.mixer.music.load(os.path.join(current_path, '이곳서강에07-8.mp3'))
pygame.mixer.music.play(-1) # 무한 반복 재생

BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join(current_path, 'Grenade01.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join(current_path, 'Gun+Silencer02.mp3'))
prof_skill2_sound = pygame.mixer.Sound(os.path.join(current_path, 'F줄꺼야.wav'))
Alros_skill2_sound = pygame.mixer.Sound(os.path.join(current_path, '알로스필살03-4.mp3'))
Professor_Win = pygame.mixer.Sound(os.path.join(current_path, 'prof_win03.mp3'))
Alros_totalwin = pygame.mixer.Sound(os.path.join(current_path, '알로스최종WIN02-4.mp3'))
levelup_sound = pygame.mixer.Sound(os.path.join(current_path, 'levelup001.wav'))

HEALTH_FONT = pygame.font.SysFont('comicsans', 20)
WINNER_FONT = pygame.font.SysFont('impact', 70, italic=True)
SCORE_FONT = pygame.font.SysFont('impact', 120, italic=True)

VEL = 7
BULLET_VEL = 7
MAX_BULLETS = 3
ALROS_WIDTH, ALROS_HEIGHT = 80, 90
PROF_WIDTH, PROF_HEIGHT = 100, 100 

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

Aloss = pygame.image.load(os.path.join(current_path, '알로스5.png')) # 대기화면
Sogang = pygame.image.load(os.path.join(current_path, 'Logo04.png'))
Sogang = pygame.transform.scale(Sogang, (80,100))

ALROS_IMAGE = pygame.image.load(os.path.join(current_path, 'alros008.png')) # 플레이어1
ALROS_IMAGE = pygame.transform.scale(ALROS_IMAGE, (ALROS_WIDTH, ALROS_HEIGHT))

PROF_IMAGE = pygame.image.load(os.path.join(current_path, '교수님002.png')) # 플레이어2
PROF_IMAGE = pygame.transform.scale(PROF_IMAGE, (PROF_WIDTH, PROF_HEIGHT))

BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join(current_path, 'sogang_campus.png')), (WIDTH, HEIGHT))

alros_win = pygame.transform.scale(pygame.image.load(os.path.join(current_path, '알로스4.png')), (120, 145))

Boom = pygame.image.load(os.path.join(current_path, 'boom.png'))
Course = pygame.image.load(os.path.join(current_path, '수강과목02.png'))





font_name = pygame.font.match_font('comicsans')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def show_go_screen():
    WIN.fill(WHITE)
    WIN.blit(Aloss, (415, 150))
    WIN.blit(Course, (265, 360))
    draw_text(WIN, "Coding Beginner", 50, WIDTH / 2, HEIGHT / 7)
    draw_text(WIN, "Can I Really Do This Class?", 40,
              WIDTH / 2, HEIGHT / 1.8)
    draw_text(WIN, "20202060 Ye-jun Lee", 15, 810, 470)
    pygame.display.flip()
    waiting = True
    while waiting:
        #clock.tick(60) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_SPACE:
                    waiting = False

def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    global yellow_healthh, red_healthh
    
    # 교수님 스킬2 '과제' 제작 (K_COMMA)
    if len(prof_bullet_xy) != 0:
        for i, bxy in enumerate(prof_bullet_xy):
            bxy[0] -= 10 # velocity
            prof_bullet_xy[i][0] = bxy[0]
            if bxy[0] < yellow.x and bxy[0] + 70 > yellow.x: 
                if bxy[1] > yellow.y - 20 and bxy[1] < yellow.y + 70: 
                    pygame.event.post(pygame.event.Event(YELLOW_HIT))
                    prof_bullet_xy.remove(bxy) # 충돌시 총알 사라지도록
            if bxy[0] <= 0:
                prof_bullet_xy.remove(bxy)
    if len(prof_bullet_xy) != 0: # draw
        for bx, by in prof_bullet_xy:
            WIN.blit(prof_bullet, (bx, by))

    # 교수님 스킬3 'F' 제작 (K_PERIOD)
    if len(prof_bullet2_xy) != 0:
        for i, bxy in enumerate(prof_bullet2_xy):
            bxy[0] -= 4
            prof_bullet2_xy[i][0] = bxy[0]
            if bxy[0] - 30 < yellow.x and bxy[0] + 220 > yellow.x:
                if bxy[1] > yellow.y - 280 and bxy[1] < yellow.y + 50:
                    prof_bullet2_xy.remove(bxy)
                    yellow_healthh -= 1
                    BULLET_HIT_SOUND.play()
            if bxy[0] <= -500:
                prof_bullet2_xy.remove(bxy)
    if len(prof_bullet2_xy) != 0:
        for bx, by in prof_bullet2_xy:
            WIN.blit(prof_bullet2, (bx, by))

    # 알로스 스킬2 '죄송' 제작 (K_TAB)
    if len(alros_bullet_xy) != 0:
        for i, bxy in enumerate(alros_bullet_xy):
            bxy[0] += 10
            alros_bullet_xy[i][0] = bxy[0]
            if bxy[0] > red.x and bxy[0] - 70 < red.x: 
                if bxy[1] > red.y - 20 and bxy[1] < red.y + 80:
                    pygame.event.post(pygame.event.Event(RED_HIT))
                    alros_bullet_xy.remove(bxy)
            if bxy[0] > WIDTH:
                alros_bullet_xy.remove(bxy)
    if len(alros_bullet_xy) != 0: 
        for bx, by in alros_bullet_xy:
            WIN.blit(alros_bullet, (bx, by))

    # 알로스 스킬3 '소강르타' 제작 (K_q)
    if len(alros_bullet2_xy) != 0:
        for i, bxy in enumerate(alros_bullet2_xy):
            bxy[0] += 4
            alros_bullet2_xy[i][0] = bxy[0]
            if bxy[0] + 100 > red.x and bxy[0] - 40 < red.x: 
                if bxy[1] > red.y - 280 and bxy[1] < red.y + 80:
                    alros_bullet2_xy.remove(bxy)
                    red_healthh -= 1
                    BULLET_HIT_SOUND.play()
            if bxy[0] > WIDTH:
                alros_bullet2_xy.remove(bxy)
    if len(alros_bullet2_xy) != 0:
        for bx, by in alros_bullet2_xy:
            WIN.blit(alros_bullet2, (bx, by))


    

    red_health_text = HEALTH_FONT.render(str(red_health) + " Prof of Visual Programming", 1, BLACK)
    yellow_health_text = HEALTH_FONT.render("Coding Beginner " + str(yellow_health), 1, BLACK)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))

    WIN.blit(ALROS_IMAGE, (yellow.x, yellow.y))
    WIN.blit(PROF_IMAGE, (red.x, red.y))

    for c in levelup_list:
        c.draw()

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    pygame.display.update()


def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: 
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:  
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: 
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15: 
        yellow.y += VEL


def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH: 
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0: 
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15:
        red.y += VEL


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet): # 총알이 알로스와 충돌하면 총알 삭제
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0: # 총알이 화면 밖으로 나가면 총알 삭제
            red_bullets.remove(bullet)


def draw_winner(text):
    if "Professor" in text:
        draw_text = WINNER_FONT.render(text, 1, BLACK)
        WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() / 2, HEIGHT/2 - draw_text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(1000)
        Professor_Win.play()
    elif "CODING" in text:
        draw_text = WINNER_FONT.render(text, 1, BLACK)
        WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() / 2, HEIGHT/2 - draw_text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(1000)
        Alros_totalwin.play()
        pygame.time.delay(5000)
    else:
        draw_text = SCORE_FONT.render(text, 1, BLACK)
        WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() / 2, HEIGHT/2 - draw_text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(2000)


class Levelup():
    def __init__(self, x, y):
        self.image = pygame.image.load(os.path.join(current_path, 'levelup01.png'))
        self.image = pygame.transform.scale(self.image, (70, 60))
        self.life_tick = 25
        self.x = x
        self.y = y
    def update(self,):
        self.life_tick -= 1
    def draw(self,):
        WIN.blit(self.image, (self.x, self.y))
 

def main():
    global prof_bullet, prof_bullet_xy, yellow_healthh, alros_bullet, alros_bullet_xy, red_healthh, prof_bullet2, prof_bullet2_xy, levelup_list, alros_bullet2, alros_bullet2_xy
    prof_bullet = pygame.image.load(os.path.join(current_path, '과제04.png'))
    prof_bullet = pygame.transform.scale(prof_bullet, (70,50))
    prof_bullet_xy = []
    prof_bullet2 = pygame.image.load(os.path.join(current_path, 'F_1.png'))
    prof_bullet2 = pygame.transform.scale(prof_bullet2, (220,300))
    prof_bullet2_xy = []
    alros_bullet = pygame.image.load(os.path.join(current_path, '죄송04.png'))
    alros_bullet = pygame.transform.scale(alros_bullet, (70,50))
    alros_bullet_xy = []
    alros_bullet2 = pygame.image.load(os.path.join(current_path, '소강르타01.png'))
    alros_bullet2 = pygame.transform.scale(alros_bullet2, (220,300))
    alros_bullet2_xy = []

    red = pygame.Rect(700, 300, PROF_WIDTH, PROF_HEIGHT)
    yellow = pygame.Rect(100, 300, ALROS_WIDTH, ALROS_HEIGHT)

    red_bullets = []
    yellow_bullets = []

    red_healthh = 5
    yellow_healthh = 5

    levelup_list = []

    clock = pygame.time.Clock()

    red_win_count = 0
    yellow_win_count = 0

    show_go_screen()

    run = True
    while run:  # 누군가 3승을 하기 전까지 while문 반복

        WIN.fill(GRAY)
        WIN.blit(BACKGROUND_IMAGE, (0, 0))
        WIN.blit(Sogang, (410, 60))
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 7)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 7)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_COMMA:
                    prof_bullet_x = red.x
                    prof_bullet_y = red.y + 30
                    if yellow_healthh <= 4:
                        if len(prof_bullet_xy) <= 0:
                            prof_bullet_xy.append([prof_bullet_x, prof_bullet_y])
                            prof_skill2_sound.play()

                if event.key == pygame.K_PERIOD:
                    prof_bullet2_x = red.x - 230
                    prof_bullet2_y = red.y + 30
                    if yellow_healthh <= 3:
                        #if len(prof_bullet_xy) == 0: # 스킬간에도 갯수제한을 주려면 설정
                        if len(prof_bullet2_xy) <= 0: #== 0:
                            prof_bullet2_xy.append([prof_bullet2_x, prof_bullet2_y])
                            prof_skill2_sound.play()

                if event.key == pygame.K_TAB:
                    alros_bullet_x = yellow.x
                    alros_bullet_y = yellow.y
                    if red_healthh <= 4:
                        if len(alros_bullet_xy) <= 0:
                            alros_bullet_xy.append([alros_bullet_x, alros_bullet_y])
                            BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_q:
                    alros_bullet2_x = yellow.x
                    alros_bullet2_y = yellow.y
                    if red_healthh <= 3:
                        if len(alros_bullet2_xy) <= 0:
                            alros_bullet2_xy.append([alros_bullet2_x, alros_bullet2_y])
                            Alros_skill2_sound.play()
            
            if event.type == RED_HIT:
                red_healthh -= 1
                if red_healthh == 4:
                    levelup_sound.play()
                    c = Levelup(yellow.x - 20, yellow.y - 40)
                    levelup_list.append(c)
                elif red_healthh == 3:
                    levelup_sound.play()
                    f = Levelup(yellow.x - 20, yellow.y - 40)
                    levelup_list.append(f)
                else:
                    BULLET_HIT_SOUND.play()
                

            if event.type == YELLOW_HIT:
                yellow_healthh -= 1
                if yellow_healthh == 4:
                    levelup_sound.play()
                    s = Levelup(red.x - 20, red.y - 40)
                    levelup_list.append(s)
                elif yellow_healthh == 3:
                    levelup_sound.play()
                    g = Levelup(red.x - 20, red.y - 40)
                    levelup_list.append(g)
                else:
                    BULLET_HIT_SOUND.play()

        for c in levelup_list:
            c.update()

        levelup_list = [c for c in levelup_list if c.life_tick >= 0]

        winner_text = ""

        if red_healthh == 0:
            WIN.blit(PROF_IMAGE, (red.x, red.y))
            WIN.blit(ALROS_IMAGE, (yellow.x, yellow.y))
            
            winner_text = "I CAN DO THE CODING!"

            yellow_win_count += 1
            if yellow_win_count < 3:
                draw_winner(str(yellow_win_count) + " : " + str(red_win_count))
                red_healthh = 5 # 목숨 초기화
                yellow_healthh = 5

                red.x = 700 # 위치초기화
                red.y = 300
                yellow.x = 100
                yellow.y = 300

                yellow_bullets = [] # 총알 생성 초기화
                red_bullets = []
                prof_bullet_xy = []
                prof_bullet2_xy = []
                alros_bullet_xy = []
                alros_bullet2_xy = []
                continue
            if yellow_win_count == 3: 
                WIN.blit(alros_win, (yellow.x - 23, yellow.y - 19))
                draw_winner(winner_text) # 승자 띄우기
                red_healthh = 5
                yellow_healthh = 5
                red.x = 700
                red.y = 300
                yellow.x = 100
                yellow.y = 300
                yellow_win_count = 0
                red_win_count = 0
                break
            

        if yellow_healthh == 0:
            WIN.blit(ALROS_IMAGE, (yellow.x, yellow.y))
            WIN.blit(Boom, (yellow.x, yellow.y))
            WIN.blit(PROF_IMAGE, (red.x, red.y))
 
            winner_text = "Professor WIN!"

            red_win_count += 1
            if red_win_count < 3:
                draw_winner(str(yellow_win_count) + " : " + str(red_win_count))
                red_healthh = 5
                yellow_healthh = 5

                red.x = 700
                red.y = 300
                yellow.x = 100
                yellow.y = 300

                yellow_bullets = []
                red_bullets = []
                prof_bullet_xy = []
                prof_bullet2_xy = []
                alros_bullet_xy = []
                alros_bullet2_xy = []
                continue
            if red_win_count == 3: 
                draw_winner(winner_text)
                pygame.time.delay(10000)
                red_healthh = 5
                yellow_healthh = 5
                red.x = 700
                red.y = 300
                yellow.x = 100
                yellow.y = 300
                yellow_win_count = 0
                red_win_count = 0
                break

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        draw_window(red, yellow, red_bullets, yellow_bullets, red_healthh, yellow_healthh)
        handle_bullets(yellow_bullets, red_bullets, yellow, red)    

        clock.tick(60)  

    main() # 누군가 3승을 해서 끝나면 다시 대기화면으로 돌아가기.


if __name__ == "__main__":
    main()