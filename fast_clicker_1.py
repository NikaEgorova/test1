import pygame
import time
from random import randint
pygame.init()

'''створюємо вікно програми'''
back = (200, 255, 255) #колір фону (background)
mw = pygame.display.set_mode((500, 500)) # вікно програми (main window)
mw.fill(back)
clock = pygame.time.Clock()

'''клас прямокутник'''
class Area():
  def __init__(self, x=0, y=0, width=10, height=10, color=None):
      self.rec = pygame.Rect(x, y, width, height) # Прямокутник
      self.fill_color = color
  def color(self, new_color):
      self.fill_color = new_color
  def fill(self):
      pygame.draw.rect(mw, self.fill_color, self.rec)
  def outline(self, frame_color, thickness): #обведення існуючого прямокутника
      pygame.draw.rect(mw, frame_color, self.rec, thickness)

'''клас напис'''
class Label(Area):
  def set_text(self, text, fsize=12, text_color=(200, 0, 0)):
      self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)
  def draw(self, shift_x=0, shift_y=0):
      self.fill()
      mw.blit(self.image, (self.rec.x + shift_x, self.rec.y + shift_y))

RED = (255, 0, 0)
GREEN = (0, 255, 51)
YELLOW = (255, 255, 0)
DARK_BLUE = (0, 0, 100)
BLUE = (80, 80, 255)
cards = []
num_cards = 4
x = 70
for i in range(num_cards):
  new_card = Label(x, 170, 70, 100, YELLOW)
  new_card.outline(BLUE, 10)
  new_card.set_text('CLICK', 26)
  cards.append(new_card)
  x += 100
 
wait = 0
while True:
  if wait == 0:
      #Переносимо напис:
      wait = 25 #стільки тиків напис буде на одному місці
      click = randint(1, num_cards)
      for i in range(num_cards):
          cards[i].color(YELLOW)
          if (i + 1) == click:
              cards[i].draw(10, 40)
          else:
              cards[i].fill()
  else:
      wait -= 1
 
  pygame.display.update()
  clock.tick(40)
