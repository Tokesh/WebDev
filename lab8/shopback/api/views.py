from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse,JsonResponse
from django.shortcuts import render
from django.core import serializers
from django.forms.models import model_to_dict
import json
from .models import Product, Category


#products = [{"id":1,"name":"iPhone 12 Pro Max","price":969,"description":"Wireless carrier\tUnlocked for All Carriers\nBrand\tApple\nMemory storage capacity\t128 GB\nOperating system\tIOS 14\nColour\tGraphit\nModel year\t2020","rating":4.2,"imageSrc":"https://m.media-amazon.com/images/I/71Ujb4adTRL._AC_SL1500_.jpg","amazonLink":"https://www.amazon.de/-/en/A2411/dp/B08PCDHMWQ/ref=sr_1_4?crid=2BJAVEKRLH4LE&keywords=iphone+13+pro+max&qid=1646431415&rnid=1703609031&s=telephone&sprefix=iphone+13+pro+ma%2Caps%2C167&sr=1-4","prodcategory":"1","shows":True,"likes":0},{"id":2,"name":"iPhone 11 Pro Max","price":732,"description":"Model name\tApple iPhone 11 Pro Max\nWireless carrier\tUnlocked\nBrand\tApple\nForm factor\tTouchscreen\nMemory storage capacity\t256 GB\nOperating system\tIOS","rating":4.1,"imageSrc":"https://m.media-amazon.com/images/I/81nxsVyBAlL._AC_SL1500_.jpg","amazonLink":"https://www.amazon.de/-/en/dp/B082DK5W6Z/ref=sr_1_2?crid=2BJAVEKRLH4LE&keywords=iphone%2B13%2Bpro%2Bmax&qid=1646431466&rnid=1703609031&s=telephone&sprefix=iphone%2B13%2Bpro%2Bma%2Caps%2C167&sr=1-2&th=1","prodcategory":1,"shows":True,"likes":0},{"id":3,"name":"iPhone XS","price":782,"description":"Model name\tApple iPhone XS 64GB\nWireless carrier\tUnlocked\nBrand\tApple\nForm factor\tSmartphone\nMemory storage capacity\t64 GB\nOperating system\tIOS","rating":4,"imageSrc":"https://m.media-amazon.com/images/I/512F7mwDVyL._AC_SL1024_.jpg","amazonLink":"https://www.amazon.de/-/en/Apple-iPhone-XS-Refurbished-64GB/dp/B07N9HM3Z4/ref=sr_1_1?crid=ULNFHA2GVAWW&keywords=iphone+XS&qid=1646431885&sprefix=iphone+xs%2Caps%2C160&sr=8-1","prodcategory":1,"shows":True,"likes":0},{"id":4,"name":"iPhone XR","price":347,"description":"Model name\tApple iPhone XR 64GB\nWireless carrier\tUnlocked\nBrand\tApple\nForm factor\tSmartphone\nMemory storage capacity\t64 GB\nOperating system\tIOS","rating":4.3,"imageSrc":"https://object.pscloud.io/cms/cms/Photo/img_0_77_2752_3_1.jpg","amazonLink":"https://www.amazon.de/-/en/Apple-iPhone-XR-64GB-Refurbished/dp/B07N9HM3ZR/ref=sr_1_1?crid=3H4FU87DVRT1T&keywords=iphone&qid=1646432054&sprefix=iphone%2Caps%2C179&sr=8-1&th=1","prodcategory":1,"shows":True,"likes":0},{"id":5,"name":"iPhone X","price":485,"description":"Model name\tIPhone X\nWireless carrier\tUnlocked for All Carriers\nBrand\tApple\nForm factor\tBar\nMemory storage capacity\t256 GB","rating":4,"imageSrc":"https://m.media-amazon.com/images/I/51pQi346XcL._AC_SL1154_.jpg","amazonLink":"https://www.amazon.de/-/en/X_PARENT/dp/B0797Q5771/ref=sr_1_6?crid=3H4FU87DVRT1T&keywords=iphone&qid=1646432054&sprefix=iphone%2Caps%2C179&sr=8-6","prodcategory":1,"shows":True,"likes":0},{"id":6,"name":"Apple iPhone 8 64GB Silver","price":230,"description":"Model name\tIPhone 8\nWireless carrier\tAu\nBrand\tApple\nForm factor\t1\nMemory storage capacity\t64 GB","rating":4.2,"imageSrc":"https://m.media-amazon.com/images/I/41I4w-DDABL._AC_.jpg","amazonLink":"https://www.amazon.de/-/en/MQ6H2B-A_64/dp/B0797P5BCV/ref=sr_1_12?crid=3H4FU87DVRT1T&keywords=iphone&qid=1646432054&sprefix=iphone%2Caps%2C179&sr=8-12","prodcategory":1,"shows":True,"likes":0},{"id":7,"name":"iPhone 7","price":158,"description":"Model name\tIPhone 7\nWireless carrier\tUnlocked\nBrand\tApple\nForm factor\tSmartphone\nMemory storage capacity\t32 GB\nOperating system\tIOS","rating":4,"imageSrc":"https://m.media-amazon.com/images/I/51rxj5TepeL._AC_.jpg","amazonLink":"https://www.amazon.de/-/en/Apple-iPhone-refurbished-32GB-Black/dp/B01N9VBVN1/ref=sr_1_2?crid=3H4FU87DVRT1T&keywords=iphone&qid=1646432054&sprefix=iphone%2Caps%2C179&sr=8-2&th=1","prodcategory":1,"shows":True,"likes":0},{"id":8,"name":"Samsung Galaxy A12","price":201,"description":"Display: 6,5 Zoll (16,63 cm)\nHauptkamera: 48 + 5 + 2 + 2 MP\nSpeicher: 128 GB / 4 GB RAM\nAkku: 5000 mAh","rating":4.5,"imageSrc":"https://m.media-amazon.com/images/I/91akbfdbByL._AC_SL1500_.jpg","amazonLink":"https://www.amazon.de/-/en/Samsung-Galaxy-128GB-Mobile-Android/dp/B08Q8GJXPF/ref=sr_1_2?crid=2ZF9UC4U7J8EN&keywords=samsung&qid=1646432461&sprefix=samsun%2Caps%2C189&sr=8-2","prodcategory":2,"shows":True,"likes":0},{"id":9,"name":"Samsung Galaxy S20","price":454,"description":"Model name\tSamsung Galaxy S20 FE\nWireless carrier\tUnlocked for All Carriers\nBrand\tSamsung\nForm factor\tBar\nMemory storage capacity\t6 GB\nOperating system\tAndroid 11.0","rating":4.5,"imageSrc":"https://m.media-amazon.com/images/I/61GbkDVtLwL._AC_SL1100_.jpg","amazonLink":"https://www.amazon.de/-/en/Samsung-Galaxy-Smartphone-Cloud-Android/dp/B096G5MZ34/ref=sr_1_18?crid=2ZF9UC4U7J8EN&keywords=samsung&qid=1646432550&sprefix=samsun%2Caps%2C189&sr=8-18","prodcategory":2,"shows":True,"likes":0},{"id":10,"name":"Samsung Galaxy S21","price":772,"description":"Model name\tR9\nWireless carrier\tUnlocked for All Carriers\nBrand\tSamsung\nForm factor\tBar\nMemory storage capacity\t6 GB\nOperating system\tAndroid 12","rating":4.4,"imageSrc":"https://m.media-amazon.com/images/I/81u8oHzGLmL._AC_SL1500_.jpg","amazonLink":"https://www.amazon.de/-/en/Samsung-Galaxy-Smartphone-Phantom-Android/dp/B08QX85YKM/ref=sr_1_17?crid=2ZF9UC4U7J8EN&keywords=samsung&qid=1646432550&sprefix=samsun%2Caps%2C189&sr=8-17","prodcategory":2,"shows":True,"likes":0},{"id":11,"name":"Samsung Galaxy A32","price":272,"description":"Model name\tSamsung Galaxy A32\nWireless carrier\tUnlocked for All Carriers\nBrand\tSamsung\nForm factor\tTouchscreen\nMemory storage capacity","rating":4.5,"imageSrc":"https://m.media-amazon.com/images/I/71xetlaYOTL._AC_SL1500_.jpg","amazonLink":"https://www.amazon.de/-/en/Samsung-Galaxy-Smartphone-128GB-Black/dp/B08W1V1226/ref=sr_1_11?crid=1OSCH0XCHFZXF&keywords=samsung&qid=1646857726&sprefix=samsung%2Caps%2C214&sr=8-11","prodcategory":2,"shows":True,"likes":0},{"id":12,"name":"Samsung Galaxy A22","price":216,"description":"Model name\tGalaxy A22\nWireless carrier\tUnlocked for All Carriers\nBrand\tSamsung\nForm factor\tSmartphone\nMemory storage capacity\t64 GB","rating":4.5,"imageSrc":"https://m.media-amazon.com/images/I/71zAlS6+6rL._AC_SL1500_.jpg","amazonLink":"https://www.amazon.de/-/en/Samsung-Galaxy-A225-Black-Dual/dp/B0937JCNXT/ref=sr_1_2?crid=309KM17H57HSZ&keywords=samsung+galaxy+a22&qid=1646857796&sprefix=samsung+galaxy+a2%2Caps%2C173&sr=8-2","prodcategory":2,"shows":True,"likes":0},{"id":13,"name":"Xiaomi Poco M3 Pro","price":218,"description":"Model name\tPoco M3 Pro 5G\nWireless carrier\tUnlocked for All Carriers\nBrand\tXiaomi\nForm factor\tTouchscreen\nMemory storage capacity\t4 GB","rating":4.5,"imageSrc":"https://m.media-amazon.com/images/I/518-LW36OCS._AC_SL1001_.jpg","amazonLink":"https://m.media-amazon.com/images/I/518-LW36OCS._AC_SL1001_.jpg","prodcategory":3,"shows":True,"likes":0},{"id":14,"name":"Xiaomi Poco X3","price":293,"description":"Model name\tPoco X3\nWireless carrier\tUnlocked for All Carriers\nBrand\tXiaomi\nForm factor\tBlock\nMemory storage capacity\t8 GB","rating":4.6,"imageSrc":"https://m.media-amazon.com/images/I/71fdWd4SqFL._AC_SL1380_.jpg","amazonLink":"https://www.amazon.de/-/en/Xiaomi-Poco-X3-Pro-Smartphone/dp/B08Z84SB3R/ref=sr_1_15?crid=3RJ6OMFYB044C&keywords=xiaomi&qid=1646857971&sprefix=xiaomi%2Caps%2C173&sr=8-15&th=1","prodcategory":3,"shows":True,"likes":0},{"id":15,"name":"Xiaomi Redmi Note 11","price":283,"description":"\nWireless carrier\tUnlocked for All Carriers\nBrand\tXiaomi\nForm factor\tTouchscreen\nMemory storage capacity\t128 GB\nColour\tStar Blue","rating":5,"imageSrc":"https://m.media-amazon.com/images/I/51-JEJPrRDL._AC_SL1000_.jpg","amazonLink":"https://www.amazon.de/-/en/Xiaomi-Smartphone-DotDisplay-Snapdragon-Camera-Star-Blue/dp/B09QYK466Y/ref=sr_1_2?crid=2NU0ZUOS1LL83&keywords=xiaomi+redmi+note+11&qid=1646857987&sprefix=xiaomi+redmi+note+11%2Caps%2C170&sr=8-2","prodcategory":3,"shows":True,"likes":0},{"id":16,"name":"Xiaomi Redmi Note 10","price":212,"description":"Model name\tRedmi Note 10\nWireless carrier\tUnlocked for All Carriers\nBrand\tXiaomi\nForm factor\tSchieberegler\nMemory storage capacity\t128 GB","rating":4.6,"imageSrc":"https://m.media-amazon.com/images/I/71CcXhAu9kS._AC_SL1500_.jpg","amazonLink":"https://www.amazon.de/-/en/Xiaomi-Redmi-Note-10-Chrome/dp/B095BLF64H/ref=sr_1_1?crid=39JABBJIWFLUI&keywords=xiaomi%2Bremi%2Bnote%2B10&qid=1646858006&sprefix=xiaomi%2Bredmi%2Bnote%2B10%2Caps%2C171&sr=8-1&th=1","prodcategory":3,"shows":True,"likes":0},{"id":17,"name":"Xiaomi Redmi 9C","price":151,"description":"Model name\tRedmi 9C\nWireless carrier\tUnlocked for All Carriers\nBrand\tXiaomi\nForm factor\tSmartphone\nMemory storage capacity\t3 GB\nOperating system\tAndroid 10.0","rating":4.4,"imageSrc":"https://m.media-amazon.com/images/I/81DvJbWniDL._AC_SL1500_.jpg","amazonLink":"hhttps://www.amazon.de/-/en/MZB07Q0EU-Xiaomi-Redmi-9C-Smartphone/dp/B08DVHL2DV/ref=sr_1_1?crid=3RJ6OMFYB044C&keywords=xiaomi&qid=1646857971&sprefix=xiaomi%2Caps%2C173&sr=8-1&th=1","prodcategory":3,"shows":True,"likes":0},{"id":18,"name":"HTC Desire 500","price":326,"description":"Wireless carrier\tUnlocked\nBrand\tHTC\nForm factor\tTouchscreen\nMemory storage capacity\t8 GB\nOperating system\tAndroid 4.2","rating":3,"imageSrc":"https://m.media-amazon.com/images/I/41j9oKsdLkL._AC_.jpg","amazonLink":"https://www.amazon.de/-/en/Desire-Unlocked-Smartphone-Android-Jelly/dp/B00E4TLZ4I/ref=sr_1_4?keywords=htc%2Bsmartphone&qid=1646858423&sprefix=htc%2Bsmar%2Caps%2C158&sr=8-4&th=1","prodcategory":4,"shows":True,"likes":0},{"id":19,"name":"HTC One M9","price":200,"description":"Model name\tHTC One M9\nWireless carrier\tUnlocked\nBrand\tHTC\nForm factor\tStandard (Bar)\nMemory storage capacity\t32 GB","rating":4.1,"imageSrc":"https://m.media-amazon.com/images/I/71K4WAf9vnL._AC_SL1500_.jpg","amazonLink":"https://www.amazon.de/-/en/HTC-One-M9-Gold/dp/B00TX5QRAA/ref=sr_1_8?keywords=htc+smartphone&qid=1646858423&sprefix=htc+smar%2Caps%2C158&sr=8-8","prodcategory":4,"shows":True,"likes":0},{"id":20,"name":"HTC Desire 21 Pro","price":319,"description":"Model name\tDesire 21 Pro 5G\nWireless carrier\tUnlocked for All Carriers\nBrand\tHTC\nForm factor\tSto??absorbierend\nMemory storage capacity\t6 GB","rating":4.2,"imageSrc":"https://m.media-amazon.com/images/I/41n3VHQBxtL._AC_.jpg","amazonLink":"https://www.amazon.de/-/en/HTC-Desire-21-Pro-5G-blue/dp/B092JP9YWH/ref=sr_1_1?keywords=htc+smartphone&qid=1646858384&sprefix=htc+smar%2Caps%2C158&sr=8-1","prodcategory":4,"shows":True,"likes":0},{"id":21,"name":"HTC Desire X","price":104,"description":"Model name\tX\nWireless carrier\tNET\nBrand\tHTC\nForm factor\tTouchscreen\nMemory storage capacity\t4096 MB","rating":3.7,"imageSrc":"https://m.media-amazon.com/images/I/71vK8U+4yaL._AC_SL1456_.jpg","amazonLink":"https://www.amazon.de/-/en/Desire-Smartphone-Android-Sense-Bluetooth/dp/B009GGY852/ref=sr_1_2?keywords=htc+smartphone&qid=1646858384&sprefix=htc+smar%2Caps%2C158&sr=8-2","prodcategory":4,"shows":True,"likes":0},{"id":22,"name":"HTC Desire 816","price":157,"description":"Model name\tHTC Desire 816\nBrand\tHTC\nForm factor\tStandard (Bar)\nMemory storage capacity\t8 GB\nOperating system\tAndroid 4.4\nColour\tWei??","rating":4.6,"imageSrc":"https://m.media-amazon.com/images/I/61oiYM+h4gL._AC_SL1000_.jpg","amazonLink":"https://www.amazon.de/-/en/Smartphone-Megapixel-Touchscreen-Quad-Core-Processor/dp/B00ISUSB3M/ref=sr_1_3?keywords=htc+smartphone&qid=1646858384&sprefix=htc+smar%2Caps%2C158&sr=8-3","prodcategory":4,"shows":True,"likes":0}]
#categories = [{"id":1, "name":'iPhone'}, {"id":2, "name":'Samsung'},{"id":3, "name":'Xiaomi'},{"id":4, "name":'HTC'}]

def product_list(request):
    prod = Product.objects.all()
    data = [p.to_json() for p in prod]
    return JsonResponse(data, safe=False)

def product_detail(request, product_id):
    prod = Product.objects.filter(id=product_id).first()
    if prod:
        return JsonResponse(prod.to_json())
    return JsonResponse({'message':'Not found'})


def prod_list_category(request, product_category):
    prod_ll = Product.objects.filter(prodcategory=product_category)
    data = [p.to_json() for p in prod_ll]
    return JsonResponse(data, safe=False)


def categories_list(request):
    categ_ll = Category.objects.all()
    data = [c.to_json() for c in categ_ll]
    return JsonResponse(data, safe=False)

def categories_d(request, cat_id):
    categ = Category.objects.filter(id = cat_id).first()
    if categ:
        return JsonResponse(categ.to_json())
    return JsonResponse({'message': 'Category not found with selected ID'})

# def create_categories(request):
#     for i in range(len(categories)):
#         name = categories[i]['name']
#         cat_name = {
#             'name': name
#         }
#         Category.objects.create(name=name)


# def create_product(request):
#     for i in range(len(products)):
#         name = products[i]['name']
#         price = products[i]['price']
#         description = products[i]['description']
#         count = 10
#         rating = products[i]['rating']
#         imageSrc = products[i]['imageSrc']
#         amazonLink = products[i]['amazonLink']
#         prodcategory = products[i]['prodcategory']
#         is_active = True
#         likes = products[i]['likes']
#         Product.objects.create(name=name, price=price, description=description, count=count, rating=rating, imageSrc=imageSrc, amazonLink=amazonLink, prodcategory=prodcategory, is_active= True, likes=likes)

# def object_to_json(prod):
#     Prods = Product.objects.all()
#     if prod in Prods:
#         data = {
#             'name': prod.name,
#             'price': prod.price,
#             'description': prod.description,
#             'count': prod.count,
#             'rating': prod.rating,
#             'imageSrc': prod.imageSrc,
#             'amazonLink': prod.amazonLink,
#             'prodcategory': prod.prodcategory,
#             'is_active': prod.is_active,
#             'likes': prod.likes,
#         }
#         return data
#     return None
# def object_to_json_category(cat):
#     Categories = Category.objects.all()
#     if cat in Categories:
#         data = {
#             'name': cat.name
#         }
#         return data
#     return None