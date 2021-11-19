from __init__ import *
class Certificate:
    def __init__(self, name, issued_to, validity):
        self.name = name
        self.issued_to = issued_to
        self.validity = validity
        
        self.date = datetime.now()
        self.date = str(self.date)
        self.date = self.date.split(' ')
        self.date = str(self.date[0])

        self.certificate_number = str(os.urandom(8).hex())

    def saving_to_db(self):
        con = pymysql.connect(ip_db, login_db, password_db, name_db)
        cur = con.cursor()

        if self.validity.lower() == 'at all':
            validity_time = 999999999999999999
            cur.execute("INSERT INTO name_table (certificate_key, name_course, name_user, date, validity_time) values(%s, %s, %s, %s, %s)", (self.certificate_number, self.name, self.issued_to, self.date, validity_time))
            con.commit()
        else:
            validity_time = time.time() + self.validity
            cur.execute("INSERT INTO name_table (certificate_key, name_course, name_user, date, validity_time) values(%s, %s, %s, %s, %s)", (self.certificate_number, self.name, self.issued_to, self.date, validity_time))
            con.commit()

    def create_certificate(self):
        self.issued_to = self.issued_to.replace('+', ' ')
        res = 'Вы успешно окончили курс: '+str(self.name)+'\nСертификат выдан: '+str(self.issued_to)+'\nДата выдачи: '+str(self.date)+'\nУникальный ключ: '+str(self.certificate_number)
        return res

def checkCertificate(certificate_number):
    con = pymysql.connect(ip_db, login_db, password_db, name_db)
    cur = con.cursor()
    cur.execute("SELECT * FROM name_table")
    for row in cur.fetchall():
        a = list(row)
        certificate_number_bd = a[1]
        if certificate_number == certificate_number_bd:
            validity_time = a[5]
            if validity_time > time.time():
                name_course = a[2]
                name_user = a[3]
                date = a[4]
                answer = 'Сертификат действителен!\nСертификат об окончании курса: '+str(name_course)+'\nПринадлежит: '+str(name_user)+'\nВыдан: '+str(date)
                return answer
            else:
                return 'Сертификат устарел'
    return 'Сертификат с таким номером не обнаружен!'

def checking_characters(pattern, string):
        
    string_source_list = list(string)
        
    number_of_matches = re.findall(pattern, string)
        
    if len(number_of_matches) == len(string_source_list):
        return True
    return False

def check_args_amount(answer, amount_args):
    if len(answer) <= amount_args <= len(answer):
        return True
    else:
        return False
    
