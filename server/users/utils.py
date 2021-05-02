from server import db 

class CreateUser:
    def post(self, **kwargs):
        sql = "INSERT INTO users (full_name,email,phone_number,password) VALUES (%s,%s,%s,%s)"
        sqldata = (kwargs['full_name'], kwargs['email'],kwargs['phone_number'],kwargs['password'])

        c = db.Cursor('reservate', sql, sqldata)
        createUser = c.connect()

        if 'no results to fetch' in createUser:
            return '200'
        return '400'

    def get(self, email,phone_number):
        sql = f"SELECT id FROM users WHERE email={email} OR phone_number={phone_number}"
        sqldata = ()

        c = db.Cursor('reservate', sql, sqldata)
        getEmailOrPhoneNumber = c.connect()
        
        if len(getEmailOrPhoneNumber) > 0:
            return '400'
        return '200'

class LoginUser:
    def put(self, id,token):
        sql = f"UPDATE users SET token={token} WHERE id={id} RETURNING id"
        sqldata = ()

        c = db.Cursor('reservate', sql, sqldata)
        loginUser = c.connect()

        if len(loginUser) > 0:
            for i in loginUser:
                id = i.get('id')
            return id
        return '400'

    def get(self, **kwargs):
        sql = f"SELECT id FROM users WHERE email=%s AND password=%s"
        sqldata = (kwargs['email'], kwargs['password'])

        c = db.Cursor('reservate', sql, sqldata)
        getUserId = c.connect()
        
        if len(getUserId) > 0:
            for i in getUserId:
                id = i.get('id')
            return self.put(id, kwargs['token'])
        return '400'
    
class LogoutUser:
    def put(self, id):
        sql = f"UPDATE users SET token='null' WHERE id={id}"
        sqldata = ()

        c = db.Cursor('reservate', sql, sqldata)
        logoutUser = c.connect()

        if 'no results to fetch' in logoutUser:
            return '200'
        return '400'