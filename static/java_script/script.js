
		$(document).ready(function() {
		var NavY = $('header').offset().top;
	 
		var stickyNav = function(){
		var ScrollY = $(window).scrollTop();
		  
		if (ScrollY > NavY) { 
			$('header').addClass('sticky');
		} else {
			$('header').removeClass('sticky'); 
		}
		};
	 
		stickyNav();
	 
		$(window).scroll(function() {
		stickyNav();
		});
		});
	
