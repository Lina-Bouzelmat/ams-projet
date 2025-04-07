#!/bin/bash

DB_PATH="/home/uapv2202351/data/systeme_monitor.db"
OUTPUT_DIR="/home/uapv2202351/scripts"
TMP_FILE="/tmp/metrics.tsv"

# Extraction des données CPU et RAM
sqlite3 -separator $'\t' "$DB_PATH" "SELECT timestamps, cpu_usage, ram_usage FROM system_metrics ORDER BY id ASC;" > "$TMP_FILE"

# Générer le graphique avec Gnuplot
gnuplot "$OUTPUT_DIR/generate_metrics.gnuplot"

echo "Graphiques générés dans $OUTPUT_DIR"
