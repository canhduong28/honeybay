# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class DealItem(Item):
    
    offer = Field()
    company = Field()
    start_date = Field()
    end_date = Field()
    s_price = Field()
    us_price = Field()
    discount = Field()
    category = Field()
    main_deal = Field()	
    sold = Field()
    total_sales = Field()
    merchant = Field()
    merchant_contact = Field()
    deal_in_DayWatch = Field()
    offer_id = Field()
    link = Field()