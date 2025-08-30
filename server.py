from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''
<!doctype html>
<html>
    <head>
        </head>
        <body bgcolor="cyan">
            <table border="1" align="center" bgcolor="pink" cellpadding="10">
            <caption><h1>list of protocols</h1><caption>
            <tr><th>s.no.</th><th>name of the layers</th>
                <th>name of the protocols</th>
            </tr>
            <tr>
                <td>1</td><td>application layer</td><td>http,ftp</td>
            
            </tr>
            <tr>
                <td>2</td><td>transport layer</td><td>TCP & UDP</td>

            </tr>
            <tr>
                <td>3</td><td>network layer</td><td>IP,ICMP</td>

            </tr>
            <tr>
                <td>4</td><td>data link layer</td><td>Ethernet,PPP</td>
            </tr>
            <tr>
                <td>5</td><td>physical layer</td><td>DSL,ISDN</td>
            </table>



            
        </body>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()