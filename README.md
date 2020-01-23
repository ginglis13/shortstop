# shortstop

🤖 Bot for SVS 2020 groupme. Flask app run on a Digital Ocean droplet

### Functionality

- all caps messages will be notified of a noise complaint and reported accordingly
- !detain <user> - detain a user
- !attendance - get the class sign in URL
- !weather <location> - Lets you know the weather at redwood, att or menlo
- !commute [TODO] <transitsystem> <station> - Lets you know when the next train/bus for <transitsystem> at <station> is coming
- !calendar [TODO] <timeframe> - See what Dierre has scheduled for the next <timeframe> (day, week)
- !party <building> <room> <timewindow> - Let the group know there's a party at your place
- !dierre [TODO] - get a dierre quote or picture :heart:
- shortstop keeps track of the calendar and will wish you a happy birthday!
- !roseceremony - retrieve the list of current bachelor contestants

### References

[Groupme Dev API](https://dev.groupme.com/)

[Traffic](https://511.org/sites/default/files/pdfs/511%20SF%20Bay%20Open%20Data%20Specification%20-%20Transit.pdf)

[Weather API](https://openweathermap.org/api)


### TODO

Restructure app into separate modules, use `reload` function
Reference Bobbit module loading: https://github.com/pbui/bobbit-ng/blob/master/bobbit.py
