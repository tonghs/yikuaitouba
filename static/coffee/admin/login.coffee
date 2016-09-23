vm_login = new Vue({
    el: '#login-form'
    data: {
        user: ''
        pwd: ''
    }
    methods: {
        login: ->
            if this.user and this.pwd
                $.ajax(
                    url: '/j/admin/login'
                    data: this.$data
                    method: 'POST'
                    success: (o)->
                        if o.result
                            vm_login.user = ''
                            vm_login.pwd = ''
                            location.href = '/admin/index'
                        else
                            alert o.msg
                    error: ->
                )
    }
})
