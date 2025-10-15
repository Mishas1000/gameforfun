import pygame

class Game:
  def __init__(self):
    pygame.init()
    # Window name
    pygame.display.set_caption('Da Game')
    # Screen resolution
    screen = pygame.display.set_mode((1280, 720))
    # Clock
    clock = pygame.time.Clock()
    # Game quit when false
    running = True

  def run(self):
    while self.running:
      # fill the screen with a color to wipe away anything from last frame
      self.screen.fill((14, 219, 248))
      # poll for events
      # pygame.QUIT event means the user clicked X to close your window
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              self.running = False

      # RENDER YOUR GAME HERE
      pygame.draw.rect(self.screen, "red", pygame.Rect([0, 0, 40, 40])) # If each tile is 40x40px, then the screen is 32x18 tiles

      # flip() the display to put your work on screen
      pygame.display.update()

      self.clock.tick(60)  # limits FPS to 60

  pygame.quit()
