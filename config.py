# config.py
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
TOKEN = '5776066556:AAE8uLvD0a7vhbiKHyVtlGU2QXe17abNkoo'  # Replace with your bot token
OWNER_USER_ID = 6426928410  # Replace with your user ID
OPENWEATHERMAP_API_KEY = '3865822f731ebc30e889367ce489e234'  # Replace with your OpenWeatherMap API key
MEME_API_KEY = 'https://meme-api.com/gimme'  # Replace with your Meme API key
ANILIST_API_URL = 'https://graphql.anilist.co'  # AniList GraphQL API URL
OMDB_API_KEY = 'http://www.omdbapi.com/?i=tt3896198&apikey=f9802666'  # Replace with your OMDB API key
OMDB_API_URL = 'http://www.omdbapi.com/'  # OMDB API URL
