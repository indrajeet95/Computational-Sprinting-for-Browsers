chrome.runtime.onMessage.addListener(
	function(request, sender, sendResponse) {
	if (request.answers)
		sendResponse({result: "DONE"});
	var soln = request.answers;
	var res = soln.split("_",8);
	var http = new XMLHttpRequest();
	var url = "http://localhost/connect.php?link=" + res[0] + "&prerequest=" + res[1] + "&latency=" + res[2] + "&server=" + res[3] + "&domloading=" + res[4] + "&domcomplete=" + res[5] + "&loadtime=" + res[6] + "&total=" + res[7];
	http.open("GET", url, true);
	http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	http.send();
});


