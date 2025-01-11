# 表结构在这个文件中定义
from exts import db
from datetime import datetime

"""
Integer 整型
String(50) 长度为50的字符串
Text  一段文本
DateTime  表示为 Python datetime 对象的 时间和日期  default=datetime.now
Float 存储浮点值
Boolean 存储布尔值
PickleType 存储为一个持久化的 Python 对象
LargeBinary 存储一个任意大的二进制数据
"""

# for example
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True) # 用户id
    username =  db.Column(db.String(16)) # 用户名
    password = db.Column(db.String(16)) # 密码
    sex = db.Column(db.String(4)) # 性别
    phone_num = db.Column(db.String(16))  # 电话号码
    weight = db.Column(db.Float)  # 体重
    height = db.Column(db.Float)   # 身高
    chestLine = db.Column(db.Float) # 胸围
    waistline = db.Column(db.Float) # 腰围

    def __init__(self, id,username,password, sex, phoneNum, weight,height,chestLine,waistline):
        self.id = id
        self.username = username
        self.password = password
        self.sex = sex
        self.phoneNum = phoneNum
        self.weight = weight
        self.height = height
        self.chestLine = chestLine
        self.waistline = waistline

# TODO: add your table here, and you can delete the User table
