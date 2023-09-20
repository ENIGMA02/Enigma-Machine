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
message="TEST"
cipher_text=""
for letters in message:
    cipher_text=cipher_text+ENIGMA.encipher(letters)

print(cipher_text)

#print(ENIGMA.encipher("A"))