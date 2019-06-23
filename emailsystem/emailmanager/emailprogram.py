import smtplib


def email_func(reusername, subject, body):
    """
    author: veenit kumar shukla
    description: send mail to the render
    :param reusername:takes the receivers username
    :param subject: subject of the body
    :param body: elaboration of the subject
    :return: confirmation
    """
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
        return print("mail send")
    except:
        return print("something is wrong")
