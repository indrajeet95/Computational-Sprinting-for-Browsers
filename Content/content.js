function cutUrl(str) {
    var matched = str.match(/([^/]*\/){3}/);
    return matched ? matched[0] : str/* or null if you wish */;
}

window.onload = function () {

	window.setTimeout(function () {

	var p = {};
	p.prerequestTime = performance.timing.requestStart - performance.timing.navigationStart;
	p.latencyTime = performance.timing.responseStart - performance.timing.requestStart;
	p.serverTime = performance.timing.responseEnd - performance.timing.responseStart;
	p.domLoadingTime = performance.timing.domInteractive - performance.timing.responseEnd;
	p.domCompleteTime = performance.timing.domComplete - performance.timing.domInteractive;
	p.loadTime = performance.timing.loadEventEnd - performance.timing.domComplete;
	p.onloadTime = performance.timing.loadEventEnd - performance.timing.navigationStart;
	
	query = window.location.href;
	//alert(cutUrl(query));
	var answers = cutUrl(query) + '_' + p.prerequestTime + '_' + p.latencyTime + '_' + p.serverTime + '_' + p.domLoadingTime + '_' + p.domCompleteTime + '_' + p.loadTime + '_' + p.onloadTime;
	//console.log(answers);
	//chrome.runtime.sendMessage({from:"script1",message:"hello!"});
	//alert(answers);
	//var hiddenElement = document.createElement('a');
	//hiddenElement.href = 'data:attachment/text,' + encodeURI(answers);
	//hiddenElement.target = '_blank';
	//hiddenElement.download = Date.now() + '.txt';
	//hiddenElement.click();

	chrome.runtime.sendMessage({answers: answers}, function(response) {
		console.log(response.result);
	});

}, 0);
}

