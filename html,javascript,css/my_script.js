function myFunction(nbr1, txt) {
    //get text from text field
    //text_data = document.getElementById("data").value
    //basic numeric calculation
    //result = nbr1++;
    
    //insert some text with jQuery
    //$("#result").text(txt + result + text_data);
    //create html object with Javascript
    
    /*
    var i;
    for (i = 0; i < 10; i++) {
        var newPara = document.createElement("p");
        newPara.appendChild(document.createTextNode("hello"+ i));
        document.body.insertBefore(newPara, document.getElementById("result")); 
    }
    document.getElementById("title").innerHTML = "Playing with HTML, css and Javascript";
    */
    //Get firstname from my LinkedIn profile
    IN.API.Profile("me").fields(["firstName"]).result(function(result) {
        $("#result").text(result.values[0].firstName)})  
   
}
