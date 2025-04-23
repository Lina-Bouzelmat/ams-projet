# Interface Web - Projet AMS

## Description


L'interface Web du projet AMS permet de consulter graphiquement l'évolution de l'utilisation du CPU et de la RAM sur une période donnée, ainsi que les dernières données collectées. Ces informations sont extraites d'une base de données SQLite nommée `systeme_monitor.db`. Le script de l'interface Web génère dynamiquement une page HTML avec le graphique d'évolution et les dernières mesures.

## Fonctionnalités


- **Affichage graphique dynamique** : Le graphique de l'évolution du CPU et de la RAM est généré en utilisant l'image `evolution_graph.png`.

- **Affichage des dernières mesures** : Les 5 dernières valeurs de l'utilisation du CPU et de la RAM sont extraites et affichées sur l'interface.

- **Interface Web simple** : L'interface est accessible via un navigateur à l'adresse `http://localhost:8080`.

- **Réactivité** : Chaque rechargement de la page affiche les données les plus récentes, générées par la base de données SQLite.

## Fonctionnement du script `web_interface.sh`


Le fichier `web_interface.sh` est un script Bash qui génère dynamiquement une page Web servant les informations CPU et RAM sur le port 8080. Voici une description détaillée de chaque composant du script.

### Variables définies dans le script


- `PORT=8080`: Le port sur lequel l'interface Web sera accessible via `netcat`.
- `IMG_PATH="/home/uapv2202351/scripts/evolution_graph.png"`: Le chemin vers l'image générée représentant l'évolution de l'utilisation du CPU et de la RAM.
- `TMP_DATA="/tmp/web_data.txt"`: Le fichier temporaire où les dernières mesures extraites de la base de données seront stockées.

### Fonction `generate_webpage`


Cette fonction génère la page HTML que l'utilisateur voit lorsqu'il accède à l'interface via son navigateur.

1. **En-têtes HTTP** :  
   La première ligne de la fonction définit le type de réponse HTTP comme étant un code de succès `200 OK` et spécifie que le type de contenu est du HTML :
   ```bash
   echo -e "HTTP/1.1 200 OK"
   echo -e "Content-Type: text/html\n"
