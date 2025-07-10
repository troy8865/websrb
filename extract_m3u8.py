import subprocess
import json

url = "https://www.showtv.com.tr/canli-yayin"
cmd = ["yt-dlp", "-g", url]

try:
    m3u8_link = subprocess.check_output(cmd).decode().strip()
    with open("linkler.json", "w") as f:
        json.dump({"showtv": m3u8_link}, f)
    print("✅ Link saxlanıldı:", m3u8_link)
except Exception as e:
    print("❌ Xəta:", e)
