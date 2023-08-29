
from sqlalchemy import Column, String, Text

from app.models.abstract_base import BaseProjectDonation


class CharityProject(BaseProjectDonation):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)
