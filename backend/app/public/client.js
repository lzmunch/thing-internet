// client-side js
// run by the browser each time your view template is loaded

// by default, you've got jQuery,
// add other scripts at the bottom of index.html

$(document).ready(function () {
  
  // intecept redirects
  $('a').on('click', function(event){
    event.preventDefault();
    
    var target_url = event.currentTarget.href;
    console.log('target_url: ' + target_url)
    
    // try to figure out if it is a relative link
    target_url = target_url.replace('https://goat-internet-backend.glitch.me', '').replace('/goat?input_url=', '')
    console.log('stripped url to ' + target_url)
    
    // fix relative links
    if (target_url.charAt(0) == '/' && target_url.substring(0,4) != 'http'){
      console.log(target_url.charAt(0))
      let input_url = window.location.href.replace('https://goat-internet-backend.glitch.me', '')
      target_url = input_url + target_url;
      console.log('fixed relative url link: ' + target_url);
    }
    
    target_url = 'https://goat-internet-backend.glitch.me/goat?input_url=' + target_url
    console.log('updated url to ' + target_url);
    
    // for debugging
    // let res = confirm('link redirects are still a WIP. this link may not work');
    // let res = confirm('ARE YOU SURE WANT TO LEAVE THING INTERNET??!!!');
    let res = true;
    if (res)
      window.location.href = target_url
  });
});