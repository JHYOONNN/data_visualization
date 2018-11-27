import pykorbit
import time
'''
starttime = time.time()
collecting_data = 0
while (b < 10):
    a = pykorbit.get_current_price("BTC")
    print(a)
    time.sleep(2)
    b+=1
'''
class take_bit_coin_price():
    def __init__(self):
        self.price = pykorbit.get_current_price("BTC")
        
    def print_price(self):
        print(self.price)
        
class main():
    def __init__(self):
        self.start_time = time.time()
        self.take_price_for_time()
        
    def take_price_for_time(self):
        count = 0
        while(count < 10):
            self.price_of_bit = take_bit_coin_price()
            self.price_of_bit.print_price()
            time.sleep(5)
            count += 1

if __name__ == "__main__":
    main()