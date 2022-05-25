# Telegram bot talk

In this repo you can find the examples that were explained in the talk "How to make a
Telegram bot with Python", from the PyConAr 2021. [Link to the video.](https://www.youtube.com/watch?v=9x1oF5cCd8k)

## Settings to run these examples

### Telegram Settings

- Talk to BotFather on Telegram, to create a new bot and get your bot token. You can
some related documentation [here](https://core.telegram.org/bots#6-botfather)
- create a `local_settings.py` file in your repo's root with the following content:
```python
BOT_TOKEN = "10201543:A..."  # place here your bot's token.
```


### Google Drive Settings

To be able to connect to a Google Drive Spreadsheet (for feedback's commands for
example) you will need some credentials:

- Create Google Drive credentials by following [these steps](https://medium.com/@a.marenkov/how-to-get-credentials-for-google-sheets-456b7e88c430#)
- Save the json created with your credentials in a file named `sheet_client_key.json` in
the root of your repo.
- Create a Spreadsheet and share it with the user of your recently created credentials
(`...@...iam.gserviceaccount.com`)
- Update the variables `FEEDBACK_SPREADSHEET_NAME` and `FEEDBACK_WORKSHEET_INDEX` in
the file `settings.py` with the name of your spreadsheet and the index of its sheet
where you want to add the feedback (0 is the first sheet)


## Install the dependencies

Before running the bot, you need to install some dependencies. I recommend to create them
inside a virtualenv:

```bash
>> python3 -m venv myvenv
>> . myvenv/bin/activate
>> pip install -r requirements.txt
```

## Run the bots

Now you can run any of the bots! (remember to run these commands inside your virtualenv)

```bash
python first_bot.py
```

or:

```bash
python real_bot.py
```

## Deploy the bot in HEROKU

- Create account in [Heroku](https://signup.heroku.com/)
- Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
- [Create an app](https://devcenter.heroku.com/articles/creating-apps) on Heroku.
- Add a remote to your local repository
```bash
>> heroku git:remote -a example-app
set git remote heroku to https://git.heroku.com/example-app.git
```
Replace `example-app` for your Heroku app name.

- Deploy by simply pushing your changes
```bash
>> git push heroku master
```


Note: you need to have a `Procfile` file pointing to a web app, like the one you can
find in the root of this repo.
