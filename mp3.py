import pygame
import tkinter as tk
from tkinter import filedialog

# Инициализируем pygame
pygame.init()

# Создаем окно
window = pygame.display.set_mode((1240, 720), pygame.RESIZABLE)

# Устанавливаем начальный статус плеера
STATUS_PLAYING = 'playing'
STATUS_PAUSED = 'paused'
STATUS_STOPPED = 'stopped'
player_status = STATUS_STOPPED

# Устанавливаем начальную громкость
pygame.mixer.music.set_volume(0.5)
current_volume = 0.5




# Функция для установки громкости
def set_volume(volume):
    global current_volume
    pygame.mixer.music.set_volume(volume)
    current_volume = volume

# Функция для изменения громкости
def change_volume(change):
    new_volume = current_volume + change
    if new_volume < 0:
        new_volume = 0
    elif new_volume > 1:
        new_volume = 1
    set_volume(new_volume)

# Функция для обновления названия окна с текущим статусом плеера
def update_title():
    if player_status == STATUS_PLAYING:
        pygame.display.set_caption(f'MP3 плеер - воспроизведение (Громкость: {current_volume*100}%)')
    elif player_status == STATUS_PAUSED:
        pygame.display.set_caption('MP3 плеер - пауза')
    else:
        pygame.display.set_caption('MP3 плеер')

# Функция для обработки событий плеера
def handle_events():
    global player_status
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Закрываем окно при нажатии на кнопку "Закрыть"
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Пауза / Воспроизведение при нажатии на клавишу "Пробел"
                if player_status == STATUS_PLAYING:
                    pygame.mixer.music.pause()
                    player_status = STATUS_PAUSED
                elif player_status == STATUS_PAUSED:
                    pygame.mixer.music.unpause()
                    player_status = STATUS_PLAYING

            if event.key == pygame.K_s:
                # Остановка воспроизведения при нажатии на клавишу "S"
                if player_status != STATUS_STOPPED:
                    pygame.mixer.music.stop()
                    player_status = STATUS_STOPPED

            if event.key == pygame.K_o:
                # Выбор файла для загрузки при нажатии на клавишу "O"
                root = tk.Tk()
                root.withdraw()
                file_path = filedialog.askopenfilename(title="Выберите MP3 файл", filetypes=[("MP3 files","*.mp3")])
                if file_path != "":
                    # Загружаем трек
                    pygame.mixer.music.load(file_path)
                    # Воспроизводим трек
                    pygame.mixer.music.play()
                    player_status = STATUS_PLAYING

            if event.key == pygame.K_UP:
                # Увеличение громкости при нажатии на клавишу "Вверх"
                change_volume(0.1)

            if event.key == pygame.K_DOWN:
                # Уменьшение громкости при нажатии на клавишу "Вниз"
                change_volume(-0.1)

# Основной цикл игры
while True:
    


    # Обрабатываем события плеера
    handle_events()

    # Обновляем название окна
    update_title()

    # Обновляем экран
    pygame.display.update()

    # Draw "HELLO WORLD" in the center of the screen
    font = pygame.font.SysFont("arial", 30)
    text3 = font.render("developer : rakuzan2weak#2522", True, (255, 255, 0))
    text_rect3 = text3.get_rect(center=(window.get_width()/2, window.get_height()/2.4))
    text = font.render("Инструкция: space - воспроизведение/пауза", True, (255, 255, 255))
    text_rect = text.get_rect(center=(window.get_width()/2, window.get_height()/2))
    text2 = font.render("o - выбрать mp3-файл | клавиши up, down - изменение громкости", True, (255, 255, 255))
    text_rect2 = text2.get_rect(center=(window.get_width()/2, window.get_height()/1.7))
    window.blit(text, text_rect)
    window.blit(text2, text_rect2)
    window.blit(text3, text_rect3)
