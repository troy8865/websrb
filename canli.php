<?php
$json = file_get_contents("link.json");
$data = json_decode($json, true);

if (isset($data["showtv"])) {
    $link = $data["showtv"];
    header("Location: $link");
    exit;
} else {
    echo "⚠️ Link tapılmadı.";
}
