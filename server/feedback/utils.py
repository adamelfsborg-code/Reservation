from server import db 

class AddCommentToRestaurant:
    def post(self, **kwargs):
        sql = "INSERT INTO comments (user_id, restaurant_id,comment) VALUES (%s,%s,%s)"
        sqldata = (kwargs['user_id'],kwargs['restaurant_id'],kwargs['comment'])

        c = db.Cursor('reservate', sql, sqldata)
        addCommentToRestaurant = c.connect()

        if 'no results to fetch' in addCommentToRestaurant:
            return '200'
        return '400' 

class AddRatingToRestaurant:
    def post(self, **kwargs):
        sql = "INSERT INTO ratings (user_id,restaurant_id,rating) VALUES (%s,%s,%s)"
        sqldata = (kwargs['user_id'],kwargs['restaurant_id'],kwargs['rating'])

        c = db.Cursor('reservate', sql, sqldata)
        addRatingToRestaurant = c.connect()

        if 'no results to fetch' in addRatingToRestaurant:
            return '200'
        return '400'

class SubmitReportToRestaurant:
    def post(self, **kwargs):
        sql = "INSERT INTO report (user_id,restaurant_id,type_of_msg,message) VALUES (%s,%s,%s,%s)"
        sqldata = (kwargs['user_id'],kwargs['restaurant_id'],kwargs['type_of_msg'],kwargs['message'])

        c = db.Cursor('reservate', sql, sqldata)
        submitReportToRestaurant = c.connect()

        if 'no results to fetch' in submitReportToRestaurant:
            return '200'
        return '400'

class GetAllCommentsForRestaurant:
    def get(self, id):
        sql = f"SELECT COMMENTS.id,user_id,restaurant_id,COMMENT,COMMENTS.created_at, full_name,profile_image FROM COMMENTS FULL JOIN users ON COMMENTS.user_id = users.id WHERE restaurant_id={id}"
        sqldata = ()

        c = db.Cursor()
        getAllCommentsForRestaurant = c.connect()

        comments = {
            'comment': []
        }

        if len(getAllCommentsForRestaurant) > 0:
            for i in getAllCommentsForRestaurant:
                comments['comment'].append(i)
            return comments
        return '404'

class GetAvgRatingForRestaurant:
    def get(self, id):
        sql = f"SELECT avg(rating) FROM ratings WHERE restaurant_id={id}"
        sqldata = ()

        c = db.Cursor('reservate', sql, sqldata)
        getAvgRatingForRestaurant = c.connect()

        ratings = {
            'rating': []
        }

        if len(getAvgRatingForRestaurant) > 0:
            for i in getAvgRatingForRestaurant:
                ratings['rating'].append(i)
            return ratings
        return '404'

class GetReportsForRestaurant:
    def get(self, id):
        sql = f"SELECT report.id,user_id,restaurant_id,type_of_msg,message,report.created_at,full_name, profile_image,location FROM report FULL JOIN users ON report.user_id = users.id restaurant_id={id} ORDER BY report.created_at DESC"
        sqldata = ()

        c = db.Cursor('reservate', sql, sqldata)
        getReportsForRestaurant = c.connect()

        reports = {
            'report': []
        }

        if len(getReportsForRestaurant) > 0:
            for i in getReportsForRestaurant:
                reports['report'].append(i)
            return reports
        return '404'