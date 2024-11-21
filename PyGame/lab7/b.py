import pygame
import os


pygame.init()
pygame.mixer.init()

width, height = 600, 400  
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Музыкальный Плеер")

background_color = (30, 30, 30)
text_color = (255, 255, 255)
highlight_color = (100, 100, 255)

font = pygame.font.SysFont("Arial", 24, bold=True)
title_font = pygame.font.SysFont("Arial", 32, bold=True)

music_folder = r"C:\Users\Baurzhan\Desktop\PyGame"  
supported_formats = (".mp3", ".wav", ".ogg") 

playlist = [f for f in os.listdir(music_folder) if f.endswith(supported_formats)]
playlist.sort() 
current_index = 0 

def load_song(index):
    song_path = os.path.join(music_folder, playlist[index])
    pygame.mixer.music.load(song_path)
    print(f"Загружена: {playlist[index]}")

def play_song():
    pygame.mixer.music.play()
    print("Воспроизведение...")

def stop_song():
    pygame.mixer.music.stop()
    print("Остановлено.")

def next_song():
    global current_index
    current_index = (current_index + 1) % len(playlist)
    load_song(current_index)
    play_song()

def previous_song():
    global current_index
    current_index = (current_index - 1) % len(playlist)
    load_song(current_index)
    play_song()


def draw_interface():
    window.fill(background_color)
    
    title_text = title_font.render("Музыкальный Плеер", True, highlight_color)
    window.blit(title_text, (width // 2 - title_text.get_width() // 2, 20))
    
    if playlist:
        song_text = font.render(f"Сейчас играет: {playlist[current_index]}", True, text_color)
    else:
        song_text = font.render("Песни не найдены в папке!", True, text_color)
    window.blit(song_text, (width // 2 - song_text.get_width() // 2, height // 2 - 20))
    
    instructions = [
        "Управление:",
        "P - Play / Pause",
        "S - Stop",
        "N - Next",
        "B - Previous",
        "Q - Quit"
    ]
    y_offset = height - 150
    for line in instructions:
        instruction_text = font.render(line, True, text_color)
        window.blit(instruction_text, (width // 2 - instruction_text.get_width() // 2, y_offset))
        y_offset += 30

    pygame.display.flip()

if playlist:
    load_song(current_index)
else:
    print("Песни не найдены в указанной папке!")

print("Управление: P = Play, S = Stop, N = Next, B = Previous, Q = Quit")

running = True
playing = False 

while running:
    draw_interface()  
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  
                if not playing:
                    play_song()
                    playing = True
                else:
                    pygame.mixer.music.pause()
                    playing = False
            elif event.key == pygame.K_s:  
                stop_song()
                playing = False
            elif event.key == pygame.K_n:  
                next_song()
                playing = True
            elif event.key == pygame.K_b: 
                previous_song()
                playing = True
            elif event.key == pygame.K_q:  
                running = False
                print("Выход из плеера...")


pygame.quit()
