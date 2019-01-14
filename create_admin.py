from AtlasSwitch.models import User
from AtlasSwitch import db

# stuff should be the relevant things you want to add in the initial db
user = User(stuff)

db.session.add(user)
db.session.commit()
