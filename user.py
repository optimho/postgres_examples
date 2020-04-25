from database import db_cursor_connection_from_pool


class User:
    def __init__(self, email, first_name, last_name, _id):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.id = _id

    def __repr__(self):
        return "<User {} >".format(self.first_name)

    def store_in_database(self):
        with db_cursor_connection_from_pool() as cursor:
            cursor.execute('INSERT INTO users (email, firstname, lastname ) VALUES (%s, %s, %s )', (self.email,
                                                                                                self.first_name,
                                                                                                self.last_name))



    @classmethod
    def read_out_database_by_email(cls, email):
        with db_cursor_connection_from_pool() as cursor:
            cursor.execute('SELECT * FROM users WHERE email=%s', (email,))
            return_data = cursor.fetchone()
            return cls(email=return_data[1], last_name=return_data[3], first_name=return_data[2], _id=return_data[0])
