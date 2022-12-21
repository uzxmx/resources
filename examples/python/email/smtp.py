#!/usr/bin/env python

import argparse
import sys
import os

import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.message import EmailMessage
import mimetypes

class SMTPCommand:
    def __init__(self):
        self.parser = argparse.ArgumentParser(prog='smtp', description='SMTP utility.')
        self.parser.add_argument('--server', type=str, default='smtp.163.com', help='SMTP server with SSL enabled')
        self.parser.add_argument('-s', '--sender', type=str, default=os.getenv('MAIL_FROM_ADDRESS'), help='Sender email address')
        self.parser.add_argument('-p', '--password', type=str, default=os.getenv('MAIL_PASSWORD'), help='Sender password')
        self.parser.add_argument('--to', type=str, nargs='+', action='extend', required=True, help='One or more receiver email addresses')
        self.parser.add_argument('-t', '--type', type=str, default='text', help='Mail type: text, html, html_with_image, attachment')
        self.parser.add_argument('-a', '--attachment', type=argparse.FileType('rb'), nargs='*', action='extend', help='One or more attachments')

    def run(self, args):
        parsed = self.parser.parse_args(args)

        if not parsed.sender:
            print('A sender email address is required by `-s`')
            sys.exit(1)
        self.sender = parsed.sender

        if not parsed.password:
            print('A sender password is required by `-p`')
            sys.exit(1)
        self.password = parsed.password

        self.receivers = parsed.to

        self.smtp = smtplib.SMTP_SSL(parsed.server)
        self.smtp.login(self.sender, self.password)

        try:
            if parsed.type == 'text':
                self.send_text()
            elif parsed.type == 'html':
                self.send_html()
            elif parsed.type == 'html_with_image':
                self.send_html_with_image()
            elif parsed.type == 'attachment':
                if not parsed.attachment or len(parsed.attachment) == 0:
                    print('One or more attachments are required by `-a`')
                    sys.exit(1)
                self.send_attachment(parsed.attachment)
            else:
                print('Unsupported mail type: %s' % parsed.type)
        finally:
            self.smtp.quit()

    def send_text(self):
        msg = MIMEText('Test content', 'plain', 'utf-8')
        msg['Subject'] = Header('Test Subject', 'utf-8')
        msg['From'] = Header(self.sender, 'utf-8')
        msg['To'] = Header(', '.join(self.receivers), 'utf-8')

        self.smtp.sendmail(self.sender, self.receivers, msg.as_string())

    def send_html(self):
        html = '''<p>foo</p>
        <p>bar</p>
        <a href="http://www.baidu.com">link</a>
        '''
        msg = MIMEText(html, 'html', 'utf-8')
        msg['Subject'] = Header('Test Subject', 'utf-8')
        msg['From'] = Header(self.sender, 'utf-8')
        msg['To'] = Header(', '.join(self.receivers), 'utf-8')

        self.smtp.sendmail(self.sender, self.receivers, msg.as_string())

    def send_attachment(self, attachments):
        msg = EmailMessage()
        msg.set_content('Test content')

        for e in attachments:
            ctype, encoding = mimetypes.guess_type(e.name)
            if ctype is None or encoding is not None:
                # No guess could be made, or the file is encoded (compressed), so
                # use a generic bag-of-bits type.
                ctype = 'application/octet-stream'
            maintype, subtype = ctype.split('/', 1)
            msg.add_attachment(e.read(), maintype=maintype, subtype=subtype, filename=e.name)

        msg['Subject'] = 'Test Subject'
        msg['From'] = self.sender
        msg['To'] = ', '.join(self.receivers)

        self.smtp.sendmail(self.sender, self.receivers, msg.as_string())

    def send_html_with_image(self):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = 'Test Subject'
        msg['From'] = self.sender
        msg['To'] = ', '.join(self.receivers)

        html = '''<p>HTML with embeded image</p>
        <p><img decoding="async" src="cid:image1"></p>
        '''
        msg.attach(MIMEText(html, 'html', 'utf-8'))

        with open('attachment2.png', 'rb') as f:
            image = MIMEImage(f.read())

        image.add_header('Content-ID', '<image1>')
        msg.attach(image)

        self.smtp.sendmail(self.sender, self.receivers, msg.as_string())

if __name__ == '__main__':
    SMTPCommand().run(sys.argv[1:])
