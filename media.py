class Movie(object):
    '''Parent class for any movie instances.
    Stores trailer, title, and poster image data'''
    def __init__(self, trailer_youtube_url, title, poster_image_url):
        self.trailer_youtube_url = trailer_youtube_url
        self.title = title
        self.poster_image_url = poster_image_url
