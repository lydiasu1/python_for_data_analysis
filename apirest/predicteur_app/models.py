from django.db import models

# Create your models here.
class Incident(models.Model):
    time_sys             = models.FloatField()
    active               = models.FloatField()
    reassignment_count   = models.FloatField()
    reopen_count         = models.FloatField()
    sys_mod_count        = models.FloatField()
    made_sla             = models.FloatField()
    impact               = models.FloatField()
    urgency              = models.FloatField()
    priority             = models.FloatField()
    knowledge            = models.FloatField()

    #The dependent variable y :
    time_completion      =models.FloatField(null=True)


    created = models.DateTimeField(auto_now_add=True)
    
    class Metat:
        oredering=['created']

"""
"time_sys"             = -0.9189107952496294
"active"               =  0.0
"reassignment_count"   =  -0.5999365773445644
"reopen_count"         =  -0.09061081556378088
"sys_mod_count"        =  -0.31646565342768107
"made_sla"             =  0.007739622801644428
"impact"               =  0.11174352039119535
"urgency"              =  0.07771297753790767
"priority"             =  0.039449136623093205
"knowledge"            =  2.4176472964815408
"""

#{"time_sys":"-37.054167","active":"0","reassignment_count":"0","reopen_count":"0","sys_mod_count":"4","made_sla":"1","impact":"2","urgency":"2","priority":"2","knowledge":"1"}         