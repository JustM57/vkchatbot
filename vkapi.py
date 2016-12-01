import config as cn
import vk
import json
import time

session = vk.AuthSession(app_id=cn.vk_client_id, user_login=cn.user_mail, user_password=cn.user_pswd, scope=cn.vk_scope)
api = vk.API(session, v='5.60')
with open('/home/justm/PycharmProjects/vkchatbot/messages.json', mode='w') as f:
    i = 0
    while i < 2:
        json.dump(api.messages.get(out=1, count=1, offset=(200*i)), f)
        f.write(',\n')
        i += 1
        if (i % 3) == 2:
            time.sleep(1)
with open('/home/justm/PycharmProjects/vkchatbot/messages.json', mode='r') as f:
    print(json.load(f))

