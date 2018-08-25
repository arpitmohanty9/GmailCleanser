import imaplib
# import email
import sys


if sys.argv[1] is not None:
    user_name = sys.argv[1]
if sys.argv[2] is not None:
    password = sys.argv[2]
if sys.argv[3] is not None:
    label = sys.argv[3]
if sys.argv[4] is not None:
    keyword = sys.argv[4]
if sys.argv[5] is not None:
    from_address = sys.argv[5]

ORG_DOMAIN = "@gmail.com"
USER_EMAIL = user_name + ORG_DOMAIN
USER_PWD = password
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993


def trash_mail():
    try:
        mail_server = imaplib.IMAP4_SSL(SMTP_SERVER);
        connection_message = mail_server.login(USER_EMAIL, USER_PWD);
    except imaplib.IMAP4_SSL.error as ex:
        print(ex);
    except imaplib.IMAP4_SSL.abort as ex:
        print(ex);
    except imaplib.IMAP4_SSL.readonly as ex:
        print(ex);
    except Exception as ex:
        print(ex);
    finally:
        print(connection_message);
        print('connection to gmail server successful');

    print('Selecting the gmail label folder as provided by the user');

    # mail_server is the email class object, and we selected the 'inbox' label for the same.
    mail_server.select(label);

    print('searching the mails based on the user given subject / keyword');

    # a specific search can work and collect the needed/selected  mails in the email object.
    if from_address is not None:
        search_status, search_result = mail_server.search(None, '(FROM "%s")' % from_address) ;
    elif keyword is not None :
        search_status, search_result = mail_server.search(None, '(SUBJECT "%s")' % keyword) ;
    else:
        print('A from address or a keyword need to be provided for search')
    #
    if len(search_result[0]) == 0:
        print('No such email found');
    else:
        print('Going to put {} file(s) in the trash folder'.format(len(search_result[0])));
        for mail_id in search_result[0].split():
            mail_server.store(mail_id, '+X-GM-LABELS', '\\Trash');
        mail_server.expunge()


trash_mail()
