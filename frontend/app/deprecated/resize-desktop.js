let vh = window.innerHeight;
const container_padding = 100;
let container = $('#goat-content-container');
let browser_area = $('#goat-browser-area');
container.height(vh - browser_area.height() - container_padding)