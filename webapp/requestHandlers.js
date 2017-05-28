var querystring = require("querystring");
var twitter = require("./twitter");

function start(response, postData) {
  console.log("Request handler 'start' was called.");
  
  var body = '<html>'+
    '<head>'+
    '<meta http-equiv="Content-Type" content="text/html; '+
    'charset=UTF-8" />'+
    '</head>'+
    '<body>'+
    '<form action="/listTweets" method="post">'+
    '<textarea name="text" rows="20" cols="60"></textarea>'+
    '<input type="submit" value="Show tweets" />'+
    '</form>'+
    '</body>'+
    '</html>';
  response.writeHead(200, {"Content-Type": "text/html"});
  response.write(body);
  response.end();


}

function upload(response, postData) {
  console.log("Request handler 'upload' was called.");
  response.writeHead(200, {"Content-Type": "text/plain"});
  response.write("You've sent: " +
  querystring.parse(postData).text);
  response.end();

}

function listTweets(response, postData) {
  console.log("Request handler 'listTweets' was called.");
  twitter.listTweets(response, querystring.parse(postData).text);

}

exports.start = start;
exports.upload = upload;
exports.listTweets = listTweets;
