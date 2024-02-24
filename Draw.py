import pygame

def draw(enigma, screen, width, height, margins, gap, font):
    #Draw enigma machine
    enigma.kb.Draw(screen, 300, 750, margins["top"], 50, font)
    enigma.pb.Draw(screen, 300, 600, margins["top"], 100, font)
    enigma.r3.Draw(screen, 300, 450, margins["top"], 100, font)
    enigma.r2.Draw(screen, 300, 300, margins["top"], 100, font)
    enigma.r1.Draw(screen, 300, 150, margins["top"], 100, font)
    enigma.re.Draw(screen, 300, 25, margins["top"], 75, font)