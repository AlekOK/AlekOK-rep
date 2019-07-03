import pygame
pygame.init()
gameDisplay=pygame.display.set_mode((800,500))
pygame.display.set_caption("My first game")
clock=pygame.time.Clock()
crashed=False
x=0
y=0
width=70
height=60
vol=45


while not crashed:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed=True
        
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x> 5:
        x=x-vol 
    if  keys[pygame.K_RIGHT] and x <730:   
        x=x+vol
    if keys[pygame.K_UP] and y > 5:            
        y=y-vol  
    if keys[pygame.K_DOWN] and y <435:
        y=y+vol
    gameDisplay.fill((125,244,8))            
    pygame.draw.rect(gameDisplay,(255,0,0),[x,y,width,height],8)    
    pygame.display.update()

    clock.tick(60)

pygame.quit()
#quit()
