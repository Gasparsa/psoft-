#coding: utf-8
import socket
import sys
from threading import Thread
import os
usuarios = {}
def cliente(conexao):
    conexao.send(("vc está conectado\nQual seu nome: ").encode())
    nome = conexao.recv(4096).decode('utf-8').strip()
    usuarios[conexao] = nome
    conexao.send("> ".encode())    
    while True:
        mensagem = conexao.recv(4096).decode('utf-8').strip()
        if mensagem == ":bye": 
            conexao.send("saiu.\n".encode())
            print("%s saiu."% nome)
            conexao.close()
            del usuarios[conexao]
            for conectado in usuarios:
                conectado.send(("%s saiu\n"%nome).encode())
            exit()            
        if mensagem:
            print("%s disse: %s"%(nome, mensagem))
            for conectado in usuarios:
                if not (conectado == conexao):
                    conectado.send(("%s disse: %s \n> "%(nome, mensagem)).encode())
                else: conectado.send("> ".encode())
porta = int(sys.argv[1] if len(sys.argv) > 1 else 9090)
host_ip = socket.gethostbyname(socket.gethostname())
with socket.socket() as s:
    s.bind((host_ip, porta))
    s.listen()
    print("Conectar no ip %s pela porta %s"%(host_ip, porta))
    
    while True:
        conexao, address = s.accept()
        print("O ip %s se conectou"%address[0])
        Thread(target=cliente, args=(conexao,)).start()
