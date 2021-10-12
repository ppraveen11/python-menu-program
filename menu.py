import os
import subprocess as sp

print("""\n
        press:1 About me
        press:2 for to know date
        press:3 for to show the calendar
        press:4 for to open browser
        press:5 for to know in which  folder your in 
        press:6 for to configure httpd web server
        """)

choice = int(input("enter your choice: "))


if choice == 1 :
    os.system("espeak-ng 'hello  this is parthanaboina praveen'")
elif choice == 2 :
    os.system("espeak-ng 'today date is' -s 100 -p 50")
    os.system("date | espeak-ng -s 100 -p 50")
    os.system("date")
elif choice == 3 :
    os.system("zenity --calendar")
elif choice == 4 :
    os.system("espeak-ng 'opening firefox'")
    os.system("firefox")
elif choice == 5:
    os.system("pwd | espeak-ng")
elif choice == 6 :
    os.system("espeak-ng 'httpd configration'")
  os.system("yum install httpd -y")
    os.system("systemctl start httpd")
    os.system("systemctl enable httpd")
    os.system("systemctl status httpd")
