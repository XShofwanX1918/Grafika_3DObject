import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Fungsi load texture (sama seperti sebelumnya)
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

# Fungsi menggambar bola
def draw_sphere(radius, texture):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture)
    
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
    
    # Variabel rotasi otomatis
    rotation_x = 0
    rotation_y = 0
    
    # Kecepatan rotasi
    rotation_speed_x = 0.5  # Rotasi vertikal
    rotation_speed_y = 1.0  # Rotasi horizontal
    
    clock = pygame.time.Clock()
    
    # Mode rotasi
    rotation_modes = [
        "horizontal",  # Rotasi horizontal
        "vertical",    # Rotasi vertikal
        "diagonal"     # Rotasi diagonal
    ]
    current_mode = 0
    
    # Loop utama
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            # Ganti mode rotasi dengan spasi
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    current_mode = (current_mode + 1) % len(rotation_modes)
        
        # Bersihkan layar
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Reset matrix
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5)
        
        # Rotasi otomatis berdasarkan mode
        if rotation_modes[current_mode] == "horizontal":
            rotation_y += rotation_speed_y
        elif rotation_modes[current_mode] == "vertical":
            rotation_x += rotation_speed_x
        else:  # diagonal
            rotation_x += rotation_speed_x
            rotation_y += rotation_speed_y
        
        # Terapkan rotasi
        glRotatef(rotation_x, 1, 0, 0)
        glRotatef(rotation_y, 0, 1, 0)
        
        # Gambar bola
        draw_sphere(1.0, texture)
        
        # Update layar
        pygame.display.flip()
        
        # Kontrol frame rate
        clock.tick(60)

# Jalankan program
if __name__ == "__main__":
    main()