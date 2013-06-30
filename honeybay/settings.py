# Scrapy settings for honeybay project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'honeybay'
LOG_LEVEL = 'DEBUG'
SPIDER_MODULES = ['honeybay.spiders']
NEWSPIDER_MODULE = 'honeybay.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'honeybay (+http://www.yourdomain.com)'
