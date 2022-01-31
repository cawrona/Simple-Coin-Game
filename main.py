
import pgzrun
import pygame
from random import randint #how to get random
import time



#screen --> constant
import pygame.mixer

WIDTH = 775
HEIGHT = 400
speed = 5
player = Actor('player_01') #you can change the image that you want
player.pos = 300, 200
score = 0
timer = 60
game_over = False
animation_coin = 1
coin = Actor("coin-1")
slime = Actor("slime")
coin.pos = 200, 200


pygame.mixer.init()
pygame.mixer.music.load('sounds/music.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

coinSound = pygame.mixer.Sound('sounds/collect_coins.wav')
endSound = pygame.mixer.Sound('sounds/gameover.wav')


#create a function to make the coin move randomly
def place_coin():
  coin.x = randint(20, (WIDTH -20))
  coin.y = randint(20, (HEIGHT -20))
  

#give us the background and the player and the coin
def draw():
  screen.fill("light green")
  player.draw()
  coin.draw()
  slime.draw()
  screen.draw.text("Score: " + str(score),fontsize=40, color = "black", topleft=(10,10))
  
  screen.draw.text(str(timer),fontsize=150, color = "black", topleft=(325,10))

  if game_over:
    
    screen.fill("red")
    screen.draw.text(("game over"),fontsize=100, color = "black", topleft=(200, 100))
    pygame.mixer.music.stop()
    endSound.play()
    endSound.set_volume(0.5)
    
    





#make the player move with the keyboard
def update():
    global speed
    global score
    global animation_coin
    global game_over
    
    if animation_coin == 1:
      coin.image="coin-2"
      animation_coin = animation_coin + 1
    else:
      coin.image="coin-1"
      animation_coin = animation_coin - 1

    if keyboard.left and player.x > player.width/2:
      player.x = player.x - speed
      player.image = "player_14"

    elif keyboard.right and player.x < WIDTH-player.width/2:
        player.x = player.x + speed
        player.image="player_11"
    elif keyboard.up and player.y > player.height/2:
        player.y = player.y - speed
        player.image="player_02"
    if keyboard.down and player.y < HEIGHT-player.height/2:
        player.y = player.y + speed
        player.image="player_01"

    if player.colliderect(coin):
      place_coin()
      score = score + 1
      coinSound.play()
      
   
    if player.colliderect(slime):
      game_over = True  
        
def update_clock():

  global timer
  global game_over

  timer = timer - 1
  if timer == 0:
    game_over = True

def slime_movement():
  slime.pos = randint(0, WIDTH), randint(0, HEIGHT)

clock.schedule_interval(slime_movement,3)
clock.schedule_interval(update_clock,1)

pgzrun.go()
