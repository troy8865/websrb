<?php
$kanal = $_GET['kanal'] ?? 'kinomiks';

function getM3U8Link($kanal) {
    // Məsələn, bu URL-də canlı tokenli m3u8 var
    $source_url = "https://www.showtv.com.tr/canli-yayin/player.php?id=" . urlencode($kanal);

    // Qaynaq HTML-i al
    $html = file_get_contents($source_url);

    // M3U8 linki çıxar (regex ilə)
    if (preg_match('/(https?:\/\/[^\s\'"]+\.m3u8[^\'"\s]*)/', $html, $matches)) {
        return $matches[1]; // Tapılan link
    }

    return false;
}

$link = getM3U8Link($kanal);

if ($link) {
    // Əgər link tapıldısa yönləndir
    header("Location: $link");
    exit;
} else {
    echo "Link tapılmadı";
}
