'''
Copyright (C) 2017-2021  Bryant Moscon - bmoscon@gmail.com

Please see the LICENSE file for the terms and conditions
associated with this software.
'''
import os

from cryptofeed import FeedHandler
from cryptofeed.callback import OrderInfoCallback, FillsCallback
from cryptofeed.defines import ORDER_INFO, FILLS
from cryptofeed.exchanges import FTX

async def order_info(**kwargs):
    print(f"Order Update for {kwargs['feed']}")
    print(kwargs)

async def fills(**kwargs):
    print(f"Fills Update for {kwargs['feed']}")
    print(kwargs)


def main():
    f = FeedHandler()
    f.add_feed(FTX(channels=[ORDER_INFO, FILLS], callbacks={ORDER_INFO: OrderInfoCallback(order_info),
                                                            FILLS: FillsCallback(fills)},
                   config={'ftx': {'key_id': os.environ['key'], 'key_secret': os.environ['secret']}}))
    f.run()


if __name__ == '__main__':
    main()
