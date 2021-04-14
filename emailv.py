import requests
# import smtplib
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
counter=0
def check(emaillist):
    temp_all=[] # temp_all[[valid_emails],[invalid_emails]]
    temp_invalid=[]
    temp_valid=[]
    for mail in emaillist:
        try:
            url = 'PASTE THE URL OF THE WEBSITE YOU ARE USING TO VALIDATE THE EMAIL'
            myobj = {"email":str(mail)}
            x = requests.post(url, data = myobj)
            condition=x.json()['email']['valid']
            # print("Email : ",email," is ",condition)
        except:
            print("Something Went Wrong")
            condition=False
            f7=open("error.txt",'a')
            f7.write(str(temp_valid))
            f7.close()
        if(condition):
            temp_valid.append(mail)
        else:
            temp_invalid.append(mail)
    temp_all.append(temp_valid)
    temp_all.append(temp_invalid)
    return temp_all



#1280 emails at max
#160 domains at max
#
combo=['support@','contact@',LIKE THIS YOU CAN ALSO WRITE MORE PREFIXES OF EMAIL YOU WANT TO CREATE FOR MULTIPLE DOMAINS]
all_emails=[]# list of combos of sites
valid_emails=[]
invalid_sites=[]
f1=open('data.txt','r')
list_domains=f1.read().splitlines()
for site in list_domains: #
    temp=[] #this list will intialize whenever we will move to new site
    for prefix in combo:
        temp.append(prefix+site)
    all_emails.append(temp)

for combolist in all_emails: #[[],[]]
    counter=counter+1
    print("Checking Site :",counter)
    temp_all_list=check(combolist) #[[valids][invalid]]
    temp_list=temp_all_list[0]
    temp_ilist=temp_all_list[1] #["aasdd,sd"]
    if(len(temp_list)<8 and len(temp_list)>0):
        valid_emails.append(temp_list)
    elif(len(temp_list)==8):
        invalid_sites.append(temp_list[0])
    else:
        if(len(temp_ilist)>0):
            invalid_sites.append(temp_ilist[0])


print("Total Domains Provided : ",len(all_emails))
print("Total Valid Sites :",len(valid_emails))
print("Total Invalid Sites :",len(invalid_sites))
print("Emails List Below : ",valid_emails)
print("Emails Invalid List Below",invalid_sites)
# def send(dest,senderemail):
#     s = smtplib.SMTP('smtp.gmail.com', 587)
#     s.starttls()
#     s.login(senderemail,"Password")
#     message ="""
#     Write the message here"""

#     s.sendmail(senderemail,dest, message)
#     s.quit()
#     print("Email Sent")
def send(dest,senderemail):
    message = MIMEMultipart("alternative")
    message["Subject"] = "WRITE THE SUBJECT OF THE EMAIL YOU ARE SENDING"
    message["From"] = senderemail
    message["To"] = dest

# Create the plain-text and HTML version of your message
    text = """\
WRITE THE BODY OF THE EMAIL"""

    part1 = MIMEText(text, "plain")

    message.attach(part1)


# Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(senderemail, "PASSWORD OF THE EMAIL ID YOU ARE USING TO SEND THE EMAILS")
        server.sendmail(
        senderemail, dest, message.as_string()
    )


#valid_emails=[[]]
def begin():
    email_sent=0
    for li_site in valid_emails: #valid_emails= [['contact@boxtal.org'], ['admin@boxxed.com','ABC@boxxed.com]]
        for dest in li_site:
            email_sent=email_sent+1
            if(email_sent==560):
                print("All Emails Exhauseted")
                f8=open("last.txt",'r')
                f8.write(str(dest))
                f8.close()
            print("Email Sent",email_sent)
            if(email_sent>=0 and email_sent<=80):
                try:
                    send(dest,"1ST EMAIL YOU ARE USING TO SEND EMAILS")
                except:
                    f5=open('error_email.txt','a')
                    f5.write("Something Went Wrong Sending Email 1ST EMAIL YOU ARE USING TO SEND EMAILS ")
                    f5.close
                    print("Something Went Wrong Sending Email 1ST EMAIL YOU ARE USING TO SEND EMAILS ")
            elif(email_sent>80 and email_sent <=160):
                try:
                    send(dest,"2ND EMAIL YOU ARE USING TO SEND EMAILS")
                except:
                    f5=open('error_email.txt','a')
                    f5.write("Something Went Wrong Sending Email 2ND EMAIL YOU ARE USING TO SEND EMAILS ")
                    f5.close
                    print("Something Went Wrong Sending Email 2ND EMAIL YOU ARE USING TO SEND EMAILS ")
            elif(email_sent>160 and email_sent<=240):
                try:
                    send(dest,"3RD EMAIL YOU ARE USING TO SEND EMAILS")
                except:
                    f5=open('error_email.txt','a')
                    f5.write("Something Went Wrong Sending Email 3RD EMAIL YOU ARE USING TO SEND EMAILS ")
                    f5.close
                    print("Something Went Wrong Sending Email 3RD EMAIL YOU ARE USING TO SEND EMAILS")
            elif(email_sent>240 and email_sent<=320):
                try:
                    send(dest,"4TH EMAIL YOU ARE USING TO SEND EMAILS")
                except:
                    f5=open('error_email.txt','a')
                    f5.write("Something Went Wrong Sending Email 4TH EMAIL YOU ARE USING TO SEND EMAILS ")
                    f5.close
                    print("Something Went Wrong Sending Email 4TH EMAIL YOU ARE USING TO SEND EMAILS")
            elif(email_sent>320 and email_sent<=400):
                try:
                    send(dest,"5TH EMAIL YOU ARE USING TO SEND EMAILS")
                except:
                    f5=open('error_email.txt','a')
                    f5.write("Something Went Wrong Sending Email 5TH EMAIL YOU ARE USING TO SEND EMAILS")
                    f5.close
                    print("Something Went Wrong Sending Email 5TH EMAIL YOU ARE USING TO SEND EMAILS ")

            elif(email_sent>400 and email_sent<=480):
                try:
                    send(dest,"6TH EMAIL YOU ARE USING TO SEND EMAILS")
                except:
                    f5=open('error_email.txt','a')
                    f5.write("Something Went Wrong Sending Email 6TH EMAIL YOU ARE USING TO SEND EMAILS ")
                    f5.close
                    print("Something Went Wrong Sending Email 6TH EMAIL YOU ARE USING TO SEND EMAILS ")
            elif(email_sent>480 and email_sent<=560):
                try:
                    send(dest,"7TH EMAIL YOU ARE USING TO SEND EMAILS")
                except:
                    f5=open('error_email.txt','a')
                    f5.write("Something Went Wrong Sending Email 7TH EMAIL YOU ARE USING TO SEND EMAILS ")
                    f5.close
                    print("Something Went Wrong Sending Email 7TH EMAIL YOU ARE USING TO SEND EMAILS ")
            elif(email_sent>560 and email_sent<=640):
                try:
                    send(dest,"8TH EMAIL YOU ARE USING TO SEND EMAILS")
                except:
                    f5=open('error_email.txt','a')
                    f5.write("Something Went Wrong Sending Email 8TH EMAIL YOU ARE USING TO SEND EMAILS ")
                    f5.close
                    print("Something Went Wrong Sending Email 8TH EMAIL YOU ARE USING TO SEND EMAILS ")
            elif(email_sent>640 and email_sent<=720):
                try:
                    send(dest,"9TH EMAIL YOU ARE USING TO SEND EMAILS")
                except:
                    f5=open('error_email.txt','a')
                    f5.write("Something Went Wrong Sending Email 9TH EMAIL YOU ARE USING TO SEND EMAILS ")
                    f5.close
                    print("Something Went Wrong Sending Email 9TH EMAIL YOU ARE USING TO SEND EMAILS ")
            elif(email_sent>720 and email_sent<=800):
                try:
                    send(dest,"10TH EMAIL YOU ARE USING TO SEND EMAILS")
                except:
                    f5=open('error_email.txt','a')
                    f5.write("Something Went Wrong Sending Email 10TH EMAIL YOU ARE USING TO SEND EMAILS ")
                    f5.close
                    print("Something Went Wrong Sending Email 10TH EMAIL YOU ARE USING TO SEND EMAILS ")





f4=open('valid_emails.txt','a')
f4.write(str(valid_emails))
f4.close()
f5=open('invalid_sites.txt','a')
f5.write(str(invalid_sites))
f5.close()
print("Sending Emails Beginning")
try:
    begin()
except:
    print("Something Went Wrong")