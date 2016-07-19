$('#alipay-pc').click ->
	$.post('/j/pay/charge', {channel: 'alipay_pc_direct'}, (res)->
		console.log res
		pingppPc.createPayment(JSON.stringify(res), (result, err) ->
			console.log(result)
			console.log(err.msg)
			console.log(err.extra)
		)
	)

$('#alipay-mobile').click ->
	$.post('/j/pay/charge', {channel: 'alipay_wap'}, (res)->
		console.log res
		pingpp.createPayment(JSON.stringify(res), (result, err) ->
			console.log(result)
			console.log(err.msg)
			console.log(err.extra)
		)
	)
