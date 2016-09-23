window.set_data = (data)->
    vm_project = new Vue({
        el: '#project-form'
        data: data
        methods: {
            submit: ->
                $.ajax(
                    url: '/admin/edit_project'
                    data: this.$data
                    method: 'POST'
                    success: ->
                        location.reload()
                    error: ->
                )
        }
    })
