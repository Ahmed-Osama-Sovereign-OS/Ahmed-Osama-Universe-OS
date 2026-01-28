
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math, sys, time, subprocess

# ==========================================
# 1. نظام شفرة التفعيل السيادية (Security)
# ==========================================
def check_activation():
    SOVEREIGN_KEY = "AO-2026-UNIVERSE" 
    print("\n" + "="*40)
    print("   AHMED OSAMA UNIVERSE OS - SECURITY")
    print("="*40)
    user_input = input("أدخل شيفرة التفعيل للعبور إلى العالم الجديد: ")
    if user_input == SOVEREIGN_KEY:
        print("\n[✔] تم التحقق.. أهلاً بك أيها القائد أحمد أسامة.")
        return True
    else:
        print("\n[✘] شفرة خاطئة! لا يمكنك كسر نظام السيادة.")
        sys.exit()

# ==========================================
# 2. شاشة الترحيب الكونية (Splash Screen)
# ==========================================
def splash_screen():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720), pygame.NOFRAME)
    clock = pygame.time.Clock()
    try:
        logo = pygame.image.load("installer_logo.png")
        logo = pygame.transform.scale(logo, (450, 450))
    except:
        logo = pygame.Surface((400, 400), pygame.SRCALPHA)
        pygame.draw.circle(logo, (50, 0, 100), (200, 200), 180)

    start_time = pygame.time.get_ticks()
    angle = 0
    while pygame.time.get_ticks() - start_time < 6000:
        screen.fill((2, 0, 10))
        angle += 4
        rotated_logo = pygame.transform.rotate(logo, angle)
        scale = 1 + 0.05 * math.sin(pygame.time.get_ticks() * 0.005)
        new_size = (int(rotated_logo.get_size()[0] * scale), int(rotated_logo.get_size()[1] * scale))
        final_logo = pygame.transform.scale(rotated_logo, new_size)
        screen.blit(final_logo, final_logo.get_rect(center=(640, 360)))
        
        font = pygame.font.Font(None, 40)
        text = font.render("Initiating Predator Mode... Sovereign AI Online", True, (0, 255, 200))
        screen.blit(text, (380, 660))
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

# ==========================================
# 3. محرك النظام ومتجر الافتراس (Core & Store)
# ==========================================
class UniverseOS:
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((1280, 720), DOUBLEBUF | OPENGL)
        pygame.display.set_caption("AO Universe OS - Core")
        gluPerspective(45, (1280/720), 0.1, 500.0)
        glTranslatef(0, 0, -15)

    def predator_store(self):
        print("\n--- AO PREDATOR STORE ---")
        print("[1] Windows Emulator | [2] Android Bridge | [3] Apple Isolation")
        choice = input("اختر التطبيق المراد افتراسه: ")
        print(f"جاري دمج العنصر {choice} داخل السيادة...")
        time.sleep(2)
        print("تم الافتراس بنجاح!")

    def run(self):
        self.predator_store()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT: pygame.quit(); sys.exit()
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glRotatef(1, 1, 1, 0)
            glBegin(GL_LINES)
            for i in range(10):
                glColor3f(0.5, 0, 1)
                glVertex3f(math.cos(i), math.sin(i), 0)
                glVertex3f(0, 0, 0)
            glEnd()
            pygame.display.flip()
            pygame.time.wait(10)

if __name__ == "__main__":
    if check_activation():
        splash_screen()
        UniverseOS().run()
