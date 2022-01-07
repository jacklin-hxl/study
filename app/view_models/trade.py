

class TradeInfo:

    def __init__(self, trades):
        self.total = 0
        self.trades = []
        self.__parse(trades)

    def __parse(self, trades):
        self.total = len(trades)
        self.trades = [self.__map_to_trade(trade) for trade in trades]

    def __map_to_trade(self, trade):
        create_datetime = trade.create_datetime
        if create_datetime:
            create_datetime = create_datetime.strftime("%Y-%m-%d")
        else:
            create_datetime = "未知"
        return dict(user_name=trade.user.nickname,
                    time=create_datetime,
                    id=trade.id)
