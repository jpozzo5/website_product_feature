# -*- coding: utf-8 -*-
{
    'name': "Caracteristicas de productos",

    'summary': """
        Agrega nuevas caracteristicas en el producto en el sitio web y plantilla de producto del backoffice,

        """,

    'description': """
        
    """,

    'author': "Jesus pozzo",
    'website': "",


    'category': 'web',
    'version': '12.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','web','website','website_sale','sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/inherit_product_template.xml',
        'views/product_template_feature.xml',

    ],

}