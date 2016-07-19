(function($) { 
$.fn.acSlides = function(){ 
    //slides
    $(".slides").each(function(){
        var _this = $(this),
            _wraper = _this.find(".slides_wraper"),
            _slide = _wraper.find(".slides_li"),
            _width = _this.width(),
            _height = _this.height(),
            _num = _slide.length;
        //初始化
        _wraper.css("width",_width*_num+"px");
        _slide.css({
            "width":_width+"px",
            "height":_height+"px",
        });
        var _html = '<div class="slides_nav"><ul>';
        for(i=0;i<_num;i++){
            _html += '<li><a href="javascript:void(0);"></a></li>'
        }
        _html += '</ul></div>';
        $(_html).appendTo(_this);
        
        var _nav = _this.find(".slides_nav"),
            _dots = _nav.find("a"); 
        
        _dots.eq(0).addClass("current");
        //绑定事件
        _nav.on('click','a',function(){
            _dots.removeClass("current");
            $(this).addClass("current");
            var index = _dots.index(this);
            _wraper.css("left",_width*index*-1+"px");
        })
    })
}; 
})(jQuery); 
