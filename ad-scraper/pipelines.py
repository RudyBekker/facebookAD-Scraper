# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb


class PoweradsPipeline:

    # def process_item(self, item, spider):
    #     return item

    def __init__(self):
        self.conn = MySQLdb.connect(
            host='localhost',
            user='root',
            passwd='',
            db='powerads',
            charset="utf8",
            use_unicode=True
        )
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            if item['table_name'] == 'fb_ads':
                self.cursor.execute(
                    """INSERT INTO fb_ads
                    (id, verified, affiliate_network_id, tags, tags_status, built_with, ad_position, ad_type,
                     post_owner_image, post_owner, ad_url, ad_text, likes, comment, share, ad_image_video, ad_title,
                     image_video_url, news_feed_description, post_owner_id, post_date, last_seen, country)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (
                        item['id'], item['verified'],
                        item['affiliate_network_id'], item['tags'].encode('utf-8'),
                        item['tags_status'], item['built_with'].encode('utf-8'),
                        item['ad_position'].encode('utf-8'), item['ad_type'].encode('utf-8'),
                        item['post_owner_image'].encode('utf-8'), item['post_owner'].encode('utf-8'),
                        item['ad_url'].encode('utf-8'), item['ad_text'].encode('utf-8'),
                        item['likes'], item['comment'], item['share'], item['ad_image_video'].encode('utf-8'),
                        item['ad_title'].encode('utf-8'), item['image_video_url'].encode('utf-8'),
                        item['news_feed_description'].encode('utf-8'), item['post_owner_id'],
                        item['post_date'], item['last_seen'],
                        item['country'].encode('utf-8')
                    )
                )

                self.conn.commit()

            elif item['table_name'] == 'fb_ad_details':
                self.cursor.execute(
                    """INSERT INTO fb_ad_details
                    (id, ad_id, ad_image_video, ad_position, ad_text, ad_title, ad_url, built_with, call_to_action,
                    category, city, comment, country, country_code, days_running, destination_scraper_status,
                    destination_url, ad_domain, domain_registered_date, facebook_id, final_url, firstSeenOnDesktop,
                    first_seen, image_video_url, iso, lander_path, lander_status, lastSeenOnDesktop, last_seen, likes,
                    lower_age, news_feed_description, platform, png_file, post_date, post_owner, post_owner_image,
                    redirect_destination_url_source, redirect_url, screenshot_url, share, source_url, state, ad_type,
                    upper_age, url, url_type, version, white_ad_screenshot)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s)""", (
                        item['id'], item['ad_id'],
                        item['ad_image_video'].encode('utf-8'), item['ad_position'].encode('utf-8'),
                        item['ad_text'].encode('utf-8'), item['ad_title'].encode('utf-8'),
                        item['ad_url'].encode('utf-8'), item['built_with'].encode('utf-8'),
                        item['call_to_action'].encode('utf-8'), item['category'].encode('utf-8'),
                        item['city'].encode('utf-8'), item['comment'],
                        item['country'].encode('utf-8'), item['country_code'].encode('utf-8'),
                        item['days_running'], item['destination_scraper_status'],
                        item['destination_url'].encode('utf-8'), item['domain'].encode('utf-8'),
                        item['domain_registered_date'].encode('utf-8'), item['facebook_id'],
                        item['final_url'].encode('utf-8'), item['firstSeenOnDesktop'].encode('utf-8'),
                        item['first_seen'].encode('utf-8'), item['image_video_url'].encode('utf-8'),
                        item['iso'].encode('utf-8'), item['lander_path'].encode('utf-8'), item['lander_status'],
                        item['lastSeenOnDesktop'].encode('utf-8'), item['last_seen'].encode('utf-8'),
                        item['likes'], item['lower_age'], item['news_feed_description'].encode('utf-8'),
                        item['platform'].encode('utf-8'), item['png_file'].encode('utf-8'),
                        item['post_date'].encode('utf-8'), item['post_owner'].encode('utf-8'),
                        item['post_owner_image'].encode('utf-8'), item['redirect_destination_url_source'].encode('utf-8'),
                        item['redirect_url'].encode('utf-8'), item['screenshot_url'].encode('utf-8'),
                        item['share'], item['source_url'].encode('utf-8'),
                        item['state'].encode('utf-8'), item['ad_type'].encode('utf-8'),
                        item['upper_age'], item['url'].encode('utf-8'), item['url_type'].encode('utf-8'),
                        item['version'].encode('utf-8'), item['white_ad_screenshot'].encode('utf-8')
                    )
                )

                self.conn.commit()

            elif item['table_name'] == 'fb_ad_comment_likes_share_details':
                self.cursor.execute(
                    """INSERT INTO fb_ad_comment_likes_share_details
                    (id, facebook_ad_id, date, comment, likes, share)
                    VALUES (%s, %s, %s, %s, %s, %s)""",
                    (
                        item['id'], item['facebook_ad_id'], item['date'], item['comment'],
                        item['likes'], item['share']
                    )
                )

                self.conn.commit()

            elif item['table_name'] == 'fb_ad_like_hits_details':
                self.cursor.execute(
                    """INSERT INTO fb_ad_like_hits_details
                    (id, facebook_ad_id, date, hits)
                    VALUES (%s, %s, %s, %s)""",
                    (
                        item['id'], item['facebook_ad_id'], item['date'], item['hits']
                    )
                )

                self.conn.commit()

            elif item['table_name'] == 'fb_user_info':
                self.cursor.execute(
                    """INSERT INTO fb_user_info
                    (facebook_id, name, age, gender, current_country, current_country_id, 
                    others_places_lived, relationship_status)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
                    (
                        item['facebook_id'], item['name'], item['age'], item['gender'],
                        item['current_country'], item['current_country_id'], item['others_places_lived'],
                        item['relationship_status']
                    )
                )

                self.conn.commit()

            elif item['table_name'] == 'fb_ad_country_info':
                self.cursor.execute(
                    """INSERT INTO fb_ad_country_info
                    (facebook_ad_id, country)
                    VALUES (%s, %s)""",
                    (
                        item['facebook_ad_id'], item['country']
                    )
                )

                self.conn.commit()

        except MySQLdb.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))

        return item
