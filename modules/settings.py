import math
width, height = 800, 600
#game environment settings
sky_color = (135, 206, 235)
floor_color = (110, 110, 110)
wall_color = (200, 0, 0)

#player variables
player_x, player_y = width // 2, height // 2
player_angle = 0
player_speed = 1
player_turn_speed = 0.5

# Ayarlar
FOV = math.pi / 3  # 60 Derece görüş açısı
HALF_FOV = FOV / 2
NUM_RAYS = 120      # Performans için şimdilik düşük tutalım (Ekran genişliği kadar olabilir)
MAX_DEPTH = 800     # Işın ne kadar uzağa gidebilir?
DELTA_ANGLE = FOV / NUM_RAYS # Işınlar arası açı farkı
TILE_SIZE = 50  # Her bir duvar bloğu 50x50 piksel
MAP_SIZE = 10   # 10x10 bir harita alanı