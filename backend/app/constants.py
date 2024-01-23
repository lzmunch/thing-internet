import time
import json
import os


# holds links to images for a bunch of "things"
# created in server.py
LINK_DICT = None
WORD_DICT = {
  'goat': ['goat', 'GOAT', 'Goat', 'goat', 'GOAT', 'Goat', 'gOaT', 'Goaty McGoaty', 'Goatalicious', 'baaaaaaaaahhhhhhhhh', 'baahh', 'BAAHHH', 'baaahhh'],
  'fish': ['fish', 'FISH', 'Fish', 'fish', 'FISH', 'Fish','fIsH', 'Fishy McFishface', 'blub blub blub', 'glub glub', 'bloop bloop'],
  'worm': ['worm', 'WORM', 'Worm','worm', 'WORM', 'Worm', 'wOrM', 'dirt', 'DIRT', '*wiggle*', '*wiggle wiggle*', '*worm sounds*', '*WORM SOUNDS*'],
  'toaster': ['toaster', 'TOASTER', 'Toaster', 'toast', 'TOAST', 'toaster', 'TOASTER', 'Toaster', 'toast', 'TOAST','tOaSt', 'ding ding', 'DING', 'YOUR TOAST IS BURNT', 'ZAP', 'DO NOT PUT THAT FORK IN ME'],
  'internet': ['internet', 'Internet', 'INTERNET', 'internet', 'Internet', 'INTERNET', 'iNtErNeT', 'beep', 'boop', 'beepboop', '*random harrassment*', 'cyberbullying', 'furry porn', '*slur*']
}

GOAT_IMG_URL = 'https://maymont.org/wp-content/uploads/2020/07/banner-goat-c-Carla-Murray-1400x934.jpg'
GOAT_ICON_URL = "https://cdn.glitch.global/78167da7-6d04-4bcd-8dcd-cf8fe9b35f0e/goat_icon.svg?v=1703911119547"

EXT_LIST = ['.png', '.svg', '.jpg', '.webp']