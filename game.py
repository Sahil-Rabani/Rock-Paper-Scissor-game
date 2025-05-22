# -----------CodeSoft---------------------------------
# -----------Python Programming-----------------------
# -----------Task 4:- Rock-Paper-Scissors Game--------

import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock-Paper-Scissors")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)


font = pygame.font.SysFont(None, 36)

choices = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0
result_text = ""
user_choice = ""
computer_choice = ""

button_width = 150
button_height = 50
buttons = {
    "Rock": pygame.Rect(50, 300, button_width, button_height),
    "Paper": pygame.Rect(225, 300, button_width, button_height),
    "Scissors": pygame.Rect(400, 300, button_width, button_height)
}

def draw_text(text, x, y, color=BLACK):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

def get_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Scissors" and computer == "Paper") or \
         (user == "Paper" and computer == "Rock"):
        return "You win!"
    else:
        return "Computer wins!"

running = True
while running:
    screen.fill(WHITE)

    draw_text("Rock-Paper-Scissors", 180, 20)
    draw_text(f"Your Choice: {user_choice}", 50, 80)
    draw_text(f"Computer Choice: {computer_choice}", 50, 120)
    draw_text(f"Result: {result_text}", 50, 160)
    draw_text(f"Your Score: {user_score}  |  Computer Score: {computer_score}", 50, 200)

    for name, rect in buttons.items():
        pygame.draw.rect(screen, GRAY, rect)
        draw_text(name, rect.x + 30, rect.y + 10)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for name, rect in buttons.items():
                if rect.collidepoint(pos):
                    user_choice = name
                    computer_choice = random.choice(choices)
                    result_text = get_winner(user_choice, computer_choice)

                    if "You win" in result_text:
                        user_score += 1
                    elif "Computer wins" in result_text:
                        computer_score += 1

pygame.quit()
sys.exit()