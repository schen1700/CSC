/* for the first text */
// to change the given HTML paragraph
document.getElementById("text").innerHTML = "Hey, there! How are you doing?";

// to change the text
document.getElementById("btn").onclick = function() {
		document.getElementById("text").innerHTML = "<em>This is a simple JavaScript!</em>";
}
// to update a new text
document.getElementById("second-btn").onclick = function() {
	document.getElementById("text").innerHTML = "<strong>You updated this text!</strong>";
}

/* for the empty text */
// to create a text
document.getElementById("create").onclick = function() {
	document.getElementById("empty-text").innerHTML = "<strong>You created a text! </strong>";
}