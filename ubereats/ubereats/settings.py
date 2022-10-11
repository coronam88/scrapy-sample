# Scrapy settings for ubereats project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from dotenv import dotenv_values 
import os


basedir = os.path.abspath(os.path.dirname(__file__))
config = dotenv_values(os.path.join(basedir, '../../.env'))

BOT_NAME = 'ubereats'

SPIDER_MODULES = ['ubereats.spiders']
NEWSPIDER_MODULE = 'ubereats.spiders'


# playwrights specific stuff
DOWNLOAD_HANDLERS = {
    'http': 'scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler',
    'https': 'scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler',
}

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ubereats (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True


# Mongo stuff
MONGODB_SERVER = config.get("MONGODB_SERVER")
MONGODB_PORT = config.get("MONGODB_PORT")
MONGO_INITDB = config.get("MONGO_INITDB_DATABASE")
MONGODB_COLLECTION = config.get("MONGODB_COLLECTION")
MONGO_INITDB_ROOT_USERNAME=config.get("MONGO_INITDB_ROOT_USERNAME")
MONGO_INITDB_ROOT_PASSWORD=config.get("MONGO_INITDB_ROOT_PASSWORD")
MONGO_PATH_TLS_PEM=config.get("PATH_TLS_PEM")

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'ubereats.middlewares.UbereatsSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'ubereats.middlewares.UbereatsDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'ubereats.pipelines.UbereatsPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

USER_AGENTS_LIST = [
'Dalvik/2.1.0 (Linux; U; Android 10; TC26 Build/10-16-10.00-QG-U28-STD-HEL-04)',
'Mozilla/5.0 (X11; CrOS x86_64 9592.3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.10 Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.0; F3212) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4_0) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/95.0.150 Chrome/89.0.4389.150 Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.1.0; T8116 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36/RpAqrbGi-53',
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.4; ja-JP-mac; rv:1.9.2.28) Gecko/20120306 Firefox/3.6.28',
'Mozilla/5.0 (Linux; U; Android 9; en-gb; CPH1861 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.116 Mobile Safari/537.36 HeyTapBrowser/15.7.7.1',
'Mozilla/5.0 (Linux; Android 6.0.1; SM-G389F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.0; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.88 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; LON-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.88 Mobile Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4532.2 Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.0.1; SM-N910S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0.1; Redmi Note 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4530.6 Mobile Safari/537.36']