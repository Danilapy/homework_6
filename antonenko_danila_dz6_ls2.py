with open('nginx_logs.txt', 'r', encoding="utf-8") as logs:
    remote_address_list = [line[:line.find('')] for line in logs]

address_max = max(set(remote_address_list), key=remote_address_list.count)
print(address_max, remote_address_list.count(address_max))