// var name = '{{jobId|tojson}}'
// data = JSON.parse(name.slice(1,name.length-1))
// var pathname = window.location.pathname;
// var heading = pathname.split('/')[3].split('-')[0][0].toUpperCase(0) + pathname.split('/')[3].split('-')[0].substring(1)
// console.log(data)
$('#heading').append('<h3>'+heading+' Recruitment 2021 For '+data['title']+'</h3>')
$('#jobTitle').append('<h5><strong>Job Title - </strong>'+data['title']+'</h5>')
$('#jobLocation').append('<h5><strong>Location - </strong>'+data['location']+'</h5>')
$('#jobexperience').append('<h5>Experience - <span>'+data['experience']+'</span></h5>')
$('#jobBody').append(decodeEntities(data["description1"]))
$('.applyButton').append('<a href="'+data["urlLink"]+'" class="btn btn-primary btn-lg active" role="button" aria-pressed="true"> Apply </a>')

function decodeEntities(encodedString) {
  var textArea = document.createElement('textarea');
  textArea.innerHTML = encodedString;
  return textArea.value;
}