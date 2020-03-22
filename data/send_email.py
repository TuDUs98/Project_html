import smtplib  # Импортируем библиотеку по работе с SMTP

# Добавляем необходимые подклассы - MIME-типы
from email.mime.multipart import MIMEMultipart  # Многокомпонентный объект
from email.mime.text import MIMEText  # Текст/HTML
from email.mime.image import MIMEImage  # Изображения
import random


alphabet = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
code = None


def send_email(address_to):
    global code

    address_from = "kaktak.group@gmail.com"  # Адресат
    address_to = address_to  # Получатель
    password = "nazar40221987"  # Пароль

    msg = MIMEMultipart()  # Создаем сообщение
    msg['From'] = address_from  # Адресат
    msg['To'] = address_to  # Получатель
    msg['Subject'] = 'Тема сообщения'  # Тема сообщения

    code = str([random.choice(list(alphabet)) for _ in range(20)])

    html = f"""\
    <html>
      <head></head>
      <body>
        <div style="text-align: center; font-size: 30px">
            Спасибо за регистрацию в проекте КакТак!
        </div>
        <div style="text-align: center; font-size: 30px">
            Чтобы подтвердить регистрацию перейдите по ссылке нижже:
        </div>
        <a href="http://kaktak.herokuapp.com/submit_email/{code}">Ссылка</a>
      </body>
    </html>
    """
    msg.attach(MIMEText(html, 'html', 'utf-8'))  # Добавляем в сообщение HTML-фрагмент

    server = smtplib.SMTP('smtp.gmail.com', 587)        # Создаем объект SMTP
    server.starttls()                                   # Начинаем шифрованный обмен по TLS
    server.login(address_from, password)                   # Получаем доступ
    server.send_message(msg)                            # Отправляем сообщение
    server.quit()                                       # Выходим


def get_code():
    return code
