#thu vien
import pygame,sys
import random
pygame.init()
clock = pygame.time.Clock()
def update_score(score,highscore):
    if score > highscore:
        highscore=score
    return highscore
def create_pipe():
    random_pipe_pos= random .choice(pipe_high)
    bottom_pipe= pipe_surface.get_rect(midtop=(500,random_pipe_pos))
    top_pipe= pipe_surface.get_rect(midtop=(500,random_pipe_pos-700))
    return bottom_pipe,top_pipe
def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx-=3
    return pipes
def draw_pipe(pipes):
    for pipe in pipes:
        if pipe.bottom >=768:
            screen.blit(pipe_surface,pipe)
        else:
            flip_pipe= pygame.transform.flip(pipe_surface,False,True)
            screen.blit(flip_pipe,pipe)    
def check_collision(pipes):
    for pipe in pipes:
        if bird_hcn.colliderect(pipe):
            return False
    if bird_hcn.top<=-75 or bird_hcn.bottom>=650:
            return False
    return True
def rotate_bird(bird1):
    new_bird=pygame.transform.rotozoom(bird1,-bird_move*4,1)
    return new_bird
def score_display(game_state):
    if game_state == 'main game':
        score_surface=game_font.render(str(int(score)),True,(255,255,255))
        score_surface_hcn=score_surface.get_rect(center =(216,100))
        screen.blit(score_surface,score_surface_hcn)
    if game_state =='game_over':
        score_surface=game_font.render(f'Score: {str(int(score))}',True,(255,255,255))
        score_surface_hcn=score_surface.get_rect(center =(216,100))
        screen.blit(score_surface,score_surface_hcn)

        highscore_surface=game_font.render(f'High score: {str(int(highscore))}',True,(255,255,255))
        highscore_surface_hcn=highscore_surface.get_rect(center =(216,610))
        screen.blit(highscore_surface,highscore_surface_hcn)
# tao bien tro choi
game_font=pygame.font.Font(r'D:\code\visual code\game\FileGame\04B_19.TTF',40)
p=0.10
game_active=True 
score=0
highscore=0
#tieu de va icon,background
pygame.display.set_caption('Game flappy bird')
icon=pygame.image.load(r'D:\code\visual code\game\icon.png')
bg=pygame.image.load(r'D:\code\visual code\game\FileGame\assets\background-night.png')
bg = pygame.transform.scale2x(bg)
pygame.display.set_icon(icon)
fl=pygame.image.load(r'D:\code\visual code\game\FileGame\assets\floor.png')
fl = pygame.transform.scale2x(fl)
fl_x=0 

# man hinh ket thuc
end=pygame.image.load(r'D:\code\visual code\game\FileGame\assets\message.png')
end = pygame.transform.scale2x(end)
end_hcn=end.get_rect(center=(216,370))
# Bird
bird=pygame.image.load(r'D:\code\visual code\game\FileGame\assets\yellowbird-midflap.png')
bird = pygame.transform.scale2x(bird)
bird_hcn=bird.get_rect(center=(100,384))
bird_move=0

# Pipe
pipe_surface=pygame.image.load(r'D:\code\visual code\game\FileGame\assets\pipe-green.png')
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list=[]

#Tao time
spawn_pipe= pygame.USEREVENT
pygame.time.set_timer(spawn_pipe,1200)
pipe_high=[300,400,500]
#cua so game
screen=pygame.display.set_mode((432,768))

#vong lap xu li game
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE and game_active :
                bird_move=0
                bird_move=-5
            if event.key==pygame.K_SPACE and game_active==False:
                game_active=True
                pipe_list.clear()
                bird_hcn.center=(100,284)
                bird_move=0
                score=0

        if event.type==spawn_pipe:
            pipe_list.extend(create_pipe())
    screen.blit(bg,(0,0))
#game active
    if game_active:
    # bird
        bird_move+=p
        rotated_bird= rotate_bird(bird)
        bird_hcn.centery+=bird_move
        screen.blit(rotated_bird,bird_hcn)
        game_active=check_collision(pipe_list)
    #pipe
        pipe_list= move_pipe(pipe_list)
        draw_pipe(pipe_list)
    # score
        score_display('main game')
        score+=0.01

    else:
        highscore=update_score(score,highscore)
        score_display('game_over')
        screen.blit(end,end_hcn)
#floor
    fl_x-=1   
    screen.blit(fl,(fl_x,650))
    screen.blit(fl,(fl_x+432,650))
    if fl_x==-432:
        fl_x=0

    pygame.display.update()
    clock.tick(120)