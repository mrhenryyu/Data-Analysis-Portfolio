# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 21:04:32 2016

@author: HenryYu
"""

#media.py
import webbrowser

class Video():
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
    
class Movie(Video):
    """This class provides a way to store movie information """    
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        Video.__init__(movie_title, duration)        
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube 
    
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
class TVShow()