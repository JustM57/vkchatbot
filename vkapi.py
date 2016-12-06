import config as cn
import vk
import time
import sqlite3

session = vk.AuthSession(app_id=cn.vk_client_id, user_login=cn.user_mail, user_password=cn.user_pswd, scope=cn.vk_scope)
api = vk.API(session, v='5.60')
nol = 0

conn = sqlite3.connect('outbox_messages.db')
c = conn.cursor()
for i in range(1644):
    response = api.messages.get(out=1, offset=i*200, count=200)
    messages = response['items']
    print("обработано исходящих ", i*200)
    for j in range(200):
        if (messages[j]['user_id']>0) and (messages[j]['body']!=''):
            c.execute("INSERT INTO messages (id,in_id,user_id,msg_date,message) VALUES (?,?,?,?,?)",(messages[j]['id'],nol,messages[j]['user_id'],messages[j]['date'],messages[j]['body']))
            conn.commit()
    if (i % 3) == 2:
        time.sleep(1)
c.close()
conn.close()

conn = sqlite3.connect('imbox_messages.db')
c = conn.cursor()
for i in range(1644):
    response = api.messages.get(out=0, offset=i*200, count=200)
    messages = response['items']
    print("обработано исходящих ", i*200)
    for j in range(200):
        if (messages[j]['user_id']>0) and (messages[j]['body']!=''):
            c.execute("INSERT INTO messages (id,out_id,user_id,msg_date,message) VALUES (?,?,?,?,?)",(messages[j]['id'],nol,messages[j]['user_id'],messages[j]['date'],messages[j]['body']))
            conn.commit()
    if (i % 3) == 2:
        time.sleep(1)
c.close()
conn.close()
