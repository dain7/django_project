from django import template
import re

register = template.Library()

@register.filter
def add_link(value):
    content = value.posting_content

    tags = value.tagging.all()
    for tag in tags:
        content = re.sub(r'\#' + tag.tag_content + r'\b',
            '<a href="/post/search/'+tag.tag_content+'">#'+tag.tag_content+'</a>', content)
    return content
