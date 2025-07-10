<?php
$kanal = $_GET['id'] ?? null;
if (!$kanal) {
    die("❌ Kanal ID verilməyib.");
}

$links = json_decode(file_get_contents("linkler.json"), true);

if (isset($links[$kanal])) {
    header("Location: " . $links[$kanal]);
    exit;
} else {
    die("❌ Kanal tapılmadı.");
}
