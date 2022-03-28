'''#file handiling

#read,write,append,fetching all data in one file & to print image.

file = open("coin.jpg","rb")

f1=open("mypic.jpg","wb")

for i in file:
    f1.write(i)'''
    
import smtplib
try:
    #Create your SMTP session
    smtp = smtplib.SMTP('smtp.gmail.com', 587)

   #Use TLS to add security
    smtp.starttls()

    #User Authentication
    smtp.login("sabarialovableman@gmail.com","sabarichella@8588")

    #Defining The Message
    message = "Message_you_need_to_send"

    #Sending the Email
    smtp.sendmail("sabarialovableman@gmail.com", "cibinishanths@gmail.com",message)

    #Terminating the session
    smtp.quit()
    print ("Email sent successfully!")

except Exception as ex:
    print("Something went wrong....",ex)


    
    



