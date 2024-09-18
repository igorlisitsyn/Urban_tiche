
SENDER_ = "university.help@gmail.com"
DOMEN_ = [".com", ".ru", "net"]

# определяем условие наличие "@"
def seach(recipient, sender):
    if "@" in recipient and "@" in sender:
        return True
    else: return False

# определяем условие  на наличие ".com"/".ru"/".net"
def domen(recipient, sender):
    key_1 = False
    key_2 = False
    for i in DOMEN_:
        if i in recipient: key_1 = True
        if i in sender: key_2 = True

    if key_1 and key_2:
        return True
    else: return False


def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    matches_domen = domen(recipient, sender)
    matces = seach(recipient, sender)
    if recipient == sender:
        print(f'Нельзя отправить письмо самому себе!')
        exit()
    if sender == SENDER_:
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
        exit()

    if matches_domen and matces and sender != SENDER_:

        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
        exit()
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        exit()



def main():
    send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')


if __name__ == '__main__':
    main()