# Models de pret

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

# Region
class Region(Base):
    __tablename__ = "region"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String)

    # Relations
    prets = relationship("Pret", back_populates="region")
