# 🤖LAMBDA-BOT (λ)

Welcome to the  LAMBDA-BOT (λ) repository! This bot is designed to provide various functionalities, including Google search, weather information, Wikipedia search and more. Below, you'll find information on how to use the bot and set it up for your own use.

## Getting Started

### Prerequisites
1. Python 3
2. Required Python packages (install using `pip install -r requirements.txt`):
   - telebot
   - google
   - requests
   - qrcode
   - beautifulsoup4

### Setup
1. Clone this repository to your local machine.

    ```bash
    git clone https://github.com/HARAJIT05/RED-LAMBDA.git
    ```

2. Install the required Python packages.

    ```bash
    pip install -r requirements.txt
    ```

3. Create a new bot on Telegram and obtain the API token. Follow the [official Telegram Bot documentation](https://core.telegram.org/bots#botfather) for instructions on creating a new bot.

4. Replace the placeholder token in the code (`TOKEN = 'YOUR_BOT_TOKEN'`) with the token obtained from BotFather.

5. Replace other placeholder values, such as `OWNER_USER_ID`, `OPENWEATHERMAP_API_KEY`, with your own values.

6. Run the bot.

    ```bash
    python bot.py
    ```

## Bot Commands

1. **Ping** 🏓
   - `/ping`: Check if the bot is responsive.

2. **Help** ℹ️
   - `/help`: Display a list of available commands and their descriptions.

3. **System Information** 💻
   - `/systeminfo`: Show system information.

4. **Generate QR Code** 🆔
   - `/generateqr <text>`: Generate a QR code from the provided text.

5. **Weather Information** 🌦️
   - `/weather <city>`: Get current weather information for a specific city.

6. **Google Search** 🔍
   - `/google <query>`: Perform a Google search and display the results.

7. **Wikipedia Search** 📚
   - `/wikipedia <query>`: Search Wikipedia for information.

8. **Speedtest** ⚡
   - `/speedtest`: Perform a speedtest.

9. **Random Meme** 😄
   - `/meme`: Get a random meme.

10. **Anime Information** 🎌
    - `/anime <anime_name>`: Get information about an anime.

11. **IMDb Information** 🎬
    - `/imdb <movie_title>`: Get information about a movie from IMDb.

## Notes
- The bot owner can view the log file using the `/viewlog` command.
- Some commands may require additional API keys (e.g., OpenWeatherMap,omdb for imdb database).

Feel free to explore and customize the bot based on your needs! If you have any questions or encounter issues, please reach out to the bot [creator](https://linktr.ee/harajit). 

**Enjoy using the Telegram Bot!** 🚀
