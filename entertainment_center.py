import media
import page_create

# Instance containing title and links to trailer/poster for The Godfather
godfather_pt1 = media.Movie('https://www.youtube.com/watch?v=sY1S34973zA',
                            'The Godfather',
                            'https://i.pinimg.com/originals/a3/92/82/'
                            'a39282230e8b0d2c140fe87578061b26.jpg')

# Instance containing title and links to trailer/poster for Inside Out
inside_out = media.Movie('https://youtu.be/_MC3XuMvsDI',
                         'Inside Out',
                         'https://images-na.ssl-images-amazon.com/images/I/'
                         '51vmcbYAakL.jpg')

# Instance containing title and link to trailer/poster for Road to Perdition
road_perdition = media.Movie('https://youtu.be/IjbSYkY5hVA',
                             'Road to Perdition',
                             'https://www.movieposter.com/posters/archive/main'
                             '/97/MPW-48593')

# list containing movie instances that feeds page_create to show movies
movies = [godfather_pt1, inside_out, road_perdition]

# Creates the tiles displaying the movies
page_create.create_movie_tiles_content(movies)
# Creates and opens fresh_tomatoes.html file displaying movies
page_create.open_movies_page(movies)

