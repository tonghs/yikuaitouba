vm_video = new Vue({
    el: '#video-form'
    data: {
        link: ''
    }
    methods: {
        submit: ->
            $.ajax(
                url: '/admin/video'
                data: this.$data
                method: 'POST'
                success: ->
                    vm_video.link= ''
                error: ->
            )
    }
})
