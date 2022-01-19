from sqlalchemy import Column, String, Integer
from .base import Base


class Drift(Base):
    """
    请求赠送的字段信息
    """

    # 赠送人信息
    # 赠送人姓名/id
    giver_name = Column(String(20), nullable=False)
    giver_id = Column(Integer(), nullable=False)

    # 请求者信息
    # 请求者姓名/id
    supplicant_name = Column(String(20), nullable=False)
    supplicant_id = Column(Integer(), nullable=False)
    adrress = Column(String(50), nullable=False)
    mobile = Column(String(20), nullable=False)
    recipient_name = Column(String(20), nullable=False)
    message = Column(String())

    # 书籍信息
    # isbn
    isbn = Column(String(50), nullable=False)

    # 交易的状态
    pending = Column(Integer(), nullable=False)







