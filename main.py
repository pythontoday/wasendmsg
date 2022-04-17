import pywhatkit
import os


def send_message_inst():
    # mobile = input('Введите номер получателя: ')
    mobile = os.getenv('MOBILE')
    message = input('Введите текст сообщения: ')
    
    pywhatkit.sendwhatmsg_instantly(phone_no=mobile, message=message)
    
    
def send_message():
    # mobile = input('Введите номер получателя: ')
    mobile = os.getenv('MOBILE')
    message = input('Введите текст сообщения: ')
    hour = int(input('Введите часы: '))
    minutes = int(input('Введите минуты: '))
    
    pywhatkit.sendwhatmsg(phone_no=mobile, message=message, time_hour=hour, time_min=minutes)

    
def main():
    # send_message_inst()
    # send_message()
    pywhatkit.image_to_ascii_art(img_path='hack_achiv.png')
    
    
if __name__ == '__main__':
    main()
