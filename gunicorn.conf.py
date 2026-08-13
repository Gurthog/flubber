bind = '127.0.0.1:8000'

# restart workers after x requests
# defends against memory leaks
max_requests = 500

timeout = 30

workers = 5

worker_class = 'sync'

