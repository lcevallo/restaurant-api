class Config:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/restaurant_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False