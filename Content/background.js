chrome.runtime.onMessage.addListener(
	function(request, sender, sendResponse) {
	//alert(request.answers);
	if (request.answers)
		sendResponse({result: "DONE"});
	var soln = request.answers;
	//alert(soln);	
	var res = soln.split("_",8);
	//alert(res[0]);
	var http = new XMLHttpRequest();
	var url = "http://localhost/connect.php?link=" + res[0] + "&prerequest=" + res[1] + "&latency=" + res[2] + "&server=" + res[3] + "&domloading=" + res[4] + "&domcomplete=" + res[5] + "&loadtime=" + res[6] + "&total=" + res[7];
	alert(url);	
	http.open("GET", url, true);
	
	//Send the proper header information along with the request
	http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

	//http.onreadystatechange = function() {//Call a function when the state changes.
	//if(http.readyState == 4 && http.status == 200) {
	//	alert(http.responseText);
	//}
	//http://localhost/connect.php?link=ohio&prerequest=987&latency=90&server=121&domloading=567&domcomplete=123&loadtime=112&total=111
	//http://localhost/connect.php?answers=ohoogoogogoasdasda
	http.send();
});


