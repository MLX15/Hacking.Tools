# coding=utf-8
import os

from core import HackingTool
from core import HackingToolsCollection


class Setoolkit(HackingTool):
    TITLE = "Setoolkit"
    DESCRIPTION = "The Social-Engineer Toolkit is an open-source penetration\n" \
                  "testing framework designed for social engineering"
    INSTALL_COMMANDS = [
        "git clone https://github.com/trustedsec/social-engineer-toolkit.git",
        "sudo python social-engineer-toolkit/setup.py"
    ]
    RUN_COMMANDS = ["sudo setoolkit"]
    PROJECT_URL = "https://github.com/trustedsec/social-engineer-toolkit"


class SocialFish(HackingTool):
    TITLE = "SocialFish"
    DESCRIPTION = "Automated Phishing Tool & Information Collector"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/UndeadSec/SocialFish.git && sudo apt-get install python3 python3-pip python3-dev -y",
        "cd SocialFish && sudo python3 -m pip install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd SocialFish && sudo python3 SocialFish.py root pass"]
    PROJECT_URL = "https://github.com/UndeadSec/SocialFish"


class HiddenEye(HackingTool):
    TITLE = "HiddenEye"
    DESCRIPTION = "Modern Phishing Tool With Advanced Functionality And " \
                  "Multiple Tunnelling Services \n" \
                  "\t [!]https://github.com/DarkSecDevelopers/HiddenEye"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/DarkSecDevelopers/HiddenEye.git ;sudo chmod 777 HiddenEye",
        "cd HiddenEye;sudo pip3 install -r requirements.txt;sudo pip3 install requests;pip3 install pyngrok"
    ]
    RUN_COMMANDS = ["cd HiddenEye;sudo python3 HiddenEye.py"]
    PROJECT_URL = "https://github.com/DarkSecDevelopers/HiddenEye"


class Evilginx2(HackingTool):
    TITLE = "Evilginx2"
    DESCRIPTION = "evilginx2 is a man-in-the-middle attack framework used " \
                  "for phishing login credentials along with session cookies,\n" \
                  "which in turn allows to bypass 2-factor authentication protection.\n\n\t " \
                  "[+]Make sure you have installed GO of version at least 1.14.0 \n" \
                  "[+]After installation, add this to your ~/.profile, assuming that you installed GO in /usr/local/go\n\t " \
                  "[+]export GOPATH=$HOME/go \n " \
                  "[+]export PATH=$PATH:/usr/local/go/bin:$GOPATH/bin \n" \
                  "[+]Then load it with source ~/.profiles."
    INSTALL_COMMANDS = [
        "sudo apt-get install git make;go get -u github.com/kgretzky/evilginx2",
        "cd $GOPATH/src/github.com/kgretzky/evilginx2;make",
        "sudo make install;sudo evilginx"
    ]
    RUN_COMMANDS = ["sudo evilginx"]
    PROJECT_URL = "https://github.com/kgretzky/evilginx2"


class ISeeYou(HackingTool):
    TITLE = "I-See_You(Get Location using phishing attack)"
    DESCRIPTION = "[!] ISeeYou is a tool to find Exact Location of Victom By" \
                  " User SocialEngineering or Phishing Engagment..\n" \
                  "[!] Users can expose their local servers to the Internet " \
                  "and decode the location coordinates by looking at the log file"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/Viralmaniar/I-See-You.git",
        "cd I-See-You && sudo chmod u+x ISeeYou.sh"
    ]
    RUN_COMMANDS = ["cd I-See-You && sudo bash ISeeYou.sh"]
    PROJECT_URL = "https://github.com/Viralmaniar/I-See-You"


class SayCheese(HackingTool):
    TITLE = "SayCheese (Grab target's Webcam Shots)"
    DESCRIPTION = "Take webcam shots from target just sending a malicious link"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/hangetzzu/saycheese"]
    RUN_COMMANDS = ["cd saycheese && sudo bash saycheese.sh"]
    PROJECT_URL = "https://github.com/hangetzzu/saycheese"


class QRJacking(HackingTool):
    TITLE = "QR Code Jacking"
    DESCRIPTION = "QR Code Jacking (Any Website)"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/cryptedwolf/ohmyqr.git && sudo apt-get install scrot"]
    RUN_COMMANDS = ["cd ohmyqr && sudo bash ohmyqr.sh"]
    PROJECT_URL = "https://github.com/cryptedwolf/ohmyqr"


class ShellPhish(HackingTool):
    TITLE = "ShellPhish"
    DESCRIPTION = "Fhishing Tool for 18 social media"
    INSTALL_COMMANDS = ["git clone https://github.com/An0nUD4Y/shellphish.git"]
    RUN_COMMANDS = ["cd shellphish;sudo bash shellphish.sh"]
    PROJECT_URL = "https://github.com/An0nUD4Y/shellphish"


class BlackPhish(HackingTool):
    TITLE = "BlackPhish"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/iinc0gnit0/BlackPhish.git",
        "cd BlackPhish;sudo bash install.sh"
    ]
    RUN_COMMANDS = ["cd BlackPhish;sudo python3 blackphish.py"]
    PROJECT_URL = "https://github.com/iinc0gnit0/BlackPhish"

    def __init__(self):
        super(BlackPhish, self).__init__([('Update', self.update)])

    def update(self):
        os.system("cd BlackPhish;sudo bash update.sh")


class PhishingAttackTools(HackingToolsCollection):
    TITLE = "Phishing attack tools"
    TOOLS = [
        Setoolkit(),
        SocialFish(),
        HiddenEye(),
        Evilginx2(),
        ISeeYou(),
        SayCheese(),
        QRJacking(),
        ShellPhish(),
        BlackPhish()
    ]
