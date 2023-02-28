"""
  _              _      
 | |            (_)     
 | |_ ___   __ _ _ _ __ 
 | __/ _ \ / _` | | '__|
 | || (_) | (_| | | |   
  \__\___/ \__, |_|_|   
            __/ |       
           |___/        
        
    by @kawasaji
    https://github.com/kawasaji/togir

"""

import sys


sys.path.insert(1, 'Package/services')
sys.path.insert(1, 'Package/handler')
sys.path.insert(1, 'Package/photos')
sys.path.insert(1, 'Package')

from math import *

import aiogram
from aiogram import *
from aiogram import Bot, Dispatcher, executor
import sqlite3
import asyncio

from datetime import datetime


API_TOKEN = '5935466932:AAEI3myOJ_5Bv2oDmrSIEwA8AvP9ELVrqjw'

admins = (1058211493)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
conn = sqlite3.connect('chats.db')
cur = conn.cursor()
from db import BotDB
BotDB = BotDB('chats.db')


