from AtlasSwitch.models import User, History
from AtlasSwitch import db

# stuff should be the relevant things you want to add in the initial db
#user = User(stuff)

#history = History('')

db.session.add(history)
db.session.commit()
