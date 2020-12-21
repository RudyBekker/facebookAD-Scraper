/*
SQLyog Ultimate v8.55 
MySQL - 5.5.5-10.4.11-MariaDB : Database - powerads
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`powerads` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `powerads`;

/*Table structure for table `fb_ad_comment_likes_share_details` */

DROP TABLE IF EXISTS `fb_ad_comment_likes_share_details`;

CREATE TABLE `fb_ad_comment_likes_share_details` (
  `id` bigint(20) NOT NULL,
  `facebook_ad_id` int(11) DEFAULT NULL,
  `date` bigint(20) DEFAULT NULL,
  `comment` int(11) DEFAULT NULL,
  `likes` int(11) DEFAULT NULL,
  `share` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `fb_ad_country_info` */

DROP TABLE IF EXISTS `fb_ad_country_info`;

CREATE TABLE `fb_ad_country_info` (
  `facebook_ad_id` int(11) DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `fb_ad_details` */

DROP TABLE IF EXISTS `fb_ad_details`;

CREATE TABLE `fb_ad_details` (
  `id` int(11) DEFAULT NULL,
  `ad_id` bigint(20) DEFAULT NULL,
  `ad_image_video` varchar(255) DEFAULT NULL,
  `ad_position` varchar(255) DEFAULT NULL,
  `ad_text` text DEFAULT NULL,
  `ad_title` varchar(255) DEFAULT NULL,
  `ad_url` varchar(255) DEFAULT NULL,
  `built_with` varchar(255) DEFAULT NULL,
  `call_to_action` varchar(255) DEFAULT NULL,
  `category` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `comment` int(11) DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  `country_code` varchar(255) DEFAULT NULL,
  `days_running` int(11) DEFAULT NULL,
  `destination_scraper_status` int(11) DEFAULT NULL,
  `destination_url` varchar(255) DEFAULT NULL,
  `ad_domain` varchar(255) DEFAULT NULL,
  `domain_registered_date` date DEFAULT '0000-00-00',
  `facebook_id` bigint(20) DEFAULT NULL,
  `final_url` varchar(255) DEFAULT NULL,
  `firstSeenOnDesktop` datetime DEFAULT '0000-00-00 00:00:00',
  `first_seen` datetime DEFAULT '0000-00-00 00:00:00',
  `image_video_url` varchar(255) DEFAULT NULL,
  `iso` varchar(255) DEFAULT NULL,
  `lander_path` varchar(255) DEFAULT NULL,
  `lander_status` int(11) DEFAULT NULL,
  `lastSeenOnDesktop` datetime DEFAULT '0000-00-00 00:00:00',
  `last_seen` datetime DEFAULT '0000-00-00 00:00:00',
  `likes` int(11) DEFAULT NULL,
  `lower_age` int(11) DEFAULT NULL,
  `news_feed_description` text DEFAULT NULL,
  `platform` int(11) DEFAULT NULL,
  `png_file` varchar(255) DEFAULT NULL,
  `post_date` datetime DEFAULT '0000-00-00 00:00:00',
  `post_owner` varchar(255) DEFAULT NULL,
  `post_owner_image` varchar(255) DEFAULT NULL,
  `redirect_destination_url_source` int(11) DEFAULT NULL,
  `redirect_url` varchar(255) DEFAULT NULL,
  `screenshot_url` varchar(255) DEFAULT NULL,
  `share` int(11) DEFAULT NULL,
  `source_url` varchar(255) DEFAULT NULL,
  `state` varchar(255) DEFAULT NULL,
  `ad_type` varchar(255) DEFAULT NULL,
  `upper_age` int(11) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `url_type` varchar(255) DEFAULT NULL,
  `version` varchar(255) DEFAULT NULL,
  `white_ad_screenshot` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `fb_ad_like_hits_details` */

DROP TABLE IF EXISTS `fb_ad_like_hits_details`;

CREATE TABLE `fb_ad_like_hits_details` (
  `id` bigint(20) NOT NULL,
  `facebook_ad_id` int(11) DEFAULT NULL,
  `date` bigint(20) DEFAULT NULL,
  `hits` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `fb_ads` */

DROP TABLE IF EXISTS `fb_ads`;

CREATE TABLE `fb_ads` (
  `id` int(11) DEFAULT NULL,
  `verified` int(11) DEFAULT NULL,
  `affiliate_network_id` int(11) DEFAULT NULL,
  `tags` varchar(255) DEFAULT NULL,
  `tags_status` int(11) DEFAULT NULL,
  `built_with` varchar(255) DEFAULT NULL,
  `ad_position` varchar(255) DEFAULT NULL,
  `ad_type` varchar(255) DEFAULT NULL,
  `post_owner_image` varchar(255) DEFAULT NULL,
  `post_owner` varchar(255) DEFAULT NULL,
  `ad_url` varchar(255) DEFAULT NULL,
  `ad_text` text DEFAULT NULL,
  `likes` int(11) DEFAULT NULL,
  `comment` int(11) DEFAULT NULL,
  `share` int(11) DEFAULT NULL,
  `ad_image_video` text DEFAULT NULL,
  `ad_title` varchar(255) DEFAULT NULL,
  `image_video_url` varchar(255) DEFAULT NULL,
  `news_feed_description` varchar(255) DEFAULT NULL,
  `post_owner_id` int(11) DEFAULT NULL,
  `post_date` date DEFAULT '0000-00-00',
  `last_seen` date DEFAULT '0000-00-00',
  `country` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Table structure for table `fb_user_info` */

DROP TABLE IF EXISTS `fb_user_info`;

CREATE TABLE `fb_user_info` (
  `facebook_id` bigint(20) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `gender` varchar(255) DEFAULT NULL,
  `current_country` varchar(255) DEFAULT NULL,
  `current_country_id` int(11) DEFAULT NULL,
  `others_places_lived` varchar(255) DEFAULT NULL,
  `relationship_status` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
