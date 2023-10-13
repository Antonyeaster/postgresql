from sqlalchemy import (
    create_engine, Column, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from the localhost "chinook" db
db = create_engine("postgresql:///chinook")
base = declarative_base()


# creat a class based-model for the programmer table
# class Programmer(base):
#     __tablename__ = "Programmer"
#     id = Column(Integer, primary_key=True)
#     first_name = Column(String)
#     last_name = Column(String)
#     gender = Column(String)
#     nationality = Column(String)
#     famous = Column(String)


class FavouriteCountries(base):
    __tablename__ = "Countries"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    capital_city = Column(String)
    population = Column(Integer)

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)

# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# creating records for our favourite country records

new_zealand = FavouriteCountries(
    name="New Zealand",
    capital_city="Auckland",
    population=5000000
)


romania = FavouriteCountries(
    name="Romania",
    capital_city="Bucharest",
    population=19000000
)


cook_islands = FavouriteCountries(
    name="Cook Island",
    capital_city="Rarotonga",
    population=14123
)

# creating records on our Programmer table

# ada_lovelace = Programmer(
#     first_name="Ada",
#     last_name="Lovelace",
#     gender="F",
#     nationality="British",
#     famous="First Programmer"
# )


# alan_turning = Programmer(
#     first_name="Alan",
#     last_name="Turning",
#     gender="M",
#     nationality="British",
#     famous="Modern Computing"
# )


# grace_hopper = Programmer(
#     first_name="Grace",
#     last_name="Hopper",
#     gender="F",
#     nationality="American",
#     famous="COBAL language"
# )


# margaret_hamilton = Programmer(
#     first_name="Margaret",
#     last_name="Hamilton",
#     gender="F",
#     nationality="American",
#     famous="Apollo 11"
# )


# bill_gates = Programmer(
#     first_name="Bill",
#     last_name="Gates",
#     gender="M",
#     nationality="American",
#     famous="Microsoft"
# )


# tim_berners_lee = Programmer(
#     first_name="Tim",
#     last_name="Berners-Lee",
#     gender="M",
#     nationality="British",
#     famous="World Wide Web"
# )


# antony_easter = Programmer(
#     first_name="Antony",
#     last_name="Easter",
#     gender="M",
#     nationality="British",
#     famous="Being Ginger"
# )


# add each instance of our programmers to our session
# session.add(ada_lovelace)
# session.add(alan_turning)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(antony_easter)
# session.add(new_zealand)
# session.add(romania)
# session.add(cook_islands)




# commit the session to the database
session.commit()

# updating a single record
# programmer = session.query(Programmer).filter_by(id=9).first()
# programmer.famous = "Eating loads of food"


# updating multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()


# deleting a single record
# fname = input("Enter a first name ")
# lname = input("Enter a last name ")
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# # defensive programming
# if programmer is not None:
#     print("Programmer found ", programmer.first_name + " " + programmer.last_name)
#     confirmation = input("Are you sure you want to delete this record? (y/n)")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted")
#     else:
#         print("Programmer not deleted")
# else:
#     print("No records found")

country_name = input("Enter country name ")
country = session.query(FavouriteCountries).filter_by(name=country_name).first()
if country is not None:
    print("Country found ", country.name)
    confirmation = input("Are you sure you want to delete this record? (y/n)")
    if confirmation.lower() == "y":
        session.delete(country)
        session.commit()
        print("Country has been deleted")
    else:
        print("Country not deleted")
else:
    print("No records found")

# query the database to find all Programmers
# programmers = session.query(Programmer)
# for programmer in programmers:
#     print(
#         programmer.id,
#         programmer.first_name + " " + programmer.last_name,
#         programmer.gender,
#         programmer.nationality,
#         programmer.famous,
#         sep=" | "  
#     )


countries = session.query(FavouriteCountries)
for country in countries:
    print(
        country.id,
        country.name,
        country.capital_city,
        country.population,
        sep=" | "
    )