from server import db 


class CreateMenuForRestaurant:
    def post(self, **kwargs):
        sql = "INSERT INTO menus (restaurant_id,food,drink,dessert) VALUES(%s,%s,%s)"
        sqldata = (kwargs['restaurant_id'], kwargs['food'], kwargs['drink'],kwargs['dessert'])

        c = db.Cursor('reservate', sql, sqldata)
        createMenu = c.connect()

        if 'no results to fetch' in createMenu:
            return '200'
        return '400'

class GetMenuForRestaurant:
    def get(self, id):
        sql = f"SELECT * FROM menus where restaurant_id={id}"
        sqldata = ()

        c = db.Cursor('reservate', sql, sqldata)
        getMenuForRestaurant = c.connect()

        menus = {
            'menu': []
        }

        if len(getMenuForRestaurant) > 0:
            for i in getMenuForRestaurant:
                menus['menu'].append(i)
            return menus 
        return '404'