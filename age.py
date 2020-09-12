driving = input('請問你開過車嗎?')
if driving != '有' and driving != '沒有':
	print('請輸入有或沒有，謝謝。')
	raise SystemExit

age = input('請問你的年齡?')
age = int(age)
if driving == '有':
	if age > 18:
		print('你考過駕照了對吧?')
	else:
		print('嗯?怎麼會?')
elif driving =='沒有':
	if age > 18:
		print('考慮學開車嗎?')
	else:
		print('等成年後就可以學開車了喔!')