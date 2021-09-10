import csv

from app import db
from models.pokemon import Pokemon
from utils.paths import CSV_PATH


def load_data():
    """
    Read the csv file and save the data in DB
    """
    csv_name = CSV_PATH
    column_names = True
    with open(csv_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if column_names:
                column_names = False
                continue
            pokemon = Pokemon(
                number=int(row[0]),
                name=row[1],
                type1=row[2],
                type2=row[3],
                total=int(row[4]),
                hp=int(row[5]),
                attack=int(row[6]),
                defense=int(row[7]),
                speed_atk=int(row[8]),
                speed_def=int(row[9]),
                speed=int(row[10]),
                generation=int(row[11]),
                legendary=row[12] == 'True',
            )
            db.session.add(pokemon)

    db.session.commit()


db.create_all()

load_data()
