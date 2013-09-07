""" sequence membership eg for list and in operator  """

database = [['albert', '1234'],['dilbert', '4242'],
           ['smith', '7524'], ['jones', '9843']]

username = raw_input('Enter username: ')
pin = raw_input('Pin: ')

if [username, pin] in database:
    print "Access granted"
    
