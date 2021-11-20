import os
import subprocess as sp

print("""\n
        press:1 About me
        press:2 for to know date
        press:3 for to show the calendar
        press:4 for to open browser
        press:5 for to know in which  folder your in 
        press:6 for to configure httpd web server
        press:7 to install docker and docker menu
        """)

choice = int(input("enter your choice: "))


if choice == 1 :
    os.system("espeak-ng 'hello  everyone'")
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
elif choice == 7 :
       import subprocess
       import os
       import time
       login = input("Login remotely or Localy (r/l) : ")
       if  "l" in login or  "L" in login:
         # DOCKER
         # Docker Configure in yum
         print(subprocess.getoutput("touch yum.repo"))
         docker_repo = open('/etc/yum.repos.d/yum.repo','w')
         docker_conf = """[Docker]
         name=Yum form Docker
         baseurl=https://download.docker.com/linux/centos/7/x86_64/stable/
         gpgcheck=0"""
         docker_repo.writelines(docker_conf)
         docker_repo.close()
         check = subprocess.getoutput("docker --version")
         # Installing Docker
       if "Docker" not in check and " version" not in check and "build" not in check:
          os.system("dnf install docker-ce --nobest -y")
       else:
         print("Docker Already exists")
         print()
           # Docker Menu
         print()
         print("   Welcome To a Docker Menu")
         print("      Docker Successfully Configured and Installed...")
         print()
         print("=============================================================")

         while True:
          print()
          print("1. Start Docker")
          print("2. Stop Docker")
          print("3. Status of Docker")
          print("4. Remove Docker from this System")
          print("5. Exit")
          # Select Option
          choice = input("Enter your option (1/2/3/4/5) : ") or "5"


          os.system("clear")
          # Start Docker 
          if choice in "1":
           print()
           print("   Docker Started..")
           print("=======================================================")
           print()
           while True:
            # Menu Docker tasts
            print(subprocess.getoutput("systemctl start docker"))
            print("Docker Menu")
            print("1. Pull new Images.")
            print("2. Display all Images.")
            print("3. Launch New Container.")
            print("4. Display List of Containers")
            print("5. Start Container")
            print("6. Stop Container")
            print("7. Remove Image")
            print("8. Remove Container")
            print("9. Display Running Instances")
            print("10. Remove All Container")
            print("11. Containers Menu")
            print("12. Exit")
           dchoice = input("Enter your choice : ")
            os.system("clear")
            print()
            print()
            # 1) Pull New Images from docker hub
            if dchoice in "1":
             print("Pull new Image from Docker hub")
             print()
             imageName = input("Enter Image Name : ") or "centos"
             imageV = ( ":"+input("Enter Version orelse takes default latest version : ")) or ""
             os.system("docker pull {}{}".format(imageName,imageV))
        # 2) Show  Images
            if dchoice in "2":
             print("Docker Images present in ur system")
             print()
             print(subprocess.getoutput("docker images"))
        # 3) Launch new Container
            if dchoice in "3":
             print("Create New Container")
             print()
             try:
              ImageName = input("Enter Image Name orelse takes default takes centOS: ") or "centos"
              ConName = "--name "+input("Enter Container Name(optional) : ") or ""
              os.system("docker run -it {} {} /bin/bash ".format(ConName,ImageName))
              print("Container Launched...")
        except Exception as a:
              print("Error: "+e+" occured!")
            # 4) Display list of Containers
            if dchoice in "4":
             print("List of containers available")
             print()
             print(subprocess.getoutput("docker ps -a "))
        # 5) Start Container
            if "5"in dchoice:
             os.system("docker ps -a")
             ConName = input("Enter Container Name or ID from above list : " ) or ""
             os.system("docker start {}".format(ConName))
             os.system("docker attach {}".format(ConName))
        # 6) Stop Contaner
            if "6" in dchoice:
             print(subprocess.getoutput("docker ps"))
             ConName = input("Enter Container Name or ID to stop from above list : " ) or ""
             print(subprocess.getoutput("docker stop {}".format(ConName)))
        # 7) Remove Image
            if "7" in dchoice:
             print(subprocess.getoutput("docker images"))
             ImageName = input("Enter Image Name to remove : ") or ""
             os.system("docker rmi {} -f".format(ImageName))
        # 8) Remove Container
            if dchoice in "8":
             print(subprocess.getoutput("docker ps -a "))
             ConName = input("Enter Container Name or ID from above list : " ) or ""
             os.system("docker rm {} -f".format(ConName))
        # 9) Display all Running Instances
            if dchoice in "9":
             print(subprocess.getoutput("docker ps"))
        # 10) Remove All Containers
            if "10" in dchoice:
             print(subprocess.getoutput("docker ps -a "))
             rm = input("Are you sure wants to remove all CONTAINERS (y/n) : ") or "n"
             if rm in "y":
              os.system("docker container rm  -f `docker container ls -a -q`")
            # 11) Menu conatainer
            if "11" in dchoice:
             try:
              print(subprocess.getoutput("systemctl start firewalld"))
              print(subprocess.getoutput("firewall-cmd --zone=public --add-masquerade --permanent"))
              print(subprocess.getoutput("firewall-cmd --zone=public --add-port=80/tcp"))
              print(subprocess.getoutput("firewall-cmd --zone=public --add-port=443/tcp"))
              print(subprocess.getoutput("firewall-cmd --reload"))
              print(subprocess.getoutput("systemctl restart docker"))
              print(subprocess.getoutput("docker ps -a "))
              ConName = input("Enter Container Name or ID from above list : " ) or ""
              print(subprocess.getoutput("docker start {} ".format(ConName)))
              print(subprocess.getoutput("docker exec {} date".format(ConName)))
              print(subprocess.getoutput("docker start {} ".format(ConName)))
              print("{} Container Started".format(ConName))
              print()
              while True:
               print("   Container Menu.")
               print("================================================================")
               print("1. Install httpd")
               print("2. Start httpd ")
               print("3. Install python")
               print("4. Create Html file ")
               print("5. Exit from container ")
               ch = input("Enter your option (1/2/3/4/5) : ")
               if ch in "1":
                print(subprocess.getoutput("docker exec {} yum install httpd -y".format(ConName)))
               if ch in "2":
                print(subprocess.getoutput("docker exec {} /usr/sbin/httpd".format(ConName)))
               if ch in "3":
                print(subprocess.getoutput("docker exec {} yum install python3 -y".format(ConName)))
               if ch in "4":
                print(subprocess.getoutput("docker exec {} touch hello.html".format(ConName)))

               if ch in "5":
                os.system("clear")
                break;
               time.sleep(2)
               os.system("clear")
             except Exception as e:
              print("Error: "+e+" occured!")
        # 12) Exit from docker menu
            if "12" in dchoice:
             os.system("clear")
             break
            time.sleep(3)
          if choice in "2":
           print("Docker is stopping...")
           print(subprocess.getoutput("systemctl stop docker"))
           print()
          if choice in "3":
           print(subprocess.getoutput("systemctl status docker"))
           print()
          if choice in "4":
           rm = input("Are you sure wants to remove Docker (y/n) : ") or "n"
           if rm in "y":
            os.system("yum remove docker-ce")
            print("Docker removed from your system")
           exit()
          if choice in "5":
           print("You choose 5 to quite")
           print("Exiting from menu..Thank you have nice day..")
           time.sleep(2)
           os.system("clear")
           exit()

        
