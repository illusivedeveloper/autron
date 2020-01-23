#!/usr/bin/python3
import cgi

print("content-type: text/html")
print()
x= cgi.FieldStorage()
IP= x.getvalue('ip')
def connect():
    print("""
            <a href='http://{}:4200' target='myredhat'>Click here to show OS</a>
            <iframe width='100%' height='100%' name='myredhat' />
            """.format(IP))
