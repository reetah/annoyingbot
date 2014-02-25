import time
import praw
import string


r = praw.Reddit(user_agent ='Tester annoying bot')
r.login('whydoyoulovetrp', 'trptrptrp')
print "login success \n"
while True:
	time.sleep(5)
	comments = r.get_comments('badphilosophy')
	t = 0
	for t in range(10000):
		live = next(comments)
		print t
		#thing = live.get_info(id)
		if live.author.name=='lawofmurray':
			live.reply('Why do you love TRP so much?')
			print('found him!')