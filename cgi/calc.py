#!/usr/bin/env python3
print("Content-type: text/html\n")

print("""

<title>Kalkulaator ;)</title>

<form action="/cgi/calc.py" method="post">
Tehe: <input type="text" name="tehe" />

<input type="submit" value="Arvuta!" />
</form>

""")

import cgi

form = cgi.FieldStorage()
tehe = form['tehe'].value

from math import * # et oleks, mida arvutada
print(tehe)
print('=')
print(eval(tehe))
