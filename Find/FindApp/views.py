from django.shortcuts import render, HttpResponse
from .models import JdBags,JdAccessories,JdBelt,JdDecoration,JdCloth,JdShoe,JdWallet,SkAccessories,SkBags,SkCloth,SkJewellery,TmBags,TmBeautyMakeup,JdBeautyMakeup,SkBeautyMakeup,TmJewelry,TmColth,TmShoe,mall
from django.http import JsonResponse
from django.db.models import Q


def home(request):
    return render(request,'home.html')

# Create your views here.
def JdBagDetail(list, count, data):
    datamessage = {}
    datadetail = []
    sum = 0
    if count == 0:
        data['status'] = 0
    else:
        for each in list:
            datadetail2 = {}
            datadetail2["name"] = each.name
            datadetail2["price"] = each.price
            datadetail2["size"] = each.size
            datadetail2["material"] = each.material
            datadetail2["sex"] = each.sex
            datadetail2["brand"] = each.brand
            datadetail2["type"] = each.type
            datadetail2["origin"] = each.origin

            datadetail.append(datadetail2)
            price = each.price  # null情况
            try:
                price = float(price.split(":")[-1])
                sum += price
            except Exception as e:
                continue
        data['datadetail'] = datadetail
        data['datamessage'] = datamessage
        data['status'] = 1
        datamessage['count'] = count
        datamessage['avg'] = int(sum / count)

def JdAccessoriesDetail(list, count, data):
    datamessage = {}
    datadetail = []
    sum = 0
    if count == 0:
        data['status'] = 0
    else:
        for each in list:
            datadetail2 = {}
            datadetail2["name"] = each.name
            datadetail2["price"] = each.price
            datadetail2["material"] = each.material
            datadetail2["sex"] = each.sex
            datadetail2["brand"] = each.brand
            datadetail2["type"] = each.type
            datadetail2["origin"] = each.origin

            datadetail.append(datadetail2)
            price = each.price  # null情况
            try:
                price = float(price.split(":")[-1])
                sum += price
            except Exception as e:
                continue
        data['datadetail'] = datadetail
        data['datamessage'] = datamessage
        data['status'] = 1
        datamessage['count'] = count
        datamessage['avg'] = int(sum / count)

def JdBeltDetail(list, count, data):
    datamessage = {}
    datadetail = []
    sum = 0
    if count == 0:
        data['status'] = 0
    else:
        for each in list:
            datadetail2 = {}
            datadetail2["name"] = each.name
            datadetail2["price"] = each.price
            datadetail2["size"] = each.size
            datadetail2["style"] = each.style
            datadetail2["material"] = each.material
            datadetail2["sex"] = each.sex
            datadetail2["brand"] = each.brand
            datadetail2["type"] = each.type
            datadetail2["origin"] = each.origin

            datadetail.append(datadetail2)
            price = each.price  # null情况
            try:
                price = float(price.split(":")[-1])
                sum += price
            except Exception as e:
                continue
        data['datadetail'] = datadetail
        data['datamessage'] = datamessage
        data['status'] = 1
        datamessage['count'] = count
        datamessage['avg'] = int(sum / count)

def JdDecorationDetail(list, count, data):
    datamessage = {}
    datadetail = []
    sum = 0
    if count == 0:
        data['status'] = 0
    else:
        for each in list:
            datadetail2 = {}
            datadetail2["name"] = each.name
            datadetail2["price"] = each.price

            datadetail2["material"] = each.material
            datadetail2["sex"] = each.sex
            datadetail2["brand"] = each.brand
            datadetail2["type"] = each.type
            datadetail2["origin"] = each.origin

            datadetail.append(datadetail2)
            price = each.price  # null情况
            try:
                price = float(price.split(":")[-1])
                sum += price
            except Exception as e:
                continue
        data['datadetail'] = datadetail
        data['datamessage'] = datamessage
        data['status'] = 1
        datamessage['count'] = count
        datamessage['avg'] = int(sum / count)

def JdClothDetail(list, count, data):
    datamessage = {}
    datadetail = []
    sum = 0
    if count == 0:
        data['status'] = 0
    else:
        for each in list:
            datadetail2 = {}
            datadetail2["size"] = each.size
            datadetail2["material"] = each.material
            datadetail2["age"] = each.age
            datadetail2["style"] = each.style
            datadetail2["color"] = each.color

            datadetail2["origin"] = each.origin

            datadetail2["price"] = each.price
            datadetail2["brand"] = each.brand

            datadetail2["name"] = each.name

            datadetail2["producturl"] = each.producturl
            datadetail2["number"] = each.number


            datadetail.append(datadetail2)
            price = each.price  # null情况
            try:
                price = float(price.split(":")[-1])
                sum += price
            except Exception as e:
                continue
        data['datadetail'] = datadetail
        data['datamessage'] = datamessage
        data['status'] = 1
        datamessage['count'] = count
        datamessage['avg'] = int(sum / count)

def JdShoeDetail(list, count, data):
    datamessage = {}
    datadetail = []
    sum = 0
    if count == 0:
        data['status'] = 0
    else:
        for each in list:
            datadetail2 = {}
            datadetail2["name"] = each.name
            datadetail2["price"] = each.price

            datadetail2["color"] = each.color
            datadetail2["size"] = each.size
            datadetail2["material"] = each.material
            datadetail2["sex"] = each.sex
            datadetail2["brand"] = each.brand
            datadetail2["type"] = each.type
            datadetail2["origin"] = each.origin

            datadetail.append(datadetail2)
            price = each.price  # null情况
            try:
                price = float(price.split(":")[-1])
                sum += price
            except Exception as e:
                continue
        data['datadetail'] = datadetail
        data['datamessage'] = datamessage
        data['status'] = 1
        datamessage['count'] = count
        datamessage['avg'] = int(sum / count)

def JdWalletDetail(list, count, data):
    datamessage = {}
    datadetail = []
    sum = 0
    if count == 0:
        data['status'] = 0
    else:
        for each in list:
            datadetail2 = {}
            datadetail2["name"] = each.name
            datadetail2["price"] = each.price

            datadetail2["color"] = each.color

            datadetail2["material"] = each.material
            datadetail2["sex"] = each.sex
            datadetail2["brand"] = each.brand
            datadetail2["type"] = each.type
            datadetail2["origin"] = each.origin

            datadetail.append(datadetail2)
            price = each.price  # null情况
            try:
                price = float(price.split(":")[-1])
                sum += price
            except Exception as e:
                continue
        data['datadetail'] = datadetail
        data['datamessage'] = datamessage
        data['status'] = 1
        datamessage['count'] = count
        datamessage['avg'] = int(sum / count)

def JdBeautyMakeupDetail(list, count, data):
    datamessage = {}
    datadetail = []
    sum = 0
    if count == 0:
        data['status'] = 0
    else:
        for each in list:
            datadetail2 = {}
            datadetail2["effect"] = each.effect
            datadetail2["type"] = each.type
            datadetail2["name"] = each.name
            datadetail2["weight"] = each.weight
            datadetail2["brand"] = each.brand
            datadetail2["wherefrom"] = each.wherefrom
            datadetail2["skin"] = each.skin
            datadetail2["origin"] = each.origin
            datadetail2["price"] = each.price

            datadetail.append(datadetail2)

            try:
                price = each.price  # null情况
                price = float(price)
                sum += price
            except Exception as e:
                continue
        data['datadetail'] = datadetail
        data['datamessage'] = datamessage
        data['status'] = 1
        datamessage['count'] = count
        datamessage['avg'] = int(sum / count)

def SkAccessoriesDetail(list, count, data):
    datamessage = {}
    datadetail = []
    sum = 0
    if count == 0:
        data['status'] = 0
    else:
        for each in list:
            datadetail2 = {}
            datadetail2["name"] = each.name
            datadetail2["price"] = each.price
            datadetail2["productproperties"] = each.productproperties
            datadetail2["brand"] = each.brand
            datadetail2["size"] = each.size
            datadetail2["origin"] = each.origin

            datadetail.append(datadetail2)
            try:
                price = each.price  # null情况
                price = price.split(":")[-1]
                price = price.replace(",", "")
                price = float(price)
                sum += price
            except Exception as e:
                continue

        data['datadetail'] = datadetail
        data['datamessage'] = datamessage
        data['status'] = 1
        datamessage['count'] = count
        datamessage['avg'] = int(sum / count)

def SkBagsDetail(list, count, data):
    datamessage = {}
    datadetail = []
    sum = 0
    if count == 0:
        data['status'] = 0
    else:
        for each in list:
            datadetail2 = {}
            datadetail2["name"] = each.name
            datadetail2["price"] = each.price
            datadetail2["size"] = each.size
            datadetail2["material"] = each.material
            datadetail2["color"] = each.color
            datadetail2["ApplicablePeople"] = each.ApplicablePeople
            datadetail2["brand"] = each.brand

            datadetail2["origin"] = each.origin

            datadetail.append(datadetail2)
            try:
                price = each.price  # null情况
                price = price.split(":")[-1]
                price = price.replace(",", "")
                price = float(price)
                sum += price
            except Exception as e:
                continue

        data['datadetail'] = datadetail
        data['datamessage'] = datamessage
        data['status'] = 1
        datamessage['count'] = count
        datamessage['avg'] = int(sum / count)

def SkClothDetail(list, count, data):
    datamessage = {}
    datadetail = []
    sum = 0
    if count == 0:
        data['status'] = 0
    else:
        for each in list:
            datadetail2 = {}
            datadetail2["name"] = each.name
            datadetail2["price"] = each.price
            datadetail2["material"] = each.material
            datadetail2["style"] = each.style
            datadetail2["brand"] = each.brand
            datadetail2["origin"] = each.origin
            datadetail.append(datadetail2)
            try:
                price = each.price  # null情况
                price = price.split(":")[-1]
                price = price.replace(",", "")
                price = float(price)
                sum += price
            except Exception as e:
                continue

        data['datadetail'] = datadetail
        data['datamessage'] = datamessage
        data['status'] = 1
        datamessage['count'] = count
        datamessage['avg'] = int(sum / count)

def SkJewelleryDetail(list, count, data):
    datamessage = {}
    datadetail = []
    sum = 0
    if count == 0:
        data['status'] = 0
    else:
        for each in list:
            datadetail2 = {}
            datadetail2["name"] = each.name
            datadetail2["price"] = each.price
            datadetail2["materialproperties"] = each.materialproperties
            datadetail2["productproperties"] = each.productproperties
            datadetail2["style"] = each.style
            datadetail2["size"] = each.size
            datadetail2["style"] = each.style
            datadetail2["brand"] = each.brand
            datadetail2["origin"] = each.origin
            datadetail.append(datadetail2)
            try:
                price = each.price  # null情况
                price = price.split(":")[-1]
                price = price.replace(",", "")
                price = float(price)
                sum += price
            except Exception as e:
                continue

        data['datadetail'] = datadetail
        data['datamessage'] = datamessage
        data['status'] = 1
        datamessage['count'] = count
        datamessage['avg'] = int(sum / count)

def SkBeautyMakeupDetail(list, count, data):
    datamessage = {}
    datadetail = []
    sum = 0
    if count == 0:
        data['status'] = 0
    else:
        for each in list:
            datadetail2 = {}
            datadetail2["people"] = each.people
            datadetail2["price"] = each.price
            datadetail2["name"] = each.name
            datadetail2["shelflife"] = each.shelflife
            datadetail2["weight"] = each.weight
            datadetail2["scenario"] = each.scenario
            datadetail2["material"] = each.material
            datadetail2["efficacy"] = each.efficacy
            datadetail2["origin"] = each.origin
            datadetail2["skin"] = each.skin
            datadetail2["brand"] = each.brand
            datadetail.append(datadetail2)
            try:
                price = each.price  # null情况

                price = price.replace(",", "")
                price = float(price)
                sum += price
            except Exception as e:
                continue

        data['datadetail'] = datadetail
        data['datamessage'] = datamessage
        data['status'] = 1
        datamessage['count'] = count
        datamessage['avg'] = int(sum / count)

def TmBagsDetail(list, count, data):
    datamessage = {}
    datadetail = []
    sum = 0
    if count == 0:
        data['status'] = 0
    else:
        for each in list:
            datadetail2 = {}
            datadetail2["name"] = each.name
            datadetail2["price"] = each.price
            datadetail2["sex"] = each.sex
            datadetail2["size"] = each.size
            datadetail2["material"] = each.material
            datadetail2["color"] = each.color
            datadetail2["style"] = each.style
            datadetail2["type"] = each.type
            datadetail2["brand"] = each.brand

            datadetail.append(datadetail2)
            try:
                price = each.price  # null情况
                price = float(price)
                sum += price
            except Exception as e:
                continue
        data['datadetail'] = datadetail
        data['datamessage'] = datamessage
        data['status'] = 1
        datamessage['count'] = count
        datamessage['avg'] = int(sum / count)

def TmBeautyMakeupDetail(list, count, data):
    datamessage = {}
    datadetail = []
    sum = 0
    if count == 0:
        data['status'] = 0
    else:
        for each in list:
            datadetail2 = {}
            datadetail2["name"] = each.name
            datadetail2["price"] = each.price
            datadetail2["shelf"] = each.shelf
            datadetail2["datelimit"] = each.datelimit
            datadetail2["weight"] = each.weight
            datadetail2["effect"] = each.effect
            datadetail2["skin"] = each.skin
            datadetail2["type"] = each.type
            datadetail2["brand"] = each.brand

            datadetail.append(datadetail2)
            try:
                price = each.price  # null情况
                price = float(price)
                sum += price
            except Exception as e:
                continue
        data['datadetail'] = datadetail
        data['datamessage'] = datamessage
        data['status'] = 1
        datamessage['count'] = count
        datamessage['avg'] = int(sum / count)

def TmJewelryDetail(list, count, data):
    datamessage = {}
    datadetail = []
    sum = 0
    if count == 0:
        data['status'] = 0
    else:
        for each in list:
            datadetail2 = {}
            datadetail2["price"] = each.price
            datadetail2["color"] = each.color
            datadetail2["appraisaltype"] = each.appraisaltype
            datadetail2["vicegrade"] = each.vicegrade
            datadetail2["specifications"] = each.specifications
            datadetail2["name"] = each.name
            datadetail2["appraisalmarks"] = each.appraisalmarks
            datadetail2["paragraph"] = each.paragraph
            datadetail2["material"] = each.material
            datadetail2["certificationmark"] = each.certificationmark
            datadetail2["brand"] = each.brand
            datadetail2["use"] = each.use
            datadetail2["maingrade"] = each.maingrade

            datadetail2["url"] = each.url


            datadetail.append(datadetail2)
            try:
                price = each.price  # null情况
                price = float(price)
                sum += price
            except Exception as e:
                continue
        data['datadetail'] = datadetail
        data['datamessage'] = datamessage
        data['status'] = 1
        datamessage['count'] = count
        datamessage['avg'] = int(sum / count)

def TmColthDetail(list, count, data):
    datamessage = {}
    datadetail = []
    sum = 0
    if count == 0:
        data['status'] = 0
    else:
        for each in list:
            datadetail2 = {}
            datadetail2["name"] = each.name
            datadetail2["year"] = each.year
            datadetail2["age"] = each.age
            datadetail2["size"] = each.size
            datadetail2["brand"] = each.brand
            datadetail2["color"] = each.color
            datadetail2["style"] = each.style
            datadetail2["price"] = each.price
            datadetail2["kuanshi"] = each.kuanshi
            datadetail2["material"] = each.material
            datadetail2["url"] = each.url
            datadetail.append(datadetail2)
            try:
                price = each.price  # null情况
                price = float(price)
                sum += price
            except Exception as e:
                continue
        data['datadetail'] = datadetail
        data['datamessage'] = datamessage
        data['status'] = 1
        datamessage['count'] = count
        datamessage['avg'] = int(sum / count)

def TmShoeDetail(list, count, data):
    datamessage = {}
    datadetail = []
    sum = 0
    if count == 0:
        data['status'] = 0
    else:
        for each in list:
            datadetail2 = {}
            datadetail2["name"] = each.name
            datadetail2["year"] = each.year
            datadetail2["material"] = each.material
            datadetail2["price"] = each.price
            datadetail2["brand"] = each.brand
            datadetail2["color"] = each.color
            datadetail2["style"] = each.style
            datadetail2["price"] = each.price
            datadetail2["weight"] = each.weight
            datadetail2["size"] = each.size
            datadetail2["people"] = each.people
            datadetail2["kuansi"] = each.kuansi
            datadetail2["url"] = each.url
            datadetail.append(datadetail2)
            try:
                price = each.price  # null情况
                price = float(price)
                sum += price
            except Exception as e:
                continue
        data['datadetail'] = datadetail
        data['datamessage'] = datamessage
        data['status'] = 1
        datamessage['count'] = count
        datamessage['avg'] = int(sum / count)

def find(request):
    shop = request.GET['shop']
    type = request.GET['type']
    try:
        brand = request.GET['brand']
    except Exception as e:
        brand = None

    try:
        name = request.GET['name']
    except Exception as e:
        name = None
    data = {}

    web_type = shop+type
    if web_type.lower() == "JdBags".lower():
        if brand is not None:
            list = JdBags.objects.filter(brand__contains=brand).filter(~Q(price="NULL"))
            count = len(list)
            JdBagDetail(list, count, data)
            data['where_brand'] = brand

        if name is not None:
            list = JdBags.objects.filter(name__contains=name).filter(~Q(price="NULL"))
            count = len(list)
            JdBagDetail(list, count, data)
            data['where_name'] = name

    elif web_type.lower() == "JdAccessories".lower():
        if brand is not  None:
            list = JdAccessories.objects.filter(brand__contains=brand).filter(~Q(price="NULL"))
            count = len(list)
            JdAccessoriesDetail(list, count, data)
            data['where_brand'] = brand

        if name is not None:
            list = JdAccessories.objects.filter(name__contains=name).filter(~Q(price="NULL"))
            count = len(list)
            JdAccessoriesDetail(list, count, data)
            data['where_name'] = name

    elif web_type.lower() == "JdBelt".lower():
        if brand is not None:
            list = JdBelt.objects.filter(brand__contains=brand).filter(~Q(price="NULL"))
            count = len(list)
            JdBeltDetail(list, count, data)
            data['where_brand'] = brand

        if name is not None:
            list = JdBelt.objects.filter(name__contains=name).filter(~Q(price="NULL"))
            count = len(list)
            JdBeltDetail(list, count, data)
            data['where_name'] = name

    elif web_type.lower() == "JdDecoration".lower():
        if brand is not None:
            list = JdDecoration.objects.filter(brand__contains=brand).filter(~Q(price="NULL"))
            count = len(list)
            JdDecorationDetail(list, count,data)
            data['where_brand'] = brand

        if name is not None:
            list = JdDecoration.objects.filter(name__contains=name).filter(~Q(price="NULL"))
            count = len(list)
            JdDecorationDetail(list, count, data)
            data['where_name'] = name

    elif web_type.lower() == "JdCloth".lower():
        if brand is not None:
            list = JdCloth.objects.filter(brand__contains=brand).filter(~Q(price="NULL"))
            count = len(list)
            JdClothDetail(list, count,data)
            data['where_brand'] = brand

        if name is not None:
            list = JdCloth.objects.filter(name__contains=name).filter(~Q(price="NULL"))
            count = len(list)
            JdClothDetail(list, count, data)
            data['where_name'] = name

    elif web_type.lower() == "JdShoe".lower():
        if brand is not None:
            list = JdShoe.objects.filter(brand__contains=brand).filter(~Q(price="NULL"))
            count = len(list)
            JdShoeDetail(list, count, data)
            data['where_brand'] = brand

        if name is not None:
            list = JdShoe.objects.filter(name__contains=name).filter(~Q(price="NULL"))
            count = len(list)
            JdShoeDetail(list, count, data)
            data['where_name'] = name

    elif web_type.lower() == "JdWallet".lower():
        if brand is not None:
            list = JdWallet.objects.filter(brand__contains=brand).filter(~Q(price="NULL"))
            count = len(list)
            JdWalletDetail(list, count, data)
            data['where_brand'] = brand

        if name is not None:
            list = JdWallet.objects.filter(name__contains=name).filter(~Q(price="NULL"))
            count = len(list)
            JdWalletDetail(list, count, data)
            data['where_name'] = name

    elif web_type.lower() == "JdBeautyMakeup".lower():
        if brand is not None:
            list = JdBeautyMakeup.objects.filter(brand__contains=brand).filter(~Q(price="NULL"))
            count = len(list)
            JdBeautyMakeupDetail(list, count, data)
            data['where_brand'] = brand

        if name is not None:
            list = JdBeautyMakeup.objects.filter(name__contains=name).filter(~Q(price="NULL"))
            count = len(list)
            JdBeautyMakeupDetail(list, count, data)
            data['where_name'] = name

    elif web_type.lower() == "SkAccessories".lower():
        if brand is not None:
            list = SkAccessories.objects.filter(brand__contains=brand).filter(~Q(price="NULL"))
            count = len(list)
            SkAccessoriesDetail(list, count,data)
            data['where_brand'] = brand

        if name is not None:
            list = SkAccessories.objects.filter(name__contains=name).filter(~Q(price="NULL"))
            count = len(list)
            SkAccessoriesDetail(list, count, data)
            data['where_name'] = name

    elif web_type.lower() == "SkBeautyMakeup".lower():
        if brand is not None:
            list = SkBeautyMakeup.objects.filter(brand__contains=brand).filter(~Q(price="NULL"))
            count = len(list)
            SkBeautyMakeupDetail(list, count, data)
            data['where_brand'] = brand

        if name is not None:
            list = SkBeautyMakeup.objects.filter(name__contains=name).filter(~Q(price="NULL"))
            count = len(list)
            SkBeautyMakeupDetail(list, count, data)
            data['where_name'] = name

    elif web_type.lower() == "SkBags".lower():
        if brand is not None:
            list = SkBags.objects.filter(brand__contains=brand).filter(~Q(price="NULL"))
            count = len(list)
            SkBagsDetail(list, count, data)
            data['where_brand'] = brand

        if name is not None:
            list = SkBags.objects.filter(name__contains=name).filter(~Q(price="NULL"))
            count = len(list)
            SkBagsDetail(list, count, data)
            data['where_name'] = name

    elif web_type.lower() == "SkCloth".lower():
        if brand is not None:
            list = SkCloth.objects.filter(brand__contains=brand).filter(~Q(price="NULL"))
            count = len(list)
            SkClothDetail(list, count, data)
            data['where_brand'] = brand

        if name is not None:
            list = SkCloth.objects.filter(name__contains=name).filter(~Q(price="NULL"))
            count = len(list)
            SkClothDetail(list, count, data)
            data['where_name'] = name

    elif web_type.lower() == "SkJewellery".lower():
        if brand is not None:
            list = SkJewellery.objects.filter(brand__contains=brand).filter(~Q(price="NULL"))
            count = len(list)
            SkJewelleryDetail(list, count, data)
            data['where_brand'] = brand

        if name is not None:
            list = SkJewellery.objects.filter(name__contains=name).filter(~Q(price="NULL"))
            count = len(list)
            SkJewelleryDetail(list, count, data)
            data['where_name'] = name

    elif web_type.lower() == "TmBags".lower():
        if brand is not None:
            list = TmBags.objects.filter(brand__contains=brand).filter(~Q(price="NULL"))
            count = len(list)
            TmBagsDetail(list, count, data)
            data['where_brand'] = brand

        if name is not None:
            list = TmBags.objects.filter(name__contains=name).filter(~Q(price="NULL"))
            count = len(list)
            TmBagsDetail(list, count, data)
            data['where_name'] = name

    elif web_type.lower() == "TmBeautyMakeup".lower():
        if brand is not None:
            list = TmBeautyMakeup.objects.filter(brand__contains=brand).filter(~Q(price="NULL"))
            count = len(list)
            TmBeautyMakeupDetail(list, count, data)
            data['where_brand'] = brand

        if name is not None:
            list = TmBeautyMakeup.objects.filter(name__contains=name).filter(~Q(price="NULL"))
            count = len(list)
            TmBeautyMakeupDetail(list, count, data)
            data['where_name'] = name

    elif web_type.lower() == "TmJewelry".lower():
        if brand is not None:
            list = TmJewelry.objects.filter(brand__contains=brand).filter(~Q(price="NULL"))
            count = len(list)
            TmJewelryDetail(list, count, data)
            data['where_brand'] = brand

        if name is not None:
            list = TmJewelry.objects.filter(name__contains=name).filter(~Q(price="NULL"))
            count = len(list)
            TmJewelryDetail(list, count, data)
            data['where_name'] = name

    elif web_type.lower() == "TmCloth".lower():
        if brand is not None:
            list = TmColth.objects.filter(brand__contains=brand).filter(~Q(price="NULL"))
            count = len(list)
            TmColthDetail(list, count, data)
            data['where_brand'] = brand

        if name is not None:
            list = TmColth.objects.filter(name__contains=name).filter(~Q(price="NULL"))
            count = len(list)
            TmColthDetail(list, count, data)
            data['where_name'] = name

    elif web_type.lower() == "TmShoe".lower():
        if brand is not None:
            list = TmShoe.objects.filter(brand__contains=brand).filter(~Q(price="NULL"))
            count = len(list)
            TmShoeDetail(list, count, data)
            data['where_brand'] = brand

        if name is not None:
            list = TmShoe.objects.filter(name__contains=name).filter(~Q(price="NULL"))
            count = len(list)
            TmShoeDetail(list, count, data)
            data['where_name'] = name

    data['where_Shop'] = shop
    data['where_type'] = type


    return JsonResponse(data)


def malls(request, id):
    id = int(id)
    if id == 0:
        data = mall.objects.filter(pid__isnull=True)
    else:
        data = [{}]
    list = []
    for each in data:
        list.append([each.id, each.title, each.title2])
    return JsonResponse({'data': list})

def types(request, id):
    id = int(id)
    typelist = mall.objects.filter(pid_id=id)
    list = []
    for each in typelist:
        list.append({"id": each.id, "title": each.title, "title2": each.title2})
    return JsonResponse({"data": list})