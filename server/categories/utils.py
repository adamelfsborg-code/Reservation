from server import db 

class GetAllCategories:
    def get(self,id):
        sql = "SELECT * FROM categories"
        sqldata = ()

        c = db.Cursor('reservate', sql, sqldata)
        getAllCategories = c.connect()

        g = {
            "categories": [],
            "pinned_categories": []
        }

        if len(getAllCategories) > 0:
            for i in getAllCategories:
                g['categories'].append(i)

            p = GetPinnedCategories()
            pinned = p.get(id)
            if pinned != '404':
                g['pinned_categories'].append(pinned)
            return g 
        return '404'    

class GetPinnedCategories:
    def get(self, id):
        sql = f"SELECT pinned_categories.id,category_id,pinned_categories.created_at,title FROM pinned_categories FULL JOIN categories ON pinned_categories.category_id = categories.id WHERE user_id={id}"
        sqldata = ()

        c = db.Cursor('reservate', sql, sqldata)
        getPinnedCategories = c.connect()

        if len(getPinnedCategories) > 0:
            for i in getPinnedCategories:
                return i
        return '404'            

class PinCategory:
    def post(self, **kwargs):
        sql = "INSERT INTO pinned_categories (user_id, category_id) VALUES (%s,%s)"
        sqldata = (kwargs['user_id'], kwargs['category_id'])

        c = db.Cursor('reservate', sql, sqldata)
        pinCategory = c.connect()

        if 'no results to fetch' in pinCategory:
            return '200'
        return '400'