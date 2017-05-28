var twit = require('twit');

var config = {
  consumer_key: '',  
  consumer_secret: '',
  access_token: '',  
  access_token_secret: ''
}

var Twitter = new twit(config);


function listTweets(response, screen_name) {
  var params = { 'screen_name' : screen_name}
  var tweet_texts = ''

  Twitter.get('statuses/user_timeline', params, function(err,data,resp) {
    if (resp.statusCode == '200') {
      for(var key in data) {
        tweet = data[key];
        tweet_texts = tweet_texts+ '\n\n' +tweet['text']
      }
      response.writeHead(200, {"Content-Type": "text/plain"});
      response.write("Tweets: \n" +tweet_texts); 
      response.end();
    } else {
      response.writeHead(200, {"Content-Type": "text/plain"});
      response.write("Screen name not found!"); 
      response.end();
    }

  });


 
}

exports.listTweets = listTweets;
