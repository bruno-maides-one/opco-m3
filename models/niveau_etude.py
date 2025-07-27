# Models de pret

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

# Niveau d'étude
class Niveau_etude(Base):
    __tablename__ = "niveau_etude"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String)

    # Relations
    prets = relationship("Pret", back_populates="niveau_etude")
