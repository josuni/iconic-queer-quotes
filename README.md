# Setup and Run Instructions

1. Install requirements: `pip install -r requirements.txt`

2. Create .env file with lines `CONFIG_SECRET_KEY = [config key you want]` and `ADMIN_KEY = [admin key you want]`

3. Run app: `flask --app flasky run`

# Description

This website is meant to host a database of iconic quotes from queer media figures as well as everyday queer people. 

Anyone can submit a quote. Admins then can either approve or reject the submission. If approved, the submission will be put into the Iconic Queer Quotes Database for everyone to see. There is a random quote generator, which randomly selects and displays a quote from the database. There is also the "Iconic Queer Quote of the Day" (determined by bucket-hashing) which is displayed on the home page of the website.

# Citations
1. By Guanaco and subsequent editors - SVG source (version of 17:56, 30 Sep 2011), Public Domain, https://commons.wikimedia.org/w/index.php?curid=479191