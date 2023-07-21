from django.utils import timezone
from django.utils.translation import gettext as _

def time_since_created_at(obj):
    now = timezone.now()
    diff = now - obj.created_at

    if diff.days > 365:
        years = diff.days // 365
        return _('{years} ano(s) atrás').format(years=years)
    elif diff.days > 30:
        months = diff.days // 30
        return _('{months} mês(es) atrás').format(months=months)
    elif diff.days > 0:
        return _('{days} dia(s) atrás').format(days=diff.days)
    elif diff.seconds > 3600:
        hours = diff.seconds // 3600
        return _('{hours} hora(s) atrás').format(hours=hours)
    elif diff.seconds > 60:
        minutes = diff.seconds // 60
        return _('{minutes} minuto(s) atrás').format(minutes=minutes)
    else:
        return _('agora')