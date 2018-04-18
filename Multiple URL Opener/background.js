chrome.browserAction.onClicked.addListener(function(tab) 
{
	chrome.tabs.getSelected(null,function(tab) 
	{
		chrome.tabs.create({url: "app.html"}, function (tab) {});
	});
});

function onInstall() 
{
	chrome.tabs.create({url: "app.html"}, function (tab) {});
}

function onUpdate() {	}

function getVersion() 
{
	var details = chrome.app.getDetails();
	return details.version;
}

// Check if the version has changed.
var currVersion = getVersion();
var prevVersion = localStorage['version'];

if (currVersion != prevVersion) 
{
	// Check if we just installed this extension.
	if (typeof prevVersion == 'undefined')
	{
		onInstall();
	} 
	else 
	{
		onUpdate();
	}
	localStorage['version'] = currVersion;
}