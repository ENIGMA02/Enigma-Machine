import pygame
pygame.init()

font = pygame.font.Font('freesansbold.ttf', 32)
 

class keyboard:
    def forward(self,letter):
        signal="ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter)
        return signal

    def backward(self,signal):
        letter="ABCDEFGHIJKLMNOPQRSTUVWXYZ"[signal]
        return letter


    def Draw(self,screen,x,y,w,h, font):

        #rectangle
        r =pygame.Rect(x,y,w,h)
        pygame.draw.rect(screen, "white", r, width=2, border_radius=15)

        #letters
        for i in range(26):
            letter="ABCDEFGHIJKLMNOPQRSTUVWXYZ"[i]
            letter= font.render(letter, True, "grey")
            text_box = letter.get_rect(center = (x + (i + 0.5) * (w / 26), y + h / 2))
            screen.blit(letter, text_box)
        
    
#k=keyboard()
#print(k.forward("A"))
#print(k.backward(0))