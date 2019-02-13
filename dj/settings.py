# -*- coding: utf-8 -*-
"""
Django settings for dj project.
Generated by 'django-admin startproject' using Django 1.11.10.
For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#5xvrjzddr3@qqxr@2&k2a9gt+q_eclit*uu^odd0_dw(w5-9@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'cmdb.apps.SuitConfig',  # 放admin前面，覆盖admin默认样式
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap3',
    'cmdb.apps.CmdbConfig',
    'channels',  # websocket
    'readonly',  # Django添加只读权限

    'django_otp',
    'django_otp.plugins.otp_totp',  # 时间戳
    # 'django_otp.plugins.otp_hotp',
    'elfinder',  # SFTP


]

LOGIN_URL = '/login'

# AUTH_USER_MODEL = 'cmdb.UserProfile'
AUTH_PROFILE_MODULE = 'cmdb.UserProfile'

# AUTHENTICATION_BACKENDS = (
# 'django.contrib.auth.backends.ModelBackend', # django默认的backend
# 'guardian.backends.ObjectPermissionBackend',
# 'django.contrib.auth.backends.RemoteUserBackend',
# )


# SESSION
SESSION_COOKIE_AGE = 60 * 60 * 14  # cookie有效期*秒
# False：会话cookie可以在用户浏览器中保持有效期。True：关闭浏览器，则Cookie失效
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
# SESSION_COOKIE_DOMAIN = "*" #作用域

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_otp.middleware.OTPMiddleware',  # OTP验证
    # 'django.contrib.auth.middleware.RemoteUserMiddleware',
    # 'django.contrib.auth.middleware.PersistentRemoteUserMiddleware',
]

ROOT_URLCONF = 'dj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# 使用sqlite3
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# try:
#     import psycopg2
#     # 默认使用PostgreSQL
#     engine = 'django.db.backends.postgresql_psycopg2'
#     options = {}

# except:
#     # import MySQLdb
#     # conn = MySQLdb.connect(user=db['USER'], db=db['NAME'], passwd=db['PASSWORD'], host=db['HOST'])
#     # conn.ping()
#     # conn.close()

#     # 使用MySQL
#     engine = 'django.db.backends.mysql'
#     options = {'charset': 'utf8', 'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"}

#     from django.db.backends.mysql.base import DatabaseFeatures
#     DatabaseFeatures.supports_microsecond_precision = False  # mysql5.6+ 时间不要毫秒


# user = 'root'
# password = ''
# host = '127.0.0.1'

# DATABASES = {
#     'default': {
#         'ENGINE': engine,
#         'NAME': 'dj',
#         'USER': user,
#         'PASSWORD': password,
#         'HOST': host,
#         # 'PORT': '5432',
#         # 'TEST': {'NAME': 'test',},
#         'OPTIONS': options,
#     },

# }



# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 6,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'


USE_I18N = True

USE_L10N = True

USE_TZ = False

from django.conf.locale.zh_Hans import formats
formats.DATETIME_FORMAT = 'Y-m-d H:i'
formats.DATETIME_INPUT_FORMATS = 'Y-m-d H:i'

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_ROOT = '/kf/bak'
MEDIA_URL = '/media/'

SSH_REPLAY = '/kf/replay'

REDIS = ['127.0.0.1:6379', '2019']

# Channels settings
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgi_redis.RedisChannelLayer",  # use redis backend
        "CONFIG": {
            "hosts": ['redis://:%s@%s' % (REDIS[1], REDIS[0]), ],  # set redis address
            "channel_capacity": {
                "http.request": 1000,
                "websocket.send*": 10000,
            },
            "capacity": 10000,
        },
        # "BACKEND": "asgiref.inmemory.ChannelLayer",  #开发环境中使用内存就可以了
        # "BACKEND": "asgi_ipc.IPCChannelLayer",       #daphne和runworker必需在同一服务器，不支持分布式
        "ROUTING": "dj.routing.channel_routing",    # 定义channel的根入口
        "CHANNEL_NAME": "dj.",    # channel路由名称加前缀，以区分多端口
    },
}


CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS[0],
        'OPTIONS': {
            # 'DB': 10,
            'PASSWORD': REDIS[1],
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PARSER_CLASS': 'redis.connection.HiredisParser',
            'CONNECTION_POOL_CLASS': 'redis.BlockingConnectionPool',
            'CONNECTION_POOL_CLASS_KWARGS': {
                'max_connections': 200,
                'timeout': 10,
            },
        },
        'KEY_PREFIX': 'dj'
    }
}

BOOTSTRAP3 = {
    # 修改bootstrap3.bootstrap.BOOTSTRAP3_DEFAULTS默认设置
    # 'horizontal_label_class': 'col-md-2', #默认为col-md-3
    # 'horizontal_field_class': 'col-md-8',
}