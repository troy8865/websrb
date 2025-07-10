from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re
import os

# Chrome Headless rejimdə
options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.binary_location = "/usr/bin/google-chrome"  # GitHub Actions mühitində lazım olan yol

# Mobil brauzer kimi davranmaq üçün user-agent
options.add_argument(
    "--user-agent=Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Mobile Safari/537.36"
)

driver = webdriver.Chrome(options=options)

try:
    driver.get("https://www.nowtv.com.tr/canli-yayin")
    time.sleep(5)  # JS yüklənməsini gözlə

    page_source = driver.page_source

    # Yalnız istədiyin link formatını çıxar: ercdn.net və 480p
    match = re.search(r'https://nowtv-live-ad\.ercdn\.net/nowtv/nowtv_480p\.m3u8\?[^\'"\\\s]+', page_source)
    if match:
        link = match.group(0)
        print("✅ Tapıldı:", link)

        # Faylı yaradıb içini yaz
        os.makedirs("stream", exist_ok=True)
        with open("stream/nowtv.m3u8", "w") as f:
            f.write("#EXTM3U\n")
            f.write("#EXT-X-VERSION:3\n")
            f.write("#EXT-X-STREAM-INF:BANDWIDTH=800000,RESOLUTION=854x480\n")
            f.write(link + "\n")
        print("✅ Fayl yaradıldı: stream/nowtv.m3u8")
    else:
        print("❌ İstədiyin formatda link tapılmadı.")

finally:
    driver.quit()
