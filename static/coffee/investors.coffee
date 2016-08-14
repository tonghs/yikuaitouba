$('.main-slider').unslider( {
    autoplay: true
    infinite: true
    arrows: false
    delay: 5000
})

$('.trends-slider').unslider( {
    autoplay: true
    arrows: false
    delay: 2000
})

window.scroll = (id)->
	$('html,body').animate({
		scrollTop:$("##{id}").offset().top
	},800)


$("#play").fancybox({
    padding: 0
    width: 800
    height: 490
})
