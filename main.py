"""
Test Cases:

Reflector: A
Rotors: I-II-III
Plugboard: A-R, G-K, O-X
Message: A=> X
"""

from Keyboard import keyboard
from Plugboard import plugboard
from Rotors import rotor
from Reflector import reflector
from Enigma import enigma



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
PB=plugboard(["AR", "GK", "OX"])

#Enigma machine settings
ENIGMA = enigma(A,I,II,III,PB,KB)

#Enciphering a letter
print(ENIGMA.encipher("A"))