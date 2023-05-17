from django.shortcuts import render
from . models import Home_page, Home_banner, Categories, Collection, HomeNFT_Info, Item_Market

# Create your views here.


def index(requests):
    home_info = Home_page.objects.all()[0]
    home_banner = Home_banner.objects.all()[0]
    home_categ = Categories.objects.all()
    home_collection = Collection.objects.all()
    nft_info1 = HomeNFT_Info.objects.all()[0]
    nft_info2 = HomeNFT_Info.objects.all()[1]
    nft_info3 = HomeNFT_Info.objects.all()[2]
    item_market = Item_Market.objects.all()
    
    return render(requests, 'main/index.html', context={
       'act':'index',
       'home_info':home_info,
       'home_banner':home_banner,
       'home_categ':home_categ,
       'home_collection':home_collection,
       'nft_info1':nft_info1,
       'nft_info2':nft_info2,
       'nft_info3':nft_info3,
       'item_market':item_market,
    })


def author(requests):
    home_info = Home_page.objects.all()[0]
    nft_info1 = HomeNFT_Info.objects.all()[0]
    nft_info2 = HomeNFT_Info.objects.all()[1]
    nft_info3 = HomeNFT_Info.objects.all()[2]
    return render(requests, 'main/author.html', context={
        'act':'author',
       'home_info':home_info ,
       'nft_info1':nft_info1,
       'nft_info2':nft_info2,
       'nft_info3':nft_info3,
    })


def details(requests):
    nft_info1 = HomeNFT_Info.objects.all()[0]
    nft_info2 = HomeNFT_Info.objects.all()[1]
    nft_info3 = HomeNFT_Info.objects.all()[2]
    home_info = Home_page.objects.all()[0]

    return render(requests, 'main/details.html', context={
        'act':'details',
       'home_info':home_info,
       'nft_info1':nft_info1,
       'nft_info2':nft_info2,
       'nft_info3':nft_info3,
    })


def explore(requests):
    home_info = Home_page.objects.all()[0]
    item_market = Item_Market.objects.all()

    return render(requests, 'main/explore.html', context={
        'act':'explore',
       'home_info':home_info,
       'item_market':item_market,
    })


def create(requests):
    home_info = Home_page.objects.all()[0]
    return render(requests, 'main/create.html', context={
        'act':'create',
       'home_info':home_info 
    })