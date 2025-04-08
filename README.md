# Interface Web – Projet AMS

L'interface permet de consulter graphiquement l'évolution de l'utilisation CPU et RAM, les dernières données enregistrées dans la base 'systeme_monitor.db'.

## Fonctionnalités

- Affichage web simple à l'aide de 'netcat'
- Affichage du graphique 'evolution_graph.png' (CPU & RAM)
- Affichage des 5 dernières mesures du système

## Prérequis

- 'netcat' installé  
- 'sqlite3'
- Avoir généré le graphique via le script `generate_graph.sh` (présent dans le dossier scripts)


## Lancement de l'interface

En bash
cd /home/uapv2202351/scripts
chmod +x /home/uapv2202351/scripts/web_interface.sh
bash /home/uapv2202351/scripts/web_interface.sh

le résultat est http://localhost:8080