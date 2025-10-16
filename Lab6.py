import datetime
data = {}

def main():
    def log_call(add):
    
        def wrapper(*args, **kwargs):
    
            data.update({
            "call_time":datetime.datetime.now().strftime("%X"),
            "fun_name":"add",
            "arguments":args
            })
            
            return add(*args, **kwargs)
        
        return wrapper
    
    
    
    @log_call
    def add(a, b):
        return a / b
    
    print(add(4778, 54))
    
    
    print(data)


if __name__ == '__main__':
    main()
