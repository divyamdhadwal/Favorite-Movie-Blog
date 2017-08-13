import webbrowser # Import the predefined file named webbrowser.

class Movie():
    # Documentation for class movie.
    """Documentation :
     movie_title : Specifies the title of a movie.
     movie_storyline : Stores a brief description about the movie.
     poster_image : Stores the path of image for a particular movie.
     trailer_youtube : Stores the link to youtube trailer of a movie.
    """ 
    # Declare initialize function.
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube

    # Declare show movie trailer function.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
