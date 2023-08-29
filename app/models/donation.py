from sqlalchemy import Column, ForeignKey, Integer, Text

from app.models.abstract_base import BaseProjectDonation


class Donation(BaseProjectDonation):
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)
