import requests
import re

def extract_nowtv_m3u8():
    url = "https://www.nowtv.com.tr/canli-yayin"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    text = r.text

    # İstədiyin hostla uyğun linki tapmaq üçün regex:
    pattern = r'https://nowtv-live-ad\.ercdn\.net/nowtv/nowtv_480p\.m3u8\?[^\'"\s]+'
    match = re.search(pattern, text)
    if match:
        return match.group(0)
    else:
        print("İstədiyin nowtv linki tapılmadı.")
        return None

if __name__ == "__main__":
    link = extract_nowtv_m3u8()
    if link:
        print("Tapıldı:", link)
