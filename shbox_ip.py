#!/usr/bin/python3

print("content-type: text/html")
print()

def connect():
    print("""<div align='center'>
        <form action='shbox.py'>
        Enter host IP<br>
        <input type='text' name='ip' /><br>
        <input type='submit' value='Connect' />
        </form>
        </div>""")
