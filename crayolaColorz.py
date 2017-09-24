#
#   CRAYOLA COLORZ by WILL GREENBERG, 2017
#       Fuckin' with Crayola standard colors yo
#
#
import json, sys, pygame, webcolors, time
from pygame.locals import *
import struct


# Import the JSON data

with open('crayolaColorz.json', 'r+') as data:
    jsonDict = json.load(data)
    #print(jsonDict)

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 400))
bgColorHex = jsonDict['colors'][0]['hex']
bgColorRGB = webcolors.hex_to_rgb(bgColorHex)
fontObj = pygame.font.Font('freesansbold.ttf', 32)

index = 23

while True:
    for color in jsonDict['colors']:

        bgColorHex = color['hex']
        text = color['color']
        bgColorRGB = webcolors.hex_to_rgb(bgColorHex)
        TEXT_COLOR = webcolors.hex_to_rgb(jsonDict['colors'][index]['hex'])
        textObj = fontObj.render(text, True, TEXT_COLOR)
        textRectObj = textObj.get_rect()
        textRectObj.center = (200, 200)
        DISPLAYSURF.fill(bgColorRGB)
        DISPLAYSURF.blit(textObj, textRectObj)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit
                sys.exit()

        time.sleep(0.8)
        index += 23
        index = index % 100
        pygame.display.update()
