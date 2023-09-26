# 使用官方的Golang镜像作为基础镜像
FROM golang:1.16

# 设置工作目录
WORKDIR /app

# 复制Go应用程序文件到容器中
COPY main.go .

# 构建Go应用程序
RUN go build -o main .

# 暴露容器端口
EXPOSE 8080

# 运行Go应用程序
CMD ["./main"]
