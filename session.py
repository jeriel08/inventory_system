# session.py
class ActiveUser:
    user_id = None
    username = None
    password = None
    contact_number = None
    email = None
    birthdate = None
    gender = None

    @classmethod
    def set_user(cls, user_id, username, password, contact_number, email, birthdate, gender):
        cls.user_id = user_id
        cls.username = username
        cls.password = password
        cls.contact_number = contact_number
        cls.email = email
        cls.birthdate = birthdate
        cls.gender = gender

    @classmethod
    def clear_user(cls):
        cls.user_id = None
        cls.username = None
        cls.password = None
        cls.contact_number = None
        cls.email = None
        cls.birthdate = None
        cls.gender = None
