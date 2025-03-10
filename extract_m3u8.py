import os
import requests
from bs4 import BeautifulSoup

# Hedef site URL'si
url = "https://alpha.cf-worker-bd33badc81b29df7.workers.dev/live/selcukbeinsports2/playlist.m3u8"

# Klasör ve dosya adı
output_folder = "yayin_linkleri"
output_file = os.path.join(output_folder, "yayin_listesi.m3u8")

# Klasörü oluştur
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Siteye istek gönder
response = requests.get(url)
if response.status_code != 200:
    print(f"Siteye erişilemedi. Hata kodu: {response.status_code}")
    exit()

# Eğer yanıt doğrudan bir .m3u8 dosyası ise, dosyaya kaydet
if url.endswith('.m3u8'):
    with open(output_file, 'w') as f:
        f.write(response.text)
    print(f".m3u8 dosyası '{output_file}' olarak kaydedildi.")
else:
    # HTML içeriğini parse et
    soup = BeautifulSoup(response.content, 'html.parser')

    # Yayın linklerini yakala (örnek olarak 'a' tag'leri içindeki linkler)
    links = []
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if href.endswith('.m3u8'):  # Sadece .m3u8 linklerini al
            links.append(href)

    # Linkleri dosyaya yaz
    with open(output_file, 'w') as f:
        for link in links:
            f.write(link + '\n')

    print(f"{len(links)} adet yayın linki bulundu ve '{output_file}' dosyasına kaydedildi.")
