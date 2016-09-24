var OAuth2 = require('oauth').OAuth2;
var https = require('https');

var oauth2 = new OAuth2('', '', 'https://api.twitter.com/', null, 'oauth2/token', null);


/*var access_token = oauth2.getOAuthAccessToken('', {
    'grant_type': 'client_credentials'
  }, function (e, access_token) {
      console.log(access_token); //string that we can use to authenticate request
});
*/

function listTweets(response, screen_name) {
  var options = {
      hostname: 'api.twitter.com',
      path: '/1.1/statuses/user_timeline.json?screen_name='+screen_name,
      headers: {
          Authorization: 'Bearer ' + access_token
      }
  };
  var https = require('https');
  https.get(options, function(result){
    var buffer = '';
    var tweet_texts = '';
    result.setEncoding('utf8');
    result.on('data', function(data){
      buffer += data;
    });
    result.on('end', function() {
      tweets = JSON.parse(buffer);
      for(var key in tweets) {
        tweet = tweets[key];
        tweet_texts = tweet_texts+ '\n\n' +tweet['text']
      }
      response.writeHead(200, {"Content-Type": "text/plain"});
      response.write("Tweets: \n" +tweet_texts); 
      response.end();

 
   });
  });
}

exports.listTweets = listTweets;
