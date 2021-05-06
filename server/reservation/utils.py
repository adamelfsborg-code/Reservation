from server import db 


class ReservateTable:
    def post(self, **kwargs):
        sql = "INSERT INTO reservation (user_id,id) VALUES (%s,%s)"
        sqldata = (kwargs['user_id'], kwargs['id'])
        
        c = db.Cursor('reservate', sql, sqldata)
        reservateTable = c.connect()

        if 'no results to fetch' in reservateTable:
            return '200'
        return '404'




