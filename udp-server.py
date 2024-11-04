import socket

# 设置服务器的IP地址和端口
HOST = "0.0.0.0"  # 监听本地地址，使用'0.0.0.0'可以监听所有可用的网络接口
PORT = 12345  # 使用一个未占用的端口


def udp_server():
    # 创建UDP套接字
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        # 绑定地址和端口
        server_socket.bind((HOST, PORT))
        print(f"UDP server is running on {HOST}:{PORT}")

        # 持续监听客户端请求
        while True:
            # 接收数据和客户端地址
            data, client_address = server_socket.recvfrom(1024)  # 缓冲区大小为1024字节
            print(f"Received message from {client_address}: {data.decode()}")

            # 构建并发送响应
            response = f"Received your message: {data.decode()}"
            server_socket.sendto(response.encode(), client_address)
            print(f"Sent response to {client_address}")


# 启动UDP服务器
udp_server()
