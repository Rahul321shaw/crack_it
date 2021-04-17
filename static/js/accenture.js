//--------------jobList javaScript--------------------------------------------------------------------
if(window.location.pathname.split('/').length == 3){
	var response
	var data = JSON.stringify({
	  "name":name});
	var xhr = new XMLHttpRequest();
	xhr.withCredentials = true;
	xhr.addEventListener("readystatechange", function () {
	  if (this.readyState === 4) {
	    response = JSON.parse(this.response)
	    console.log(response);
	    for (var key in response) {
	    	var el = document.createElement( 'html' );
	    	el.innerHTML = response[key]['jobDescription']
	    	text = el.getElementsByTagName("ul")[1].childNodes[3]
	    $('.list').append('<div class="card">\
	    	<a href="./'+name+'/'+key+'">\
				  <h5 class="card-header">'+response[key]['title']+'</h5></a>\
				  <span align="right"><strong>Posted -</strong><i>'+response[key]['postedDate'].split("T")[0]+'\
				  <strong>Location -</strong><i>'+response[key]['location']+','+response[key]['country']+'</i></span>\
				  <div class="card-body">\
				    <p class="card-text">'+text.innerHTML+'</p>\
				    <a href="./'+name+'/'+key+'" class="btn btn-dark">Apply</a>\
				  </div>\
				</div><br>');
	 
		    
		}
	  }
	});
	xhr.open("POST", "/getjobData");
	xhr.setRequestHeader("content-type", "application/json");
	xhr.setRequestHeader("cache-control", "no-cache");
	// xhr.setRequestHeader("postman-token", "da179bdb-fc5a-9b6c-aa30-fffa130ffb2a");
	xhr.send(data);

}

//--------------jobDetails javaScript--------------------------------------------------------------------
if (window.location.pathname.split('/').length == 4) {

	// var name = '{{jobId|tojson}}'
	// data = JSON.parse(name.slice(1,name.length-1))
	// var pathname = window.location.pathname;
	// var heading = pathname.split('/')[3].split('-')[0][0].toUpperCase(0) + pathname.split('/')[3].split('-')[0].substring(1)
	// console.log(data)
	$('#heading').append('<h3>'+heading+' Recruitment 2021 For '+data['title']+'</h3>')
	$('#jobTitle').append('<h5><strong>Job Title - </strong>'+data['title']+'</h5>')
	$('#jobLocation').append('<h5><strong>Location - </strong>'+data['location']+'</h5>')
	// $('#jobexperience').append('<h5>Experience - <span>'+data['experience']+'</span></h5>')
	$('#jobBody').append(decodeEntities(data['jobDescription']))
	$('.applyButton').append('<a href="'+data["jobDetailUrl"].replace('{0}',"in-en")+'" class="btn btn-primary btn-lg active" role="button" aria-pressed="true"> Apply </a>')

	function decodeEntities(encodedString) {
	  var textArea = document.createElement('textarea');
	  textArea.innerHTML = encodedString;
	  return textArea.value;
	}
}