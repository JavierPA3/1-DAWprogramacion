import re
ile = '<title>holaaa</title>'

match = re.search('<title>(.*?)</title>', ile)
print(match)