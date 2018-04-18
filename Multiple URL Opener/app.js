var delay = 0;
var index_0 = 0;
var total = 0;

$('#range-value').text($('#range').val());

$('#range').on("change mousemove", function() {
    delay = $(this).val();
    $('#range-value').text(delay);
});

var open_btn = document.getElementById('open');
var lines;
var myWindow = window.open("","MsgWindow");
//Opening an empty tab with the name MsgWindow so that we can maunally go to that page and open Developer tools and then also click on "Preserve Log" so that we can record the network activity for consecutive page reloads

open_btn.addEventListener('click', function()
{
	index_0 = 0;
	total = 0;
  lines = $('textarea').val().split('\n');

  total = lines.length;

	if(delay == 0 && lines.length > 0)
	{

		//var default_opt = document.getElementById('default');
		//var http_opt = document.getElementById('http');
		//var https_opt = document.getElementById('https');

		//if(default_opt.checked==true)
		//{
			for(var i = 0;i < lines.length;i++)
			{
				var url = lines[i];
				url = addhttp(url);
				if(url!="")
				window.open(url, '_blank');
			}
		//}
		/*else if(http_opt.checked==true)
		{
			for(var i = 0;i < lines.length;i++)
			{
				if(lines[i]!="")
				window.open("http://"+lines[i], '_blank');
			}
		}

		else if(https_opt.checked==true)
		{
			for(var i = 0;i < lines.length;i++)
			{
				if(lines[i]!="")
				window.open("https://"+lines[i], '_blank');
			}
		}*/
	}
	else if(delay > 0 && lines.length > 0)
	{
		poll();
	}

}, false);

function addhttp(url) {

   if (!/^(f|ht)tps?:\/\//i.test(url)) {
      url = "http://" + url;
   }
   return url;
}

//window.open(url,name) where if name is _blank, it opens in new tab, if name is _self, it opens in same tab and stops and if name is anything like
//_name_, it keeps on loading on the same tab since we refer it using the same name we assigned

function poll()
{
	if(delay > 0 && total > 0 && index_0 < total)
	{

		//var default_opt = document.getElementById('default');
		//var http_opt = document.getElementById('http');
		//var https_opt = document.getElementById('https');

		//if(default_opt.checked==true)
		//{
			var url = lines[index_0];
			//var index = tab.index + 1;
			url = addhttp(url);
			if(url!="")
			//chrome.tabs.create({'url': url, 'index': 1});
			window.open(url, 'MsgWindow');
		//}
		/*else if(http_opt.checked==true)
		{
			if(lines[index_0]!="")
			window.open("http://"+lines[index_0], '_blank');
		}

		else if(https_opt.checked==true)
		{
			if(lines[index_0]!="")
			window.open("https://"+lines[index_0], '_blank');
		}*/
		index_0++;
		setTimeout(poll, delay * 1000);
	}
};
