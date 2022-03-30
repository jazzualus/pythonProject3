#Sukurti programą, kuri:

#•Leistų įvesti darbuotojus: vardą, pavardę, gimimo datą, pareigas, atlyginimą, nuo kada dirba (data būtų nustatoma automatiškai,
# pagal dabartinę datą).
#•Duomenys būtų saugomi duomenų bazėję, panaudojant SQLAlchemy ORM (be SQL užklausų)
#•Vartotojas galėtų įrašyti, peržiūrėti, ištrinti ir atnaujinti darbuotojus.
import datetime

from main import engine, Darbuotojai
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

while True:
    pasirinkimas = int(input("""Pasirinkite veiksma:
    1 - Ivesti darbuotojus
    2 - Perziureti darbuotojus
    3 - Istrinti darbuotojus
    4 - Atnaujinti darbuotojus"""))

    if pasirinkimas == 1:
        vardas = input("Iveskite darbuotojo varda")
        pavarde = input("Iveskite darbuotojo pavarde")
        gim_data = input("Iveskite gimimo data: YYYY-MM-DD")
        ivesta_gim_data = datetime.datetime.strptime(gim_data, "%Y-%m-%d").date()
        pareigos = input("Iveskite pareigas")
        atlyginimas = input("Iveskite atlyginima")
        darbuotojas = Darbuotojai(vardas, pavarde, ivesta_gim_data, pareigos, atlyginimas)
        session.add(darbuotojas)
        session.commit

    if pasirinkimas == 2:
        darbuotojas = session.query(Darbuotojai).all()
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
        for darbuotojas in darbuotojas:
            print(darbuotojas)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>")

    if pasirinkimas == 3:
        darbuotojas = session.query(Darbuotojai).all()
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
        for darbuotojas in darbuotojas:
            print(darbuotojas)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
        trinamo_id = int(input("Pasirinkite trinamo darbuotojo ID"))
        trinamas_darbuotojas = session.query(Darbuotojai).get(trinamo_id)
        session.delete(trinamas_darbuotojas)
        session.commit()

    if pasirinkimas == 4:
        darbuotojas = session.query(Darbuotojai).all()
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
        for darbuotojas in darbuotojas:
            print(darbuotojas)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
        keiciamo_id = int(input("Pasirinkite keiciamo darbuotojo ID"))
        keiciamas_darbuotojas = session.query(Darbuotojai).get(keiciamo_id)
        pakeitimas = int(input("Ka norite pakeisti 1 - VARDA, 2 - PAVARDE, 3- GIMIMO DATA, 4 - PAREIGAS, 5 - ATLYGINIMA"))
        if pakeitimas == 1:
            keiciamas_darbuotojas.vardas = input("Iveskite nauja varda")
        if pakeitimas == 2:
            keiciamas_darbuotojas.pavarde = input("Iveskite nauja pavarde")
        if pakeitimas ==3:
            keiciamas_darbuotojas.gim_data = input("Iveskite nauja gimimo data")
        if pakeitimas == 4:
            keiciamas_darbuotojas.pareigos = input("Iveskite naujas pareigas")
        if pakeitimas == 5:
            keiciamas_darbuotojas.atlyginimas = input("Iveskite nauja atlyginima")
        session.commit()

