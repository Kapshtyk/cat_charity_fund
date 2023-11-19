from sqlalchemy import Column, String, Text

from app.models.mixins import CommonFields


class CharityProject(CommonFields):
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text, nullable=False)

    def __repr__(self):
        return f"""
            Благотворительный проект {self.name} на сумму {self.full_amount}. 
            Остаток - {self.full_amount - self.invested_amount}.
            """
