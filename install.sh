#!/bin/bash

# Renk tanımlamaları
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}>>> RayBox Kurulum Sihirbazı Başlıyor...${NC}"

# Sanal ortam sorusu
read -p "Python sanal ortamı (venv) oluşturulsun mu? (e/h): " venv_secim

if [[ "$venv_secim" == "e" || "$venv_secim" == "E" ]]; then
    if [ ! -d "venv" ]; then
        echo -e "${YELLOW}>>> Sanal ortam oluşturuluyor...${NC}"
        python -m venv venv
    fi
    source venv/bin/activate
    echo -e "${GREEN}>>> Sanal ortam aktif edildi.${NC}"
else
    echo -e "${YELLOW}>>> Sanal ortam atlanıyor, paketler global/user dizinine kurulacak.${NC}"
fi

# Kütüphaneleri kur
echo -e "${GREEN}>>> Gereksinimler yükleniyor (pip)...${NC}"
pip install -r requirements.txt

# Harita seçimini tetikle
echo -e "${GREEN}>>> Harita yapılandırması başlatılıyor...${NC}"
python map_loader.py

echo -e "${GREEN}>>> İşlem tamamlandı!${NC}"
echo -e "${YELLOW}Not: Eğer venv kullandıysan 'source venv/bin/activate' yapmayı unutma.${NC}"

rm -rf install.sh