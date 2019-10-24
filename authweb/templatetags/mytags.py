from django import template

register = template.Library()

@register.filter
def str_confirmacao(value): # Only one argument.
    """Converts a string into all lowercase"""
    if(value == 0):
        return "Nao Confirmada"
    else:
        return "Reservado"
    
@register.filter
def str_aula(value): # Only one argument.
    """Converts a string into all lowercase"""
    if(value == True):
        return "Sim"
    else:
        return "Nao"
    
@register.filter
def str_none(value): # Only one argument.
    """Converts a string into all lowercase"""
    if(value == None):
        return "Nao definido"
    else:
        return "Nao definido"


