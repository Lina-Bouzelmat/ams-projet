#!/bin/bash

# Récupérer les dernières données CPU et RAM
cpu_ram_data=$(sqlite3 /home/machine2/data/systeme_monitor.db "SELECT cpu_usage, ram_usage FROM system_metrics ORDER BY timestamp DESC LIMIT 1;")

# Envoyer ces données à la machine principale via SSH
ssh uapv2202351@10.0.2.15 "echo '$cpu_ram_data' >> /home/uapv2202351/scripts/data_from_machine2.txt"
