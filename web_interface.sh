#!/bin/bash

PORT=8080
IMG_PATH="/home/uapv2202351/scripts/evolution_graph.png"
TMP_DATA="/tmp/web_data.txt"

generate_webpage() {
    echo -e "HTTP/1.1 200 OK"
    echo -e "Content-Type: text/html\n"
    echo "<html><head><title>Dashboard AMS</title></head><body>"
    echo "<h1>Interface AMS</h1>"
    echo "<h2>Graphique d'évolution CPU & RAM</h2>"
    echo "<img src='data:image/png;base64,$(base64 -w 0 $IMG_PATH)' alt='Graphique CPU/RAM' width='800'>"
    echo "<hr>"
    echo "<h3>Dernières valeurs</h3>"
    
    sqlite3 /home/uapv2202351/data/systeme_monitor.db "SELECT * FROM system_metrics ORDER BY id DESC LIMIT 5;" > $TMP_DATA

    echo "<pre>"
    cat $TMP_DATA
    echo "</pre>"

    echo "</body></html>"
}

while true; do
    { generate_webpage; } | nc -l -p $PORT -q 1
done
