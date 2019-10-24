from lxml import html
import requests

page = requests.get('https://github.com/pricing/')
tree = html.fromstring(page.content)
print('Page Object:', tree)
plans = tree.xpath('//h3[@class="h3-mktg"]/text()')
pricing = tree.xpath('//h3[@class="h000-mktg lh-condensed-ultra my-2"]/text()')
print('Plans:', plans, "\nPricing:", pricing)