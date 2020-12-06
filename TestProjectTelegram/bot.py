from __init__ import *
from Certificate import *


bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message:types.Message):
    answer = message.text
    answer = answer.split(' ')
    command = answer[0]
    entry_func = True
    
    if command == '/getCert' or command == '/getcert':
        if check_args_amount(answer, 4):
            pass
        else:
            answer = 'Не верный формат записи! Для данной команды необходимо 3 аргумента(Смотри в /help)'
            await message.answer(answer)
            entry_func = False
            
    if command == '/checkCert' or command == '/checkcert':
        if check_args_amount(answer, 2):
            pass
        else:
            answer = 'Не верный формат записи! Для данной команды необходим 1 аргумент(Смотри в /help)'
            await message.answer(answer)
            entry_func = False
        
    if entry_func and (command == '/getCert' or command == '/getcert'):
            
        name = answer[1]
        issued_to = answer[2]
        validity = answer[3]

        pattern = r'[a-zA-Zа-яА-Я\+]'
        pattern2 = r'[0-9]'

        if checking_characters(pattern, str(issued_to)) and (validity == 'all' or validity == 'All' or checking_characters(pattern2, str(validity))):
            try:
                validity = int(validity)
            except:
                pass
                
            a = Certificate(name, issued_to, validity)
            a.saving_to_db()
            answer = a.create_certificate()
            await message.answer(answer)
        else:
            answer = 'Не допустимый формат! Могут приниматься только буквы русского и английского алфавитов'
            await message.answer(answer)
            
    elif entry_func and (command == '/checkCert' or command == '/checkcert'):
        certificate_key = answer[1]
        answer = checkCertificate(certificate_key)
        await message.answer(answer)

    elif command == '/help':
        if check_args_amount(answer, 2):
            lang = answer[1]
            if lang == 'ru' or lang == 'rus' or lang == 'RU':
                answer = 'Команды бота:\n\n1)/getCert VALUE1, VALUE2, VALUE3 - выдать сертификат\nVALUE1 - Имя курса\nVALUE2 - Имя прошедшего курс\nVALUE3 - Время валидности сертификата, если сертификат выдаётся навегда введите all\nЕсли в имени пользователя прошедшего курс необходимо указать несколько значение пример: Иван Иванов, то используйте конструкция VALUE+VALUE пример /getCert C++ Иван+Иванов all\n\n/checkCert VALUE - проверка сертификата\nVALUE - код/номер сертификата'
                await message.answer(answer)
            elif lang == 'en' or lang == 'eng' or lang == 'EN':
                answer = 'Bot commands:\n\n1)/getCert VALUE1, VALUE2, VALUE3-issue a certificate\nVALUE1-name of the course\nVALUE2 - name of the past course\nVALUE3 - time of validity of the certificate, if the certificate is issued always enter all\if the user name of the past course must specify several values example: Ivan Ivanov, then use the construction VALUE+VALUE example /getCert C++ Ivan+Ivanov all\n\n/checkCert VALUE-certificate verification\nVALUE-certificate code/number'
                await message.answer(answer)
        else:
            answer = 'Команды бота:\n\n1)/getCert VALUE1, VALUE2, VALUE3 - выдать сертификат\nVALUE1 - Имя курса\nVALUE2 - Имя прошедшего курс\nVALUE3 - Время валидности сертификата, если сертификат выдан навегда введите all\nЕсли в имени пользователя прошедшего курс необходимо указать несколько значение пример: Иван Иванов, то используйте конструкция VALUE+VALUE пример /getCert C++ Иван+Иванов all\n\n/checkCert VALUE - проверка сертификата\nVALUE - код/номер сертификата\n\nВы можете просмотреть эту информацию на английском с помощью команды /help en\nYou can choose to view this information in English using the /help en command'
            await message.answer(answer)

    else:
        if not entry_func:
            pass
        else:
            answer = 'Команда не найдена!'
            await message.answer(answer)
        

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
