"""
用户身份验证

Version:0.1
Author:李奕成

"""
username = input('请输入用户名：')
password = input('请输入口令：')

#判断身份
if username == "李奕成" and password == "Teno":
    print("身份验证成功！")
else:
    print('身份验证失败！')