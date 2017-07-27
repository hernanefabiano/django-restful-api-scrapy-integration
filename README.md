# django-restful-api-scrapy-integration
A simple django restful-api and scrapy and mongodb integration

Search API using queryset filtering.

News List
Contains scraped data from leading news portal.
Q parameter is used to search for specific news information, will scan the mongodb 
base on the parameter value stated on the url e.g. http://127.0.0.1/api/news/?q=Russia
Lookup fields are headline, section, and news summary.


Scrape news portal and save all news information in mongodb

Sample screenshot:

![Alt text](/../master/scrapy.png?raw=true "TheGuardian.com")
