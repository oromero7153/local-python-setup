def hello():
    print('Hello, Oscar')

def pack(watch, wallet, keys):
    return[watch, wallet, keys]


list=['sandwich', 'chips', 'apple']

def eat_lunch(list):
    if len(list) == 0:
        print('My lunch box is empty')
    else:
        for i in range(len(list)):
            if i==0:
                print('First I eat {list[0]}')
            else:
                print('Next I eat {list[i]}')
 
 
hello()
print(pack("watch", "wallet", "keys"))
print(eat_lunch(list))