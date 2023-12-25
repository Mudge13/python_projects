import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html_file = Path('gpt.html').read_text()
# html_template = Template(html)

email = EmailMessage()
email['from'] = 'Guts'
email['to'] = 'mihir0711shetty@gmail.com'
email['subject'] = 'dont give up'
# email.set_content(html_template.substitute(name='Miyamoto'), 'html')
email.set_content(html_file, 'html')

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("erenyeager1398@gmail.com", 'uhoieesvywwjqwwt')
    smtp.send_message(email)

print("all done")
