
# TODO 🚧

🚀 **WIP**
- polish word replacement
    - need to figure out how to replace words in paragraphs without destroying hrefs
    - don't always put word at the front of stuff
- add more pictures for all the things
- replace fish with shark
- beef up internet

🚚 **Coming Up**
- add more things:
  - horse internet
- move to github so we can use more TextBlob and NLTK to replace words better and use advanced webscraping tools
  - need to download nltk data but there is not enough space here for that
  ```
  python -m textblob.download_corpora lite
  
  add textblob to requirements.txt
  ```

- v1.2
  - remove cookie promp overlays
  - display updated URL 
  - make background-images sized right
  - send current url to parent - [see this post](https://stackoverflow.com/questions/8822907/html5-cross-browser-iframe-postmessage-child-to-parent)
  
- v2.0
  - make this into a chrome extension
  
- v3.0
  - install chrome extension into virtual browser

✅ **Done**
- fix some of the relative url fixing logic
- can use pixabay api to avoid saving images on the server?
- allow user to change 'goat' to something else
- get a collection of goat images: automatic download with [pixabay api](https://pixabay.com/api/docs/)
- add error handling (error.htmls)
- get a collection of goat images (manual)
- functional prototype
  - uses beautiful soup to scrape the actual html contents from user input url & replace words with 'goat' and images with 1 goat image
  - allow user to input new URL
  - gather url to scrape from url query
  - create separate project to display this project's processed webpages in a frame, so that the goat internet browser css may prevail
  - allow user to follow links on website to goat versions of the link
    - option a: intercept redirect
    - option b: replace links
    
💀 **Dead Ends**
- get dynamically loaded stuff (selenium? see `scrape.py` will require moving to python3)
  - may have to move backend to github/heroku/etc
  - just doesn't seem very doable tbh