from app import db


class Pokemon(db.Model):
    # ,Name,Type 1,Type 2,Total,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed,Generation,Legendary
    __tablename__ = 'pokemon'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String, nullable=False)
    type1 = db.Column(db.String, nullable=False)
    type2 = db.Column(db.String, nullable=True)
    total = db.Column(db.Integer, nullable=False)
    hp = db.Column(db.Integer, nullable=False)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    speed_atk = db.Column(db.Integer, nullable=False)
    speed_def = db.Column(db.Integer, nullable=False)
    speed = db.Column(db.Integer, nullable=False)
    generation = db.Column(db.Integer, nullable=False)
    legendary = db.Column(db.Boolean, nullable=False)

    def __init__(self, number, name, type1, type2, total, hp, attack, defense, speed_atk,
                 speed_def, speed, generation, legendary):
        self.number = number
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.total = total
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed_atk = speed_atk
        self.speed_def = speed_def
        self.speed = speed
        self.generation = generation
        self.legendary = legendary

    def __repr__(self):
        return f'Pokemon({self.number},{self.name})'

    def __str__(self):
        return self.name
