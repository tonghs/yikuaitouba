$('.main-slider').unslider( {
    autoplay: true
    infinite: true
    arrows: false
    delay: 5000
})

$('.trends-slider').unslider( {
    autoplay: true
    arrows: false
    delay: 1500
})

window.scroll = (id)->
	$('html,body').animate({
		scrollTop:$("##{id}").offset().top
	},800)


