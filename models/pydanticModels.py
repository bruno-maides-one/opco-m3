#
# Module contenant les modèles pydantic pour la gestion des prêts
# Ces classes sont utilisées pour la validation des données d'un formulaire de demande de prêt
# On utilise le sqlalchemy_to_pydantic pour créer automatique les classe pydantique depuis les modèles
#
from typing import Optional

from pydantic import BaseModel
from datetime import date
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from models import Client, Niveau_etude, Pret, Region

pdtClientBase = sqlalchemy_to_pydantic(Client)
class pdtClient(pdtClientBase):
    id: Optional[int] = None

pdtPretBase = sqlalchemy_to_pydantic(Pret)
class pdtPret(pdtPretBase):
    num_pret: Optional[int] = None

pdtRegion = sqlalchemy_to_pydantic(Region)

pdtNiveauEtude = sqlalchemy_to_pydantic(Niveau_etude)

