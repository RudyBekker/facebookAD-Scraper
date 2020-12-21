# -*- coding: utf-8 -*-
import scrapy
import json

from scrapy.http import FormRequest


class SiteProductItem(scrapy.Item):
    id = scrapy.Field()
    table_name = scrapy.Field()
    verified = scrapy.Field()
    affiliate_network_id = scrapy.Field()
    tags = scrapy.Field()
    tags_status = scrapy.Field()
    built_with = scrapy.Field()
    ad_position = scrapy.Field()
    ad_type = scrapy.Field()
    post_owner_image = scrapy.Field()
    post_owner = scrapy.Field()
    ad_url = scrapy.Field()
    ad_text = scrapy.Field()
    likes = scrapy.Field()
    comment = scrapy.Field()
    share = scrapy.Field()
    ad_image_video = scrapy.Field()
    ad_title = scrapy.Field()
    image_video_url = scrapy.Field()
    news_feed_description = scrapy.Field()
    post_owner_id = scrapy.Field()
    post_date = scrapy.Field()
    last_seen = scrapy.Field()
    country = scrapy.Field()


class AdsDetailItem(scrapy.Item):
    id = scrapy.Field()
    table_name = scrapy.Field()
    ad_id = scrapy.Field()
    ad_image_video = scrapy.Field()
    ad_position = scrapy.Field()
    ad_text = scrapy.Field()
    ad_title = scrapy.Field()
    ad_url = scrapy.Field()
    built_with = scrapy.Field()
    call_to_action = scrapy.Field()
    category = scrapy.Field()
    city = scrapy.Field()
    comment = scrapy.Field()
    country = scrapy.Field()
    country_code = scrapy.Field()
    days_running = scrapy.Field()
    destination_scraper_status = scrapy.Field()
    destination_url = scrapy.Field()
    domain = scrapy.Field()
    domain_registered_date = scrapy.Field()
    facebook_id = scrapy.Field()
    final_url = scrapy.Field()
    firstSeenOnDesktop = scrapy.Field()
    first_seen = scrapy.Field()
    image_video_url = scrapy.Field()
    iso = scrapy.Field()
    lander_path = scrapy.Field()
    lander_status = scrapy.Field()
    lastSeenOnDesktop = scrapy.Field()
    last_seen = scrapy.Field()
    likes = scrapy.Field()
    lower_age = scrapy.Field()
    news_feed_description = scrapy.Field()
    platform = scrapy.Field()
    png_file = scrapy.Field()
    post_date = scrapy.Field()
    post_owner = scrapy.Field()
    post_owner_image = scrapy.Field()
    redirect_destination_url_source = scrapy.Field()
    redirect_url = scrapy.Field()
    screenshot_url = scrapy.Field()
    share = scrapy.Field()
    source_url = scrapy.Field()
    state = scrapy.Field()
    ad_type = scrapy.Field()
    upper_age = scrapy.Field()
    url = scrapy.Field()
    url_type = scrapy.Field()
    version = scrapy.Field()
    white_ad_screenshot = scrapy.Field()


class LikeCommentShareDetailItem(scrapy.Item):
    id = scrapy.Field()
    table_name = scrapy.Field()
    facebook_ad_id = scrapy.Field()
    date = scrapy.Field()
    comment = scrapy.Field()
    likes = scrapy.Field()
    share = scrapy.Field()


class LikeHitDetailItem(scrapy.Item):
    id = scrapy.Field()
    table_name = scrapy.Field()
    facebook_ad_id = scrapy.Field()
    date = scrapy.Field()
    hits = scrapy.Field()


class UserInfoItem(scrapy.Item):
    facebook_id = scrapy.Field()
    table_name = scrapy.Field()
    name = scrapy.Field()
    age = scrapy.Field()
    gender = scrapy.Field()
    current_country = scrapy.Field()
    current_country_id = scrapy.Field()
    others_places_lived = scrapy.Field()
    relationship_status = scrapy.Field()


class CountryInfoItem(scrapy.Item):
    table_name = scrapy.Field()
    facebook_ad_id = scrapy.Field()
    country = scrapy.Field()


class PoweradspySpider(scrapy.Spider):
    name = 'poweradspy'
    allowed_domains = ['poweradspy.com']
    start_urls = ['http://app.poweradspy.com/amember/member']
    lastval = '9999999'
    step = 0
    ads_count = 0
    ads_total_count = 9999999

    LOGIN_URL = 'https://app.poweradspy.com/amember/login'
    HOME_URL = 'https://app.poweradspy.com/dashboard'

    USERNAME = 'optimizedx'
    PASSWORD = 'Password1'

    ADS_API_URL = 'https://app.poweradspy.com/getAds'
    ADS_DETAIL_URL = 'https://app.poweradspy.com/adDetails'
    ADS_LIKE_COMMENT_SHARE_URL = 'https://app.poweradspy.com/getLikeCommentShareDetails'
    ADS_LIKE_HITS_URL = 'https://app.poweradspy.com/getLikeHitsDetails'
    ADS_USER_DATA_URL = 'https://app.poweradspy.com/getFacebookUserData'
    ADS_COUNTRY_URL = 'https://app.poweradspy.com/getFacebookAdCountry'

    def start_requests(self):
        url = 'http://app.poweradspy.com/amember/member'
        yield scrapy.Request(url=url, callback=self.login_request)

    def login_request(self, response):
        login_attemp_id = response.xpath("//form[@id='am-login-form']/input[@name='login_attempt_id']/@value").extract()[0]
        amember_redirect_url = response.xpath("//form[@id='am-login-form']/input[@name='amember_redirect_url']/@value").extract()[0]

        form_data = {
            'amember_login': self.USERNAME,
            'amember_pass': self.PASSWORD,
            'login_attempt_id': login_attemp_id,
            'amember_redirect_url': amember_redirect_url
        }

        yield FormRequest(url=self.LOGIN_URL,
                          callback=self.parse_ads,
                          dont_filter=True,
                          method="POST",
                          formdata=form_data
                          )

    def parse_ads(self, response):
        form_data = {
            'currentdate': '9999999999',
            'olderdate': '0',
            'post_currentdate': '9999999999',
            'post_olderdate': '0',
            'domain_currentdate': '9999999999',
            'domain_olderdate': '0',
            'country': '',
            'type': '',
            'position[]': 'FEED',
            'gender': '',
            'lower_age': '16',
            'upper_age': '102',
            'order_column': 'last_seen',
            'order_by': 'desc',
            'keyword': '',
            'advertisername': '',
            'domainname': '',
            'take': '9',
            'skip': '0',
            'lastval': '9999999',
            'callToAction': '',
            'ecommerce': '',
            'track': '',
            'source': '',
            'ip': '0.0.0.0',
            'flag': '1',
            'funnel': '',
            'affiliate': '',
            'favorite': 'false',
            'hidden': 'false',
            'tags': '',
            'lang': '',
            'html': '',
            'commentdata': '',
            'platform': '',
            'discover_id': '',
            'verified': '',
            'page_currentdate': '9999999999',
            'page_olderdate': '0',
            'mixdata': '',
            'html_feild': '',
            'celebrity': '',
            'ocr': '',
            'logo_image': '',
            'object_image': '',
            'clear': 'false'
        }

        yield FormRequest(url=self.ADS_API_URL,
                          callback=self.parse,
                          dont_filter=True,
                          method="POST",
                          formdata=form_data
                          )

    def parse_detail(self, response):
        prod_item = AdsDetailItem()
        response_content = json.loads(response.body)
        if response_content['code'] == 200:
            response_data_info_list = response_content['data']
            for ads_index, response_data_info in enumerate(response_data_info_list):
                prod_item['id'] = int(response_data_info['id'] or 0)
                prod_item['ad_id'] = int(response_data_info['ad_id'] or 0)
                prod_item['ad_image_video'] = str(response_data_info['ad_image_video'])
                prod_item['ad_position'] = str(response_data_info['ad_position'])
                prod_item['ad_text'] = str(response_data_info['ad_text'])
                prod_item['ad_title'] = str(response_data_info['ad_title'])
                prod_item['ad_url'] = str(response_data_info['ad_url'])
                prod_item['built_with'] = str(response_data_info['built_with'])
                prod_item['call_to_action'] = str(response_data_info['call_to_action'])
                prod_item['category'] = str(response_data_info['category'])
                prod_item['city'] = str(response_data_info['city'])
                prod_item['comment'] = int(response_data_info['comment'] or 0)
                prod_item['country'] = str(response_data_info['country'])
                prod_item['country_code'] = str(response_data_info['country_code'])
                prod_item['days_running'] = int(response_data_info['days_running'] or 0)
                prod_item['destination_scraper_status'] = response_data_info['destination_scraper_status']
                prod_item['destination_url'] = str(response_data_info['destination_url'])
                prod_item['domain'] = str(response_data_info['domain'])
                prod_item['domain_registered_date'] = str(response_data_info['domain_registered_date'])
                prod_item['facebook_id'] = response_data_info['facebook_id']
                prod_item['final_url'] = str(response_data_info['final_url'])
                prod_item['firstSeenOnDesktop'] = str(response_data_info['firstSeenOnDesktop'])
                prod_item['first_seen'] = str(response_data_info['first_seen'])
                prod_item['image_video_url'] = str(response_data_info['image_video_url'])
                prod_item['first_seen'] = str(response_data_info['first_seen'])
                prod_item['iso'] = str(response_data_info['iso'])
                prod_item['lander_path'] = str(response_data_info['lander_path'])
                prod_item['lander_status'] = int(response_data_info['lander_status'] or 0)
                prod_item['lastSeenOnDesktop'] = str(response_data_info['lastSeenOnDesktop'])
                prod_item['last_seen'] = str(response_data_info['last_seen'])
                prod_item['likes'] = int(response_data_info['likes'] or 0)
                prod_item['lower_age'] = int(response_data_info['lower_age'] or 0)
                prod_item['news_feed_description'] = str(response_data_info['news_feed_description'])
                prod_item['platform'] = str(response_data_info['platform'])
                prod_item['png_file'] = str(response_data_info['png_file'])
                prod_item['post_date'] = str(response_data_info['post_date'])
                prod_item['post_owner'] = str(response_data_info['post_owner'])
                prod_item['post_owner_image'] = str(response_data_info['post_owner_image'])
                prod_item['redirect_destination_url_source'] = str(response_data_info['redirect_destination_url_source'])
                prod_item['redirect_url'] = str(response_data_info['redirect_url'])
                prod_item['screenshot_url'] = str(response_data_info['screenshot_url'])
                prod_item['share'] = int(response_data_info['share'] or 0)
                prod_item['source_url'] = str(response_data_info['source_url'])
                prod_item['state'] = str(response_data_info['state'])
                prod_item['ad_type'] = str(response_data_info['type'])
                prod_item['upper_age'] = int(response_data_info['upper_age'] or 0)
                prod_item['url'] = str(response_data_info['url'])
                prod_item['url_type'] = str(response_data_info['url_type'])
                prod_item['version'] = str(response_data_info['version'])
                prod_item['white_ad_screenshot'] = str(response_data_info['white_ad_screenshot'])
                prod_item['table_name'] = 'fb_ad_details'

                yield prod_item

    def parse_like_comment_share(self, response):
        prod_item = LikeCommentShareDetailItem()
        response_content = json.loads(response.body)
        if response_content['code'] == 200:
            response_data_info_list = response_content['data']
            for ads_index, response_data_info in enumerate(response_data_info_list):
                prod_item['id'] = int(response_data_info['id'] or 0)
                prod_item['facebook_ad_id'] = int(response_data_info['facebook_ad_id'] or 0)
                prod_item['date'] = str(response_data_info['date'])
                prod_item['comment'] = int(response_data_info['comment'] or 0)
                prod_item['likes'] = int(response_data_info['likes'] or 0)
                prod_item['share'] = int(response_data_info['share'] or 0)
                prod_item['table_name'] = 'fb_ad_comment_likes_share_details'

                yield prod_item

    def parse_like_hits(self, response):
        prod_item = LikeHitDetailItem()
        response_content = json.loads(response.body)
        if response_content['code'] == 200:
            response_data_info_list = response_content['data']
            for ads_index, response_data_info in enumerate(response_data_info_list):
                prod_item['id'] = int(response_data_info['id'] or 0)
                prod_item['facebook_ad_id'] = int(response_data_info['facebook_ad_id'] or 0)
                prod_item['date'] = str(response_data_info['date'])
                prod_item['hits'] = int(response_data_info['hits'] or 0)
                prod_item['table_name'] = 'fb_ad_like_hits_details'

                yield prod_item

    def parse_user_data(self, response):
        prod_item = UserInfoItem()
        response_content = json.loads(response.body)
        if response_content['code'] == 200:
            response_data_info_list = response_content['data']
            for ads_index, response_data_info in enumerate(response_data_info_list):
                prod_item['facebook_id'] = int(response_data_info['facebook_id'] or 0)
                prod_item['name'] = str(response_data_info['name'])
                prod_item['age'] = int(response_data_info['age'] or 0)
                prod_item['gender'] = str(response_data_info['Gender'])
                prod_item['current_country'] = str(response_data_info['current_country'])
                prod_item['current_country_id'] = int(response_data_info['current_country_id'] or 0)
                prod_item['others_places_lived'] = str(response_data_info['others_places_lived'])
                prod_item['relationship_status'] = str(response_data_info['relationship_status'])
                prod_item['table_name'] = 'fb_user_info'

                yield prod_item

    def parse_country(self, response):
        prod_item = CountryInfoItem()
        response_content = json.loads(response.body)
        if response_content['code'] == 200:
            response_data_info_list = response_content['data']
            for ads_index, response_data_info in enumerate(response_data_info_list):
                prod_item['facebook_ad_id'] = int(response_data_info['facebook_ad_id'] or 0)
                prod_item['country'] = str(response_data_info['country'])
                prod_item['table_name'] = 'fb_ad_country_info'

                yield prod_item

    def parse(self, response):
        prod_item = SiteProductItem()
        response_content = json.loads(response.body)
        if response_content['code'] == 200:
            ads_total_count = response_content['ads_count']
            if ads_total_count != 0:
                self.ads_total_count = ads_total_count
            response_data_info_list = response_content['data']
            lastval = response_data_info_list[-1]['id']
            self.lastval = lastval
            self.step = self.step + 1
            self.ads_count = self.ads_count + len(response_data_info_list)

            for ads_index, response_data_info in enumerate(response_data_info_list):
                prod_item['id'] = response_data_info['id']
                prod_item['verified'] = response_data_info['verified']
                prod_item['affiliate_network_id'] = response_data_info['affiliate_network_id']
                prod_item['tags'] = str(response_data_info['tags'])
                prod_item['tags_status'] = response_data_info['tags_status']
                prod_item['built_with'] = str(response_data_info['built_with'])
                prod_item['ad_position'] = str(response_data_info['ad_position'])
                prod_item['ad_type'] = str(response_data_info['type'])
                prod_item['post_owner_image'] = str(response_data_info['post_owner_image'])
                prod_item['post_owner'] = str(response_data_info['post_owner'])
                prod_item['ad_url'] = str(response_data_info['ad_url'])
                prod_item['ad_text'] = str(response_data_info['ad_text'])
                prod_item['likes'] = response_data_info['likes']
                prod_item['comment'] = response_data_info['comment']
                prod_item['share'] = response_data_info['share']
                prod_item['ad_image_video'] = str(response_data_info['ad_image_video'])
                prod_item['ad_title'] = str(response_data_info['ad_title'])
                prod_item['image_video_url'] = str(response_data_info['image_video_url'])
                prod_item['news_feed_description'] = str(response_data_info['news_feed_description'])
                prod_item['post_owner_id'] = response_data_info['post_owner_id']
                prod_item['post_date'] = str(response_data_info['post_date'])
                prod_item['last_seen'] = str(response_data_info['last_seen'])
                prod_item['country'] = str(response_data_info['country'])
                prod_item['table_name'] = 'fb_ads'

                yield prod_item

                form_data = {
                    'ad_id': str(prod_item['id'])
                }

                yield FormRequest(url=self.ADS_DETAIL_URL,
                                  callback=self.parse_detail,
                                  dont_filter=True,
                                  method="POST",
                                  formdata=form_data
                                  )

                yield FormRequest(url=self.ADS_LIKE_COMMENT_SHARE_URL,
                                  callback=self.parse_like_comment_share,
                                  dont_filter=True,
                                  method="POST",
                                  formdata=form_data
                                  )

                yield FormRequest(url=self.ADS_LIKE_HITS_URL,
                                  callback=self.parse_like_hits,
                                  dont_filter=True,
                                  method="POST",
                                  formdata=form_data
                                  )

                yield FormRequest(url=self.ADS_USER_DATA_URL,
                                  callback=self.parse_user_data,
                                  dont_filter=True,
                                  method="POST",
                                  formdata=form_data
                                  )

                yield FormRequest(url=self.ADS_COUNTRY_URL,
                                  callback=self.parse_country,
                                  dont_filter=True,
                                  method="POST",
                                  formdata=form_data
                                  )

            if self.ads_count < self.ads_total_count:
                form_data = {
                    'currentdate': '9999999999',
                    'olderdate': '0',
                    'post_currentdate': '9999999999',
                    'post_olderdate': '0',
                    'domain_currentdate': '9999999999',
                    'domain_olderdate': '0',
                    'country': '',
                    'type': '',
                    'position[]': 'FEED',
                    'gender': '',
                    'lower_age': '16',
                    'upper_age': '102',
                    'order_column': 'last_seen',
                    'order_by': 'desc',
                    'keyword': '',
                    'advertisername': '',
                    'domainname': '',
                    'take': '9',
                    'skip': str(self.step),
                    'lastval': str(self.lastval),
                    'callToAction': '',
                    'ecommerce': '',
                    'track': '',
                    'source': '',
                    'ip': '0.0.0.0',
                    'flag': '1',
                    'funnel': '',
                    'affiliate': '',
                    'favorite': 'false',
                    'hidden': 'false',
                    'tags': '',
                    'lang': '',
                    'html': '',
                    'commentdata': '',
                    'platform': '',
                    'discover_id': '',
                    'verified': '',
                    'page_currentdate': '9999999999',
                    'page_olderdate': '0',
                    'mixdata': '',
                    'html_feild': '',
                    'celebrity': '',
                    'ocr': '',
                    'logo_image': '',
                    'object_image': '',
                    'clear': 'false'
                }

                yield FormRequest(url=self.ADS_API_URL,
                                  callback=self.parse,
                                  dont_filter=True,
                                  method="POST",
                                  formdata=form_data
                                  )
        else:
            pass
