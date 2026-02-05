import pygame
import math
from modules.settings import *  # Ayarları içe aktar
# Eğer loaded_map.py henüz oluşmadıysa hata almamak için 
# önce loader'ı çalıştırman veya boş bir dosya oluşturman gerekir.
try:
    from loaded_map import MAP
except ImportError:
    print("Hata: Henüz bir harita yüklenmemiş. Lütfen once map_loader.py calistirin.")
    exit()

pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption("RayBox - Labirint")

def get_ray_distance(angle):
    # Işının yönü (vektör)
    ray_dir_x = math.cos(angle)
    ray_dir_y = math.sin(angle)

    # Oyuncunun haritadaki hangi karede olduğu
    map_x = int(player_x / TILE_SIZE)
    map_y = int(player_y / TILE_SIZE)

    # Her bir ızgara çizgisi arası mesafe (mutlak değer)
    # 0'a bölme hatasını engellemek için küçük bir epsilon ekliyoruz
    delta_dist_x = abs(1 / (ray_dir_x + 1e-10))
    delta_dist_y = abs(1 / (ray_dir_y + 1e-10))

    # İlk ızgara çizgisine olan mesafe ve adım yönü
    if ray_dir_x < 0:
        step_x = -1
        side_dist_x = (player_x / TILE_SIZE - map_x) * delta_dist_x
    else:
        step_x = 1
        side_dist_x = (map_x + 1.0 - player_x / TILE_SIZE) * delta_dist_x

    if ray_dir_y < 0:
        step_y = -1
        side_dist_y = (player_y / TILE_SIZE - map_y) * delta_dist_y
    else:
        step_y = 1
        side_dist_y = (map_y + 1.0 - player_y / TILE_SIZE) * delta_dist_y

    # Duvarı bulana kadar zıpla
    hit = False
    side = 0 # 0: X-tarafı, 1: Y-tarafı
    while not hit:
        if side_dist_x < side_dist_y:
            side_dist_x += delta_dist_x
            map_x += step_x
            side = 0
        else:
            side_dist_y += delta_dist_y
            map_y += step_y
            side = 1
        
        # --- GÜVENLİK KONTROLÜ BURAYA ---
        # Eğer ışın harita sınırlarının dışına çıktıysa döngüyü kır
        if 0 <= map_y < len(MAP) and 0 <= map_x < len(MAP[0]):
            if MAP[map_y][map_x] == 1:
                hit = True
        else:
            # Harita dışına çıktı, sonsuzluğa gitmemesi için durdur
            hit = True 
            distance = 1000 # Çok uzak bir mesafe ata ki ekranda boşluk görünsün

    # Duvara olan dikey mesafeyi hesapla (Balık gözü etkisini otomatik çözer)
    if side == 0:
        distance = (side_dist_x - delta_dist_x) * TILE_SIZE
    else:
        distance = (side_dist_y - delta_dist_y) * TILE_SIZE
    
    return distance, side
def draw_3d(player_x, player_y, player_angle):
    # Tavan ve Zemin
    pygame.draw.rect(screen, sky_color, (0, 0, width, height // 2)) 
    pygame.draw.rect(screen, floor_color, (0, height // 2, width, height // 2)) 
    
    start_angle = player_angle - HALF_FOV
    
    for i in range(NUM_RAYS):
        angle = start_angle + i * DELTA_ANGLE
        
        # Temiz veriyi DDA'dan alıyoruz
        distance, side = get_ray_distance(angle)

        # Balık gözü etkisini düzelt (DDA mesafesi üzerinden)
        distance *= math.cos(player_angle - angle)
        
        # Duvar yüksekliği hesapla
        # 1000 çarpanını ekran yüksekliğine göre ayarlayabilirsin
        proj_height = (TILE_SIZE * 600) / (distance + 0.0001)

        # Pürüzsüz dolgu için gölgelendirme
        color_value = 200 / (1 + distance * distance * 0.0001)

        # Yan duvar (side=1) ise pürüzlü kenar/derinlik hissi için karart
        if side == 1:
            color_value *= 0.7 

        final_color = (200, int(color_value), 0)
        
        # Çizim (COLUMN_WIDTH hesapla veya doğrudan genişliğe böl)
        col_width = width / NUM_RAYS
        pygame.draw.rect(screen, final_color, 
                        (i * col_width, (height - proj_height) // 2, 
                         col_width + 1, proj_height))

def move_player():
    global player_x, player_y, player_angle    
    # Dönüş Kontrolü
    if keys[pygame.K_a]: player_angle -= 0.05 * player_turn_speed
    if keys[pygame.K_d]: player_angle += 0.05 * player_turn_speed

    dx = math.cos(player_angle) * player_speed
    dy = math.sin(player_angle) * player_speed
    
    
    # İleri-Geri Kontrolü (Trigonometrik Hareket)
    if keys[pygame.K_w]:
        new_x = player_x + dx
        new_y = player_y + dy
        # Çarpışma Kontrolü
        if MAP[int(new_y / TILE_SIZE)][int(new_x / TILE_SIZE)] == 0:
            player_x = new_x
            player_y = new_y
        if MAP[int(player_y / TILE_SIZE)][int((player_x + dx) / TILE_SIZE)] == 0:
            player_x += dx
        if MAP[int((player_y + dy) / TILE_SIZE)][int(player_x / TILE_SIZE)] == 0:
            player_y += dy
    if keys[pygame.K_s]:
        new_x = player_x - dx
        new_y = player_y - dy
        # Çarpışma Kontrolü
        if MAP[int(new_y / TILE_SIZE)][int(new_x / TILE_SIZE)] == 0:
            player_x = new_x
            player_y = new_y
        
while True:
    keys = pygame.key.get_pressed()
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    move_player()
    # Player
    draw_3d(player_x, player_y, player_angle)

    pygame.display.flip()
    clock.tick(60) # 60 FPS sabitle