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
