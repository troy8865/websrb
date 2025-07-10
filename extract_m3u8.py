import os
import shutil
import requests
import re

source_urls = {
    "nowtv": "https://www.nowtv.com.tr/canli-yayin",
}

stream_folder = "stream"
if os.path.exists(stream_folder):
    shutil.rmtree(stream_folder)
os.makedirs(stream_folder)

def extract_m3u8(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
    }
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    text = r.text

    pattern = r'https?://[^\s\'"]+\.m3u8[^\s\'"]*'
    matches = re.findall(pattern, text)
    if matches:
        return matches[0]
    else:
        return None

def write_multi_variant(file_path, m3u8_url):
    content = (
        "#EXTM3U\n"
        "#EXT-X-VERSION:3\n"
        "#EXT-X-INDEPENDENT-SEGMENTS\n"
        "#EXT-X-STREAM-INF:BANDWIDTH=1500000,RESOLUTION=1280x720\n"
        f"{m3u8_url}\n"
    )
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    for name, url in source_urls.items():
        m3u8 = extract_m3u8(url)
        if m3u8:
            print(f"Yeni çıxarılan link ({name}): {m3u8}")
            filepath = os.path.join(stream_folder, f"{name}.m3u8")
            write_multi_variant(filepath, m3u8)
        else:
            print(f"{name} üçün link tapılmadı.")
