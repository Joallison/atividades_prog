#!/usr/bin/env python3
import argparse, socket
from datetime import datetime

MAX_BYTES = 65535

def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', port))
    print('Ouvindo em {}'.format(sock.getsockname()))
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        texto = data.decode('ascii')
        print('O cliente em {} disse {!r}'.format(address, texto))
        texto = 'Os dados enviados foram {}'.format(len(data))
        data = texto.encode('ascii')
        sock.sendto(data, address)

def client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    texto = 'Tempo: {}'.format(datetime.now())
    data = texto.encode('ascii')
    sock.sendto(data, ('127.0.0.1', port))
    print('O SO designou o endereco IP {}'.format(sock.getsockname()))
    data, address = sock.recvfrom(MAX_BYTES)
    texto = data.decode('ascii')
    print('O servidor {} respondeu {!r}'.format(address, texto))
    
if __name__ == '__main__':
    escolhas = {'client': client, 'server':server}
    parser = argparse.ArgumentParser(description = 'Envia e recebe UDP localmente')
    parser.add_argument('definicao', escolhas = escolhas, help = 'Escolha se o script e: client ou server')
    parser.add_argument('-p', metavar = 'port', type = int, default = 1060, help = 'Porta UDP (porta padrao 1060)')
    args = parser.parser_args()
    function = escolhas[args.definicao]
    function(args.p)
