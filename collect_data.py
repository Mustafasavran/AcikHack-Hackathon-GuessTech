import email
import imaplib
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-m", "--mail", type=str,
	              help="gmail adresi")
ap.add_argument("-s", "--sifre", type=str,
	help="gmail şifresi")
args = vars(ap.parse_args())
harfler = ["ş","ç","ğ"," ve "," ya da "]
def check(body):
  for i in harfler:
    if i in body:
      return True
  return False
mail = imaplib.IMAP4_SSL('imap.gmail.com')
(retcode, capabilities) = mail.login(args["mail"],args["sifre"])
mail.list()
mail.select('inbox')

n=0
(retcode, messages) = mail.search(None, '(Flagged)') #Starlı mailler için Flagged hepsi için ALL kullanılmalı
if retcode == 'OK':

   for num in messages[0].split() :
      
      n=n+1
      typ, data = mail.fetch(num,'(RFC822)')
      for response_part in data:
         if isinstance(response_part, tuple):
             original = email.message_from_bytes(response_part[1])

             raw_email = data[0][1]
             raw_email_string = raw_email.decode('utf-8')
             email_message = email.message_from_string(raw_email_string)
             for part in email_message.walk():
                        if (part.get_content_type() == "text/plain"): 
                              body = part.get_payload(decode=True)
                              save_string = str("mailler" + ".txt" )
                              try:
                                body = body.decode('utf-8')
                                
                                if check(body):
                                  
                                  myfile = open(save_string, 'a')          
                                  myfile.write(body)
                                  
                                  myfile.close()
                              except:
                                pass
                        else:
                              continue
                              

             typ, data = mail.store(num,'+FLAGS','\\Seen')

