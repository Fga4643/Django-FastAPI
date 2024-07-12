from django.db import models


class ClientInfo(models.Model):
    info = models.CharField(max_length=256, null=False, blank=False)

    class Meta:
        managed = False
        db_table = 'clients_info'


class Client(models.Model):
    client_name = models.CharField(max_length=256, null=False, blank=False)
    client_info = models.CharField(max_length=256, null=False, blank=False)

    class Meta:
        managed = False
        db_table = 'clients'


class Endpoint(models.Model):
    endpoint_name = models.CharField(max_length=256, null=False, blank=False)

    class Meta:
        managed = False
        db_table = 'endpoints'


class EndpointStates(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT, null=False, blank=False)
    endpoint = models.ForeignKey(Endpoint, on_delete=models.PROTECT, null=False, blank=False)
    state_name = models.CharField(max_length=256)
    state_reason = models.CharField(max_length=256)
    state_start = models.CharField(max_length=256)
    state_end = models.CharField(max_length=256)
    state_id = models.CharField(max_length=256)
    group_id = models.CharField(max_length=256)
    reason_group = models.CharField(max_length=256)
    info = models.JSONField(default=dict)

    class Meta:
        managed = False
        db_table = 'endpoint_states'