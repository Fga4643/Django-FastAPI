from django.contrib import admin

from polls.models import ClientInfo, Client, Endpoint, EndpointStates

admin.site.register(ClientInfo)
admin.site.register(Client)
admin.site.register(Endpoint)
admin.site.register(EndpointStates)