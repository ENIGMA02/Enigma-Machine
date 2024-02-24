import pygame
pygame.init()

font = pygame.font.Font('freesansbold.ttf', 32)

class plugboard:
    
    def __init__(self,pairs):
        self.left="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for pair in pairs:
            A = pair[0]
            B = pair[1]
            pos_A = self.left.find(A)
            pos_B = self.left.find(B)
            self.left = self.left[:pos_A] + B + self.left[pos_A+1:]
            self.left = self.left[:pos_B] + A + self.left[pos_B+1:]
            

    def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal

    def backward(self, signal):
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal
    
    def Draw(self,screen,x,y,w,h, font):

        #rectangle
        r =pygame.Rect(x,y,w,h)
        pygame.draw.rect(screen, "white", r, width=2, border_radius=15)

        #letters
        for i in range(26):

            #LHS
            letter=self.left[i]
            letter= font.render(letter, True, "grey")
            text_box = letter.get_rect(center = (x + (i + 0.5) * (w / 26), y + h / 4))
            screen.blit(letter, text_box)

            #rHS
            letter=self.right[i]
            letter= font.render(letter, True, "grey")
            text_box = letter.get_rect(center = (x + (i + 0.5) * (w / 26), y + h* 3/ 4))
            screen.blit(letter, text_box)



#p=plugboard(["AC","BH"])
#print(p.forward(7))