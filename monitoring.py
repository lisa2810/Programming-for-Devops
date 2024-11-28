import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Fungsi untuk mengecek status server
def check_server(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Server {url} is up!")
        else:
            # Format pesan dengan status code
            message = f"Server {url} is down! Status code: {response.status_code}"
            print(message)
            send_alert(message)
    except requests.exceptions.RequestException as e:
        # Format pesan untuk error
        message = f"Error accessing {url}: {e}"
        print(message)
        send_alert(message)

# Fungsi untuk mengirim email alert
def send_alert(message):
    sender = 'harahapmonalisa708@gmail.com'  # Ganti dengan email Anda
    receiver = 'jidanputra0354@gmail.com'  # Ganti dengan email penerima
    password = 'harahaplisa'  # Ganti dengan password atau App Password

    # Membuat pesan email
    msg = MIMEMultipart()
    msg['Subject'] = 'Server Down Alert'
    msg['From'] = sender
    msg['To'] = receiver
    msg.attach(MIMEText(message, 'plain'))

    # Mengirim email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Menggunakan enkripsi TLS
            server.login(sender, password)  # Login dengan App Password
            server.sendmail(sender, receiver, msg.as_string())  # Kirim email
    except Exception as e:
        print(f"Failed to send email: {e}")

# URL yang akan di-monitoring
url_to_check = "https://www.google.com"
check_server(url_to_check)
