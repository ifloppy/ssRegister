import requests
import random
import string
requests.packages.urllib3.disable_warnings()

def GetMiddleStr(content,startStr,endStr):
  startIndex = content.index(startStr)
  if startIndex>=0:
    startIndex += len(startStr)
  endIndex = content.index(endStr)
  return content[startIndex:endIndex]

print("正在初始化薅羊毛脚本，请稍后^_^")

# 此脚本仅供学习，禁止用于非法、商业用途，若发现您购买了某些不良商家的倒卖版本，请要求退款并要求对方公开道歉
# 不要用于薅羊毛，由此脚本造成的一切不良后果均由您自行承担

siteURL="机场地址(例如:https://google.com)"
getEmailURL=siteURL+"/auth/send"



session = requests.session()
session.get(siteURL, verify=False)

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.3538.77 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': siteURL + '/auth/register'
}

email_input = input("请输入您的邮箱:")
email = email_input.split('@')
email = email[0] + '%40' + email[1]

post_data = 'email=' + email
post_data = post_data.encode()

response = session.post(getEmailURL, post_data, headers=headers, verify=False)

print(response.text)

emailCode=input("请输入您收到的邮箱验证码:")

# 脚本作者:iruanp.com

ran_passwd = ''.join(random.sample(string.ascii_letters + string.digits, 16))
ran_wechat = ''.join(random.sample(string.ascii_letters + string.digits, 8))

name_tmp = email.split ("@")
name = name_tmp[0]

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.3538.77 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': siteURL + '/auth/register'
}
post_data = ("email="+email+"&name="+name+
             "&passwd="+ran_passwd+"&repasswd="+
             ran_passwd+"&wechat="+ran_wechat+
             "&imtype=1&code=0&emailcode="+emailCode)
post_data = post_data.encode()
print("正在发送数据:"+str(post_data))
response = session.post(siteURL + '/auth/register', post_data, headers=headers, verify=False)
print(response.text)
print(response)

print("邮箱:"+email)
print("密码:"+ran_passwd)



print("正在尝试登陆到机场...")
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.3538.77 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
}

post_data = 'email=' + email + '&passwd=' + ran_passwd + '&code='
response = session.post(siteURL + '/auth/login', post_data, headers=headers, verify=False)
print(response.text)
print(response)

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.3538.77 Safari/537.36',
    'Content-Type': 'text/html; charset=UTF-8',
    'Referer': siteURL + '/auth/login'
}
response=session.get(siteURL+"/user", headers=headers, verify=False)
print(response)
print(response.text)
sub=GetMiddleStr(response.text, '''<button class="copy-text btn btn-subscription col-xx-12 col-sm-3 col-lg-2" type="button" data-clipboard-text="''', '''">点击复制''')

print("邮箱:"+email_input)
print("密码:"+ran_passwd)
print("订阅:"+str(sub))
print("微信:"+ran_wechat)
