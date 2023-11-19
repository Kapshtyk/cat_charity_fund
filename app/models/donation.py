from sqlalchemy import Column, ForeignKey, Integer, Text

from app.models.mixins import CommonFields


class Donation(CommonFields):
    user_id = Column(Integer, ForeignKey("user.id"))
    comment = Column(Text)

    def __repr__(self):
        return f"""
            Пожертвование {self.id} на сумму {self.full_amount}.
            Остаток - {self.full_amount - self.invested_amount}.
            """
