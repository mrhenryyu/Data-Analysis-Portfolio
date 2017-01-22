# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 22:46:34 2016

@author: HenryYu
"""

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", 
                        "A story of a boy and his toys",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
                
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
                     
#print(avatar.storyline)
#avatar.show_trailer()
                     
school_of_rock = media.Movie("School of Rock",
                             "Using Rock Music to learn",
                             "poster url",
                             "trailer_url")
                             

movies = [toy_story, avatar, school_of_rock]

fresh_tomatoes.open_movies_page(movies)                