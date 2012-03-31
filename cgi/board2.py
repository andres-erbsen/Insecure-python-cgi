#!/usr/bin/env python3
print("Content-type: text/html\n")

print("""

<title>Textboard</title>

<form action="/cgi/board2.py" method="post">
<textarea name="postita" cols="80" rows="5">
Type your text here...
</textarea>

<input type="submit" value="postita" />
</form>

""")

import cgi
form = cgi.FieldStorage() 

if form.getvalue('postita'): # kui on olemas
    pf = open("posts.txt",'a')
    pf.write(form.getvalue('postita') + '\n') # br on htmlis uus rida
    pf.close()
    print("Postitus salvestatud. <br>")


pf = open("posts.txt",'r')
for line in pf:
    print(cgi.escape(line)+"<br>")
