import imaplib
import email
from email.parser import BytesParser

# Gmail serveri uchun ma'lumotlar
server = 'imap.gmail.com'
port = 993
username = 'your_email@gmail.com'
password = 'your_password'

# Imap serveriga ulanish
mail = imaplib.IMAP4_SSL(server)
mail.login(username, password)

# Oxirgi 5 ta xatni o'qish uchun
mail.select('inbox')
status, messages = mail.search(None, 'ALL')

# Oxirgi 5 ta xatni o'qish
for num in messages[0].split()[-5:]:
    status, data = mail.fetch(num, '(RFC822)')
    raw_email = data[0][1]
    email_message = BytesParser().parsebytes(raw_email)
    print(email_message['Subject'])
```

Kodni ishlatish uchun, `your_email@gmail.com` va `your_password` o'rniga o'zingizning Gmail yoki boshqa serverga kirish ma'lumotlarini kiritishingiz kerak.
