from rest_framework import serializers
from predicteur_app.models import Incident


class IncidentSerializer(serializers.Serializer)  :
    """ to serialize or deserialize data
    -> Serialize                               : model instance / querysets => native Python datatypes => JSON
        ** NETWORK **
    -> Deserialize                             : JSON to model instance
    """

    time_sys             = serializers.FloatField()
    active               = serializers.FloatField()
    reassignment_count   = serializers.FloatField()
    reopen_count         = serializers.FloatField()
    sys_mod_count        = serializers.FloatField()
    made_sla             = serializers.FloatField()
    impact               = serializers.FloatField()
    urgency              = serializers.FloatField()
    priority             = serializers.FloatField()
    knowledge            = serializers.FloatField()

    #The dependent variable y :
    time_completion      =serializers.FloatField(allow_null=True)


    

    def create(self, validated_data)           :
        """ Create and return a new 'Incident' instance, given the validated data """
        return Incident.objects.create(**validated_data)

    def update(self, instance, validated_data) :
        """ Update and return an existing 'Houste' instance, given the validated data """
        instance.time_sys              =validated_data.get('time_sys',instance.time_sys)
        instance.active                =validated_data.get('active',instance.active)
        instance.reassignment_count    =validated_data.get('reassignment_count',instance.reassignment_count)
        instance.reopen_count          =validated_data.get('reopen_count',instance.reopen_count)
        instance.sys_mod_count         =validated_data.get('sys_mod_count',instance.sys_mod_count)
        instance.made_sla              =validated_data.get('made_sla',instance.made_sla)
        instance.impact                =validated_data.get('impact',instance.impact)
        instance.urgency               =validated_data.get('urgency',instance.urgency)
        instance.priority              =validated_data.get('priority',instance.priority)
        instance.knowledge             =validated_data.get('knowledge',instance.knowledge)
#instance.MEDV   = validated_data.get('MEDV' , instance.MEDV)
        instance.save()
        return instance




