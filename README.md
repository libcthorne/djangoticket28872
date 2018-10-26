# Environment

Django
commit 55b0b766fbeb2f71e68331a2e14205702f681012

# DB setup

https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04

# Recreate

```
import logging
l = logging.getLogger('django.db.backends')
l.setLevel(logging.DEBUG)
l.addHandler(logging.StreamHandler())

from testapp.models import *
MyModel1.objects.filter(resource__foo__id__in=MyModel2.objects.all().values_list("id"))
```

# Run SQL

Broken:
```
SELECT "testapp_mymodel1"."id", "testapp_mymodel1"."resource" FROM "testapp_mymodel1" WHERE ("testapp_mymodel1"."resource" #> ARRAY['foo','id']) IN (SELECT U0."id" FROM "testapp_mymodel2" U0)  LIMIT 21;
```

Works (`to_jsonb` added):
```
SELECT "testapp_mymodel1"."id", "testapp_mymodel1"."resource" FROM "testapp_mymodel1" WHERE ("testapp_mymodel1"."resource" #> ARRAY['foo','id']) IN (SELECT to_jsonb(U0."id") FROM "testapp_mymodel2" U0)  LIMIT 21;
```
