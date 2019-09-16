class DevConfig:
    # SQLALCHEMY_DATABASE_URI='sqlite:///studebase.db'
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://jon:nathanoj35@localhost/Student'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY='IAMSECRET'