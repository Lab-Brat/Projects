import re
import os
import pprint

file = open('queue_mail_1.txt', 'r')
lines = file.readlines()

def parser(line):
    id = re.search(r'^[A-Z0-9]+\*', line)
    size = re.search(r'\s[0-9]+\s', line)
    patt_date = r'[A-Z][a-z][a-z]\s[A-Z][a-z][a-z]\s[\d]+\s'
    patt_time = r'(\d{2}:\d{2}:\d{2})'
    arr_time = re.search(patt_date+patt_time, line)
    email = re.search(r'[a-z.]+@[a-z-]+\.(ru|com)', line)
    return [id[0], int(size[0]), arr_time[0], [email[0]]]

def scan_mails(lines):
    qline = []
    for line in lines:
        if re.match('^[A-Z0-9]', line) and len(line)>13:
            qline.append(parser(line))
        elif re.match('^\s', line):
            ex_email = re.search(r'[a-z.]+@[a-z-]+\.(ru|com)', line)
            if ex_email != None:
                qline[-1][3].append(ex_email[0])

    return [i for i in qline if len(i[3])>10]

def write_log(etalon, to_del):
        if not os.path.exists('/home/oxxo/Downloads/queue_fix/log.txt'):
            os.mknod('/home/oxxo/Downloads/queue_fix/log.txt')
        f = open('log.txt', 'a')
        if etalon == None and to_del == []:
            f.write('[NO BUGS]')
            f.write('\n')
        else:
            f.write('[KEEP]: {0}'.format(etalon))
            f.write('\n')
            f.write('[DELETE]: {0}'.format([i for i in to_del]))
            f.write('\n')

def bug_finder(potential_bugs):
    etalon = None
    to_del = []

    for i in range(len(potential_bugs)-1):
        if potential_bugs[i][3]==potential_bugs[i+1][3] and \
           potential_bugs[i][1]==potential_bugs[i+1][1]:
           if etalon == None:
               etalon = potential_bugs[i][0]
               to_del.append(potential_bugs[i+1][0])
               if i+1 == len(potential_bugs)-1:
                   write_log(etalon, to_del)
           else:
               to_del.append(potential_bugs[i+1][0])
               if i+1 == len(potential_bugs)-1:
                   write_log(etalon, to_del)
        else:
            write_log(etalon, to_del)
            to_del = []


potential_bugs = scan_mails(lines)
bug_finder(potential_bugs)
