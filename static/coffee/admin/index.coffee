vm_project = new Vue({
    el: '#project-form'
    data: {
        name: ''
        url: ''
        logo: ''
        investor: '0'
    }
    methods: {
        submit: ->
            $.ajax(
                url: '/admin/project'
                data: this.$data
                method: 'POST'
                success: ->
                    vm_project.name = ''
                    vm_project.url = ''
                    vm_project.logo = ''
                    vm_project.investor = '0'
                error: ->
            )
    }
})
