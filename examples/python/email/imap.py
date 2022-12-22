#!/usr/bin/env python

import argparse
import sys
import os
import datetime

import email
import imaplib

class IMAPCommand:
    def __init__(self):
        self.parser = argparse.ArgumentParser(prog='imap', description='IMAP utility.')
        self.parser.add_argument('-u', '--username', type=str, help='Username')
        self.parser.add_argument('-p', '--password', type=str, help='Password')
        self.parser.add_argument('--from', dest='from_addr', type=str, help='Filter emails by sender address')
        self.parser.add_argument('--since', type=str, help='Filter emails since some time')

    def run(self, args):
        parsed = self.parser.parse_args(args)

        if not parsed.username:
            print('Username is required by `-s`')
            sys.exit(1)

        if not parsed.password:
            print('Password is required by `-p`')
            sys.exit(1)

        # Ref: https://docs.python.org/3/library/imaplib.html
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(parsed.username, parsed.password)

        res, data = mail.select('INBOX')
        total_count = int(data[0])
        print('Total emails count: %d' % total_count)

        criteria = []
        if parsed.from_addr:
            criteria.append('FROM')
            criteria.append('"%s"' % parsed.from_addr)

        if parsed.since:
            date = datetime.datetime.strptime(parsed.since, '%Y-%m-%d')
            date = date.astimezone(datetime.timezone.utc)
            criteria.append('SINCE')
            criteria.append('"%s"' % date.strftime('%d-%b-%Y'))

        if len(criteria) > 0:
            criteria = ' '.join(criteria)
            print('Search criteria: %s' % criteria)
            res, data = mail.search(None, criteria)
            message_ids = data[0].split()
        else:
            # Get top 3 emails.
            message_ids = [str(i) for i in range(total_count, total_count - 3, -1)]

        for message_id in message_ids:
            print('-' * 50)
            print('Fetching email %d' % int(message_id))
            res, msg = mail.fetch(message_id, '(RFC822)')
            for response in msg:
                if isinstance(response, tuple):
                    msg = email.message_from_bytes(response[1])
                    sender = msg['From']
                    subject = msg['Subject']
                    body = ''
                    temp = msg
                    if temp.is_multipart():
                        html_found = False
                        for part in temp.walk():
                            ctype = part.get_content_type()
                            cdispo = str(part.get('Content-Disposition'))

                            body = part.get_payload(decode=True)
                            if ctype == 'text/html':
                                break
                    else:
                        body = temp.get_payload(decode=True)

                    print()
                    print('From   : ', sender)
                    print('Subject: ', subject)
                    print('Body   : ', body.decode())

        mail.close()
        mail.logout()

if __name__ == '__main__':
    IMAPCommand().run(sys.argv[1:])
