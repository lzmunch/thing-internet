// client side js

// const mobile_threshold = 600;
// const dev_site = 'https://www.coolmathgames.com'
// const re = new RegExp("/http[s]?:\/\/(?:www)?\.?[a-zA-Z0-9-_]+\.[a-zA-Z]{2,3}/gm");

var START_THING = 'goat';
const THING_DICT = {
  'goat': {'emoji': "🐐", 'fontSize': '55px'},
  'fish': {'emoji': "🐟", 'fontSize': '55px'},
  'worm': {'emoji': "🐛", 'fontSize': '55px'},
  'toaster': {'emoji': "🍞", 'fontSize': '45px'},
  'internet': {'emoji': "🕸️", 'fontSize': '45px'},
};
const BACKEND_URL = 'https://thing-internet-backend.glitch.me';

const DEV_SITE = 'https://www.wikipedia.org';
const MOBILE_SITE = 'https://thing-internet.glitch.me/m.html';

const SAMPLE_SITES = [
  'https://www.coolmathgames.com',
  'https://www.archiveofourown.org',
  'https://www.weirdorconfusing.com',
  'https://www.neopets.com',
  'https://zapatopi.net/treeoctopus/',
  'https://www.cats.com'
];

// do some calculations as page is loading?
const STARTING_THING = Object.keys(THING_DICT)[Math.floor(Math.random()*Object.keys(THING_DICT).length)];
console.log(STARTING_THING)


function is_mobile() {
  return window.screen.availWidth < 1000 ;
}

function update_things(thing){
  // update things
  console.log('updating things', thing)
  // $("#thing-emoji").text(THING_DICT[thing]['emoji']);
  $("#thing-text-1").text(thing.toUpperCase());
  $("#thing-text-2").text(thing);
  $("#search-btn").text(thing + '!');
  
  if (is_mobile()){
    $('#goat-header').css('fontSize', THING_DICT[thing]['fontSize']);
  }
}

function update_browser_content(thing){
  let input_url = $("#goat-search-bar").val();
  input_url = input_url.toLowerCase();

  // validate url
  // if empty, go to start page
  if (input_url.length == 0){
    $('#goat-iframe').attr('src', BACKEND_URL);
    return
  }
  // if missing prefix, add it
  if (!input_url.includes('https://') && !input_url.includes('http://')) {
    input_url = 'https://' + input_url;
    $("#goat-search-bar").val(input_url);
  }

  // update iframe
  let new_url = BACKEND_URL + '/go?thing=' + thing + '&input_url=' + input_url;
  console.log('going to ' + new_url);
  $('#goat-iframe').attr('src', new_url);
  document.getElementById('goat-iframe').src = document.getElementById('goat-iframe').src;

  // update debug button
  $("#debug-iframe").attr('href', document.getElementById('goat-iframe').src);
}

// DO ALL THE STUFF ON DOCUMENT LOAD
$(document).ready(function () {
  console.log("Ready!");
  
  // redirect user to mobile site if needed
  if (is_mobile() && window.location.href != MOBILE_SITE){
      let res = confirm('MESSAGE FROM THING INTERNET:\n' + 
                        'Mobile device dimensions detected.\n' + 
                        'Go to mobile site?');
      if (res)
        window.location.href = MOBILE_SITE;
  }

  // setup debug stuff
  if (window.location.search.includes('?debug')){
    console.log('DEBUG ON')
    
    // setup debug button
    $("#debug-iframe").attr('href', document.getElementById('goat-iframe').src);
    $("#debug-iframe").attr('style', 'display:inline-block;');
    
    // for dev purposes, start with some website
    $("input").val(DEV_SITE)
  }
  else {
    // if not dev, give user a sample site
    $("input").val(SAMPLE_SITES[Math.floor(Math.random()*SAMPLE_SITES.length)])
  }
  // intecept redirects
  // why did kongregate games try to hijack us :(
  // $('a').on('click', function(event){
  //   event.preventDefault();
  //   alert('BAHHHHH this site is trying to take you away from GOAT INTERNET :-(\n Continue?');
  // });
  
  // force iframe to be a certain width on mobile
  // if (window.screen.availWidth < mobile_threshold) {
  //   // $("iframe").attr('width', 500)
  //   // $("iframe").attr('height', 700)
  //   console.log('mobile detected')
  // }
  // else {
  //   // only focus input when not on mobile
  //   $("input").focus();
  // }
  
  var thing_select = $('#thing-select');
  
   
  // pick random thing to start with
  thing_select.val(STARTING_THING);
  update_things(STARTING_THING);
  
  // set up event to update things when user changes
  // select option
  thing_select.on('change', () => {
    update_things(thing_select.val());
    update_browser_content(thing_select.val())
  });
  
  // focus on input if empty
  if ($("input").val == ''){
    $("input").focus();    
  }
  
  // setup form submit action
  $("form").submit(function (event) {
    event.preventDefault();
    update_browser_content(thing_select.val());
  });
});




// // intecept redirects
// $('a').on('click', function(event){
//   event.preventDefault();
//   confirm('ARE YOU SURE YOU WANT TO LEAVE GOAT INTERNET???')
// });