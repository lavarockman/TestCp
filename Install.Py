import os

def AddUser(name):
    os.system("useradd " + name)
    os.system("mkhomedir_helper " + name)
    os.system('mkdir -p /home/' + name +'/Media | mkdir -p /home/' + name +'/Documents | mkdir -p /home/' + name +'/Desktop')
def Users():
    AddUser(Trevor)
    AddUser(Moist)
    AddUser(Lego)
    AddUser(Weeamoo)
    AddUser(Caine)
    AddUser(ToeKnee)
    AddUser(Programer)
    AddUser(Holden)
    AddUser(Howel)
def imdfes():
    os.system("touch /home/Caine/Desktop/Weeb.png")
    os.system("touch /home/Caine/Videos/.Hentai.mp4")
    os.system('echo Its an inside joke > /home/Howel/Desktop/WhitePriv.txt')
def Group(group,username):
    os.system('usermod -a -G',group,username)
def Gops():
    Group(adm,Holden)
    Group(adm,Trevor)
    Group(adm,Weeamoo)
def poorara():
    os.system('apt-get -y install hydra')
    os.system('apt-get -y install nmap')
def Main():
    Users()
    imdfes()
    Gops()
    poorara()


Main()
