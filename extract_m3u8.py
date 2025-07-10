import requests
import re

def extract_nowtv_precise():
    url = "https://www.nowtv.com.tr/canli-yayin"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    text = r.text

    # Bu regex hostu və fayl adını dəqiq tapmağa çalışır
    pattern = r'https://nowtv-live-ad\.ercdn\.net/nowtv/nowtv_480p\.m3u8\?[^\'"\s]+'
    match = re.search(pattern, text)
    if match:
        return match.group(0)
    else:
        # Alternativ ümumi .m3u8 tap
        alt_pattern = r'https?://[^\s\'"]+\.m3u8[^\s\'"]*'
        alt_matches = re.findall(alt_pattern, text)
        if alt_matches:
            return alt_matches[0]
        else:
            return None

if __name__ == "__main__":
    link = extract_nowtv_precise()
    if link:
        print("Tapıldı:", link)
    else:
        print("Link tapılmadı.")
