import pygame

def draw(enigma, screen, width, height, margins, gap, font):
    #Draw enigma machine
    x=margins["top"]
    y=margins["left"]
    h=(height-margins["top"]-margins["bottom"]-(5*gap)) /6
    w=width-margins["left"]-margins["right"]
    # print(h)

    for componenets in [enigma.re, enigma.r1, enigma.r3,enigma.r3, enigma.pb, enigma.kb]:
        componenets.Draw(screen, y, x, w, h, font)
        x+=h+gap
    # enigma.re.Draw(screen, y, x, 1000, h, font)
    # enigma.r1.Draw(screen, y, 150, 1000, h, font)
    # enigma.r2.Draw(screen, y, 300, 1000, h, font)
    # enigma.r3.Draw(screen, y, 450, 1000, h, font)
    # enigma.pb.Draw(screen, y, 600, 1000, h, font)
    # enigma.kb.Draw(screen, y, 750, 1000, h, font)
    