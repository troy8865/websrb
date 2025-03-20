import requests
import re

# Yoda.az saytına daxil olmaq üçün lazım olan məlumatlar
YODA_URL = "https://yoda.az"
API_URL = "https://str.yodacdn.net"
ENDPOINT = "/atv/tracks-v1a1/mono.m3u8"

# User-Agent təyin edirik (brauzer kimi görünmək üçün)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def get_token():
    # Yoda.az saytına daxil oluruq
    response = requests.get(YODA_URL, headers=HEADERS)
    if response.status_code != 200:
        raise Exception("Yoda.az saytına daxil olmaq mümkün olmadı.")

    # Saytın məzmununda tokeni axtarırıq
    token_pattern = re.compile(r"token=([a-f0-9-]+)")
    match = token_pattern.search(response.text)
    if not match:
        raise Exception("Token tapılmadı.")

    token = match.group(1)
    print(f"Tapılan token: {token}")
    return token

def download_m3u8_file(token, save_path):
    # Tam .m3u8 URL-ni yaradırıq
    m3u8_url = f"{API_URL}{ENDPOINT}?token={token}"
    print(f"Yaradılan .m3u8 URL: {m3u8_url}")

    # .m3u8 faylını yükləyirik
    response = requests.get(m3u8_url, headers=HEADERS)
    if response.status_code != 200:
        raise Exception("Fayl yüklənə bilmədi.")

    # Faylı qovluğa yazırıq
    with open(save_path, "wb") as file:
        file.write(response.content)
    print(f"Fayl uğurla yükləndi və {save_path} qovluğuna yazıldı.")

if __name__ == "__main__":
    # Faylın saxlanacağı yol
    save_path = "output.m3u8"

    try:
        # Tokeni əldə edirik
        token = get_token()

        # .m3u8 faylını yükləyirik
        download_m3u8_file(token, save_path)
    except Exception as e:
        print(f"Xəta baş verdi: {e}")
