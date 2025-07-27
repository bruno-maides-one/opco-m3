# Models de pret

from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Pret(Base):
    __tablename__ = "pret"

    # Clé primaire auto-incrémentée (numero de pret)
    num_pret = Column(Integer, primary_key=True, index=True)

    age = Column(Integer)
    taille = Column(Float)
    poids = Column(Float)
    sport_licence = Column(String)
    region = Column(String)
    smoker = Column(String) # voir a mettre un bool car oui/non
    revenu_estime_mois = Column(Float)
    situation_familiale = Column(String)
    historique_credits = Column(Float)
    risque_personnel = Column(Float)
    date_creation_compte = Column(Date)
    score_credit = Column(Float)
    loyer_mensuel = Column(Float)
    montant_pret = Column(Float)

    # Clé étrangère
    # Client
    client_id = Column(Integer, ForeignKey('client.id'))
    client = relationship("Client", back_populates="prets")

    # Region
    region_id = Column(Integer, ForeignKey('region.id'))
    region = relationship("Region", back_populates="prets")

    # Niveau d'étude
    niveau_etude_id = Column(Integer, ForeignKey('niveau_etude.id'))
    niveau_etude = relationship("Niveau_etude", back_populates="prets")

