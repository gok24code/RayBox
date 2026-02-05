# 📦 RayBox (GreenDoom Engine)

RayBox, **Python** ve **Pygame** kullanılarak "safi kod" (from scratch) prensibiyle geliştirilmiş, **DDA (Digital Differential Analyzer)** algoritmasını temel alan hafif bir 3D Raycasting oyun motorudur. PS1 dönemi oyunlarının estetiğini ve günümüz modern performans optimizasyonlarını birleştirir.

## 🚀 Öne Çıkan Özellikler

- **Gerçek Zamanlı DDA Algoritması:** Adım tabanlı ışın izleme yerine, ızgara kesişimlerini hesaplayan yüksek performanslı ve glitch-free motor yapısı.
- **İnteraktif Kurulum Scripti:** Sanal ortam (venv) desteği sunan, kullanıcı dostu Bash tabanlı kurulum otomasyonu.
- **Modüler Harita Sistemi:** Farklı harita dosyalarını dinamik olarak seçebilme ve `loaded_map.py` olarak derleme özelliği.

## 🛠️ Kurulum ve Başlatma

**Linux dağıtımlarında projeyi saniyeler içinde kurmak için interaktif scripti kullanabilirsiniz:**

```bash
chmod +x install.sh
./install.sh
```

_Kurulum sırasında sanal ortam (venv) oluşturup oluşturmamak tamamen sizin tercihinize bırakılmıştır._

## 🎮 Nasıl Oynanır?

- - _Harita Yükle_: **install.sh** zaten ilk haritayı seçmenizi sağlar. Daha sonra değiştirmek isterseniz **python map_loader.py** komutunu kullanın.

- - _Motoru Çalıştır_: Harita hazır olduğunda oyuna giriş yapın:

```bash
    python main.py
```

## 🕹️ Kontroller

- - **W / S**: İleri ve Geri hareket

- - **A / D**: Sola ve Sağa bakış (Dönüş)

- - **ESC**: Çıkış

## 🗺️ Proje Yapısı

```
RayBox/
├── main.py              # Ana oyun döngüsü ve 3D rendering
├── map_loader.py        # Harita seçim ve derleme scripti
├── install.sh           # İnteraktif kurulum otomasyonu
├── requirements.txt     # Gerekli kütüphaneler (Pygame, Pillow)
├── loaded_map.py        # Aktif harita matrisi (Otomatik üretilir)
└── modules/             # Modüller ve harita kütüphanesi
    ├── settings.py      # Çözünürlük, FOV ve hız ayarları
    ├── mapgen.py        # Resimden harita üreten araç
    └── test_map.py      # Örnek labirent tasarımı

```
