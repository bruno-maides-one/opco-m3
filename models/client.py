# Models de pret

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

# Model client
class Client(Base):
    __tablename__ = "client"

    # Clé primaire auto-incrémentée (bonne pratique)
    id = Column(Integer, primary_key=True, index=True)

    # Colonnes mappées depuis le DataFrame
    nom = Column(String)
    prenom = Column(String)
    sexe = Column(String)
    nationalite_francaise = Column(String) # voir a mettre un bool car oui/non

    # Relations
    prets = relationship("Pret", back_populates="client")
