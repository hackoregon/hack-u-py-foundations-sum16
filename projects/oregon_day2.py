player1 = input('What is your name?: ')
player2 = input('What is your player2 name?: ')
player3 = input('What is your player3 name?: ')
player4 = input('What is your player4 name?: ')
player5 = input('What is your player5 name?: ')

inventory = {
	'oxen':5,
	'bullets':1000,
	'clothes':15,
	'food':1000,
	'spare parts':{
		'wagon wheel':2,
		'wagon axles':2,
		'wagon tongue':2}
	}
costs = {
	'oxen':40,
	'bullets':2,
	'clothes':10,
	'food':.2,
	'spare parts':{
		'wagon wheel':10,
		'wagon axles':10,
		'wagon tongue':10}
	}

print(inventory)


