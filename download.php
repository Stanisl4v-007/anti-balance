<?php

if (!isset($_GET['file']) || $_GET['file'] === '') {
    http_response_code(400);
    exit("Файл не указан");
}

$requested = basename($_GET['file']);

$filesDir = __DIR__ . '/files/';
$fullPath = $filesDir . $requested;

if (!file_exists($fullPath)) {
    http_response_code(404);
    exit("Файл не найден");
}

$date = date("Y-m-d H:i:s");
$ip = $_SERVER['REMOTE_ADDR'] ?? 'unknown';

$line = $requested . ';' . $date . ';' . $ip . ";\n";

$logFile = __DIR__ . '/log.txt';
file_put_contents($logFile, $line, FILE_APPEND);

header("Location: files/" . rawurlencode($requested));
exit;
?>