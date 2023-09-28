"""
Test Cases:

Reflector: A
Rotors: I-II-III
Plugboard: A-R, G-K, O-X
Message: A=> X
"""
import pygame
pygame.init()
pygame.display.set_caption("Enigma simulator")

from Keyboard import keyboard
from Plugboard import plugboard
from Rotors import rotor
from Reflector import reflector
from Enigma import enigma

#Global variables for pygame
WIDTH=1600
HEIGHT=900
SCREEN=pygame.display.set_mode((WIDTH,HEIGHT))

#Fonts
#MONO=pygame.font.SysFont("Freemono", 25)
#BOLD=pygame.font.SysFont("Freemono", 25, bold=True)

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
ENIGMA = enigma(B,IV,II,I,PB,KB)

#Enigma Ring Settings
ENIGMA.set_rings((5,26,2))

#seting the Enigma Key
ENIGMA.set_key("CAT")
#ENIGMA.r1.show()
#ENIGMA.r2.show()
#ENIGMA.r3.show()

#Enciphering a message
message="MYNAMEISKARAN"
cipher_text=""
for letters in message:
    cipher_text=cipher_text+ENIGMA.encipher(letters)

print(cipher_text)

#
animating = True
while animating:
    SCREEN.fill("#333333")
    pygame.display.flip()

    #backdrop color
    SCREEN.fill("#333333")

    #Draw enigma machine
    KB.Draw(SCREEN, 1200, 200, 300, 500)

    #update screen
    pygame.display.flip()

    #user input
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            animating=False


#print(ENIGMA.encipher("A"))