FROM registry.cn-hangzhou.aliyuncs.com/zhangyucumt/media-crawler-base:v1

RUN pip install --no-cache-dir -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

# 复制项目文件
COPY . /app/

# 启动命令
CMD ["python", "main.py"]
