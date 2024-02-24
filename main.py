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
MARGINS={"top":50, "bottom":100, "left":300, "right":300, }
GAP=50


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
#ENIGMA.r1.show()
#ENIGMA.r2.show()
#ENIGMA.r3.show()

# #Enciphering a message
# message="MYNAMEISKARAN"
# cipher_text=""
# for letters in message:
#     cipher_text=cipher_text+ENIGMA.encipher(letters)

# print(cipher_text)

#
animating = True
while animating:
    SCREEN.fill("#333333")
    #pygame.display.flip()

    #text input
    text= BOLD.render(INPUT, True, "white")
    text_box = text.get_rect(center = (HEIGHT/2,MARGINS["bottom"]/2))
    SCREEN.blit(text, text_box)


    #text output
    text= MONO.render(OUTPUT, True, "white")
    text_box = text.get_rect(center = (HEIGHT/2,MARGINS["bottom"]/2+20))
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
            else:
                key=event.unicode
                if key in "abcdefghijklmnopqrstuvwxyz":
                    letter=key.upper()
                    INPUT=INPUT+letter
                    PATH, cipher = ENIGMA.encipher(letter)
                    print(PATH)
                    OUTPUT=OUTPUT+cipher
                    print(INPUT)


#print(ENIGMA.encipher("A"))