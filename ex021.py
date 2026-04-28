#Faça um programa em python que abra e reproduza um o aúdio de um arquivo mp3
import pygame

pygame.mixer.init() #inicia o mixer
pygame.mixer.music.load('ex021.mp3') #carrega o arquivo
pygame.mixer.music.play()#Toca o arquivo

input("Pressione Enter para parar a música...")