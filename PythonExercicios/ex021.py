'''Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.'''

'''------------------------CODIGO DO GUANABARA NAO FUNCIONOU---------------------------------------'''

'''import pygame
pygame.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
pygame.event.wait()'''

'''------------------------CODIGO NOVO---------------------------------------'''
import pygame
pygame.mixer.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)