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


    def Draw(self,screen,x,y,w,h):

        #rectangle
        r =pygame.Rect(x,y,w,h)
        pygame.draw.rect(screen, "White", r, width=2, border_radius=15)

        #letters
        for i in range(26):
            letter="ABCDEFGHIJKLMNOPQRSTUVWXYZ"[i]
            letter= font.render(letter, True, "grey")
            text_box = letter.get_rect(center = (x+w/2, (i+1)*h/27))
        
    
#k=keyboard()
#print(k.forward("A"))
#print(k.backward(0))