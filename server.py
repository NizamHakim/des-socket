import socket
import des

def server_program():
    HOST = '127.0.0.1'
    PORT = 5000
    KEY = 'aBhNDJjB'

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))

    server_socket.listen(1)
    print(f"Listening on {HOST}:{PORT} ...")
    
    client_socket, addr = server_socket.accept()
    print(f"Got a connection from {addr}")
    
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        print(f'receive encrypted message: {data}')
        
        # decryptedData = des.ecbDecrypt(data, KEY) # ECB mode
        decryptedData = des.cbcDecrypt(data, KEY, KEY[::-1]) # CBC mode
        
        print(f'decrypted message: {decryptedData}')

    client_socket.close()
    print('Client disconnected, server shutting down ...')
    server_socket.close()

if __name__ == '__main__':
    server_program()