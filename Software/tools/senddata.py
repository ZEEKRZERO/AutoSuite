import socket
import time

# 创建一个TCP套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定到本地IP和端口号
local_ip = '0.0.0.0'  # 本地IP
local_port = 3333     # 本地端口号
sock.bind((local_ip, local_port))

# 监听连接请求
sock.listen(1)
print(f'Listening on {local_ip}:{local_port}...')

# 无限循环，接受客户端连接并发送数据
while True:
    # 接受客户端连接
    conn, addr = sock.accept()
    print(f'Connected by {addr}')

    # 无限循环，每隔1秒发送一次数据
    while True:
        time.sleep(0.1)

        # 待发送的数据
        data = b'\xfaQ\x01\x02\x08\xe87\x00\x00\x00%\x08\x08\x00\x00\x00\x00\x08\x00\x0fR\xfb'
        try:
            # 发送数据到客户端
            conn.send(data)
            print(f'Sent {len(data)} bytes')
        except:
            print("socket closed")
            break

        # 等待1秒后再次发送数据

    # 关闭连接
    # conn.close()
