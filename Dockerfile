FROM kalilinux/kali-rolling

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y kali-linux-headless git python3 python3-pip python3-tk

WORKDIR /app
RUN git clone https://github.com/taysmith99/PT-GUI.git
WORKDIR /app/PT-GUI
RUN pip3 install -r requirements.txt

CMD ["python3", "main.py"]
