# jobboard

This is my submission for the coding assessment. My idea was that I find it difficult to keep track of a where I am in the application process for jobs so I made this web app that is like a kanban board but tailored for job applications. You can also sign up for email reminders of what applications you have coming up. You can have an account on it and it saves whatever stages and posts you make for next time. If you drag and drop a post to a different place it saves that also. 

For the acceptance criteria, it is a Django web app so Python is used for most tasks. I used HTML, Javascript and CSS for the page view templates, the database is the built in sqlite3 database, and I also used bootstrap for the page styling. For the drag and drop on posts I used jquery draggable lists and ajax to have them save to the database when they are dropped. I did not get a chance to fully test whether emails are sending hourly and daily using the heroku scheduler, but it worked for a shorter interval of 10 minutes. 

I originally wanted to have it take information from my email account and automatically update, such as if I get an email that says I have an interview tomorrow it automatically changes that posting to the interview stage on the app. I still think it is possible but it will definitely take me more than a week so I’m still working on that part. In the meantime I did the other features where you can manually go and update it.

If you don’t have time to make an account and everything, I put my login credentials down here so you can take a look. I just put in some jobs from my university job board.

unnathy
Lucky!5109

Sources: 
For Card Styling: https://www.bootdey.com/snippets/view/events-card-widget#css
For Drag and Drop Lists: https://fluffycloudsandlines.blog/django-ajax-drag-and-drop/
Django Tutorial: https://docs.djangoproject.com/en/4.0/intro/tutorial01/
