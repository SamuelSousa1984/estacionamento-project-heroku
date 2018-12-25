from django.contrib import admin
from .models import (
    Pessoa,
    Marca,
    Veiculo,
    Parametros,
    MovRotativo,
    Mensalista,
    MovMensalista
)

class MovRotativoAdmin(admin.ModelAdmin):
    list_display = (
        'checkin', 'checkout', 'valor_hora', 'veiculo', 'total', 'horas_total',
        'pago')

class MensalistaAdmin(admin.ModelAdmin):
    list_display = (
        'veiculo', 'inicio'
    )

class MovMensalistaAdmin(admin.ModelAdmin):
    list_display = (
        'mensalista', 'dt_pgmt', 'total'
    )


admin.site.register(Pessoa)
admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Parametros)
admin.site.register(Mensalista, MensalistaAdmin)
admin.site.register(MovRotativo, MovRotativoAdmin)
admin.site.register(MovMensalista, MovMensalistaAdmin)
