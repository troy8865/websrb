import json
import subprocess

url = "https://www.showtv.com.tr/canli-yayin"
cmd = ["yt-dlp", "-g", url]

try:
    result = subprocess.check_output(cmd).decode().strip()
    with open("link.json", "w") as f:
        json.dump({"showtv": result}, f)
    print("✅ Link yeniləndi:", result)
except Exception as e:
    print("❌ Xəta baş verdi:", e)
