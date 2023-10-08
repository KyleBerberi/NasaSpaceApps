# Imports
import pgzrun
from pgzero.actor import Actor
from random import randint
from pgzero.keyboard import keyboard
import random
import time
from pygame import Rect

global music

# Variables
state = 0
music.play('spacemusic')
music.set_volume(0.3)
WIDTH = 960
HEIGHT = 540
bg = Actor('bg.png')
# slide 2 images
solarsystem = Actor('solarsystem.png')
mercurybig = Actor('mercurybig.png')
mercurybig.pos = WIDTH - 780, HEIGHT // 2
venusbig = Actor('venusbig.png')
venusbig.pos = WIDTH - 700, HEIGHT // 2 - 30
marsbig = Actor('marsbig.png')
marsbig.pos = WIDTH - 580, HEIGHT // 2 - 100
jupiterbig = Actor('jupiterbig.png')
jupiterbig.pos = WIDTH - 472, HEIGHT // 2 - 100
saturnbig = Actor('saturnbig.png')
saturnbig.pos = WIDTH - 350, HEIGHT // 2 - 160
uranusbig = Actor('uranusbig.png')
uranusbig.pos = WIDTH - 260, HEIGHT // 2 - 210
neptunebig = Actor('neptunebig.png')
neptunebig.pos = WIDTH - 185, HEIGHT // 2 - 250
cursor = Actor('cursor.png')
cursor.pos = WIDTH // 2, HEIGHT // 2 + 400
mercuryitinerary = Actor('mercuryitinerary .png')
neptuneitinerary = Actor('neptuneitinerary .png')
uranusitinerary = Actor('uranusitinerary .png')
marsitinerary = Actor('marsitinerary .png')
saturnitinerary = Actor('saturnitinerary .png')
venusitinerary = Actor('venusitinerary .png')
jupiteritinerary = Actor('jupiteritinerary .png')
filter = Actor('filter.png')
filter.pos = WIDTH - 100, HEIGHT // 2 - 200



RED = 200, 0, 0
above = Rect((800, 100), (120, 30))
below = Rect((800, 70), (120, 30))
any = Rect((800, 40), (120, 30))
all = Rect((150, 240), (660, 140))


def draw():
    screen.clear()
    if state == 0:
        screen.clear()
        bg.draw()
        cursor.draw()
        filter.draw()



    if state == 1:
        solarsystem.draw()
        mercurybig.draw()
        venusbig.draw()
        marsbig.draw()
        jupiterbig.draw()
        saturnbig.draw()
        uranusbig.draw()
        neptunebig.draw()


        cursor.draw()
        print(state)

    if state == 9: #below price range
        solarsystem.draw()
        mercurybig.draw()
        venusbig.draw()
        marsbig.draw()

        cursor.draw()

    if state == 10:
        solarsystem.draw()
        jupiterbig.draw()
        saturnbig.draw()
        uranusbig.draw()
        neptunebig.draw()

        cursor.draw()

    if state == 2:
        screen.clear()
        solarsystem.draw()
        mercurybig.draw()
        mercuryitinerary.draw()

        cursor.draw()

    if state == 3:
        screen.clear()
        solarsystem.draw()
        venusbig.draw()
        venusitinerary.draw()
        cursor.draw()

    if state == 4:
        screen.clear()
        solarsystem.draw()
        marsbig.draw()
        marsitinerary.draw()
        cursor.draw()

    if state == 5:
        screen.clear()
        solarsystem.draw()
        jupiterbig.draw()
        jupiteritinerary.draw()
        cursor.draw()

    if state == 6:
        screen.clear()
        solarsystem.draw()
        saturnbig.draw()
        saturnitinerary.draw()
        cursor.draw()

    if state == 7:
        screen.clear()
        solarsystem.draw()
        uranusbig.draw()
        uranusitinerary.draw()
        cursor.draw()

    if state == 8:
        screen.clear()
        solarsystem.draw()
        neptunebig.draw()
        neptuneitinerary.draw()
        cursor.draw()

def on_mouse_move(pos):
    cursor.x = pos[0]  # pos[0] is x
    cursor.y = pos[1]  # pos[1] is y


def on_mouse_down(pos):
    global state, music, sounds
    if all.collidepoint(pos) or any.collidepoint(pos):
        print('Start')
        sounds.click.play()
        state = 1
        print('start state', state)

    elif above.collidepoint(pos):
        state = 9
        sounds.click.play()
        print('above')

    elif below.collidepoint(pos):
        state = 10
        sounds.click.play()
        print('below')

    if state == 1:
        if mercurybig.collidepoint(pos):
            state = 2
            sounds.click.play()

        if venusbig.collidepoint(pos):
            state = 3
            sounds.click.play()

        if marsbig.collidepoint(pos):
            state = 4
            sounds.click.play()

        if jupiterbig.collidepoint(pos):
            state = 5
            sounds.click.play()

        if saturnbig.collidepoint(pos):
            state = 6
            sounds.click.play()

        if uranusbig.collidepoint(pos):
            state = 7
            sounds.click.play()

        if neptunebig.collidepoint(pos):
            state = 8
            sounds.click.play()

    elif state == 9:
        if mercurybig.collidepoint(pos):
            state = 2
            sounds.click.play()

        if venusbig.collidepoint(pos):
            state = 3
            sounds.click.play()

        if marsbig.collidepoint(pos):
            state = 4
            sounds.click.play()

    elif state == 10:
        if jupiterbig.collidepoint(pos):
            state = 5
            sounds.click.play()

        if saturnbig.collidepoint(pos):
            state = 6
            sounds.click.play()

        if uranusbig.collidepoint(pos):
            state = 7
            sounds.click.play()

        if neptunebig.collidepoint(pos):
            state = 8
            sounds.click.play()


def on_key_down(key):
    global keys, state
    if key == keys.ESCAPE:
        sounds.key.play()
        state = 0
        print('escape')
        print('Esc state', state)


pgzrun.go()
