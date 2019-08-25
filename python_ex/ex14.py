from sys import argv

script, user_name = argv

prompt = ">"

print ("Hi %s ,I'm the %s script." % (user_name, script))

print ("I'd like to ask you to few questions.")

print ("Do you like me %s ?" % (user_name))

likes = input(prompt)

print ("Where do you live %s?" % (user_name))

lives = input(prompt)

print ("What kind of computer do you have %s ?" % (user_name))

computers = input(prompt)

print ("""
	Alright, so you said %s about liking me.
	You live in %s. Not sure where that is.
	And you have a %s Computer.Nice.
	""" % (likes, lives, computers))