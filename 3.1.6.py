Name = "Max Mustermann"
Alter = 30
Geschlecht = "männlich"
Größe_in_m = 1.80
Gewicht_in_KG = 75
Augenfarbe = "braun"
Haarfarbe = "schwarz"
Beruf = "Softwareentwickler"
Hobby = "Lesen"
Charaktereigenschaften = "freundlich"

print(
    Name
    + "ist ein "
    + str(Alter)
    + "-jähriger, "
    + Charaktereigenschaften
    + "er Softwareentwickler mit "
    + Augenfarbe
    + "en Augen und "
    + Haarfarbe
    + "en Haaren, der "
    + str(Größe_in_m)
    + "m groß ist, "
    + str(Gewicht_in_KG)
    + "kg wiegt, "
    + Hobby
    + " als Hobby hat und "
    + Geschlecht
    + " ist."
)

band_name = "Metallica"
genre = "Heavy Metal"
founded_year = 1981
origin_country = "USA"
members = ["James Hetfield", "Lars Ulrich", "Kirk Hammett", "Robert Trujillo"]
most_famous_album = "Master of Puppets"
active = True

print(
    f"{band_name} is a {genre} band founded in {founded_year} in the {origin_country} that consists of the members: {", ".join(members)} which are still active and famous for the album: {most_famous_album}."
)
