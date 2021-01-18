class Cosmetics:
    def __init__(self, title, brand, size, unit, category, cosmetics_type, care_function=None):
        self.title = title
        self.brand = brand
        self.size = size
        self.unit = unit
        self.category = category
        self.cosmetics_type = cosmetics_type
        self.care_function = care_function

    def about(self):
        return self.title + ', ' + self.brand + ', ' + str(self.size) + self.unit


class Haircare(Cosmetics):
    def __init__(self, title, brand, size, unit, category, cosmetics_type, hair_type, care_function=None):
        super().__init__(title, brand, size, unit, category, cosmetics_type, care_function)
        self.hair_type = hair_type


class Skincare(Cosmetics):
    def __init__(self, title, brand, size, unit, category, cosmetics_type, care_type, bodypart, skin_type,
                 care_function=None):
        super().__init__(title, brand, size, unit, category, cosmetics_type, care_function)
        self.care_type = care_type
        self.bodypart = bodypart
        self.skin_type = skin_type

    def about(self):
        return self.title + ', ' + self.brand + ', ' + str(self.size) + self.unit + ', ' + self.skin_type


class Makeup(Cosmetics):
    def __init__(self, title, brand, size, unit, category, cosmetics_type, face_part, care_function=None,
                 color=None, spf=None):
        super().__init__(title, brand, size, unit, category, cosmetics_type, care_function)
        self.face_part = face_part
        self.color = color
        self.spf = spf


cosmetics1 = Haircare(
    title='Elvital Dream length',
    brand="L'Oreal Paris",
    size=200,
    unit='ml',
    category='hair care',
    cosmetics_type='cream',
    hair_type='long damaged hair',
    care_function='seal split-ends, strengthen lengths and tips '
)
cosmetics2 = Skincare(
    title='Eye & Lip make-up remover',
    brand="L'Oreal Paris",
    size=125,
    unit='ml',
    category='skin care',
    cosmetics_type='Makeup removers',
    care_type='Moisturising',
    bodypart='eyes and lips',
    skin_type='Normal and sensitive skin',
    care_function=None
)
cosmetics3 = Makeup(
    title='Color Correcting Cream',
    brand='Lumene',
    size=30,
    unit='ml',
    category='skin care',
    cosmetics_type='CC Creams',
    face_part='face',
    color='light',
    care_function='skin tone unifying',
    spf=20
)

items = [cosmetics1, cosmetics2, cosmetics3]
for item in items:
    print(item.about())