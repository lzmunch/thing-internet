# thing-internet
internet for things!!!!

Backup for [thing-internet](https://glitch.com/~thing-internet
) on Glitch.com

Eventually I'd like to move the "backend" to another hosting service as I need access to some NLP python libraries to improve the project and the free container on Glitch is too small.

Since this is just a backup, the projects do not work out of the box. They are specifically setup to run on Glitch.com. Only the scripts in `pexels/` will work.

Another note is that all files now have CRLF line endings but they originally had LF since Glitch containers are Linux, so these scripts may not work out of box on Glitch either.

## Contents
### backend/
A backend that scrapes a given URL and processes the contents. https://glitch.com/~thing-internet-backend

### frontend/
Contains a faux browser inferface to send URLs to the backend. 
https://glitch.com/~thing-internet

### pexels/
Contains code that makes it easy to get new image URLs from the Pexels API