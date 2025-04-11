#!/bin/bash

URL="https://www.cert.ssi.gouv.fr/"
ALERT=$(curl -s "$URL" | grep -m 1 '<article' | sed 's/>[^>]*>//g' | head -n 1)
if [ -n "$ALERT" ]; then
	echo "$ALERT" > /home/uapv2202351/data/last_alert.txt

	echo "Alerte extraite : $ALERT"
else
	echo "Acucune alerte trouvée"
fi
