import pygame
import os

pygame.init()

screen_width = 400
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Music Player")


music_directory = "c:\\Users\\Gulnaz\\Desktop\\папа музыка"
music_files = [file for file in os.listdir(music_directory) if file.endswith(".mp3")]
current_track = 0

pygame.mixer.init()
pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track]))
pygame.mixer.music.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Press 'p' to play/pause
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_s:  # Press 's' to stop
                pygame.mixer.music.stop()
            elif event.key == pygame.K_n:  # Press 'n' for next track
                current_track = (current_track + 1) % len(music_files)
                pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track]))
                pygame.mixer.music.play()
            elif event.key == pygame.K_b:  # Press 'b' for previous track
                current_track = (current_track - 1) % len(music_files)
                pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track]))
                pygame.mixer.music.play()

    pygame.display.flip()

pygame.quit() 