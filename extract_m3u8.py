import requests
import os

# M3U faylının URL-i
url = "https://mehmetaslan.serv00.net/play.php?v=https://shouurvki7jtfax.ngolpdkyoctjcddxshli469r.org/sunshine/2Rempjobcn4_cm45eOz1ald9RppQZGfkz6QAceLgsVxaucpQeIQp24ZTotAwGL-t3EqwR2MOEX_q0wBCQ72PFkU1up0Kb86V2T3LBete7VQM4KeBvWqwTm0BUMA3eVfOc8dRsH2m0y8Tlleg-MgyqQpgSYnkevUNAruYJ4vKHOak4vPusuF6vBEdLYH9xy9LT-t7is5XD-Xvw1R7AoQICdg0sFPsRJ45dX6S7CXrBag/hls/index.m3u8"

# Faylın yadda saxlanacağı qovluq
output_folder = "kanallar"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# M3U faylını yüklə
response = requests.get(url)
if response.status_code == 200:
    m3u_content = response.text
else:
    print(f"Xəta: {response.status_code}")
    exit()

# M3U faylını oxu və kanalları ayrı fayllar kimi yaz
channel_lines = m3u_content.splitlines()
channel_info = {}

for line in channel_lines:
    if line.startswith("#EXTINF:"):
        # Kanal adını çıxar (fayl adı üçün istifadə olunacaq)
        channel_name = line.split(",")[-1].strip()
        # Fayl adında qadağan olunan simvolları təmizlə
        channel_name = channel_name.replace("/", "_").replace("\\", "_").replace(":", "_")
        channel_info["name"] = channel_name
    elif line.startswith("http"):
        # Kanal URL-ni çıxar (heç bir dəyişiklik olmadan)
        channel_info["url"] = line.strip()
        
        # Fayl adını təyin et
        file_name = f"{channel_info['name']}.m3u8"
        file_path = os.path.join(output_folder, file_name)
        
        # Fayl yarad və yaz
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                # M3U8 başlıqlarını əlavə et
                f.write("#EXTM3U\n")
                f.write("#EXT-X-VERSION:3\n")
                f.write("#EXT-X-TARGETDURATION:10\n")
                f.write("#EXT-X-MEDIA-SEQUENCE:0\n")
                # Kanal məlumatını əlavə et (kanal adı olmadan)
                f.write("#EXTINF:10.0,\n")  # Kanal adı silinib
                f.write(f"{channel_info['url']}\n")
            print(f"{channel_info['name']} kanalı fayla yazıldı: {file_path}")
        except Exception as e:
            print(f"Xəta: {channel_info['name']} kanalı fayla yazıla bilmədi: {e}")
else:
    print("Bütün kanallar uğurla yazıldı.")
