from django.db import models

# Create your models here.

class JdBags(models.Model):
    _id = models.CharField(primary_key=True, max_length=200)
    brand = models.CharField(max_length=200,null=True)
    number = models.CharField(max_length=300,null=True)
    price = models.CharField(max_length=200,null=True)
    producturl = models.CharField(max_length=200,null=True)
    sex = models.CharField(max_length=50,null=True)
    element = models.CharField(max_length=50,null=True)
    size = models.CharField(max_length=200,null=True)
    color = models.CharField(max_length=100,null=True)
    name = models.CharField(max_length=100, null=True)
    material = models.CharField(max_length=200,null=True)
    origin = models.CharField(max_length=200,null=True)
    type = models.CharField(max_length=200,null=True)

    class Meta:
        db_table = "jd_bag"

class JdAccessories(models.Model):
    _id = models.CharField(primary_key=True, max_length=200)
    brand = models.CharField(max_length=50, null=True)
    material = models.CharField(max_length=100, null=True)
    price = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=200, null=True)
    origin = models.CharField(max_length=50, null=True)
    producturl = models.CharField(max_length=100, null=True)
    sex = models.CharField(max_length=20, null=True)
    type = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = "jd_accessories"

class JdBelt(models.Model):
    _id = models.CharField(primary_key=True, max_length=200)
    material = models.CharField(max_length=100, null=True)
    size = models.CharField(max_length=200, null=True)
    sex = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=200, null=True)
    brand = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=50, null=True)
    style = models.CharField(max_length=20, null=True)
    producturl = models.CharField(max_length=100, null=True)
    origin = models.CharField(max_length=50, null=True)
    price = models.CharField(max_length=20, null=True)

    class Meta:
        db_table = "jd_belt"

class JdDecoration(models.Model):
    _id = models.CharField(primary_key=True, max_length=200)
    brand = models.CharField(max_length=50, null=True)
    origin = models.CharField(max_length=50, null=True)
    sex = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=20, null=True)
    type = models.CharField(max_length=50, null=True)
    producturl = models.CharField(max_length=100, null=True)
    material = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = "jd_decoration"

class JdCloth(models.Model):
    _id = models.CharField(primary_key=True, max_length=200)
    size = models.CharField(max_length=200, null=True)
    material = models.CharField(max_length=200, null=True)
    age = models.CharField(max_length=200, null=True)
    style = models.CharField(max_length=200, null=True)
    color = models.CharField(max_length=200, null=True)
    weight = models.CharField(max_length=200, null=True)
    origin = models.CharField(max_length=100, null=True)
    price = models.CharField(max_length=100, null=True)
    brand = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=True)
    producturl = models.CharField(max_length=100, null=True)
    number = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = "jd_cloth"

class JdShoe(models.Model):
    _id = models.CharField(primary_key=True, max_length=200)
    price = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    origin = models.CharField(max_length=200, null=True)
    brand = models.CharField(max_length=200, null=True)
    size = models.CharField(max_length=200, null=True)
    sex = models.CharField(max_length=200, null=True)
    material = models.CharField(max_length=100, null=True)
    producturl = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=100, null=True)
    color = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = "jd_shoe"

class JdWallet(models.Model):
    _id = models.CharField(primary_key=True, max_length=200)
    material = models.CharField(max_length=200, null=True)
    sex = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=200, null=True)
    color = models.CharField(max_length=200, null=True)
    origin = models.CharField(max_length=200, null=True)
    brand = models.CharField(max_length=100, null=True)
    producturl = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=True)


    class Meta:
        db_table = "jd_wallet"

class JdBeautyMakeup(models.Model):
    _id = models.CharField(primary_key=True, max_length=200)
    effect = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    weight = models.CharField(max_length=200, null=True)
    brand = models.CharField(max_length=200, null=True)
    wherefrom = models.CharField(max_length=200, null=True)
    skin = models.CharField(max_length=200, null=True)
    origin = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=200, null=True)


    class Meta:
        db_table = "jd_beautymakeup"

class SkAccessories(models.Model):
    _id = models.CharField(primary_key=True, max_length=200)
    origin = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=200, null=True)
    productproperties = models.CharField(max_length=200, null=True)
    producturl = models.CharField(max_length=200, null=True)
    brand = models.CharField(max_length=200, null=True)
    size = models.CharField(max_length=500, null=True)


    class Meta:
        db_table = "sk_accessories"

class SkBags(models.Model):
    _id = models.CharField(primary_key=True, max_length=200)
    size = models.CharField(max_length=200, null=True)
    material = models.CharField(max_length=200, null=True)
    origin = models.CharField(max_length=200, null=True)
    color = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=200, null=True)
    ApplicablePeople = models.CharField(max_length=200, null=True)
    brand = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=200, null=True)


    class Meta:
        db_table = "sk_bag"

class SkCloth(models.Model):
    _id = models.CharField(primary_key=True, max_length=200)
    brand = models.CharField(max_length=200, null=True)
    style = models.CharField(max_length=200, null=True)
    material = models.CharField(max_length=200, null=True)
    origin = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)



    class Meta:
        db_table = "sk_cloth"

class SkJewellery(models.Model):
    _id = models.CharField(primary_key=True, max_length=200)
    materialproperties = models.CharField(max_length=200, null=True)
    producturl = models.CharField(max_length=200, null=True)
    productproperties = models.CharField(max_length=200, null=True)
    color = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    origin = models.CharField(max_length=200, null=True)
    size = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=200, null=True)
    style = models.CharField(max_length=200, null=True)
    brand = models.CharField(max_length=200, null=True)


    class Meta:
        db_table = "sk_jewellery"


class TmBags(models.Model):
    _id = models.CharField(primary_key=True, max_length=200)
    price = models.CharField(max_length=200, null=True)
    sex = models.CharField(max_length=200, null=True)
    size = models.CharField(max_length=200, null=True)
    color = models.TextField(null=True)
    style = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    material = models.CharField(max_length=200, null=True)
    brand = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=200, null=True)


    class Meta:
        db_table = "tm_bag"

class TmBeautyMakeup(models.Model):
    _id = models.CharField(primary_key=True, max_length=200)
    shelf = models.CharField(max_length=200, null=True)
    datelimit = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=200, null=True)
    weight = models.CharField(max_length=200, null=True)
    effect = models.CharField(max_length=200, null=True)
    skin = models.CharField(max_length=200, null=True)
    brand = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = "tm_beautymakeup"

class TmJewelry(models.Model):
    _id = models.CharField(primary_key=True, max_length=200)
    color = models.CharField(max_length=200, null=True)
    appraisaltype = models.CharField(max_length=200, null=True)
    vicegrade = models.CharField(max_length=200, null=True)
    specifications = models.TextField(null=True)
    name = models.CharField(max_length=200, null=True)
    appraisalmarks = models.CharField(max_length=200, null=True)
    paragraph = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=200, null=True)
    material = models.CharField(max_length=200, null=True)
    certificationmark = models.CharField(max_length=200, null=True)
    brand = models.CharField(max_length=200, null=True)
    use = models.CharField(max_length=200, null=True)
    maingrade = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = "tm_jewelry"

class TmColth(models.Model):
    _id = models.CharField(primary_key=True, max_length=200)
    name = models.CharField(max_length=200, null=True)
    year = models.CharField(max_length=200, null=True)
    age = models.CharField(max_length=200, null=True)
    size = models.TextField(null=True)
    brand = models.CharField(max_length=200, null=True)
    color = models.TextField(null=True)
    style = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=200, null=True)
    kuanshi = models.CharField(max_length=200, null=True)
    material = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=200, null=True)


    class Meta:
        db_table = "tm_colth"

class TmShoe(models.Model):
    _id = models.CharField(primary_key=True, max_length=200)
    year = models.CharField(max_length=200, null=True)
    material = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=200, null=True)
    brand = models.CharField(max_length=200, null=True)
    style = models.CharField(max_length=200, null=True)
    color = models.TextField(null=True)
    name = models.CharField(max_length=200, null=True)
    weight = models.CharField(max_length=200, null=True)
    size = models.CharField(max_length=200, null=True)
    people = models.CharField(max_length=200, null=True)
    kuansi = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=200, null=True)


    class Meta:
        db_table = "tm_shoe"

class SkBeautyMakeup(models.Model):
    _id = models.CharField(primary_key=True, max_length=200)
    name = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=200, null=True)
    people = models.CharField(max_length=200, null=True)
    shelflife = models.CharField(max_length=200, null=True)
    weight = models.CharField(max_length=200, null=True)
    scenario = models.CharField(max_length=200, null=True)
    material = models.CharField(max_length=200, null=True)
    efficacy = models.CharField(max_length=200, null=True)
    origin = models.CharField(max_length=200, null=True)
    skin = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=200, null=True)
    brand = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = "sk_beautymakeup"




class mall(models.Model):
    title=models.CharField(max_length=20)
    title2=models.CharField(max_length=20,null=True)
    pid=models.ForeignKey('self',null=True,blank=True)
    class Meta:
        db_table="malls"

