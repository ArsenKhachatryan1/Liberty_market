from django.db import models

# Create your models here.


class Home_page(models.Model):

    logo_img = models.ImageField('Logo image', upload_to='images')
    home = models.CharField('Home', max_length=30)
    author = models.CharField('Author', max_length=30)
    create = models.CharField('Create', max_length=30)
    details = models.CharField('Details', max_length=30)
    explore = models.CharField('Explore', max_length=30)


class Home_banner(models.Model):

    name = models.CharField('Name', max_length=60)
    text1 = models.CharField('text1', max_length=256)
    text2 = models.CharField('text2', max_length=256)
    text3 = models.CharField('text3', max_length=256)
    text4 = models.CharField('text4', max_length=256)
    text5 = models.CharField('text5', max_length=256)
    video_link = models.URLField('Video link')
    img1 = models.ImageField('Image 1', upload_to='images')
    img2 = models.ImageField('Image 2', upload_to='images')



class Categories(models.Model):

    name = models.CharField('Name', max_length=60)
    img = models.ImageField('Image', upload_to='images')

    def __str__(self) -> str:
        return self.name


class Collection(models.Model):

    img = models.ImageField('Collection image', upload_to='images')
    title = models.CharField('Title', max_length=60)
    item_col = models.CharField('Item collection', max_length=60)
    item_count = models.CharField('Item count', max_length=60)
    category = models.CharField('Category', max_length=60)
    category_name = models.CharField('Category name', max_length=60)
    btn_name = models.CharField('Collection Button Name', max_length=40)



class HomeNFT_Info(models.Model):

    img = models.ImageField('Image', upload_to='images')
    title = models.CharField('Title', max_length=60)
    text1 = models.CharField('text1', max_length=256)
    text_linked = models.CharField('Linked text', blank=True, max_length=256)
    text3 = models.CharField('text3', blank=True, max_length=256)
    link = models.URLField('Link', blank=True)



class Item_Market(models.Model):
    category = models.CharField('Category filter', max_length=60)
    img = models.ImageField('Image', upload_to='images')
    img_auth = models.ImageField('Author image', upload_to='images')
    title = models.CharField('Title', max_length=60)
    text1 = models.CharField('text1', max_length=256)
    text_linked = models.CharField('Linked text', blank=True, max_length=256)
    link = models.URLField('Link', blank=True)
    bid = models.CharField('Curent Bid', max_length=60)
    bid_value = models.CharField('Bid value', max_length=60)
    bid_price = models.CharField('Bid price (USD)', max_length=60)
    bid_ends = models.CharField('Ends In', max_length=60)
    end_time = models.CharField('Ends time', max_length=60)
    end_date = models.CharField('Ends date', max_length=60)
    btn_name = models.CharField('Item Button Name', max_length=40)

