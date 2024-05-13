import requests
import os
from threading import Thread, Lock


# 请编写请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# 指定要下载的图片前缀
prefix = "297825"

# 指定要下载的图片序号范围
start_index = 0
end_index = 99999999

# 图片URL的固定部分
base_url = "http://jyfp.sjy.net.cn/resources/40/"

# 创建一个目录来保存下载的图片
if not os.path.exists("images"):
    os.mkdir("images")

# 创建一个锁来同步打印
print_lock = Lock()


# 下载图片的函数
def download_image(index):
    # 构造完整的图片URL
    url = base_url + prefix + str(index).zfill(11) + ".jpg"

    try:
        # 发送GET请求获取图片数据
        response = requests.get(url, headers=headers)

        # 如果请求成功,保存图片到本地
        if response.status_code == 200:
            filename = prefix + str(index).zfill(11) + ".jpg"
            with open(f"images/{filename}", "wb") as f:
                f.write(response.content)
            with print_lock:
                print(f"成功下载图片: {filename}")
        else:
            with print_lock:
                # print(f"图片不存在: {url}")
                ...
    except:
        with print_lock:
            # print(f"下载图片失败: {url}")
            ...


# 创建并启动多个线程并行下载
threads = []
for index in range(start_index, end_index + 1):
    t = Thread(target=download_image, args=(index,))
    threads.append(t)
    t.start()

# 等待所有线程完成
for t in threads:
    t.join()

print("所有图片下载完成!")
