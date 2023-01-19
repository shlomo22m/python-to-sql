import targil1
#import pandas
from dotenv import load_dotenv
import dotenv




if __name__ == '__main__':
    t=targil1.Targil1()
    t.connect()
    id=t.id('eli')
    print(id)
    print(t.order_list((10)))
    t.order_sum(t.order_list(t.id('eli')))
    t.closeconnection()