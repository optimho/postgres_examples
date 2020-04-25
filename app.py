from user import User
from database import Database

Database.initialise(user='postgres', password='Blackmamba', host='localhost', database='Learning')

the_user = User(email="Terri@yahoo.com", first_name='Terri', last_name='Fetting', _id=None)
the_user.store_in_database()

the_user = User.read_out_database_by_email('skye@duplessis.nz')
print(the_user)
print('name={}  surname={}'.format(the_user.first_name, the_user.last_name))






