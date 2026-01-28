FROM debian:bookworm-slim
RUN apt-get update && apt-get install -y \
    python3-pip python3-pygame python3-opengl wine \
    && rm -rf /var/lib/apt/lists/*
RUN pip3 install numpy --break-system-packages
COPY . /app
WORKDIR /app
CMD ["python3", "main_core.py"]
