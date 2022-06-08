document.getElementById("submit").onclick = function() {
	var randomNumber = Math.random();
	randomNumber = randomNumber * 9;
	randomNumber = Math.floor(randomNumber);
	if(document.getElementById("submit").value == randomNumber) {
		alert("Well done, you guessed the right number!");
	}
	else {
		alert("Wrong! The number was " + randomNumber + "\nPlease try again.")
	}
}