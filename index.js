let selectedWord;
let shuffleWord;

function startGame() {
    document.getElementById("fguess").value = "";
    const wordList = ["hello", "html", "css", "noa" , "computer" , "university", "friends"];
    const randomIndex = Math.floor(Math.random() * wordList.length );
    selectedWord = wordList[randomIndex];
    shuffleWord = selectedWord.shuffle();

    document.getElementById("gameTextID").innerHTML = shuffleWord;
}

String.prototype.shuffle = function () {
    var a = this.split(""),
        n = a.length;

    for(var i = n - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var tmp = a[i];
        a[i] = a[j];
        a[j] = tmp;
    }
    return a.join("");
}

function check(){
    const guess = document.getElementById("fguess").value;
    if (guess === selectedWord){
        document.getElementById("gameResultID").innerHTML = "success!";
    }
    else{
        document.getElementById("gameResultID").innerHTML = "try again!";
    }
}

