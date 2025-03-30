import pygame
import sys
import time
from pygame import mixer
from camera_manager import CameraManager
from dotenv import load_dotenv
import os

load_dotenv()
pygame.init()
mixer.init()

# Screen settings
SCREEN_WIDTH = int(os.getenv('SCREEN_WIDTH'))
SCREEN_HEIGHT = int(os.getenv('SCREEN_HEIGHT'))
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_BLUE = (173, 216, 230)
NAVY_BLUE = (20, 20, 40)

# Gesture settings
PINCH_DISTANCE = 50
PINCH_HOLD_TIME = 0.2

# Calculator settings
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

button_size = 100
button_margin = 20
start_x = (SCREEN_WIDTH - (button_size * 4 + button_margin * 3)) // 2
start_y = (SCREEN_HEIGHT - (button_size * 4 + button_margin * 3)) // 2

def draw_button(screen, text, x, y, width, height, color=NAVY_BLUE):
    pygame.draw.rect(screen, color, (x, y, width, height), border_radius=15)
    pygame.draw.rect(screen, LIGHT_BLUE, (x, y, width, height), 5, border_radius=15)
    font = pygame.font.Font(None, 48)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)

def get_button_under_finger(index_pos):
    for i, row in enumerate(buttons):
        for j, label in enumerate(row):
            x = start_x + j * (button_size + button_margin)
            y = start_y + i * (button_size + button_margin)
            button_rect = pygame.Rect(x, y, button_size, button_size)
            if button_rect.collidepoint(index_pos):
                return label
    return None

def run(screen, camera_manager):
    running = True
    equation = ""
    last_selected = None
    pinch_start_time = None

    while running:
        if not camera_manager.update():
            continue

        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                camera_manager.release()
                sys.exit()

        transformed_landmarks = camera_manager.get_transformed_landmarks()
        index_pos = None

        if transformed_landmarks:
            for hand_landmarks in transformed_landmarks:
                index_pos = (int(hand_landmarks[8][0]), int(hand_landmarks[8][1]))

                pygame.draw.circle(screen, LIGHT_BLUE, index_pos, 10)

                selected_button = get_button_under_finger(index_pos)

                if selected_button:
                    pygame.draw.rect(screen, LIGHT_BLUE,
                                     (start_x + (buttons[0].index(selected_button) * (button_size + button_margin)),
                                      start_y + (buttons.index([row for row in buttons if selected_button in row][0]) * (button_size + button_margin)),
                                      button_size, button_size), 5, border_radius=15)

                    if last_selected != selected_button:
                        pinch_start_time = time.time()
                        last_selected = selected_button

                    if pinch_start_time and (time.time() - pinch_start_time) > PINCH_HOLD_TIME:
                        if selected_button == "C":
                            equation = ""
                        elif selected_button == "=":
                            try:
                                equation = str(eval(equation))
                            except:
                                equation = "Error"
                        else:
                            equation += selected_button
                        last_selected = None
                        pinch_start_time = None

        # Draw buttons
        for i, row in enumerate(buttons):
            for j, label in enumerate(row):
                x = start_x + j * (button_size + button_margin)
                y = start_y + i * (button_size + button_margin)
                draw_button(screen, label, x, y, button_size, button_size)

        # Display equation
        font = pygame.font.Font(None, 64)
        text_surface = font.render(equation, True, WHITE)
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, 100))
        screen.blit(text_surface, text_rect)

        pygame.display.flip()
        pygame.time.delay(1)
