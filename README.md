# Getting Started

This honeypot has been made for educational purpose.
It is not programmed to be placed in a real environment as it is not 100% secure.

## Prerequisites

- A functional GNU/Linux OS connected to internet.

## Installation

Check and place your working directory with
```bash
cd <directory>
```

```bash
sudo apt update

git clone https://github.com/nathangst/honeypot-ftp

cd honeypot-ftp

sudo apt install python3-venv
python -m venv VirtualEnv

pip install -r requirements.txt

sudo apt install nohup
nohup python3 main.py &

tail -f honeypot.log
```

### Multiple changes are needed
- In main.py    
  - You need to change the variable ```IP_ADDRESS = '127.0.0.1'``` to the right interface.
  - You can change the port on this line ```PORT = 987``` 
- To add more files to make it more realistic, place them in the ```contrats``` directory.
