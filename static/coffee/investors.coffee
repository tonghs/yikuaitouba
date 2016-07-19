$('.main-slider').unslider( {
    # autoplay: true
    infinite: true
    arrows: false
    delay: 5000
})

window.scroll = (id)->
	$('html,body').animate({
		scrollTop:$("##{id}").offset().top
	},800)
