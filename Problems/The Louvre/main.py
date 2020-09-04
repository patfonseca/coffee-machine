class Painting:
    museum = 'the Louvre'

    def __init__(self, title, painter, year):
        self.title = title
        self.painter = painter
        self.year = year


title_painting = input()
painter_painting = input()
year_painting = input()

painting = Painting(title_painting, painter_painting, year_painting)
print('"' + painting.title + '" by ' + painting.painter + ' (' + painting.year + ') hangs in ' + Painting.museum + '.')
