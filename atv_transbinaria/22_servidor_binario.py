import socket

HOST = ""
PORTA = 8051

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORTA))
sock.listen(1)
conn, addr = sock.accept()
print("Conectado de:", str(addr))

while True:
    raw_data = conn.recv(44032)
    #Filtrando a saida para o arquivo
    data = repr(raw_data)[2:-1]

    if (data == 'o'):
        with open ('logoifrn.jpg', 'rb') as f1:
            conn.send(f1.read(44032))
    elif (data == 'q'):
        break

conn.close()
