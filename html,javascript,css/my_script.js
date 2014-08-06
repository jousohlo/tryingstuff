function myFunction(nbr1, txt) {
    text_data = document.getElementById("data").value
    result = nbr1++;
    type = jQuery.isFunction(result);
    $("#result").text(txt + result + type + text_data);
    var i;
    for (i = 0; i < 10; i++) {
        var newPara = document.createElement("p");
        newPara.appendChild(document.createTextNode("hello"+ i));
        document.body.insertBefore(newPara, document.getElementById("result")); 
    }
    document.getElementById("title").innerHTML = "Playing with HTML, css and Javascript";
}
