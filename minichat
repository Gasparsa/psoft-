#coding: utf-8
import socket
import sys
from threading import Thread
import os
connections = {}
def cliente(connection):
    connection.send(("vc está conectado\nQual seu nome: ").encode())
    nome = connection.recv(4096).decode('utf-8').strip()
    connections[connection] = nome
    connection.send("> ".encode())    
    while True:
        mensagem = connection.recv(4096).decode('utf-8').strip()
        if mensagem == ":bye": 
            connection.send("saiu.\n".encode())
            print("%s saiu."% nome)
            connection.close()
            del connections[connection]
            for con in connections:
                con.send(("%s saiu\n"%nome).encode())
            exit()            
        if mensagem:
            print("%s disse: %s"%(nome, mensagem))
            for con in connections:
                if not (con == connection):
                    con.send(("%s disse: %s \n> "%(nome, mensagem)).encode())
                else: con.send("> ".encode())
porta = int(sys.argv[1] if len(sys.argv) > 1 else 9090)
host_ip = socket.gethostbyname(socket.gethostname())
with socket.socket() as s:
    s.bind((host_ip, porta))
    s.listen()
    print("Conectar no ip %s pela porta %s"%(host_ip, porta))
    
    while True:
        connection, address = s.accept()
        print("%s o ip se conectou"%address[0])
        Thread(target=cliente, args=(connection,)).start()
