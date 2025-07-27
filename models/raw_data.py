# Models raw_data contenant les données brutes

from sqlalchemy import Column, Integer, String, Float, Date
from .base import Base

class Raw_data(Base):
    __tablename__ = "raw_data"

    # Clé primaire auto-incrémentée (bonne pratique)
    id = Column(Integer, primary_key=True, index=True)

    # Colonnes mappées depuis le DataFrame
    nom = Column(String)
    prenom = Column(String)
    age = Column(Integer)
    taille = Column(Float)
    poids = Column(Float)
    sexe = Column(String)
    sport_licence = Column(String)
    niveau_etude = Column(String)
    region = Column(String)
    smoker = Column(String) # voir a mettre un bool car oui/non
    nationalite_francaise = Column(String) # voir a mettre un bool car oui/non
    revenu_estime_mois = Column(Float)
    situation_familiale = Column(String)
    historique_credits = Column(Float)
    risque_personnel = Column(Float)
    date_creation_compte = Column(Date)
    score_credit = Column(Float)
    loyer_mensuel = Column(Float)
    montant_pret = Column(Float)
