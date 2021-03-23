'''
Copyright (C) 2017-2021  Bryant Moscon - bmoscon@gmail.com
Please see the LICENSE file for the terms and conditions
associated with this software.
'''
from cryptofeed import FeedHandler
from cryptofeed.callback import TickerSizeCallback
from cryptofeed.defines import TICKER
from cryptofeed.exchanges import Huobi


async def ticker(feed, symbol, bid, ask, timestamp, receipt_timestamp, bid_size, ask_size):
    print(f'Timestamp: {timestamp} Feed: {feed} Pair: {symbol} Book Bid Size is {bid_size} Ask Size is {ask_size}')


def main():
    fh = FeedHandler()

    callbacks = {TICKER: TickerSizeCallback(ticker)}
    fh.add_feed(Huobi(symbols=['BTC-USDT'], channels=[TICKER], callbacks=callbacks))

    fh.run()


if __name__ == '__main__':
    main()
