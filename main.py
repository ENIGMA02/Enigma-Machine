"""
Test Cases:

Reflector: A
Rotors: I-II-III
Plugboard: A-R, G-K, O-X
Message: A=> X
"""
import pygame
pygame.font.init()
pygame.display.set_caption("Enigma simulator")

from Keyboard import keyboard
from Plugboard import plugboard
from Rotors import rotor
from Reflector import reflector
from Enigma import enigma
from Draw import draw

#Global variables for pygame
WIDTH=1600
HEIGHT=900
SCREEN=pygame.display.set_mode((WIDTH,HEIGHT))
MARGINS={"top":200, "bottom":200, "left":100, "right":100, }
GAP=100


INPUT=""
OUTPUT=""
PATH=[]

#Fonts
MONO=pygame.font.SysFont("Freemono", 25)
BOLD=pygame.font.SysFont("Freemono", 25, bold=True)

# Enigma Rotor and Reflectors Setings from the orignal WWII Era
I = rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
IV = rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
A = reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
B = reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")


#keyboard and plugboard specifics
KB=keyboard()
PB=plugboard(["AB", "CD", "EF"])

#Enigma machine settings
ENIGMA = enigma(B,I,II,III,PB,KB)

#Enigma Ring Settings
ENIGMA.set_rings((1,1,1))

#seting the Enigma Key
ENIGMA.set_key("CAT")

animating = True
while animating:
    SCREEN.fill("#000000")
    #pygame.display.flip()

    #text input
    text= BOLD.render(INPUT, True, "white")
    text_box = text.get_rect(center = (WIDTH/2,MARGINS["top"]/3))
    SCREEN.blit(text, text_box)


    #text output
    text= MONO.render(OUTPUT, True, "white")
    text_box = text.get_rect(center = (WIDTH/2,MARGINS["top"]/3+25))
    SCREEN.blit(text, text_box)




    #Enigma MAchine
    draw(ENIGMA, PATH, SCREEN, WIDTH, HEIGHT, MARGINS, GAP, BOLD)


    #update screen
    pygame.display.flip()

    #user input
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            animating=False
        elif event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                III.rotate()
            elif event.key== pygame.K_SPACE:
                INPUT=INPUT+" "
                OUTPUT=OUTPUT+" "
            elif event.key==pygame.K_ESCAPE:
                animating=False
            # elif event.key==pygame.K_BACKSPACE:   # In progress to delete the last letter and reset the path to the previous letter
            #     INPUT=INPUT[:-1]
            #     PATH, cipher = ENIGMA.encipher(" ")
            #     OUTPUT=OUTPUT[:-1]
            else:
                key=event.unicode
                if key in "abcdefghijklmnopqrstuvwxyz":
                    letter=key.upper()
                    INPUT=INPUT+letter
                    PATH, cipher = ENIGMA.encipher(letter)
                    print(PATH)
                    OUTPUT=OUTPUT+cipher
                    print(INPUT)

