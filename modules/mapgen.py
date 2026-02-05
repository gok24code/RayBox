import os
from PIL import Image

def create_map_file():
    # Kullanıcıdan girişleri al
    image_path = input("Harita yapılacak resmin yolunu gir (örn: map.png): ")
    output_name = input("Oluşturulacak dosyanın ismini gir (örn: examplemap): ")
    
    if not output_name.endswith(".py"):
        output_name += ".py"

    try:
        # Resmi aç ve siyah-beyaza çevir (0=Siyah/Duvar, 1=Beyaz/Yol)
        img = Image.open(image_path).convert('1')
        width, height = img.size
        pixels = img.load()

        # Matrisi oluştur
        map_matrix = []
        for y in range(height):
            row = []
            for x in range(width):
                # Pillow '1' modunda 0 siyah, 1 beyazdır. 
                # Biz siyahı duvar (1), beyazı boşluk (0) yapıyoruz.
                val = 1 if pixels[x, y] == 0 else 0
                row.append(val)
            map_matrix.append(row)

        # Dosyaya yazma işlemi
        with open(output_name, "w") as f:
            f.write("# Otomatik olusturulmus harita dosyasi\n")
            f.write(f"# Kaynak: {image_path}\n\n")
            f.write("MAP = [\n")
            for row in map_matrix:
                f.write(f"    {row},\n")
            f.write("]\n")

        print(f"\n[Basarili] '{output_name}' dosyasi {width}x{height} boyutlarinda olusturuldu.")
        
    except Exception as e:
        print(f"\n[Hata] Bir sorun olustu: {e}")

if __name__ == "__main__":
    create_map_file()