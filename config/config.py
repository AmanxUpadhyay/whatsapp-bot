class Config:
    DEBUG = False
    # Add other configuration settings here

class DevelopmentConfig(Config):
    DEBUG = True
    # Add development-specific configuration settings here

# Add other environment-specific configuration classes as needed

config = DevelopmentConfig()