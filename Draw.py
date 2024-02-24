import pygame

def draw(enigma,path, screen, width, height, margins, gap, font):

    #Height and Width
    h=(height-margins["top"]-margins["bottom"]-(5*gap)) /6
    w=width-margins["left"]-margins["right"]

    #Coordinates Path
    y=[margins["top"]+h/2]
    x=[margins["left"]+(signal+0.5)*w/26 for signal in path]#Keaboard
    for i in [4,3,2,1,0]:#Front Pass
        y.append(margins["bottom"]+(i+1)*(1+gap)+w*3/4)
        y.append(margins["bottom"]+(i+1)*(1+gap)+w*1/4)

    for i in [1,2,3,4]:#Back Pass
        y.append(margins["bottom"]+(i+1)*(1+gap)+w*1/4)
        y.append(margins["bottom"]+(i+1)*(1+gap)+w*3/4)
        y.append(margins["left"]+(signal+0.5)*w/26 for signal in path)#lampboard


    #Draw path
    for i in range(1,20):
        print(i)
        start =(x[i-1],y[i-1])
        end = (x[i],y[i])
        pygame.draw.line(screen,"red", start, end, width=5)
    

    #Draw enigma machine
    x=margins["top"]
    y=margins["left"]
    


    #Drawing enigma components
    for componenets in [enigma.re, enigma.r1, enigma.r2,enigma.r3, enigma.pb, enigma.kb]:
        componenets.Draw(screen, y, x, w, h, font)
        x+=h+gap