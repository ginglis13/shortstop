# shortstop

🤖 Bot for SVS 2020 groupme. Flask app run on a Raspberry Pi

### Functionality

- all caps messages will be notified of a noise complaint and reported accordingly
- !usage - show all commands

- !attendance - get the class sign in URL
- !calendar \<timeframe\> - See what Dierre has scheduled for the next <timeframe> (day, week)
- !detain \<user\> - detain a user
- !detain list - show all users who have been detained
- !dierre - get a dierre picture and a quote :heart:
- !door \<location\> - ask to be let in
- !party \<building\> \<room\> \<timewindow\> - Let the group know there's a party at your place
- !roseceremony - retrieve the list of current bachelor contestants
- !train [TODO] \<transitsystem\> \<station\> - Lets you know when the next train/bus for <transitsystem> at <station> is coming
- !weather \<location\> - Lets you know the weather at redwood, att or menlo
- !penny - shares a Pennycuff meme le epic style (like a boss)

- shortstop keeps track of the calendar and will wish you a happy birthday!

### References

[Groupme Dev API](https://dev.groupme.com/)

[Traffic](https://511.org/sites/default/files/pdfs/511%20SF%20Bay%20Open%20Data%20Specification%20-%20Transit.pdf)

[Weather API](https://openweathermap.org/api)

[Google Calendar API](https://developers.google.com/calendar/v3/reference)

### TODO

Train/Commute Module

Restructure app into separate modules, use `reload` function
Reference Bobbit module loading: https://github.com/pbui/bobbit-ng/blob/master/bobbit.py
