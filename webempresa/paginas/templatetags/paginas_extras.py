from django import template
from ..models import Pagina

register = template.Library()


# decorador
@register.simple_tag
def get_pagina_list():
    paginas = Pagina.objects.all()
    return paginas
