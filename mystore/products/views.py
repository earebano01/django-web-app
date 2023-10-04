# from django.http import HttpResponse
from django.shortcuts import render
from products.models import Products

def products(request):
    products = Products.objects.all()
    return render(request, 'products/products.html', 
                  {'product_info': products})
#     return HttpResponse(f"""
        # <!DOCTYPE html>
        #     <html>
        #     <head>
        #         <title>HTML Table Generator</title> 
        #         <style>
                    
        #         </style>
        #     </head>
        #     <body>
        #         <table>
        #             <thead>
        #                 <tr>
        #                     <th>PRODUCT NAME</th>
        #                     <th>DESCRIPTION</th>
        #                     <th>PRICE</th>
        #                     <th>STOCK</th>
        #                     <th>DATE</th>
        #                     <th>TIME</th>
        #                     <th>STATUS</th>
        #                     <th>LAST ORDER</th>
        #                     <th>SUPPLIER WEBSITE</th>
        #                     <th>SUPPLIER CONTACT</th>
        #                 </tr>
        #             </thead>
        #             <tbody>
        #                 <tr>
        #                     <td>{products[0].title}</td>
        #                     <td>{products[0].description}</td>
        #                     <td>{products[0].price}</td>
        #                     <td>{products[0].stock}</td>
        #                     <td>{products[0].date}</td>
        #                     <td>{products[0].time}</td>
        #                     <td>{products[0].status}</td>
        #                     <td>{products[0].lastorder}</td>
        #                     <td>{products[0].s_website}</td>
        #                     <td>{products[0].s_contact}</td>
        #                 </tr>
        #                 <tr>
        #                     <td>{products[1].title}</td>
        #                     <td>{products[1].description}</td>
        #                     <td>{products[1].price}</td>
        #                     <td>{products[1].stock}</td>
        #                     <td>{products[1].date}</td>
        #                     <td>{products[1].time}</td>
        #                     <td>{products[1].status}</td>
        #                     <td>{products[1].lastorder}</td>
        #                     <td>{products[1].s_website}</td>
        #                     <td>{products[1].s_contact}</td>
        #                 </tr>
        #                 <tr>
        #                     <td>{products[2].title}</td>
        #                     <td>{products[2].description}</td>
        #                     <td>{products[2].price}</td>
        #                     <td>{products[2].stock}</td>
        #                     <td>{products[2].date}</td>
        #                     <td>{products[2].time}</td>
        #                     <td>{products[2].status}</td>
        #                     <td>{products[2].lastorder}</td>
        #                     <td>{products[2].s_website}</td>
        #                     <td>{products[2].s_contact}</td>
        #                 </tr>
        #                 <tr>
        #                     <td>{products[3].title}</td>
        #                     <td>{products[3].description}</td>
        #                     <td>{products[3].price}</td>
        #                     <td>{products[3].stock}</td>
        #                     <td>{products[3].date}</td>
        #                     <td>{products[3].time}</td>
        #                     <td>{products[3].status}</td>
        #                     <td>{products[3].lastorder}</td>
        #                     <td>{products[3].s_website}</td>
        #                     <td>{products[3].s_contact}</td>
        #                 </tr>
        #             </tbody>
        #         </table>
        #     </body>
        #     </html>
# """)
