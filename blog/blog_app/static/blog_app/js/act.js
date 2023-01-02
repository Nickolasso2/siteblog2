document.querySelectorAll('.menu a').forEach(element => {
	var location = window.location.href;
	var link = element.href; 
	if(location == link) {
		element.parentElement.classList.add('active');
	}
	else{
		element.parentElement.classList.remove('active');
	};	
});