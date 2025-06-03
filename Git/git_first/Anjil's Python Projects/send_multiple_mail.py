import smtplib as s
ob=s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login("user_mail", "password")
subject="leave application"
body="Dear sir, how are you?"
message="subject:{}\n\n{}".format(subject,body)
listadd=["receivermail","receivermail1"]
ob.sendmail("usermail",listadd,message)
print("sendmail")
ob.quit()