import smtplib  # Импортируем библиотеку по работе с SMTP

# Добавляем необходимые подклассы - MIME-типы
from email.mime.multipart import MIMEMultipart  # Многокомпонентный объект
from email.mime.text import MIMEText  # Текст/HTML
from email.mime.image import MIMEImage  # Изображения
import random

from data import config3 as config


alphabet = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
code = None


def send_email(address_to):
    global code

    address_from = config.address_from  # Адресат
    address_to = address_to  # Получатель
    password = config.password  # Пароль

    msg = MIMEMultipart()  # Создаем сообщение
    msg['From'] = address_from  # Адресат
    msg['To'] = address_to  # Получатель
    msg['Subject'] = 'Регистрация в проекте'  # Тема сообщения

    code = str([random.choice(list(alphabet)) for _ in range(20)])

    html = f"""\
    <html>
      <body>
        <div style="text-align: center; font-size: 30px">
            Спасибо за регистрацию в проекте КакТак!
        </div>
        <div style="text-align: center; font-size: 30px">
            Чтобы подтвердить регистрацию перейдите по ссылке нижже:
        </div>
        <a href="http://localhost:8080/submit_email/{code}" style="font-size: 20px;">Ссылка</a>
      </body>
    </html>
    """
    msg.attach(MIMEText(html, 'html', 'utf-8'))         # Добавляем в сообщение HTML-фрагмент

    server = smtplib.SMTP('smtp.gmail.com', 587)        # Создаем объект SMTP
                                                        # Начинаем шифрованный обмен по TLS
    server.starttls()
    server.login(address_from, password)                # Получаем доступ
    server.send_message(msg)                            # Отправляем сообщение
    server.quit()                                       # Выходим


def send_for_admin(user_list):
    address_from = config.address_from
    address_to = config.admin_adress
    password = config.password

    msg = MIMEMultipart()
    msg['From'] = address_from
    msg['To'] = address_to
    msg['Subject'] = 'Новый зарегистрированный пользователь'

    html = f"""\
    <html>
      <body>
        <div>Зарегистрирован новый пользователь:</div>
        <div>Имя: {user_list[0]}</div>
        <div>Почта: {user_list[1]}</div>
      </body>
    </html>
    """
    msg.attach(MIMEText(html, 'html', 'utf-8'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
                                                        
    server.starttls()
    server.login(address_from, password)                
    server.send_message(msg)                            
    server.quit()                                      


def get_code():
    return code
