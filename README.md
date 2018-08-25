# GmailCleanser
A python script to delete bulk spam mails in gmail

The selection for the email(s) is based on user provided 'From:' email address or a Keyword in the subject line.
e.g. 
    1.The user can select and delete all mails from the promotional sites like ebay and amazon.
      Future scope is to prevent removal of emails which are important forever, like the joining mail with username information.
    2. The user can also provide keywords, like 'Buy', 'Fwd:', which will be selected and sent to Trash Folder.  


params:
-user_name: gmail username
-password: gmail password
-Gmail_label: we can specify the label that may hold the emails, by default I will search in 'Inbox'.
-subject_keyword: any specific keyword you want to identify the mails you want to delete.
-from_address : The targer sending account you want deleted.

usage: python gmailCleanser.py 'arpitmohanty9@gmail.com' 'password' 'Inbox' 'googlealerts-noreply@google.com'
