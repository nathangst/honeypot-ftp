
import datetime
import logging

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


IP_ADDRESS = '127.0.0.1'


def write_log(log_message):
    with open("honeypot.log", "a") as log_file:
        log_file.write(log_message + "\n")


class MyFTPHandler(FTPHandler):
    def on_connect(self):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] - Connection established from {self.remote_ip}"
        write_log(log_message)

    def on_file_received(self, file):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] - File received: {file}"
        print(log_message)
        write_log(log_message)

    def on_file_sent(self, file):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] - File downloaded: {file}"
        write_log(log_message)


def ftp_server():
    authorizer = DummyAuthorizer()
    authorizer.add_user("user", "12345", "./contrats", perm="lr")

    handler = MyFTPHandler
    handler.authorizer = authorizer
    handler.banner = "Welcome to the Honeypot FTP Server"
    handler.log_all = True

    logging.basicConfig(level=logging.INFO)
    handler.banner = "Welcome to the Honeypot FTP Server"
    address = (IP_ADDRESS, 987)
    server = FTPServer(address, handler)
    server.serve_forever()


if __name__ == "__main__":
    # Lancement du serveur FTP
    ftp_server()
