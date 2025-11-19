FROM bj-warehouse.tencentcloudcr.com/weike/python:3.12-slim-bullseye

# 设置工作目录
WORKDIR /app

# 设置时区
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo 'Asia/Shanghai' > /etc/timezone

RUN cat > /etc/apt/sources.list <<'EOF'
deb https://mirrors.aliyun.com/debian/ bullseye main non-free contrib
deb-src https://mirrors.aliyun.com/debian/ bullseye main non-free contrib
deb https://mirrors.aliyun.com/debian-security/ bullseye-security main
deb-src https://mirrors.aliyun.com/debian-security/ bullseye-security main
deb https://mirrors.aliyun.com/debian/ bullseye-updates main non-free contrib
deb-src https://mirrors.aliyun.com/debian/ bullseye-updates main non-free contrib
EOF

# 设置环境变量
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ADD google/chrome-linux64 /opt/google/chrome
ADD google/chromedriver-linux64/chromedriver /usr/bin/chromedriver

# 安装系统依赖
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        vim  \
        curl \
        procps \
        gcc \
        g++ \
        make \
        zlib1g-dev \
        libjpeg-dev \
        libpng-dev \
        libfreetype6-dev \
        libgl1-mesa-glx \
        libglib2.0-0 \
        nodejs \
        libnss3 \
        libnspr4 \
        libatk1.0-0 \
        libcups2 \
        libxcomposite1 \
        libxrandr2 \
        libxdamage1 \
        libxfixes3 \
        libxkbcommon0 \
        libpango1.0-0 \
        libgbm1 \
        libasound2 \
        libatspi2.0-0 \
        libgtk-3-0 \
    && rm -rf /var/lib/apt/lists/*

# 复制依赖文件
COPY requirements.txt /app/

# 安装 Python 依赖
RUN pip install -U setuptools -i https://mirrors.aliyun.com/pypi/simple/

RUN pip install --no-cache-dir -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

# 复制项目文件
COPY . /app/

# 启动命令
CMD ["python", "main.py"]
