class DevConfig:
    SQLALCHEMY_DATABASE_URI='sqlite:///studebase.db'
    # SQLALCHEMY_DATABASE_URI='mysql:///jon:nathanoj35/Student'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY='IAMSECRET'