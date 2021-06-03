import re
import os
import pprint

class email_debugger_5000():
    def __init__(self, data):
        self.data = data
        self.lines = data.readlines()
        self.patt_id = '^[A-Z0-9]+\*'
        self.patt_size = r'\s[0-9]+\s'
        self.patt_date = r'[A-Z][a-z][a-z]\s[A-Z][a-z][a-z]\s[\d]+\s'
        self.patt_time = r'(\d{2}:\d{2}:\d{2})'
        self.patt_email = r'[a-z.]+@[a-z-]+\.(ru|com)'
        self.log_path = '/home/oxxo/Downloads/queue_fix/log.txt'

    def parser(self, line):
        ''' Parse a line of text, return ID, size, time and email '''
        ID = re.search(self.patt_id, line)
        size = re.search(self.patt_size, line)
        arr_time = re.search(self.patt_date+self.patt_time, line)
        email = re.search(self.patt_email, line)

        return [ID[0], int(size[0]), arr_time[0], [email[0]]]

    def scan_mails(self, lines):
        ''' Scan a file line by line, output emails that have 10+ recipients '''
        qline = []
        for line in lines:
            if re.match(self.patt_id, line) and len(line)>13:
                qline.append(self.parser(line))
            elif re.match('^\s', line):
                ex_email = re.search(self.patt_email, line)
                if ex_email != None:
                    qline[-1][3].append(ex_email[0])

        return [i for i in qline if len(i[3])>10]

    def write_log(self, etalon, to_del):
        ''' Writes program output to a log file '''
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

    def find_diff(self, em_1, em_2):
        ems_1 = set(em_1[3])
        ems_2 = set(em_2[3])
        differences = (ems_1-ems_2).union(ems_2-ems_1)

        total = len(em_1[3]) + len(em_2[3])
        percentage = (len(differences)/total)*100
        return differences, percentage, total

    def debug(self, diff_output=False):
        ''' Get the list of potentially buggy emails and search it for bugs'''
        potential_bugs = self.scan_mails(self.lines)
        etalon = None
        to_del = []

        for i in range(len(potential_bugs)-1):
            em_current, em_next = potential_bugs[i], potential_bugs[i+1]
            diff, perc, tot = self.find_diff(em_current, em_next)

            if em_current[3]==em_next[3] or perc < 5 and em_current[1]==em_next[1]:
               if etalon == None:
                   etalon = em_current[0]
                   to_del.append(em_next[0])
                   if i+1 == len(potential_bugs)-1:
                       self.write_log(etalon, to_del)
               else:
                   to_del.append(em_next[0])
                   if i+1 == len(potential_bugs)-1:
                       self.write_log(etalon, to_del)
            else:
                self.write_log(etalon, to_del)
                etalon = None
                to_del = []

            if diff_output==True:
                print('Differences are: ')
                pprint.pprint(diff)
                print("in {0} emails, {1:.2f}% are different".format(tot,perc))

            print('\n')
            print("check the log file here: {0}".format(self.log_path))
            print('\n')

if __name__ == "__main__":
    # queue = input("Please enter the file name of your queue: ")
    queue = 'queue_mail_1.txt'
    data = open(queue, 'r')
    email_debugger_5000(data).debug(diff_output=True)
