from project.config.Database import connection
from flask import jsonify


class Mobile:

    def __init__(self):
        self.conn = connection()
        self.cursor = self.conn.connection.cursor(dictionary=True)

    def add_mobile(self, params):
        val = "'{}'".format(params['mobile_id'])
        val2 = "'{}'".format(params['cat_id'])
        self.cursor.execute("INSERT INTO mobilaty.mobile" +
                            " (mobile_id , mobile_name ,cat_id,display_size,main_camera,selfie_camera,chipset,storage_and_ram,battary,price)" +
                            " VALUES (" + val + ",'" + params['mobile_name'] +
                            "'," + val2+ ",'" + params['display_size'] + "','" + params['main_camera']
                           + "','" + params['selfie_camera'] + "','" + params['chipset'] + "','" + params['storage_and_ram']
                           + "','" + params['battary'] + "','" + params['price']+ "')")
        self.conn.connection.commit()

    def delete_mobile(self, params):
        val = "'{}'".format(params['mobile_id'])
        self.cursor.execute('DELETE FROM  mobilaty.mobile WHERE mobile_id= ' +val)
        self.conn.connection.commit()
        # row = cursor.fetchone()

    def show_AllMobile(self):
        self.cursor.execute('SELECT * FROM mobilaty.mobile')
        row = self.cursor.fetchall()
        return row

    def update_mobile(self, params):
        val = "'{}'".format(params['mobile_id'])
        val2 = "'{}'".format(params['cat_id'])
        self.cursor.execute("update mobilaty.mobile set mobile_name = '" +
                            params['mobile_name'] + "'and cat_id= " +
                            params['cat_id'] +
                            + " and display_size= '" + params['display_size'] 
                            + "'and main_camera= '" + params['main_camera']
                            + "'and selfie_camera= '" + params['selfie_camera']
                            + "'and chipset= '" + params['chipset']
                            + "'and storage_and_ram= '" + params['storage_and_ram']
                            + "'and battary= '" + params['battary']
                            + "'and price= '" + params['price']+ "' where mobile_id = " + val)
        self.conn.connection.commit()

    def show_mobile(self, params):
        val = "'{}'".format(params['mobile_id'])
        self.cursor.execute('SELECT * FROM mobilaty.mobile WHERE mobile_id = ' + val + " ORDER BY RAND()")
        row = self.cursor.fetchall()
        return row

    def findByMobileId(self, params):
        val = "'{}'".format(params['mobile_id'])
        self.cursor.execute('SELECT * FROM mobilaty.mobile WHERE mobile_id = ' + val)
        row = self.cursor.fetchall()
        return row
