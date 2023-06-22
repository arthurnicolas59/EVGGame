import pygame, sys
from states.sprites import PixelAnimation
from states.healthbar import HealthBar

class GameState():
  
    def __init__(self, screen):
        self.state = 'intro'
        
        #screen info
        self.screen = screen
        self.screen_w, self.screen_h = self.screen.get_size()

        #global image
        self.quit_image = pygame.transform.scale(pygame.image.load('assets/images/message-24-error.png').convert_alpha(), (36, 36))  # Replace "image.jpg" with the path to your image file
        self.quit_image_rect = self.quit_image.get_rect(topleft = (self.screen_w - self.quit_image.get_width(),0))

        #intro variables
        self.intro_bg = pygame.image.load('assets/images/polution2.jpeg')
        self.intro_bg_rescale = pygame.transform.scale(self.intro_bg, (self.screen_w, self.screen_h))
        self.intro_font = pygame.font.Font('assets/font/arcade_ya/ARCADE_R.TTF', size=self.screen_w//18)
        self.intro_text = self.intro_font.render('THE GAETAN GAME', True, 52)
        self.gaetan_group = pygame.sprite.Group()
        for _ in range(8):
            image = PixelAnimation(max_w=self.screen_w, max_h=self.screen_h, image_path="assets/images/gaetan_pixelart.png",
                                   image_w= 256 // 2.5, image_h= 256 // 2.5)
            self.gaetan_group.add(image)

        #input stage variables
        self.input_bg = pygame.image.load('assets/images/background_input.jpeg')
        self.input_bg_rescale = pygame.transform.scale(self.input_bg, (self.screen_w, self.screen_h))
        self.input_font = pygame.font.Font('assets/font/arcade_ya/ARCADE_R.TTF', size=self.screen_w//35)
        self.input_question = self.input_font.render('COMBIEN GAETAN A DE PTS DE VIE', True, (255, 0, 0))
        self.input_answer_1 = self.input_font.render('100 points de vie', True, (255, 0, 0))
        self.input_answer_2 = self.input_font.render('75 points de vie', True, (255, 0, 0))
        self.input_answer_3 = self.input_font.render('50 points de vie', True, (255, 0, 0))
        self.input_answer_4 = self.input_font.render('25 points de vie', True, (255, 0, 0))
        # self.veine_group = pygame.sprite.Group()
        # for _ in range(3):
        #     image = PixelAnimation(max_w=self.screen_w, max_h=self.screen_h, image_path="assets/images/veine.png",
        #                            image_w= 500 // 3, image_h= 375 // 3)
        #     self.veine_group.add(image)
        
        self.input_rect_1 = self.input_answer_1.get_rect(center=((self.screen_w // 2,
                                            (self.screen_h - self.input_answer_1.get_height()) // 10 * 3)))
        self.input_rect_2 = self.input_answer_2.get_rect(center = (self.screen_w // 2,
                                            (self.screen_h - self.intro_text.get_height()) // 10 * 5))
        self.input_rect_3 = self.input_answer_3.get_rect(center = (self.screen_w // 2,
                                            (self.screen_h - self.intro_text.get_height()) // 10 * 7))
        self.input_rect_4 = self.input_answer_4.get_rect(center = (self.screen_w // 2,
                                            (self.screen_h - self.intro_text.get_height()) // 10 * 9))
        
        #main_game variables
        self.main_game_bg = pygame.image.load('assets/images/background_main_game.jpeg')
        self.main_game_rescale = pygame.transform.scale(self.main_game_bg, (self.screen_w, self.screen_h))
        self.healthbar = HealthBar(x=self.screen_w // 4, y= self.screen_h - (self.screen_h // 15 * 3), w = self.screen_w // 2, h= self.screen_h // 15 - 20, max_hp= 100)
        self.main_game_font = pygame.font.Font('assets/font/arcade_ya/ARCADE_R.TTF', size=self.screen_w//50)
        self.main_game_question = self.main_game_font.render("QUEL IMPACT SUR L'EMPRUNTE CARBONE DE GAETAN", True, (255, 0, 0))
        self.main_game_answer_1 = self.main_game_font.render("+100, Quelqu'un a pris l'avion", True, (255, 0, 0))
        self.main_game_answer_2 = self.main_game_font.render("+50, 5 veines sur le front", True, (255, 0, 0))
        self.main_game_answer_3 = self.main_game_font.render("+25, 2,5 veines sur le front", True, (255, 0, 0))
        self.main_game_answer_4 = self.main_game_font.render("+10, 1 veine sur le front", True, (255, 0, 0))
        self.main_game_rect_1 = self.main_game_answer_1.get_rect(center=((self.screen_w // 2,
                                                (self.screen_h - self.main_game_answer_1.get_height()) // 12 * 3)))
        self.main_game_rect_2 = self.main_game_answer_2.get_rect(center = (self.screen_w // 2,
                                                (self.screen_h - self.intro_text.get_height()) // 12 * 5))
        self.main_game_rect_3 = self.main_game_answer_3.get_rect(center = (self.screen_w // 2,
                                                (self.screen_h - self.intro_text.get_height()) // 12 * 7))
        self.main_game_rect_4 = self.main_game_answer_4.get_rect(center = (self.screen_w // 2,
                                                (self.screen_h - self.intro_text.get_height()) // 12 * 9))
        self.veine = pygame.image.load('assets/images/veine.png')

        self.image_veine = pygame.transform.scale(pygame.image.load('assets/images/veine.png').convert_alpha(), (133, 100))  # Replace "image.jpg" with the path to your image file
        self.image_veine.set_colorkey((255, 255, 255))  # Set white color as transparent
        
        #game over variables
        self.game_over_font = pygame.font.Font('assets/font/arcade_ya/ARCADE_R.TTF', size=self.screen_w//18)
        self.game_over_text = self.intro_font.render('GAME OVER', True, (255, 255, 255))
        self.game_over_image = pygame.image.load('assets/images/gaetan_pixelart.png')
        self.game_over_image.set_colorkey((255, 255, 255))  # Set white color as transparent
        self.game_over_group = pygame.sprite.Group()
        for _ in range(25):
                    image = PixelAnimation(max_w=self.screen_w, max_h=self.screen_h, image_path="assets/images/shotpixelart.png",
                                        image_w= 256 // 2.5, image_h= 256 // 2.5)
                    self.game_over_group.add(image)

    def intro(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = 'input_stage'
                if self.quit_image_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
        
        #Drawing
        self.screen.fill('black')
        self.screen.blit(self.intro_bg_rescale, (0,0))
        self.screen.blit(self.intro_text, ((self.screen_w - self.intro_text.get_width()) // 2,
                                            (self.screen_h - self.intro_text.get_height()) // 2))
        self.gaetan_group.update()
        self.gaetan_group.draw(self.screen)
        self.screen.blit(self.quit_image, self.quit_image_rect)


        #Render
        pygame.display.flip()
    
    def input_stage(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.input_rect_1.collidepoint(event.pos):
                    self.healthbar.hp = 0
                    self.state = 'main_game'
                if self.input_rect_2.collidepoint(event.pos):
                    self.healthbar.hp = 25
                    self.state = 'main_game'
                if self.input_rect_3.collidepoint(event.pos):
                    self.healthbar.hp = 50
                    self.state = 'main_game'
                if self.input_rect_4.collidepoint(event.pos):
                    self.healthbar.hp = 75
                    self.state = 'main_game'
                if self.quit_image_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
        
        #Drawing
        self.screen.fill('black')
        self.screen.blit(self.input_bg_rescale, (0,0))
        self.screen.blit(self.input_question, ((self.screen_w - self.input_question.get_width()) // 2,
                                            (self.screen_h - self.input_question.get_height()) // 10))
        self.screen.blit(self.input_answer_1, self.input_rect_1)
        self.screen.blit(self.input_answer_2, self.input_rect_2)
        self.screen.blit(self.input_answer_3, self.input_rect_3)
        self.screen.blit(self.input_answer_4, self.input_rect_4)
        #self.veine_group.update()
        #self.veine_group.draw(self.screen)
        self.screen.blit(self.quit_image, self.quit_image_rect)

        #render
        pygame.display.flip()


    def main_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.main_game_rect_1.collidepoint(event.pos):
                    self.healthbar.hp = self.healthbar.hp + 100
                    if self.healthbar.hp >= 100:
                        self.state = 'game_over'
                if self.main_game_rect_2.collidepoint(event.pos):
                    self.healthbar.hp = self.healthbar.hp + 50
                    if self.healthbar.hp >= 100:
                        self.state = 'game_over'
                if self.main_game_rect_3.collidepoint(event.pos):
                    self.healthbar.hp = self.healthbar.hp + 25
                    if self.healthbar.hp >= 100:
                        self.state = 'game_over'
                if self.main_game_rect_4.collidepoint(event.pos):
                    self.healthbar.hp = self.healthbar.hp + 10
                    if self.healthbar.hp >= 100:
                        self.state = 'game_over'
                if self.quit_image_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
        
        #Drawing
        self.screen.fill('black')
        self.screen.blit(self.main_game_rescale, (0,0))
        self.healthbar.draw(self.screen)
        self.screen.blit(self.main_game_question, ((self.screen_w - self.main_game_question.get_width()) // 2,
                                            (self.screen_h - self.main_game_question.get_height()) // 10))
        self.screen.blit(self.main_game_answer_1, self.main_game_rect_1)
        self.screen.blit(self.main_game_answer_2, self.main_game_rect_2)
        self.screen.blit(self.main_game_answer_3, self.main_game_rect_3)
        self.screen.blit(self.main_game_answer_4, self.main_game_rect_4)
        if self.healthbar.hp >= 5:
            self.screen.blit(self.image_veine, (0,self.screen_h - self.image_veine.get_height()))
        if self.healthbar.hp >= 15:
            self.screen.blit(self.image_veine, (self.image_veine.get_width(),self.screen_h - self.image_veine.get_height()))
        if self.healthbar.hp >= 25:
            self.screen.blit(self.image_veine, (self.image_veine.get_width() * 2,self.screen_h - self.image_veine.get_height()))
        if self.healthbar.hp >= 35:
            self.screen.blit(self.image_veine, (self.image_veine.get_width() * 3,self.screen_h - self.image_veine.get_height()))
        if self.healthbar.hp >= 45:
            self.screen.blit(self.image_veine, (self.image_veine.get_width() * 4,self.screen_h - self.image_veine.get_height()))
        if self.healthbar.hp >= 55:
            self.screen.blit(self.image_veine, (self.image_veine.get_width() * 5,self.screen_h - self.image_veine.get_height()))
        if self.healthbar.hp >= 65:
            self.screen.blit(self.image_veine, (self.image_veine.get_width() * 6,self.screen_h - self.image_veine.get_height()))
        if self.healthbar.hp >= 75:
            self.screen.blit(self.image_veine, (self.image_veine.get_width() * 7,self.screen_h - self.image_veine.get_height()))
        if self.healthbar.hp >= 85:
            self.screen.blit(self.image_veine, (self.image_veine.get_width() * 8,self.screen_h - self.image_veine.get_height()))
        if self.healthbar.hp >= 95:
            self.screen.blit(self.image_veine, (self.image_veine.get_width() * 9,self.screen_h - self.image_veine.get_height()))
        self.screen.blit(self.quit_image, self.quit_image_rect)


        #render
        pygame.display.flip()

    def game_over(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = 'intro'
                if self.quit_image_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
        
        #Drawing
        self.screen.fill('black')
        self.screen.blit(self.game_over_text, ((self.screen_w - self.game_over_text.get_width()) // 2,
                                            (self.screen_h - self.game_over_text.get_height()) // 5))
        self.screen.blit(self.game_over_image, (self.screen_w // 2 - 256 / 2, self.screen_h // 2 - 256 / 2))
        self.game_over_group.update()
        self.game_over_group.draw(self.screen)
        self.screen.blit(self.quit_image, self.quit_image_rect)

        #render
        pygame.display.flip()


    def state_manager(self):
        if self.state == 'intro':
            self.intro()
        
        if self.state == 'input_stage':
            self.input_stage()
        
        if self.state == 'main_game':
            self.main_game()

        if self.state == 'game_over':
            self.game_over()
