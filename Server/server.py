import socketserver

class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(2048).strip()
        print(self.data.decode("utf-8"))
        self.request.sendall(self.data)

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    with socketserver.TCPServer((HOST, PORT), TCPHandler) as server:
        print("Server started")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("Server stopped")
            server.shutdown()
            server.server_close()
            quit()