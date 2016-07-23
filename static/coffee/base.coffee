$(window).scroll( ->
	if $(window).scrollTop() > 60
		$('#scroll-to-top').css('display', 'inherit')
	else
		$('#scroll-to-top').css('display', 'none')
)
