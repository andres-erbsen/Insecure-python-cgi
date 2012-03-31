#!/usr/bin/env python3
print("Content-type: text/html\n")

print("""
<title>Unustasin parooli</title>

<form action="/cgi/forgot.py" method="post">
<input type="submit" value="Unustasin parooli!" />
</form>
""")


import random
import os
random.seed(os.urandom(100)) # millest alustada

print('Uus parool: ', random.randint(0,9999999999999))

