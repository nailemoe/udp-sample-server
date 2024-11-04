FROM python:3.12-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录下的代码到容器内
COPY udp-server.py .

# 暴露UDP服务的端口
EXPOSE 12345/udp

# 启动UDP服务
CMD ["python", "udp-server.py"]