"""json-server db.json команда для запуска сервера и доступа к БД"""
import requests, subprocess

import hashlib

url = "http://localhost:3000/users" 
subprocess.call(['json-server', 'db.json'])


def get_req():
    return requests.get(url).json

def post_req(data):
    requests.post(url, json=data)

def check_mail(mail):
    #TODO:Если всё ок, return 'OK'
    return 'OK'

def check_nickname(nick):
    #TODO: Если всё ок, return 'OK'
    return 'OK'

def register(nick, mail, password):
    pass
