#!/usr/bin/env python3
print("Content-type: text/html\n")

print("""
<title>Unixi-stiilis kalender</title>

<form action="/cgi/cal.py" method="post">
Aasta: <input type="text" name="aasta" />

<input type="submit" value="Kalender" />
</form>
<plaintext>
""")

import cgi
form = cgi.FieldStorage() 

if form.getvalue('aasta'): # kui on olemas
    aasta = form.getvalue('aasta')
else:
    aasta = ''

import os
os.system('cal ' +aasta+ ' > cal.txt')
f = open('cal.txt')
cal = f.read()
print(cal)

