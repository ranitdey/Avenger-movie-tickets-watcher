# Avenger-movie-tickets-watcher

This script will poll from www.Bookmyshow.com for Avenger : Endgame ticktes periodically. It can be run locally (on your laptop/desktop), or be deployed on Heroku. 

Currently it only works for Bengaluru(India) location. But it can be changed to any location by making minimal changes to code.

## How to run on local:
1. Make sure your system has python 3.0 or > 3.0
2. Clone this project and go to the project direcory
3. Install required packages  
```
pip install requirements.txt 
```

4. Run the app  
```
Python scrapper.py &
```

This will keep running it in the background, **poll bookmyshow every 3 hours**, and check if Avengers: Endgame has made it to the booking list.

> **Note**: Make sure to run this script again when you reboot your os.

Example Screenshot (for when it would get available):  

![image info](/image_asset/Screenshot%202019-04-10%20at%205.08.30%20AM.png)


## How to deploy on Heroku:

The repository is Heroku compatible. All you need to do is set up a new app in Heroku and set this (or your forked) GitHub repository as the repository for it. 

**The polling frequency is every 30 minutes** when deployed using Heroku.


### Heroku Config

#### Build pack
You'll need to add following Buildpacks to the heroku app : 

1. `heroku/python`
2. `https://github.com/heroku/heroku-buildpack-chromedriver`
3. `https://github.com/heroku/heroku-buildpack-google-chrome`

#### Config Vars
It should be noted that for running it on Heroku/Server, you do require some environment variables (**Config Vars** in Heroku). These are the following : 

| Key | Value |
| --- | --- |
| CHROMEDRIVER_PATH | `/app/.chromedriver/bin/chromedriver` |
| GOOGLE_CHROME_BIN | `/app/.apt/usr/bin/google-chrome` |
| RUNNING_ON_SERVER | TRUE |
| TARGET_TITLE | Avengers: Endgame |
| WEBHOOK | **[Your Webhook URL to which it will POST a message]** |


You could change `TARGET_TITLE` and `WEBHOOK` and the system would then search for the other movie and POST message to new Webhook. 

Currently, when the ticket becomes available, this is what it posts to the webhook : 

```json
{
	"message" : "<TARGET_TITLE> is now available on bookmyshow.com. Go over and book it!"
}
```

**Reference** :   

* [https://devcenter.heroku.com/articles/clock-processes-python](https://devcenter.heroku.com/articles/clock-processes-python)  
* [https://devcenter.heroku.com/articles/config-vars](https://devcenter.heroku.com/articles/config-vars)  
* [https://github.com/heroku/heroku-buildpack-google-chrome](https://github.com/heroku/heroku-buildpack-google-chrome)  
* [https://stackoverflow.com/questions/41059144/running-chromedriver-with-python-selenium-on-heroku](https://stackoverflow.com/questions/41059144/running-chromedriver-with-python-selenium-on-heroku)  
* [https://elements.heroku.com/buildpacks/heroku/heroku-buildpack-chromedriver](https://elements.heroku.com/buildpacks/heroku/heroku-buildpack-chromedriver)


> Tip : Currently, we've used Zapier to provide us a Webhook and we're using that as the Webhook Environment Variable here. From Zapier's webhook, we're posting the message to a Slack Channel. **So, essentially we get notified on slack whenever the movie would become available!** :)  


## Authors

[Ranit Dey](https://github.com/ranit-geek)  
[Bhavul Gauri](https://github.com/bhavul/)