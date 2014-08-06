function myFunction(nbr1, txt) {
    result = nbr1++;
    document.getElementById("result").innerHTML = txt + result;
    var i;
    for (i = 0; i < 10; i++) {
        var newPara = document.createElement("p");
        newPara.appendChild(document.createTextNode("hello"+ i));
        document.body.insertBefore(newPara, document.getElementById("result"));
    }
}