import socketserver
from util.request import Request
import os

class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        response = ""
        received_data = self.request.recv(2048)
        request = Request(received_data)
        # print(request.path)

        if request.path == '/':
            # リクエストが / の場合、public/index.html の内容を返す
            file_path = "public/index.html"
            
            if os.path.exists(file_path) and os.path.isfile(file_path):
                with open(file_path, "rb") as file:
                    content = file.read()
                
                content_length = len(content)
                content_length_header = f"Content-Length: {content_length}\r\n"
                response = (
                    b"HTTP/1.1 200 OK\r\n"
                    + content_length_header.encode("utf-8")
                    + b"Content-Type: text/html\r\n\r\n"
                    + content
                )

                            
            else:
                # ファイルが存在しない場合、404 エラーを返す
                response = b"HTTP/1.1 404 Not Found\r\nContent-Length: 6\r\n\r\ninside"

        elif request.path.startswith("/image/"):
            # リクエストが /image/ から始まる場合
            image_file_name = request.path[len("/image/"):]
            file_path = f"public/image/{image_file_name}"

            if os.path.exists(file_path) and os.path.isfile(file_path):
                with open(file_path, "rb") as file:
                    content = file.read()
                
                content_length = len(content)
                content_type_header = b"Content-Type: image/jpeg\r\n"  # JPEG画像の場合

                response = (
                    b"HTTP/1.1 200 OK\r\n"
                    + f"Content-Length: {content_length}\r\n".encode("utf-8")
                    + content_type_header
                    + b"\r\n"
                    + content
                )

        elif request.path == "/style.css":
            file_path = "public/style.css"

            if os.path.exists(file_path) and os.path.isfile(file_path):
                with open(file_path, "rb") as file:
                    content = file.read()
                
                content_length = len(content)
                content_length_header = f"Content-Length: {content_length}\r\n"
                response = (
                    b"HTTP/1.1 200 OK\r\n"
                    + content_length_header.encode("utf-8")
                    + b"Content-Type: text/css\r\n\r\n"
                    + content
                )                

        elif request.path == "/functions.js":
            file_path = "public/functions.js"

            if os.path.exists(file_path) and os.path.isfile(file_path):
                with open(file_path, "rb") as file:
                    content = file.read()
                
                content_length = len(content)
                content_length_header = f"Content-Length: {content_length}\r\n"
                response = (
                    b"HTTP/1.1 200 OK\r\n"
                    + content_length_header.encode("utf-8")
                    + b"Content-Type: text/js\r\n\r\n"
                    + content
                )

        elif request.path == "/cookie.js":
            file_path = "public/cookie.js"

            if os.path.exists(file_path) and os.path.isfile(file_path):
                with open(file_path, "rb") as file:
                    content = file.read()
                
                content_length = len(content)
                content_length_header = f"Content-Length: {content_length}\r\n"
                response = (
                    b"HTTP/1.1 200 OK\r\n"
                    + content_length_header.encode("utf-8")
                    + b"Content-Type: text/js\r\n\r\n"
                    + content
                )             

        elif request.path == "/visit-counter":
            file_path = "public/cookie.html"
            # "/visit-counter" パスにアクセスがあった場合の処理
            if os.path.exists(file_path) and os.path.isfile(file_path):
                with open(file_path, "rb") as file:
                    content = file.read()
                
                content_length = len(content)
                content_length_header = f"Content-Length: {content_length}\r\n"
                response = (
                    b"HTTP/1.1 200 OK\r\n"
                    + content_length_header.encode("utf-8")
                    + b"Content-Type: text/html\r\n\r\n"
                    + content
                )      

        else:
            # パスが / でない場合、404 エラーを返す
            response = b"HTTP/1.1 404 Not Found\r\nContent-Length: 9\r\n\r\nNot Found"

        # クライアントにレスポンスを送信
        self.request.sendall(response)

if __name__ == "__main__":
    host, port = "0.0.0.0", 8080
    server = socketserver.TCPServer((host, port), MyTCPHandler)
    print(f"Listening on {host}:{port}")

    server.serve_forever()

