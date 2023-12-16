
from config import *

bot = telebot.TeleBot(TOKEN)
LOG_FILE_PATH = 'bot.log'
GIF_FILE_PATH = 'bot.gif'
HELP = 'help.gif'
WIKIPEDIA_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
logging.basicConfig(filename=os.path.abspath(LOG_FILE_PATH), level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def remove_html_tags(text):
    soup = BeautifulSoup(text, 'html.parser')
    return soup.get_text()
@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    log_user_interaction(message)

    if message.text.startswith('/ping'):
        handle_ping(message)
    elif message.text.startswith('/help'):
        handle_help(message)
    elif message.text.startswith('/systeminfo'):
        handle_system_info(message)
    elif message.text.startswith('/start'):
        send_gif(message)
    elif message.text.startswith('/viewlog'):
        handle_view_log(message)
    elif message.text.startswith('/generateqr'):
        handle_generate_qr(message)
    elif message.text.startswith('/weather'):
        handle_weather(message)
    elif message.text.startswith('/google'):
        handle_google_search(message, bot)
    elif message.text.startswith('/wikipedia'):
        handle_wikipedia_search(message)
    elif message.text.startswith('/speedtest'):
        handle_speedtest(message)
    elif message.text.startswith('/meme'):
        handle_random_meme(message)
    elif message.text.startswith('/anime'):
        handle_anime_info(message)
    elif message.text.startswith('/imdb'):
        handle_imdb_info(message)
    else:
        handle_unrecognized_command(message)


def handle_google_search(message: Message, bot, num_results=5):
    try:
        query = message.text.split(' ', 1)[1]
        search_results = list(search(query, num_results=num_results))
        results_text = "\n".join(search_results)
        bot.reply_to(message, f"Google Search Results:\n{results_text}")
    except Exception as e:
        bot.reply_to(message, f"Error performing Google search: {e}")


def log_user_interaction(message):
    user_info = f"User ID: {message.from_user.id}, Username: {message.from_user.username}, Chat ID: {message.chat.id}"
    logging.info(f"User Interaction: {user_info}, Message: {message.text}")


# /START
def send_gif(message):
    user_name = message.from_user.first_name
    gif = open(os.path.abspath(GIF_FILE_PATH), 'rb')
    caption = f"Hello {user_name} to λ BOT! Use /help to see available commands"
    bot.send_animation(message.chat.id, gif, caption=caption)


# PING
def handle_ping(message):
    start_time = time.time()
    reply = bot.send_message(message.chat.id, "Pinging...")
    end_time = time.time()

    elapsed_time = end_time - start_time
    bot.edit_message_text(f"Pong! Response time: {elapsed_time:.2f} seconds", message.chat.id, reply.message_id)


# HELP TEXT
def handle_help(message):
    gif = open(os.path.abspath(HELP), 'rb')
    help_text = (
        "Welcome to the world of λ (LAMBDA-BOT) commands! 🤖\n"
        "Explore the commands available in λ with these exciting options: 💬\n"
        "/ping - Check if the bot is responsive 🏓\n"
        "/help - Display this interactive help message ℹ️\n"
        "/systeminfo - Peek into system information 💻\n"
        "/generateqr <text> - Craft a QR code from your text 🆔\n"
        "/weather <city> - Discover current weather in any city 🌦️\n"
        "/wikipedia <query> - Dive into the vast sea of Wikipedia 📚\n"
        "/speedtest - Measure your internet speed ⚡\n"
        "/google <query> - Search Google for information 🔍\n"
        "/meme - Unleash the power of humor with a random meme 😄\n"
        "/anime <anime_name> - Embark on an anime adventure with details 🎌\n"
        "/imdb <movie_title> - Explore movie details from IMDb 🎬\n"
        )
    bot.send_animation(message.chat.id, gif, caption=help_text)


def handle_system_info(message):
    system_info = f"System: {platform.system()} {platform.version()}\nMachine: {platform.machine()}\nProcessor: {platform.processor()}"
    bot.reply_to(message, system_info)


def handle_unrecognized_command(message):
    bot.reply_to(message, "Sorry, I didn't recognize that command. Use /help to see available commands.")


# LOG
@bot.message_handler(commands=['viewlog'])
def handle_view_log(message):
    if message.from_user.id == OWNER_USER_ID:
        try:
            with open(os.path.abspath(LOG_FILE_PATH), 'rb') as log_file:
                bot.send_document(message.chat.id, log_file, caption="Here is the log file.")
        except Exception as e:
            bot.reply_to(message, f"Error sending the log file: {e}")
    else:
        bot.reply_to(message, "You do not have permission to view the log.")


@bot.message_handler(commands=['generateqr'])
def handle_generate_qr(message):
    try:
        text_to_encode = message.text.split(' ', 1)[1]
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(text_to_encode)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img_bytes = BytesIO()
        img.save(img_bytes, format='PNG')
        img_bytes.seek(0)
        bot.send_photo(message.chat.id, img_bytes, caption=f"Generated QR code for:\n{text_to_encode}")
    except Exception as e:
        bot.reply_to(message, f"Error generating QR code: {e}")


# WEATHER
@bot.message_handler(commands=['weather'])
def handle_weather(message):
    try:
        city_name = message.text.split(' ', 1)[1]
        weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={OPENWEATHERMAP_API_KEY}&units=metric"
        response = requests.get(weather_url)
        data = response.json()

        if response.status_code == 200:
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            weather_info = (
                f"Weather in {city_name}:\n"
                f"Description: {weather_description}\n"
                f"Temperature: {temperature} C\n"
                f"Humidity: {humidity}%\n"
                f"Wind Speed: {wind_speed} m/s"
            )
            bot.reply_to(message, weather_info)
        else:
            bot.reply_to(message, f"Error fetching weather information: {data['message']}")
    except Exception as e:
        bot.reply_to(message, f"Error fetching weather information: {e}")


# Wikipedia
@bot.message_handler(commands=['wikipedia'])
def handle_wikipedia_search(message):
    try:
        query = message.text.split(' ', 1)[1]
        headers = {'User-Agent': WIKIPEDIA_USER_AGENT}
        wikipedia_url = f"https://en.wikipedia.org/w/api.php?action=query&format=json&titles={query}&prop=extracts&exintro=1"
        response = requests.get(wikipedia_url, headers=headers)
        data = response.json()

        if 'pages' in data['query']:
            page = next(iter(data['query']['pages'].values()))
            raw_html = page.get('extract', 'No information available')
            plain_text = remove_html_tags(raw_html)
            bot.reply_to(message, f"Wikipedia Summary for '{query}':\n{plain_text}")
        else:
            bot.reply_to(message, f"No Wikipedia page found for '{query}'")
    except Exception as e:
        bot.reply_to(message, f"Error performing Wikipedia search: {e}")


# SPEEDTEST
@bot.message_handler(commands=['speedtest'])
def handle_speedtest(message):
    try:
        st = speedtest.Speedtest()
        download_speed = st.download()
        upload_speed = st.upload()

        speedtest_info = (
            f"Speedtest Results:\n"
            f"Download Speed: {download_speed / 10**6:.2f} Mbps\n"  # Convert to Mbps
            f"Upload Speed: {upload_speed / 10**6:.2f} Mbps"  # Convert to Mbps
        )

        bot.reply_to(message, speedtest_info)
    except Exception as e:
        bot.reply_to(message, f"Error performing speedtest: {e}")

# RANDOM MEME
@bot.message_handler(commands=['meme'])
def handle_random_meme(message):
    try:
        response = requests.get(MEME_API_KEY)
        meme_data = response.json()

        if 'url' in meme_data:
            meme_url = meme_data['url']
            bot.send_photo(message.chat.id, meme_url, caption="Here's a random meme for you!")
        else:
            bot.reply_to(message, "Error fetching a random meme.")
    except Exception as e:
        bot.reply_to(message, f"Error fetching a random meme: {e}")


# ANIME
# ANIME INFO
@bot.message_handler(commands=['anime'])
def handle_anime_info(message):
    try:
        anime_name = message.text.split(' ', 1)[1]
        query = """
        query ($anime_name: String) {
          Media (search: $anime_name, type: ANIME) {
            title {
              romaji
              english
              native
            }
            description
            startDate {
              year
              month
              day
            }
            endDate {
              year
              month
              day
            }
            episodes
            genres
            averageScore
            coverImage {
              large
            }
            siteUrl
          }
        }
        """
        variables = {'anime_name': anime_name}
        response = requests.post(ANILIST_API_URL, json={'query': query, 'variables': variables})
        anime_data = response.json()

        if 'data' in anime_data and 'Media' in anime_data['data'] and anime_data['data']['Media']:
            anime = anime_data['data']['Media']
            title = anime['title']['english'] or anime['title']['romaji'] or anime['title']['native']
            description = anime['description']
            start_date = f"{anime['startDate']['year']}-{anime['startDate']['month']}-{anime['startDate']['day']}"
            end_date = f"{anime['endDate']['year']}-{anime['endDate']['month']}-{anime['endDate']['day']}" if anime['endDate'] else "Ongoing"
            episodes = anime['episodes']
            genres = ', '.join(anime['genres'])
            average_score = anime['averageScore']
            site_url = anime['siteUrl']

            # ... (previous code)
            anime_info = (
                f"Title: {title}\n"
                f"Description: {description}\n"
                f"Start Date: {start_date}\n"
                f"End Date: {end_date}\n"
                f"Episodes: {episodes}\n"
                f"Genres: {genres}\n"
                f"Average Score: {average_score}\n"
                f"Site URL: {site_url}\n"
                f"ANIWATCH URL: https://aniwatch.to/search?keyword={title}"
                )

# ... (remaining code)

            bot.send_message(message.chat.id, anime_info)
        else:
            bot.reply_to(message, f"No information found for the anime '{anime_name}'")
    except Exception as e:
        bot.reply_to(message, f"Error fetching anime information: {e}")


##IMDB
@bot.message_handler(commands=['imdb'])
def handle_imdb_info(message):
    try:
        movie_title = message.text.split(' ', 1)[1]
        params = {'apikey': OMDB_API_KEY, 't': movie_title}
        response = requests.get(OMDB_API_URL, params=params)
        movie_data = response.json()

        if 'Response' in movie_data and movie_data['Response'] == 'True':
            title = movie_data['Title']
            year = movie_data['Year']
            rated = movie_data['Rated']
            genre = movie_data['Genre']
            plot = movie_data['Plot']
            imdb_rating = movie_data['imdbRating']
            poster = movie_data['Poster']

            imdb_info = (
                f"Title: {title}\n"
                f"Year: {year}\n"
                f"Rated: {rated}\n"
                f"Genre: {genre}\n"
                f"Plot: {plot}\n"
                f"IMDb Rating: {imdb_rating}\n"
            )

            bot.send_photo(message.chat.id, poster, caption=imdb_info)
        else:
            bot.reply_to(message, f"No information found for '{movie_title}' on IMDb")
    except Exception as e:
        bot.reply_to(message, f"Error fetching IMDb information: {e}")
# DON'T CHANGE ANYTHING BELOW THIS LINE
if __name__ == "__main__":
    print("Starting the bot...")
    print("Press Ctrl+C to stop")
    print("----------")
    print("Bot started")
    print("----------")
    print(f"Bot username: @{bot.get_me().username}")
    print(f"Bot ID: {bot.get_me().id}")
    print("----------")
    print("Created by: HARAJIT")
    print("Follow me on Instagram: @harajit.exe")
    print("----------")
    print("Enjoy!")
    bot.polling(none_stop=True)
