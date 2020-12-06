from aiogram import Bot, Dispatcher, executor, types
from datetime import datetime
import os
import pymysql
import time


token = os.environ.get('token')
ip_db = 'ip'
login_db =  'login_db'
password_db = 'password_db'
name_db = 'name_db'
