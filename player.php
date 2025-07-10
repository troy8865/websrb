<?php
$json = file_get_contents("link.json");
$data = json_decode($json, true);
$m3u8 = $data["showtv"] ?? "";
?>
<!DOCTYPE html>
<html>
<head>
    <title>Show TV Canlı Yayım</title>
    <script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>
</head>
<body>
    <h2>Show TV - Canlı Yayım</h2>
    <video id="video" controls autoplay style="width:100%; max-width:800px;"></video>
    <script>
        var video = document.getElementById('video');
        var videoSrc = "<?= $m3u8 ?>";
        if (Hls.isSupported()) {
            var hls = new Hls();
            hls.loadSource(videoSrc);
            hls.attachMedia(video);
        } else if (video.canPlayType('application/vnd.apple.mpegurl')) {
            video.src = videoSrc;
        } else {
            alert("Bu brauzer .m3u8 formatını dəstəkləmir.");
        }
    </script>
</body>
</html>
