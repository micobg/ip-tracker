from datetime import datetime

import requests

from notifier import Notifier


def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org')
        return response.text
    except requests.RequestException as e:
        print(f'Error on getting public IP: {e}')
        return None


def read_stored_ip():
    try:
        with open('./store/ip_address.txt', 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        return None


def store_ip(ip):
    with open('./store/ip_address.txt', 'w') as f:
        f.write(ip)


public_ip = get_public_ip()

if public_ip is None:
    exit(1)

stored_ip = read_stored_ip()

if stored_ip is None or stored_ip == '':
    print(f'No stored IP address found. Storing current IP address: {public_ip}')
    store_ip(public_ip)
else:
    if public_ip != stored_ip:
        print(f'IP address has changed: {stored_ip} -> {public_ip} ({datetime.now()})')
        Notifier().message(f'IP address changed: {public_ip}')
        store_ip(public_ip)
    else:
        print(f'IP address unchanged: {public_ip} ({datetime.now()})')
