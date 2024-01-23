let data_json = {{data|tojson}}
console.log(data_json)
if ('error' in data_json){
  if ('url' in data_json){
    // document.getElementById('goat-message').innerHTML = data_json['url'] + ' does not want to be part of the goat internet :-('
    let msg = 'Something went wrong trying to get to "' + data_json['url'] + '".'
    document.getElementById('goat-message').innerHTML = 
  }
  document.getElementById('goat-errors').innerHTML = 'Details: ' +  data_json['error'];
}