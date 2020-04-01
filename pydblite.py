from pydblite import Base

db = Base('users.pdl')
db.create('name', 'password')

if db.exists():
    db.open()
