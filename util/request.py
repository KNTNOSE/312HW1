class Request:
    def __init__(self, request: bytes):
        self.request_str = request.decode("utf-8")

        self.body = b""
        self.method = ""
        self.path = ""
        self.http_version = ""
        self.headers = {}
        self.parse_headers()
        self.parse_body(request)

    def parse_headers(self):
        headers_section = self.request_str.split('\r\n\r\n', 1)[0]
        request_line = headers_section.split('\r\n')[0]
        header_list = headers_section.split('\r\n')[1:]

        parts = request_line.split(' ')
        if len(parts) >= 2:
            self.method = parts[0]
            self.path = parts[1]
            self.http_version=parts[2]
        

        for header in header_list:
            header_name, header_value = header.split(': ', 1)

            if header_name in self.headers:
                if not isinstance(self.headers[header_name], list):
                    self.headers[header_name] = [self.headers[header_name]]
                self.headers[header_name].append(header_value)
            else:
                self.headers[header_name] = header_value

    def parse_body(self, request):
        if '\r\n\r\n' in self.request_str:
            body_section = self.request_str.split('\r\n\r\n', 1)[1]
            self.body = body_section.encode("utf-8")
        else:
            # リクエストが正しくない場合、エラーレスポンスを生成
            self.body = b"Bad Request"


    def set_content_length(self):
        content_length = len(self.body)
        self.headers["Content-Length"] = str(content_length)


# request_bytes = b"GET /example HTTP/1.1\r\nHost: cse312.com\r\nUser-Agent: Mozilla/5.0\r\n\r\naaaaaaaaaaa"
# request_instance = Request(request_bytes)

# print("HTTP method", request_instance.request_str.split()[0])
# print("Request pass", request_instance.request_str.split()[1])
# print("HTTP version", request_instance.request_str.split()[2])
# print("Host header", request_instance.headers.get('Host'))
# print("Request Body", request_instance.body)
# print(request_instance.request_str.split('\r\n\r\n', 1)[1])


