driving = input('你有沒有開過車?')
if driving != '有' and driving != '沒有':
	print('只能輸入 有/沒有')
	raise SystemExit

age = input('你今年幾歲了?')
age = int(age)
if driving == '有':
	if age >= 18:
		print ('你通過測試了')
	else:
		print ('你還不能開車')
elif driving != '有':
	if age >= 18:
		print ('你可以考駕照了')
	else:
		print ('你還不能考駕照')