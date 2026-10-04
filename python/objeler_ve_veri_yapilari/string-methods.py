message = 'Hello There. My name is Nuri Yıldız.'

#message = message.upper()
#message = message.lower()
#message = message.title()
#message = message.capitalize()

#message = message.strip() #boşluları siler. rstrip sondaki lstrip baştaki boşluğu siler
#message = message.split('.')
#message = message.split()
#message = '--'.join(message)

#index= message.find('Nuri')
isFound = message.startswith('H') #endswith

message = message.replace('Nuri','Hazar')

message = message.center(100, '*') #ljust, rjust
message = message.replace('.','') 


print(message)
#print(index)
#print(message[1])
#print(isFound)