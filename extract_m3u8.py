from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re
import os

# Chrome Headless mode
options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--user-agent=Mozilla/5.0 (Linux; Android 10) Mobile Safari/537.36")  # Mobil brauzer kimi

driver = webdriver.Chrome(options=options)

try:
    driver.get("https://www.nowtv.com.tr/canli-yayin")
    time.sleep(5)  # JavaScript-in tam yüklənməsi üçün gözlə

    page_source = driver.page_source

    # Axtarış: yalnız ercdn linkləri (çünki daioncdn deyil!)
    match = re.search(r'https://nowtv-live-ad\.ercdn\.net/nowtv/nowtv_480p\.m3u8\?[^\'"\\\s]+', page_source)
    if match:
        link = match.group(0)
        print("✅ Tapıldı:", link)

        # Multi-variant formatında stream faylı yaradılır
        os.makedirs("stream", exist_ok=True)
        with open("stream/nowtv.m3u8", "w") as f:
            f.write("#EXTM3U\n")
            f.write("#EXT-X-VERSION:3\n")
            f.write("#EXT-X-STREAM-INF:BANDWIDTH=800000,RESOLUTION=854x480\n")
            f.write(link + "\n")
        print("✅ Fayl yaradıldı: stream/nowtv.m3u8")

    else:
        print("❌ ercdn link tapılmadı.")

finally:
    driver.quit()
