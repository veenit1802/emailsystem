import smtplib


def email_func(reusername, subject, body):
    username = "veenitshukla20@gmail.com"
    password = "@@@veenit@@@"
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(username, password)
        email_text = """
            from:%s
            to:%s
            subject:%s
            body:%s
            """ % (username, reusername, subject, body)
        server.sendmail(username, reusername, email_text)
        server.close()
        print("mail send")
    except:
        print("something is wrong")
