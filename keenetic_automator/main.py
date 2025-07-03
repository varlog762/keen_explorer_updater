from utils import generate_router_ip

login = input('Enter L2TP login: ')
password = input('Enter L2TP password: ')

print(generate_router_ip(login))