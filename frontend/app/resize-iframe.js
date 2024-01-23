/* Make some additional adjustments here for mobile since
 * mobile browsers vary more significantly
 */

// iframe resizer, mostly for mobile
iFrameResize({ log: true }, '#goat-frame')

// helpful for getting print statements on mobile
function debug_alert(msg_list){
  let s = msg_list.join('\n');
  alert(s);
}

// these don't work on mobile
// let window_height = window.innerHeight;

// no consistent between chrome and safari on mobile
// let window_height = screen.height;

// seems to be the best way to work around safari weirdness
// https://stackoverflow.com/questions/37112218/css3-100vh-not-constant-in-mobile-browser
let window_height = $(window).height();

// resize container
const container_padding = 50;
let container = $('#goat-content-container');
let browser_area = $('#goat-browser-area');
container.height(window_height - browser_area.height() - container_padding)


// TODO alternate btn in one line with search bar for mobile (goat emoji)
// const use_alternate_btn = false;
// if (use_alternate_btn){
//   // resize search bar
  
//   const search_padding = 100;
//   let search_bar = $('#goat-search-bar');
//   let search_btn = $('#search-btn');
//   search_bar.width(vw - search_btn.width() - search_padding)  
// }


  