#!/bin/bash
numberoflines=5
address="http://www.facebook.com/feeds/notifications.php?id=YOURNUMBER&viewer=YOURNUMBER&key=YOURKEY&format=rss20"
wget --user-agent="Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.55 Safari/533.4" -q $address -O - | grep title | sed 's/<title>//g' | sed 's/<\/title>//g' | sed "s/\&apos\;/'/g" | sed 's/\&quot\;/"/g' | sed -e 's/^[ \t]*//' | cut -c10- | sed "s/...$//" | tail -n +2 | head -n $numberoflines | fmt -w 40 -s
