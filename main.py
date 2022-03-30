#Sukurti programą, kuri:

#•Leistų įvesti darbuotojus: vardą, pavardę, gimimo datą, pareigas, atlyginimą, nuo kada dirba (data būtų nustatoma automatiškai,
# pagal dabartinę datą).
#•Duomenys būtų saugomi duomenų bazėję, panaudojant SQLAlchemy ORM (be SQL užklausų)
#•Vartotojas galėtų įrašyti, peržiūrėti, ištrinti ir atnaujinti darbuotojus.

import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///darbuotojai.db')
Base = declarative_base()

class Darbuotojai(Base):
    __tablename__='Darbuotojai'
    id = Column(Integer, primary_key=True)
    vardas = Column("Vardas", String)
    pavarde = Column("Pavarde", String)
    gim_data = Column("Gimimo Data", DateTime, default=datetime.datetime) #reikia suformatuoti string i data
    pareigos = Column("Pareigos", String)
    atlyginimas = Column("Atlyginimas", String)
    nuo_kada_dirba = Column("Dirba nuo", DateTime, default=datetime.datetime.utcnow())

    def __init__(self, vardas, pavarde, gim_data, pareigos, atlyginimas):
        self.vardas = vardas
        self.pavarde = pavarde
        self.gim_data = gim_data
        self.pareigos = pareigos
        self.atlyginimas = atlyginimas

    def __repr__(self):
        return f"{self.id} {self.vardas} {self.pavarde} {self.gim_data} {self.pareigos} {self.atlyginimas} {self.nuo_kada_dirba}"

Base.metadata.create_all(engine)

