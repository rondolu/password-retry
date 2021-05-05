password = '123456'
chance = 3
while chance > 0:
	pwd = input('請輸入密碼')
	if pwd == password:
		print('登入成功!')
		break
	else:
		chance = chance - 1
		print('密碼錯誤! 還有', chance, '次機會')