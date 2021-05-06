from server import db 


class GetRestaurantsByCategory:
    def get(self, id):
        sql = f"SELECT restaurants.id, category_id,background_cover,location,name,opening_hours,description,restaurants.created_at, title FROM restaurants FULL JOIN categories ON restaurants.category_id = categories.id WHERE categories.id={id} ORDER BY restaurants.created_at DESC"
        sqldata = ()

        c = db.Cursor('reservate', sql, sqldata)
        getRestaurantsByCategory = c.connect()

        restaurants = {
            'restaurant': []
        }

        if len(getRestaurantsByCategory) > 0:
            for i in getRestaurantsByCategory:
                restaurants['restaurant'].append(i)
            
            return restaurants
        return '404'

class GetNearestRestaurants:
    def get(self, id):
        sql = f"SELECT r1.id,r1.background_cover, r1.location,r1.name,r1.opening_hours,r1.description,r1.created_at FROM RESTAURANTS r1 INNER JOIN (SELECT * FROM users WHERE id={id} ) AS u2 ON r1.id = u2.id WHERE r1.LOCATION ->> 'Street' = u2.LOCATION ->> 'Street' OR r1.LOCATION ->> 'City' = u2.LOCATION ->> 'City' OR r1.LOCATION ->> 'Region' = u2.LOCATION ->> 'Region' OR r1.LOCATION ->> 'Country' = u2.LOCATION ->> 'Country'"
        sqldata = ()

        c = db.Cursor('reservate', sql, sqldata)
        getNearestRestaurants = c.connect()

        restaurants = {
            'restaurant': []
        }
    
        if len(getNearestRestaurants) > 0:
            for i in getNearestRestaurants:
                restaurants['restaurant'].append(i)
        return '404'

        