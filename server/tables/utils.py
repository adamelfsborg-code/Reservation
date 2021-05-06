from server import db 


class CreateTable:
    def post(self, **kwargs):
        sql = "INSERT INTO tables (restaurant_id,seats_quantity,table_nr) VALUES (%s,%s,%s)"
        sqldata = (kwargs['restaurant_id'],kwargs['seats_quantity'],kwargs['table_nr'])

        c = db.Cursor('reservate', sql, sqldata)
        createTable = c.connect()

        if 'no results to fetch' in createTable:
            return '200'
        return '404'

        