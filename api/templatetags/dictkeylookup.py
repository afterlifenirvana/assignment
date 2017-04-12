from django import template
register = template.Library()



@register.filter
def dictkeylookup(the_dict, key):
   # Try to fetch from the dict, and if it's not found return an empty string.
   return the_dict.get(key, '')