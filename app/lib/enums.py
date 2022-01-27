from enum import Enum


class PENDING(Enum):

    STATUS_DONE = 0  # 0 交易完成
    STATUS_TRADING = 1  # 1 交易进行中
    STATUS_REVOKE = 2  # 2 交易取消
    STATUS_REJECT = 4  # 3 交易拒绝
