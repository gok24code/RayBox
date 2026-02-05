import os
import importlib

def select_and_save_map():
    # modules klasöründeki dosyaları tara
    path = "modules"
    files = [f[:-3] for f in os.listdir(path) if f.endswith('.py') and f not in ['__init__.py', 'settings.py','mapgen.py','map_loader.py']]
    
    if not files:
        print("Harita bulunamadı!")
        return

    print("\n--- Mevcut Haritalar ---")
    for i, f in enumerate(files):
        print(f"{i}: {f}")
    
    try:
        secim = int(input("\nHarita No: "))
        harita_adi = files[secim]
        
        # Dinamik import
        modul = importlib.import_module(f"modules.{harita_adi}")
        
        # loaded_map.py dosyasını oluştur
        with open("loaded_map.py", "w", encoding="utf-8") as f:
            f.write(f"# '{harita_adi}' haritasından üretildi\n")
            f.write(f"MAP = {modul.MAP}\n")
            # İstersen buraya haritaya özel player_x, player_y de ekletebiliriz
            
        print(f"\n[OK] '{harita_adi}' artık 'loaded_map.py' olarak aktif!")
    except Exception as e:
        print(f"Hata: {e}")

if __name__ == "__main__":
    select_and_save_map()