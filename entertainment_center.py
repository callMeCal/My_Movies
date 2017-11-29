import media
import page_create

godfather_pt1 = media.Movie('https://www.youtube.com/watch?v=sY1S34973zA',
                            'The Godfather',
                            'https://i.pinimg.com/originals/a3/92/82/a39282230e8b0d2c140fe87578061b26.jpg')

inside_out = media.Movie('https://youtu.be/_MC3XuMvsDI',
                         'Inside Out',
                         'https://images-na.ssl-images-amazon.com/images/I/51vmcbYAakL.jpg')

# list that feeds page_create to show movies
movies = [godfather_pt1, inside_out]

page_create.create_movie_tiles_content(movies)
page_create.open_movies_page(movies)