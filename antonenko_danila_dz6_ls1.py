with open('nginx_logs.txt', 'r', encoding="utf-8") as logs:
    requests_list = []
    for line in logs:
        remote_addr = line[:line.find(' ')]
        request_type = line[line.find('"') + 1:line.find('"') + 4]
        request_resource = line[line.find('/d'):line.find('HTTP') - 1]
        tuple_requests = (remote_addr, request_type, request_resource)
        requests_list.append(tuple_requests)
        print(tuple_requests)

        