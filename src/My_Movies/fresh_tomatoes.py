import webbrowser
import os
import re
from addmovies.models import AddMovie
from addmovies.forms import AddMovieForm
from signups.forms import SignUpForm

import cgi

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Baobab!</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    
    <!-- Moved the inline CSS to static directory-->
    <style>
        /*
 * reorganized the css from the fresh_tomatoes to CSS folder
 * ---------------------------------------------------------
 */

        body {
            padding-top: 0px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>

    <script>
    // Pause the video when the modal is closed
$(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
	// Remove the src so the player itself gets removed, as this is the only
	// reliable way to ensure the video stops playing in IE
	$("#trailer-video-container").empty();
	});

// Start playing the video whenever the trailer modal is opened
$(document).on('click', '.movie-tile', function (event) {
	var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
	var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
	$("#trailer-video-container").empty().append($("<iframe></iframe>", {
		'id': 'trailer-video',
		'type': 'text-html',
		'src': sourceUrl,
		'frameborder': 0
	}));
});

// Animate in the movies when the page loads
$(document).ready(function () {
	$('.movie-tile').hide().first().show("fast", function showNext() {
	$(this).next("div").show("fast", showNext);
	});
});
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <div class="header clearfix">
        <h2 class="nav"><center>B A O B A B</center></h2>
    </div>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    <div class="navbar navbar-inverse navbar-static-top" role="navigation">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-ex1-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" rel="home" href="" title="Serge Nganou Favvorite Movies - Homepage">Serge Nganou Best Movies</a>
        </div>    
        <div class="collapse navbar-collapse navbar-ex1-collapse">
            <div class="col-sm-3 col-md-3 pull-right">
                <form class="navbar-form" role="search">
                    <div class="input-group">
                        <nav>
                            <ul class="nav nav-pills pull-right">
                                <li role="presentation" class="active"><a href="">Home</a></li>
                                <li role="presentation"><a href="/signup">Sign Up</a></li>
                                <li role="presentation"><a href="/addmovie">Add Movie</a></li>
                            </ul>
                        </nav>
                        <!--<input type="text" class="form-control" placeholder="Search" name="srch-term" id="srch-term">
                        <button class="btn btn-default" type="submit"><i class="glyphicon glyphicon-search"></i></button>-->
                    </div>
                </form>
            </div>
        </div>
    </div>
    
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <div class="thumbnail">
        <img src="{poster_image_url}" width="220" height="342">
        <div class="caption">
            <h2>{title}({release_date})</h2>
            <p>{storyline}</p>
        </div>
    </div>
</div>
'''

# Contains the addition of movies to the list of favorite movies 
movie_addition_content = '''

'''

def create_movie_tiles_content():
    # The HTML content for this section of the page
    content = ''
    for movie in AddMovie.objects.raw('SELECT * FROM addmovies_addmovie'):
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            title=movie.title,
            release_date = movie.release_date,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            storyline=movie.storyline
        )
    return content



def open_movies_page():
    # Create or overwrite the output file
    output_file = open('../static/templates/fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content())

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    #url = os.path.abspath(output_file.name)
    #webbrowser.open('file://' + url, new=2)

