from aiogram import Bot, Dispatcher, executor, types
from datetime import datetime
import os
import pymysql
import time
import re


token = os.environ.get('token')
ip_db = os.environ.get('ip_db')
login_db =  os.environ.get('login_db')
password_db = os.environ.get('password_db')
name_db = os.environ.get('name_db')
