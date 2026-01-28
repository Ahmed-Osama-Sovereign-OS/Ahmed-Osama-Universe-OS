FROM debian:bookworm-slim

# تثبيت أدوات الافتراس (المحاكيات والبرامج الأساسية)
RUN apt-get update && apt-get install -y \
    python3-pip python3-pygame python3-opengl \
    wine64 xterm firefox-esr qemu-system-x86 \
    && rm -rf /var/lib/apt/lists/*

# تثبيت مكتبات الذكاء الاصطناعي
RUN pip3 install numpy llama-cpp-python --break-system-packages

COPY . /opt/ahmed_osama_os
WORKDIR /opt/ahmed_osama_os

# تشغيل الواجهة عند الإقلاع
CMD ["python3", "main_core.py"]
