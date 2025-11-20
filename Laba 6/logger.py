import datetime

log_data = {}   # Словник для збереження логів

def log_call(func):
    def wrapper(*args, **kwargs):
        call_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        log_data[func.__name__] = {
            "time": call_time,
            "args": args,
            "kwargs": kwargs
        }

        return func(*args, **kwargs)

    return wrapper
