FROM kalilinux/kali-rolling

RUN apt update && apt install -y git python3 python3-pip python3-tk

WORKDIR /app
RUN git clone https://github.com/taysmith99/PT-GUI.git
WORKDIR /app/PT-GUI
RUN pip3 install -r requirements.txt

CMD ["python3", "main.py"]
