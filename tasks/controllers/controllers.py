from odoo import http
from odoo.http import request

class CarRental(http.Controller):
    @http.route(['/car/rental'], type="http",auth="public",website=True, csrf=False) 
    #['/car/rental'] is a url name.. need to be same with TEEMPLETE id of xml
    def carr_rental(self):
        print('carr control')
        caar = request.env['tasks.carrental'].search([])
        return request.render('tasks.car_rental_template',{'caar':caar})
        # 
        # car_rental_template ==== templete id


class CarImage(http.Controller):

    @http.route('/car/image', type='http', website=True, auth="public")
    def car_image(self, **kwargs):
        return request.render('tasks.car_images_template')