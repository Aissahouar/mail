from config import HOST,MailBody,USERNAME,PASSWORD,PORT
from email.mime.text import MIMEText
from ssl import create_default_context
from smtplib import SMTP



def send_mail(data:dict | None = None):
    msg = MailBody(**data)
    message = MIMEText(msg.body , "html")
    message["Form"] = USERNAME
    message["To"] = ",".join(msg.to)
    message["Subject"] = msg.Subject
    ctx = create_default_context()
    
    
    try:
        with SMTP(HOST,PORT) as server :
            server.ehlo()
            server.starttls(context=ctx)
            server.ehlo()
            server.login(USERNAME,PASSWORD)
            server.send_message(message)
            server.quit()
        return {"status":200,"errors":None}
    except Exception as e:
        return {"status":500,"errors":e}
    
    
    
    


