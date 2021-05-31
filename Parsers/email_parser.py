import re
import os
import pprint

class email_debugger_5000():
    def __init__(self, data):
        self.data = data
        self.lines = data.readlines()
        self.qline = []
        self.patt_id = '^[A-Z0-9]+\*'
        self.patt_size = r'\s[0-9]+\s'
        self.patt_date = r'[A-Z][a-z][a-z]\s[A-Z][a-z][a-z]\s[\d]+\s'
        self.patt_time = r'(\d{2}:\d{2}:\d{2})'
        self.patt_email = r'[a-z.]+@[a-z-]+\.(ru|com)'
        self.log_path = '/home/oxxo/Downloads/queue_fix/log.txt'

    def parser(self, line):
        ID = re.search(self.patt_id, line)
        size = re.search(self.patt_size, line)
        arr_time = re.search(self.patt_date+self.patt_time, line)
        email = re.search(self.patt_email, line)

        return [ID[0], int(size[0]), arr_time[0], [email[0]]]

    def scan_mails(self, lines):
        qline = []
        for line in lines:
            if re.match(self.patt_id, line) and len(line)>13:
                qline.append(self.parser(line))
            elif re.match('^\s', line):
                ex_email = re.search(self.patt_email, line)
                # print(ex_email)
                if ex_email != None:
                    qline[-1][3].append(ex_email[0])
            #pprint.pprint(qline)

        return [i for i in qline if len(i[3])>10]

    def write_log(self, etalon, to_del):
            if not os.path.exists(self.log_path):
                os.mknod(self.log_path)
            f = open(self.log_path, 'a')
            if etalon == None and to_del == []:
                f.write('[NO BUGS]')
                f.write('\n')
            else:
                f.write('[KEEP]: {0}'.format(etalon))
                f.write('\n')
                f.write('[DELETE]: {0}'.format([i for i in to_del]))
                f.write('\n')

    def debug(self):
        potential_bugs = self.scan_mails(self.lines)
        etalon = None
        to_del = []

        for i in range(len(potential_bugs)-1):
            if potential_bugs[i][3]==potential_bugs[i+1][3] and \
               potential_bugs[i][1]==potential_bugs[i+1][1]:
               if etalon == None:
                   etalon = potential_bugs[i][0]
                   to_del.append(potential_bugs[i+1][0])
                   if i+1 == len(potential_bugs)-1:
                       self.write_log(etalon, to_del)
               else:
                   to_del.append(potential_bugs[i+1][0])
                   if i+1 == len(potential_bugs)-1:
                       self.write_log(etalon, to_del)
            else:
                self.write_log(etalon, to_del)
                to_del = []


data = open('queue_mail_3.txt', 'r')
email_debugger_5000(data).debug()
