import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# Inisialisasi textured globe
def load_texture():
    textureSurface = pygame.image.load('Equirectangular_projection_SW.jpg')
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()

    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 
                 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)
    
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    
    return texture

# Membuat bola
def draw_sphere(radius, texture):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture)
    
    # Sphere dengan resolusi tinggi
    quadric = gluNewQuadric()
    gluQuadricTexture(quadric, GL_TRUE)
    gluSphere(quadric, radius, 100, 100)
    
    glDisable(GL_TEXTURE_2D)

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    # Konfigurasi OpenGL
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glTranslatef(0.0, 0.0, -5)
    
    # Load texture
    texture = load_texture()
    
    # Variabel rotasi
    rotation_x = 0
    rotation_y = 0
    
    clock = pygame.time.Clock()
    
    # Loop utama
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            # Kontrol rotasi dengan keyboard
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    rotation_y -= 5
                if event.key == pygame.K_RIGHT:
                    rotation_y += 5
                if event.key == pygame.K_UP:
                    rotation_x -= 5
                if event.key == pygame.K_DOWN:
                    rotation_x += 5
        
        # Bersihkan layar
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Reset matrix
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5)
        
        # Rotasi bola
        glRotatef(rotation_x, 1, 0, 0)
        glRotatef(rotation_y, 0, 1, 0)
        
        # Gambar bola
        draw_sphere(1.0, texture)
        
        # Update layar
        pygame.display.flip()
        clock.tick(60)

# Jalankan program
if __name__ == "__main__":
    main()