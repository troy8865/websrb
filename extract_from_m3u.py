import os
import requests
from slugify import slugify

# Qaynaq M3U linki
m3u_url = "https://sivrisinek.tufansiken.workers.dev/DeaTHLesS-Red-iptv.m3u"

# stream qovluğu
os.makedirs("stream", exist_ok=True)

# M3U faylını yüklə
response = requests.get(m3u_url)
content = response.text

lines = content.splitlines()
current_name = None

for line in lines:
    if line.startswith("#EXTINF"):
        # Kanal adını çıxarırıq
        if "," in line:
            current_name = line.split(",", 1)[-1].strip()
        else:
            current_name = "unknown"
    elif line.startswith("http"):
        if current_name:
            filename = f"stream/{slugify(current_name)}.m3u8"
            with open(filename, "w", encoding="utf-8") as f:
                f.write("#EXTM3U\n")
                f.write("#EXT-X-VERSION:3\n")
                f.write("#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5)\n")
                f.write(line.strip() + "\n")
