# config.py
TOKEN = '6896380150:AAFVVRSHi6CRUaFShL1MGYtnCIUUrI4_wdM'  # Replace with your bot token
OWNER_USER_ID = 6426928410  # Replace with your user ID
OPENWEATHERMAP_API_KEY = '8e238375b0ed5d203301c1c6e0ba961f'  # Replace with your OpenWeatherMap API key
MEME_API_KEY = 'https://meme-api.com/gimme'  # Replace with your Meme API key
ANILIST_API_URL = 'https://graphql.anilist.co' # AniList GraphQL API URL
OMDB_API_KEY = "34c4ed25" # OMDB API URL
OMDB_API_URL = "http://www.omdbapi.com/" # OMDB API URL
import os
import time
import telebot
from googlesearch import search
from telebot import types
import platform
import logging
import requests
import qrcode
from io import BytesIO
from telebot.types import Message
from googlesearch import search
from telebot.types import Message
import wikipediaapi
from bs4 import BeautifulSoup
import speedtest
from PIL import Image