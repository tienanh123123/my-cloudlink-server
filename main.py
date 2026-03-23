import cloudlink
import os

# Khởi tạo server
server = cloudlink.server()

# Lấy cổng (Port) từ hệ thống Render cấp phát
# Nếu không có thì mặc định dùng 10000
port = int(os.environ.get("PORT", 10000))

print(f"--- Server CloudLink đang chạy trên cổng {port} ---")

# Chạy server với host 0.0.0.0 để nhận kết nối từ bên ngoài
server.run(host="0.0.0.0", port=port)
