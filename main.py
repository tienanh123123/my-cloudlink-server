import cloudlink

# Khởi tạo server CloudLink
server = cloudlink.server()

print("Server đang khởi động...")
# Port 10000 là mặc định của Render
server.run(host="0.0.0.0", port=10000)
