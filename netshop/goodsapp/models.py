from django.db import models

# Create your models here.
class Category(models.Model):
    """类别表"""
    cname = models.CharField(max_length=10)#类别名称

    def __str__(self):
        return self.cname

class Goods(models.Model):
    """商品表"""
    gname = models.CharField(verbose_name='商品名称', max_length=100)
    gdesc = models.CharField(verbose_name='商品描述', max_length=100)
    oldprice = models.DecimalField(verbose_name='原价', max_digits=5, decimal_places=2)
    price = models.DecimalField(verbose_name='现价', max_digits=5, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='类别id')

    def __str__(self):
        return self.gname

class GoodsDetailName(models.Model):
    """详情名称表"""
    gdname = models.CharField(verbose_name='详情名称', max_length=30)

    def __str__(self):
        return self.gdname

class GoodsDetail(models.Model):
    """商品详情表"""
    gdurl = models.ImageField(verbose_name='详情图片地址', upload_to='')
    detailname = models.ForeignKey(GoodsDetailName, on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)

    def __str__(self):
        return self.detailname.gdname

class Size(models.Model):
    """尺寸表"""
    sname = models.CharField(verbose_name='尺寸名称', max_length=10)

    def __str__(self):
        return self.sname

class Color(models.Model):
    colorname = models.CharField(verbose_name='颜色名称', max_length=10)
    colorurl = models.ImageField(verbose_name='颜色图片地址', upload_to='color/')

    def __str__(self):
        return self.colorname

class Inventory(models.Model):
    """库存表"""
    count = models.PositiveIntegerField(verbose_name='库存数量')
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
