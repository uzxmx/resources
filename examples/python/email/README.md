# Python email examples

## Send emails

```
# Send text message.
./smtp.py --to receiver@example.com

# Send html message.
./smtp.py --to receiver@example.com -t html

# Send html message with image embeded.
./smtp.py --to receiver@example.com -t html_with_image

# Send attachments.
./smtp.py --to receiver@example.com -t attachment -a attachment1.txt -a attachment2.png
```

## Receive emails

To read emails from gmail server, we need to generate an `App Password`. Visit
[here](https://support.google.com/accounts/answer/185833) for how to generate.

```
# Get top 3 emails.
./imap.py -u foo@gmail.com -p "$APP_PASSWORD"

# Get emails by sender and date.
./imap.py -u foo@gmail.com -p "$APP_PASSWORD" --from bar@example.com --since '2022-12-21'
```
