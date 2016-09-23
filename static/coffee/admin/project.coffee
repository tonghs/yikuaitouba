window.del = (id)->
    if confirm('是否删除')
        $.ajax(
            url: '/admin/del_project'
            data: {id: id}
            method: 'POST'
            success: (o)->
                location.reload()
            error: ->
        )
