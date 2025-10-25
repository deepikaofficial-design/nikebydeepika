from flask import Flask, render_template_string
import os

app = Flask(__name__)

if not os.path.exists('static'):
    os.makedirs('static')

HTML_TEMPLATE = '''

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nike Slideshow - Fixed Progress Ring</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            background-color: white;
            font-family: Arial, sans-serif;
        }

        /* Header - Responsive */
        .header-container {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background-color: black;
            padding: 8px 15px;
            min-height: 40px;
        }

        .logo-container {
            display: flex;
            align-items: center;
        }

        .logo-container img {
            width: 60px;
            height: 40px;
        }

        .text-container {
            text-align: center;
            font-size: 16px;
            font-weight: 700;
            letter-spacing: 2px;
            color: white;
            position: absolute;
            left: 50%;
            transform: translateX(-50%);
            z-index: 1;
        }
        
        .mobile-menu-icon {
            display: none !important;
        }
        .top-right-menu {
            display: flex;
            align-items: center;
            gap: 15px;
            font-size: 12px;
            color: white;
            position: relative;
            z-index: 10;
        }

        .top-right-menu a {
            color: white;
            text-decoration: none;
        }

        .top-right-menu a:hover {
            text-decoration: underline;
        }

        .top-right-menu .separator {
            color: white;
        }

        /* Navigation - Responsive */
        .nav-menu {
            background-color: white;
            padding: 0 40px;
            height: 60px;
            display: flex;
            align-items: center;
            justify-content: flex-start;
            position: sticky;
            z-index: 100;
            top: 0;
            gap: 20px;
        }

        .nav-logo {
            display: flex;
            align-items: center;
            margin-right: 50px;
        }

        .nav-logo img {
            width: 60px;
            height: 36px;
        }

        .nav-links-container {
            display: flex;
            gap: 25px;
            align-items: center;
            flex: 1;
        }

        .nav-link, .new-featured-link, .men-link, .women-link, 
        .kids-link, .sale-link, .snkrs-link {
            color: black;
            text-decoration: none;
            font-size: 16px;
            font-weight: 600;
            padding: 8px 10px;
            cursor: pointer;
        }

        .nav-link:hover, .new-featured-link:hover, .men-link:hover, 
        .women-link:hover, .kids-link:hover, .sale-link:hover, .snkrs-link:hover {
            border-bottom: 2px solid black;
        }

        .new-featured-trigger, .men-trigger, .women-trigger, 
        .kids-trigger, .sale-trigger, .snkrs-trigger {
            position: relative;
            display: inline-block;
        }

        /* Dropdown Menus */
        .new-featured-menu, .men-menu, .women-menu, 
        .kids-menu, .sale-menu, .snkrs-menu {
            display: none;
            position: fixed;
            top: 90px;
            left: 0;
            right: 0;
            background-color: white;
            padding: 40px 60px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
            z-index: 200;
        }

        .new-featured-trigger:hover .new-featured-menu, 
        .men-trigger:hover .men-menu,
        .women-trigger:hover .women-menu, 
        .kids-trigger:hover .kids-menu,
        .sale-trigger:hover .sale-menu, 
        .snkrs-trigger:hover .snkrs-menu {
            display: block;
        }

        .new-featured-content, .men-content, .women-content, 
        .kids-content, .sale-content, .snkrs-content {
            display: grid;
            gap: 40px;
            max-width: 1400px;
            margin: 0 auto;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        }

        .new-featured-heading, .men-heading, .women-heading, 
        .kids-heading, .sale-heading, .snkrs-heading {
            font-size: 16px;
            font-weight: 540;
            margin-bottom: 20px;
            color: black;
        }

        .new-featured-item, .men-item, .women-item, 
        .kids-item, .sale-item, .snkrs-item {
            font-size: 14px;
            margin-bottom: 12px;
            color: #666;
            text-decoration: none;
            display: block;
        }

        .new-featured-item:hover, .men-item:hover, 
        .women-item:hover, .kids-item:hover, 
        .sale-item:hover, .snkrs-item:hover {
            color: black;
            text-decoration: underline;
        }

        .search-container {
            display: flex;
            align-items: center;
            gap: 20px;
        }

        .search-bar {
            background-color: #f5f5f5;
            border: 1px solid #ccc;
            border-radius: 20px;
            padding: 8px 20px;
            font-size: 16px;
            width: 200px;
            outline: none;
        }

        .search-bar:focus {
            background-color: #e8e8e8;
            border-color: #999;
        }

        .favorites-icon {
            font-size: 34px;
            cursor: pointer;
            color: black;
            text-decoration: none;
        }

        .heart-outline {
            display: inline-block;
        }

        .heart-filled {
            display: none;
        }

        .favorites-icon:hover .heart-outline {
            display: none;
        }

        .favorites-icon:hover .heart-filled {
            display: inline-block;
        }

        .basket-icon {
            font-size: 24px;
            cursor: pointer;
            color: black;
        }

        /* Text Slideshow Container */
        .text-slideshow-container {
            position: relative;
            width: 100%;
            height: 150px;
            overflow: hidden;
            background: white;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-top: 80px;
            margin-bottom: 40px;
        }

        .text-slide {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 70px;
            font-weight: bold;
            color: black;
            opacity: 0;
            z-index: 0;
        }

        .text-slide:first-child {
            opacity: 1;
            z-index: 2;
        }

        .text-slide.text-active {
            animation: textSlideInRight 0.4s ease-in-out forwards;
            z-index: 2;
        }

        .text-slide.text-slide-out {
            animation: textSlideOutLeft 0.4s ease-in-out forwards;
            z-index: 1;
        }

        @keyframes textSlideInRight {
            from {
                transform: translateX(100%);
                opacity: 0;
            }
            to {
                transform: translateX(0);
                opacity: 1;
            }
        }

        @keyframes textSlideOutLeft {
            from {
                transform: translateX(0);
                opacity: 1;
            }
            to {
                transform: translateX(-100%);
                opacity: 0;
            }
        }

        /* Slideshow Container */
        .slideshow-container {
            position: relative;
            width: 100%;
            height: 600px;
            overflow: hidden;
            background: #000;
        }

        .slide {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center;
            opacity: 0;
            z-index: 0;
        }

        .slide:first-child {
            opacity: 1;
            z-index: 2;
            pointer-events: auto;
        }

        .slide.active {
            animation: slideInRight 0.4s ease-in-out forwards;
            z-index: 2;
            pointer-events: auto;
        }

        .slide.slide-out {
            animation: slideOutLeft 0.4s ease-in-out forwards;
            z-index: 1;
        }

        video.slide {
            object-fit: cover;
            object-position: center;
        }

        img.slide {
            object-fit: cover;
            object-position: center;
        }

        @keyframes slideInRight {
            from {
                transform: translateX(100%);
                opacity: 0;
                z-index: 2;
            }
            to {
                transform: translateX(0);
                opacity: 1;
                z-index: 2;
            }
        }

        @keyframes slideOutLeft {
            from {
                transform: translateX(0);
                opacity: 1;
                z-index: 1;
            }
            to {
                transform: translateX(-100%);
                opacity: 0;
                z-index: 1;
            }
        }

        /* Shop Button */
        .shop-button {
            position: absolute;
            bottom: 60px;
            left: 50%;
            transform: translateX(-50%);
            background-color: white;
            color: black;
            padding: 12px 24px;
            border: none;
            cursor: pointer;
            font-size: 16px;
            font-weight: 600;
            z-index: 10;
            border-radius: 50px;
        }

        .shop-button:hover {
            background-color: black;
            color: white;
        }

        /* Slideshow Controls */
        .slideshow-controls {
            position: absolute;
            bottom: 40px;
            right: 40px;
            display: flex;
            gap: 15px;
            z-index: 20;
        }

        .slideshow-control-btn {
            width: 44px;
            height: 44px;
            border-radius: 50%;
            background-color: #666;
            backdrop-filter: blur(5px);
            border: none;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 18px;
            font-weight: bold;
            color: white;
            transition: all 0.2s ease;
            position: relative;
            box-shadow: none;
        }

        .slideshow-control-btn:hover {
            background-color: black;
            transform: scale(1.02);
            box-shadow: none;
        }

        .slideshow-control-btn:active {
            transform: scale(0.95);
        }

        /* Pause/Play Icons */
        .pause-icon,
        .play-icon {
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .pause-icon {
            gap: 4px;
        }
        

        .pause-bar {
            width: 3px;
            height: 16px;
            background-color: #fff;
            border-radius: 1.5px;
        }

        .play-icon::before {
            content: '';
            width: 0;
            height: 0;
            border-left: 12px solid #fff;
            border-top: 8px solid transparent;
            border-bottom: 8px solid transparent;
            margin-left: 2px;
        }

        /* Arrow Buttons */
        .slideshow-control-btn svg {
            width: 20px;
            height: 20px;
            fill: none;
            stroke: currentColor;
            stroke-width: 2.5;
            stroke-linecap: round;
            stroke-linejoin: round;
        }

        .slide-indicators {
            position: absolute;
            bottom: 15px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            gap: 8px;
            z-index: 20;
            max-width: 100px; /* Add this to limit visible dots */
            overflow: hidden; /* Add this to hide extra dots */
        }

        .slide-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background-color: rgba(255, 255, 255, 0.4);
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .slide-dot.active {
            background-color: white;
            width: 10px;
            height: 10px;
        }

        .slide-dot:hover {
            background-color: rgba(255, 255, 255, 0.7);
        }

        /* Content Wrapper - Responsive */
        .content-wrapper {
                padding: 0 20px;
            }
        
        .athlete-image {
            height: 200px;
        }
            
            /* Featured (What's Hot) images - prevent trimming */
        .featured-images-container {
            grid-template-columns: 1fr;
            gap: 15px;
        }
            
        .featured-image {
            height: 400px;
            object-fit: contain;
            background-color: #f5f5f5;
        }

        /* Sections - Responsive Typography */
        .athlete-title, .features-title, .gear-title, 
        .sports-title, .discover-title, .nba-section-title,
        .select-icons-title {
            font-size: 28px;
            font-weight: normal;
            margin: 100px 0 30px 0;
        }

        .featured-main-title {
            font-size: 30px;
            font-weight: bold;
            margin-bottom: 10px;
            text-align: center;
        }

        .featured-subtitle {
            font-size: 24px;
            color: #757575;
            margin-bottom: 15px;
            text-align: center;
        }

        .featured-cta-button {
            background-color: black;
            color: white;
            padding: 12px 24px;
            border: none;
            cursor: pointer;
            font-size: 16px;
            font-weight: bold;
            border-radius: 50px;
            display: block;
            margin: 0 auto;
        }

        .featured-cta-button:hover {
            background-color: #333;
        }

        /* Image Grids - Responsive */
        .athlete-images-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 10px;
            margin-bottom: 40px;
        }

        .athlete-image {
            width: 100%;
            height: 300px;
            object-fit: cover;
            transition: transform 0.3s ease;
        }

        .athlete-image:hover {
            transform: scale(1.09);
        }

        .discover-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            grid-template-rows: repeat(2, 1fr);
            gap: 0;
            margin-bottom: 40px;
            line-height: 0;
        }

        .discover-image {
            width: 100%;
            height: 620px;
            object-fit: cover;
            display: block;
        }

        .featured-images-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 10px;
            margin-bottom: 40px;
        }
        .featured-image {
            width: 100%;
            height: 500px;
            object-fit: cover;
            transition: filter 0.3s ease;
        }

        .featured-image:hover {
            opacity: 0.8;
            
        }

        /* Shop Tabs for What's Hot Section */
        .featured-image-wrapper {
            position: relative;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .featured-image-wrapper .shop-tab-button {
            position: absolute;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%);
            z-index: 10;
        }

        .shop-tab-button {
            background-color: white;
            color: black;
            padding: 12px 24px;
            border: none;
            cursor: pointer;
            font-size: 18px;
            font-weight: bold;
            border-radius: 50px;
            transition: all 0.3s ease;
        }

        .shop-tab-button:hover {
            background-color: black;
            color: white;
        }

        .gear-image {
            width: 100%;
            height: 600px;
            object-fit: cover;
            margin-bottom: 40px;
        }

        /* Sliders - Responsive */
        .sports-slider-container {
            position: relative;
            overflow: hidden;
            margin-bottom: 80px;
        }

        .sports-slider {
            display: flex; 
            gap: 8px;
            overflow-x: auto;
            scroll-behavior: smooth;
            scrollbar-width: none;
            padding: 20px 0;
        }

        .sports-slider::-webkit-scrollbar {
            display: none;
        }

        .sports-item {
            flex: 0 0 calc(25% - 12px);
            min-width: 280px;
            cursor: pointer;
        }

        .sports-image {
            width: 100%;
            height: 500px;
            object-fit: cover;
            margin-bottom: 12px;
            transition: filter 0.3s ease;
        }

        .sports-image:hover {
            opacity: 0.8;
        }

        .sports-text {
            text-align: center;
            font-size: 15px;
            font-weight: normal;
            text-transform: uppercase;
        }

        .slider-btn {
            position: absolute;
            background-color: rgba(255, 255, 255, 0.9);
            border: none;
            width: 50px;
            height: 50px;
            cursor: pointer;
            font-size: 36px;
            color: black;
            display: flex;
            align-items: center;
            justify-content: center;
            top: 50%;
            transform: translateY(-80%);
            border-radius: 50%;
            z-index: 10;
        }

        .slider-btn:hover {
            background-color: rgba(255, 255, 255, 1);
        }

        .slider-btn.hidden {
            opacity: 0;
            pointer-events: none;
        }

        .slider-btn.left {
            left: 20px;
        }

        .slider-btn.right {
            right: 20px;
        }

        /* Icons Slider - Infinite Loop */
        .icons-slider-container {
            position: relative;
            overflow: hidden;
            margin-bottom: 80px;
        }

        .icons-slider {
            display: flex; 
            gap: 15px;
            overflow-x: auto;
            scroll-behavior: smooth;
            scrollbar-width: none;
            padding: 20px 0;
        }
        

        .icons-slider::-webkit-scrollbar {
            display: none;
        }

        @keyframes infiniteScroll {
            0% {
                transform: translateX(0);
            }
            100% {
                transform: translateX(-50%);
            }
        }

        .icon-item {
            flex: 0 0 240px;
            min-width: 350px;
            cursor: pointer;
        }

        .icon-image {
            width: 100%;
            height: 380px;
            object-fit: contain;
            margin-bottom: 12px;
            transition: transform 0.3s ease;
        }

        .icon-image:hover {
            transform: scale(1.08);
        }

        .icons-slider-btn {
            position: absolute;
            background-color: rgba(255, 255, 255, 0.9);
            border: none;
            width: 50px;
            height: 50px;
            cursor: pointer;
            font-size: 36px;
            color: black;
            display: flex;
            align-items: center;
            justify-content: center;
            top: 50%;
            transform: translateY(-80%);
            border-radius: 50%;
            z-index: 10;
        }

        .icons-slider-btn:hover {
            background-color: rgba(255, 255, 255, 1);
        }

        .icons-slider-btn.hidden {
            opacity: 0;
            pointer-events: none;
        }

        .icons-slider-btn.left {
            left: 20px;
        }

        .icons-slider-btn.right {
            right: 20px;
        }

        /* NBA Slider - Responsive */
        .nba-slider {
            display: flex;
            gap: 15px;
            overflow-x: auto;
            scroll-behavior: smooth;
            scrollbar-width: none;
            padding: 20px 0;
            margin-bottom: 220px;
        }

        .nba-slider::-webkit-scrollbar {
            display: none;
        }

        .nba-item {
            flex: 0 0 calc(25% - 12px);
            min-width: 280px;
        }

        .nba-image {
            width: 100%;
            height: 320px;
            object-fit: cover;
            margin-bottom: 12px;
            transition: filter 0.3s ease;
        }

        .nba-image:hover {
            opacity: 0.8;
        }

        .nba-item-title {
            font-size: 16px;
            font-weight: 600;
            margin-bottom: 8px;
        }

        .nba-description {
            font-size: 14px;
            color: #757575;
            margin-bottom: 8px;
            font-weight: normal;
        }

        .nba-price {
            font-size: 13px;
            font-weight: 300;
        }

        .nba-slider-btn {
            position: absolute;
            background-color: rgba(255, 255, 255, 0.9);
            border: none;
            width: 50px;
            height: 50px;
            cursor: pointer;
            font-size: 36px;
            color: black;
            display: flex;
            align-items: center;
            justify-content: center;
            top: 50%;
            transform: translateY(-650%);
            border-radius: 50%;
            z-index: 10;
        }

        .nba-slider-controls {
            position: relative;
            margin-top: -200px;
            pointer-events: none;
        }

        .nba-slider-btn {
            pointer-events: auto;
        }

        .nba-slider-btn:hover {
            background-color: rgba(255, 255, 255, 1);
        }

        .nba-slider-btn.hidden {
            opacity: 0;
            pointer-events: none;
        }

        .nba-slider-btn.left {
            left: 20px;
        }

        .nba-slider-btn.right {
            right: 20px;
        }

        /* Footer - Responsive */

        .footer-section {
            background-color: white;
            padding: 60px 48px;
            margin-top: 150px;
            border-top: 1px solid black;
        }
        .footer-content {
            display: flex;
            justify-content: flex-start;
            max-width: 100%;
            margin: 0;
            margin-bottom: 40px;
            gap: 150px;
        }

        .footer-column {
            flex: 0 0 auto;
            min-width: 200px;
        }

        .footer-location-column {
            margin-left: auto;
            flex: 0 0 auto;
        }

        .footer-column-title {
            font-size: 13px;
            font-weight: 500;
            margin-bottom: 16px;
            color: black;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .footer-link {
            color: #7e7e7e;
            text-decoration: none;
            font-size: 12px;
            margin-bottom: 12px;
            display: block;
            line-height: 1.5;
        }

        .footer-link:hover {
            color: black;
            text-decoration: underline;
        }

        .footer-location-column {
            display: flex;
            align-items: flex-start;
            justify-content: flex-end;
        }

        .footer-location {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 12px;
            color: black;
        }

        .location-icon {
            width: 18px;
            height: 18px;
        }

        .footer-bottom {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 20px;
            padding-top: 0;
            margin-top: 0;
            max-width: 100%;
            margin-left: 0;
            margin-right: 0;
            font-size: 14px;
            color: #7e7e7e;
        }

        .footer-bottom-left {
            display: flex;
            gap: 24px;
            flex-wrap: wrap;
            align-items: center;
        }

        .footer-bottom-right {
            display: flex;
            gap: 12px;
        }

        .footer-bottom-link {
            color: #7e7e7e;
            text-decoration: none;
            font-size: 14px;
        }

        .footer-bottom-link:hover {
            color: black;
            text-decoration: underline;
        }

        /* Mobile Responsive - Phone screens only */
        @media (max-width: 768px) {
            .footer-content {
                flex-direction: column;
                gap: 30px;
            }
            
            .footer-section {
                padding: 40px 20px;
            }
        }

        /* Popups - Responsive */
        .sports-popup, .icons-popup {
            position: fixed;
            display: none;
            background-color: white;
            border: 1px solid #ddd;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
            z-index: 1000;
            border-radius: 12px;
            overflow: hidden;
            max-width: 400px;
            pointer-events: none;
        }

        .sports-popup.active, .icons-popup.active {
            display: block;
        }

        .sports-popup-image, .icons-popup-image {
            width: 100%;
            height: 400px;
            object-fit: cover;
        }

        .sports-popup-text, .icons-popup-text {
            padding: 20px;
            text-align: center;
            font-size: 16px;
            font-weight: bold;
            text-transform: uppercase;
        }

        /* Mobile Responsive - Phone screens only */
        @media (max-width: 768px) {
            .text-container {
                font-size: 10px;
                letter-spacing: 1px;
            }
            
            .top-right-menu {
                display: none !important;
            }
            
            /* Hamburger Menu Icon for Mobile */
            .mobile-menu-icon {
                display: flex !important;
                flex-direction: column;
                justify-content: space-between;
                width: 30px;
                height: 22px;
                color: white;
                padding: 4px;
                border-radius: 4px;
                cursor: pointer;
                position: fixed;
                right: 15px;
                top: 10px;
                z-index: 1000;
            }
            
            .mobile-menu-icon span {
                width: 100%;
                height: 3px;
                color: white;
                border-radius: 2px;
            }

            /* Slideshow mobile - keep consistent height */
            .slideshow-container {
                height: 30vh;
                max-height: 300px;
                margin-top: 200px;
            }

            .slide {
                width: 100%;
                height: 100%;
                object-fit: cover;
                object-position: center center;
            }

            video.slide {
                object-fit: cover;
            }

            
            /* Show slideshow controls below slideshow on mobile */
            .slideshow-controls {
                position: relative;
                bottom: auto;
                right: auto;
                display: flex;
                justify-content: center;
                gap: 10px;
                margin-top: 15px;
                margin-bottom: 20px;
                padding: 0 20px;
            }
            
            .slideshow-control-btn {
                width: 40px;
                height: 40px;
                font-size: 16px;
            }
            
            /* Text slideshow adjustments for mobile */
            .text-slideshow-container {
                height: 80px;
                margin-top: 40px;
                margin-bottom: 20px;
            }
            
            .text-slide {
                font-size: 28px;
                white-space: nowrap;
                padding: 0 10px;
            }
            
            .nav-menu {
                padding: 0 20px;
                height: 50px;
                justify-content: center;
            }
            
            .nav-logo {
                margin-right: 0;
            }
            
            .nav-logo img {
                width: 45px;
                height: 27px;
            }
            
            /* HIDE nav links, favorites, and basket on phone screens */
            .nav-links-container,
            .search-container {
                display: none !important;
            }
            
            .content-wrapper {
                padding: 0 20px;
            }
            
            .athlete-title, .features-title, .gear-title, 
            .sports-title, .discover-title, .nba-section-title,
            .select-icons-title {
                font-size: 20px;
                margin: 50px 0 15px 0;
                font-weight: normal;
            }
            
            .featured-main-title {
                font-size: 25px;
            }
            
            .featured-subtitle {
                font-size: 20px;
            }
            
            .sports-item, .icon-item, .nba-item {
                min-width: 200px;
            }
            
            .icon-image {
                margin-bottom: 5px;
            }
            
            .icons-slider {
                padding: 10px 0;
            }
            
            .select-icons-title {
                margin: 30px 0 10px 0;
            }
            
            .slider-btn, .nba-slider-btn {
                width: 40px;
                height: 40px;
                font-size: 28px;
            }
            
            .footer-content {
                grid-template-columns: 1fr;
                gap: 30px;
            }
        }
    </style>
</head>
<body>
    <div class="header-container">
        <div class="logo-container">
            <img src="/static/logo.png" alt="Nike Logo">
        </div>
        <div class="text-container">JUST DO IT.</div>
        <div class="top-right-menu">
            <a href="/find-stores">Find Stores</a>
            <span class="separator">|</span>
            <a href="/help">Help</a>
            <span class="separator">|</span>
            <a href="/join">Join Us</a>
            <span class="separator">|</span>
            <a href="/signin">Sign In</a>
        </div>
        <div class="mobile-menu-icon">
            <span></span>
            <span></span>
            <span></span>
        </div>
    </div>
    
    <div class="nav-menu">
        <div class="nav-logo">
            <img src="/static/nikelogo.png" alt="Nike">
        </div>
        <div class="nav-links-container">
            <div class="new-featured-trigger">
                <a href="/new-featured" class="new-featured-link">New & Featured</a>
                <div class="new-featured-menu">
                    <div class="new-featured-content">
                     <div class="new-featured-column">
                            <div class="new-featured-heading">Featured</div>
                            <a href="#new-drops" class="new-featured-item">New & Upcoming Drops</a>
                            <a href="#new-arrivals" class="new-featured-item">New Arrivals</a>
                            <a href="#bestsellers" class="new-featured-item">Bestsellers</a>
                            <a href="#snkrs-calendar" class="new-featured-item">SNKRS Launch Calendar</a>
                            <a href="#snkrs-calendar" class="new-featured-item">Customise with Nike By You</a>
                            <a href="#snkrs-calendar" class="new-featured-item">Jordans</a>
                            <a href="#snkrs-calendar" class="new-featured-item">LeBron James</a>
                        </div>
                        <div class="new-featured-column">
                            <div class="new-featured-heading">Trending</div>
                            <a href="#more-colors" class="new-featured-item">More Colours,More Running</a>
                            <a href="#trending" class="new-featured-item">What's Trending</a>
                            <a href="#trending" class="new-featured-item">Running Shoe Finder</a>
                            <a href="#trending" class="new-featured-item">24.7 Collection</a>
                            <a href="#trending" class="new-featured-item">Vomero Premium</a>
                            <a href="#collections" class="new-featured-item">Collections</a>
                            <a href="#retro-running" class="new-featured-item">Retro Running</a>
                        </div>
                        <div class="new-featured-column">
                            <div class="new-featured-heading">Shop Icons</div>
                            <a href="#lifestyle" class="new-featured-item">Lifestyle</a>
                            <a href="#af1" class="new-featured-item">Air Force 1</a>
                            <a href="#aj1" class="new-featured-item">Air Jordan 1</a>
                            <a href="#airmax" class="new-featured-item">Air Max</a>
                            <a href="#dunk" class="new-featured-item">Cortez</a>
                            <a href="#dunk" class="new-featured-item">Blazer</a>
                            <a href="#dunk" class="new-featured-item">Vomero</a>
                            <a href="#dunk" class="new-featured-item">Dunk</a>
                            <a href="#dunk" class="new-featured-item">Pegasus</a>
                        </div>
                        <div class="new-featured-column">
                            <div class="new-featured-heading">Shop By Sport</div>
                            <a href="#running" class="new-featured-item">Running</a>
                            <a href="#basketball" class="new-featured-item">Basketball</a>
                            <a href="#football" class="new-featured-item">Football</a>
                            <a href="#golf" class="new-featured-item">Golf</a>
                            <a href="#tennis" class="new-featured-item">Tennis</a>
                            <a href="#tennis" class="new-featured-item">Gym and Training</a>
                            <a href="#tennis" class="new-featured-item">Yoga</a>
                            <a href="#tennis" class="new-featured-item">Skateboarding</a>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="men-trigger">
                <a href="/men" class="men-link">Men</a>
                <div class="men-menu">
                    <div class="men-content">
                        <div class="men-column">
                            <div class="men-heading">Featured</div>
                            <a href="#new-arrivals" class="men-item">New Arrivals</a>
                            <a href="#bestsellers" class="men-item">Bestsellers</a>
                            <a href="#shop-all-sale" class="men-item">Shop All Sale</a>
                        </div>
                        <div class="men-column">
                            <div class="men-heading">Shoes</div>
                            <a href="#all-shoes" class="men-item">All Shoes</a>
                            <a href="#lifestyle" class="men-item">Lifestyle</a>
                            <a href="#jordan" class="men-item">Jordan</a>
                            <a href="#running" class="men-item">Running</a>
                            <a href="#basketball" class="men-item">Basketball</a>
                            <a href="#basketball" class="men-item">Football</a>
                            <a href="#basketball" class="men-item">Gym and Training</a>
                            <a href="#basketball" class="men-item">Skateboarding</a>
                            <a href="#basketball" class="men-item">Sandals and Slides</a>
                            <a href="#basketball" class="men-item">Nike By You</a>
                        </div>
                        <div class="men-column">
                            <div class="men-heading">Clothing</div>
                            <a href="#all-clothing" class="men-item">All Clothing</a>
                            <a href="#tops-shirts" class="men-item">Tops and T-Shirts</a>
                            <a href="#shorts" class="men-item">Shorts</a>
                            <a href="#hoodies" class="men-item">Hoodies and Sweatshirts</a>
                            <a href="#jackets" class="men-item">Jackets and Gilets</a>
                            <a href="#jackets" class="men-item">Pants and Leggings</a>
                            <a href="#jackets" class="men-item">Jerseys and Kits</a>
                            <a href="#jackets" class="men-item">Jordans</a>
                            
                        </div>
                        <div class="men-column">
                            <div class="men-heading">Shop By Sport</div>
                            <a href="#running" class="men-item">Running</a>
                            <a href="#basketball" class="men-item">Basketball</a>
                            <a href="#football" class="men-item">Football</a>
                            <a href="#golf" class="men-item">Golf</a>
                            <a href="#tennis" class="men-item">Tennis</a>
                            <a href="#tennis" class="men-item">Gym and Training</a>
                            <a href="#tennis" class="men-item">Yoga</a>
                            <a href="#tennis" class="men-item">Skateboarding</a>
                        </div>
                        <div class="men-column">
                            <div class="men-heading">Accessories</div>
                            <a href="#all-accessories" class="men-item">Accessories and Equipment</a>
                            <a href="#bags" class="men-item">Bags and Backpacks</a>
                            <a href="#socks" class="men-item">Socks</a>
                            <a href="#hats" class="men-item">Hats and Headwear</a>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="women-trigger">
                <a href="/women" class="women-link">Women</a>
                <div class="women-menu">
                    <div class="women-content">
                    <div class="women-column">
                            <div class="women-heading">Featured</div>
                            <a href="#new-arrivals" class="women-item">New Arrivals</a>
                            <a href="#bestsellers" class="women-item">Bestsellers</a>
                            <a href="#shop-all-sale" class="women-item">Shop All Sale</a>
                        </div>
                         <div class="women-column">
                            <div class="women-heading">Shoes</div>
                            <a href="#all-shoes" class="women-item">All Shoes</a>
                            <a href="#lifestyle" class="women-item">Lifestyle</a>
                            <a href="#jordan" class="women-item">Jordan</a>
                            <a href="#running" class="women-item">Running</a>
                            <a href="#basketball" class="women-item">Basketball</a>
                            <a href="#basketball" class="women-item">Football</a>
                            <a href="#basketball" class="women-item">Gym and Training</a>
                            <a href="#basketball" class="women-item">Skateboarding</a>
                            <a href="#basketball" class="women-item">Sandals and Slides</a>
                            <a href="#basketball" class="women-item">Nike By You</a>
                        </div>
                        <div class="women-column">
                            <div class="women-heading">Clothing</div>
                            <a href="#all-clothing" class="women-item">All Clothing</a>
                            <a href="#all-clothing" class="women-item">Performance Essentials</a>
                            <a href="#tops-shirts" class="women-item">Tops and T-Shirts</a>
                            <a href="#shorts" class="women-item">Shorts</a>
                            <a href="#hoodies" class="women-item">Hoodies and Sweatshirts</a>
                            <a href="#jackets" class="women-item">Jackets and Gilets</a>
                            <a href="#jackets" class="women-item">Pants and Leggings</a>
                            <a href="#jackets" class="women-item">Jerseys and Kits</a>
                            <a href="#jackets" class="women-item">Jordans</a>
                            <a href="#jackets" class="women-item">Sports Bra</a>
                            <a href="#jackets" class="women-item">Skirts and Dresses</a>
                            <a href="#jackets" class="women-item">Modest Wear</a>
                            <a href="#jackets" class="women-item">Plus Size</a>
                            <a href="#jackets" class="women-item">Nike Maternity</a>
                            
                        </div>
                           <div class="women-column">
                            <div class="women-heading">Shop By Sport</div>
                            <a href="#running" class="women-item">Running</a>
                            <a href="#basketball" class="women-item">Basketball</a>
                            <a href="#football" class="women-item">Football</a>
                            <a href="#golf" class="women-item">Golf</a>
                            <a href="#tennis" class="women-item">Tennis</a>
                            <a href="#tennis" class="women-item">Gym and Training</a>
                            <a href="#tennis" class="women-item">Yoga</a>
                            <a href="#tennis" class="women-item">Skateboarding</a>
                        </div>
                        <div class="women-column">
                            <div class="women-heading">Accessories</div>
                            <a href="#all-accessories" class="women-item">Accessories and Equipment</a>
                            <a href="#bags" class="women-item">Bags and Backpacks</a>
                            <a href="#socks" class="women-item">Socks</a>
                            <a href="#hats" class="women-item">Hats and Headwear</a>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="kids-trigger">
                <a href="/kids" class="kids-link">Kids</a>
                <div class="kids-menu">
                    <div class="kids-content">
                        <div class="kids-column">
                            <div class="kids-heading">Featured</div>
                            <a href="#new-arrivals" class="kids-item">New Arrivals</a>
                            <a href="#bestsellers" class="kids-item">Bestsellers</a>
                            <a href="#back-to-school" class="kids-item">Back to School</a>
                            <a href="#back-to-school" class="kids-item">Sports Gear</a>
                            <a href="#back-to-school" class="kids-item">Lifestyle Looks</a>
                        </div>
                        <div class="kids-column">
                            <div class="kids-heading">Shoes</div>
                            <a href="#all-shoes" class="kids-item">All Shoes</a>
                            <a href="#lifestyle" class="kids-item">Lifestyle</a>
                            <a href="#jordan" class="kids-item">Jordan</a>
                            <a href="#running" class="kids-item">Running</a>
                            <a href="#basketball" class="kids-item">Basketball</a>
                            <a href="#basketball" class="kids-item">Football</a>
                        </div>
                        <div class="kids-column">
                            <div class="kids-heading">Clothing</div>
                            <a href="#all-clothing" class="kids-item">All Clothing</a>
                            <a href="#tops" class="kids-item">Tops and T-shirts</a>
                            <a href="#tops" class="kids-item">Sports Bra</a>
                            <a href="#hoodies" class="kids-item">Hoodies and Sweatshirts</a>
                            <a href="#pants" class="kids-item">Pants and Leggings</a>
                            <a href="#shorts" class="kids-item">Shorts</a>
                            <a href="#shorts" class="kids-item">Jackets and Gilets</a>
                        </div>
                        <div class="kids-column">
                            <div class="kids-heading">By Age</div>
                            <a href="#older-kids" class="kids-item">Older Kids (7-14 years)</a>
                            <a href="#younger-kids" class="kids-item">Younger Kids (4-7 years)</a>
                            <a href="#babies" class="kids-item">Babies & Toddlers (0-4 years)</a>
                            <div class="kids-heading" style="margin-top: 15px;">Shop By Sports</div>
                            <a href="#football-sport" class="kids-item">Football</a>
                            <a href="#basketball-sport" class="kids-item">Basketball</a>
                            <a href="#basketball-sport" class="kids-item">Running</a>
                            <a href="#basketball-sport" class="kids-item">Gym and Training</a>
                        </div>
                        <div class="kids-column">
                            <div class="kids-heading">Accessories and Equipments</div>
                            <a href="#all-accessories" class="kids-item">Accessories & Equipmentss</a>
                            <a href="#bags" class="kids-item">Bags and Backpacks</a>
                            <a href="#socks" class="kids-item">Socks</a>
                            <a href="#hats" class="kids-item">Hats and Headwear</a>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="sale-trigger">
                <a href="/sale" class="sale-link">Sale</a>
                <div class="sale-menu">
                    <div class="sale-content">
                        <div class="sale-column">
                            <div class="sale-heading">Sale & Offers</div>
                            <a href="#shop-all-sale" class="sale-item">Shop All Sale</a>
                            <a href="#bestsellers" class="sale-item">Bestsellers</a>
                            <a href="#last-chance" class="sale-item">Last Chance</a>
                        </div>
                        <div class="sale-column">
                            <div class="sale-heading">Men's Sale</div>
                            <a href="#men-shoes" class="sale-item">Shoes</a>
                            <a href="#men-clothing" class="sale-item">Clothing</a>
                            <a href="#men-accessories" class="sale-item">Accessories & Equipments</a>
                        </div>
                        <div class="sale-column">
                            <div class="sale-heading">Women's Sale</div>
                            <a href="#women-shoes" class="sale-item">Shoes</a>
                            <a href="#women-clothing" class="sale-item">Clothing</a>
                            <a href="#women-accessories" class="sale-item">Accessories & Equipments</a>
                        </div>
                        <div class="sale-column">
                            <div class="sale-heading">Kids' Sale</div>
                            <a href="#kids-shoes" class="sale-item">Shoes</a>
                            <a href="#kids-clothing" class="sale-item">Clothing</a>
                            <a href="#kids-accessories" class="sale-item">Accessories & Equipments</a>
                        </div>
                        <div class="sale-column">
                            <div class="sale-heading">Shop By Sports</div>
                            <a href="#football" class="sale-item">Football</a>
                            <a href="#running" class="sale-item">Running</a>
                            <a href="#basketball" class="sale-item">Basketball</a>
                            <a href="#gym-training" class="sale-item">Gym & Training</a>
                            <a href="#tennis" class="sale-item">Tennis</a>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="snkrs-trigger">
                <a href="/snkrs" class="snkrs-link">SNKRS</a>
                <div class="snkrs-menu">
                    <div class="snkrs-content">
                        <div class="snkrs-column">
                            <div class="snkrs-heading">Featured</div>
                            <a href="#snkrs-launch-calendar" class="snkrs-item">SNKRS Launch Calendar</a>
                            <a href="#exclusive-launches" class="snkrs-item">Exclusive Launches</a>
                            <a href="#new-releases" class="snkrs-item">New Releases</a>
                            <a href="#upcoming" class="snkrs-item">Upcoming</a>
                        </div>
                       <div class="snkrs-column">
                            <div class="snkrs-heading">Shop Icons</div>
                            <a href="#lifestyle" class="snkrs-item">Lifestyle</a>
                            <a href="#af1" class="snkrs-item">Air Force 1</a>
                            <a href="#aj1" class="snkrs-item">Air Jordan 1</a>
                            <a href="#airmax" class="snkrs-item">Air Max</a>
                            <a href="#cortez" class="snkrs-item">Cortez</a>
                            <a href="#vomero" class="snkrs-item">Vomero</a>
                            <a href="#dunk" class="snkrs-item">Dunk</a>
                            <a href="#pegasus" class="snkrs-item">Pegasus</a>
                        </div>
                        <div class="snkrs-column">
                            <div class="snkrs-heading">Collections</div>
                            <a href="#mens-sneakers" class="snkrs-item">Men's Sneakers</a>
                            <a href="#womens-sneakers" class="snkrs-item">Women's Sneakers</a>
                            <a href="#kids-sneakers" class="snkrs-item">Kids' Sneakers</a>
                        </div>
                        <div class="snkrs-column">
                            <div class="snkrs-heading">Shoes</div>
                            <a href="#all-shoes" class="snkrs-item">All Shoes</a>
                            <a href="#lifestyle" class="snkrs-item">Lifestyle</a>
                            <a href="#jordan" class="snkrs-item">Jordan</a>
                            <a href="#running" class="snkrs-item">Running</a>
                            <a href="#basketball" class="snkrs-item">Basketball</a>
                            <a href="#basketball" class="snkrs-item">Football</a>
                            <a href="#basketball" class="snkrs-item">Gym and Training</a>
                            <a href="#basketball" class="snkrs-item">Skateboarding</a>
                            <a href="#basketball" class="snkrs-item">Sandals and Slides</a>
                            <a href="#basketball" class="snkrs-item">Nike By You</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="search-container">
            <input type="text" class="search-bar" placeholder="Search">
            <a href="/favorites" class="favorites-icon">
                <span class="heart-outline">♡</span>
                <span class="heart-filled">♥</span>
            </a>
            <a href="/basket" class="basket-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="9" cy="21" r="1"></circle>
                    <circle cx="20" cy="21" r="1"></circle>
                    <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path>
                </svg>
            </a>
        </div>
    </div>
    
    <div class="slideshow-container">
        {% for i in range(5) %}
        <img src="/static/ssf3.avif" class="slide{% if i == 0 %} active{% endif %}" alt="Slide {{ i*3 + 1 }}">
        <video class="slide" muted playsinline preload="metadata">
            <source src="/static/slideshow2.mp4" type="video/mp4">
        </video>
        <video class="slide" muted playsinline preload="metadata">
            <source src="/static/slideshow.mp4" type="video/mp4">
        </video>
        {% endfor %}
        
        <button class="shop-button">Shop</button>
        
        <div class="slideshow-controls">
            <button class="slideshow-control-btn" onclick="togglePause()" id="pauseBtn">
                <div class="pause-icon">
                    <div class="pause-bar"></div>
                    <div class="pause-bar"></div>
                </div>
            </button>
            <button class="slideshow-control-btn" onclick="prevSlide()">
                <svg viewBox="0 0 24 24">
                    <polyline points="15 18 9 12 15 6"></polyline>
                </svg>
            </button>
            <button class="slideshow-control-btn" onclick="nextSlide()">
                <svg viewBox="0 0 24 24">
                    <polyline points="9 18 15 12 9 6"></polyline>
                </svg>
            </button>
        </div>
        <div class="slide-indicators" id="slideIndicators"></div>
    </div>

    <div class="text-slideshow-container">
        {% for i in range(20) %}
        <div class="text-slide{% if i == 0 %} text-active{% endif %}">THREADS, NO CAP.</div>
        <div class="text-slide">UNLEASH YOUR POTENTIAL.</div>
        <div class="text-slide">THE DRIP SECTION.</div>
        <div class="text-slide">WHERE CHAMPIONS ARE MADE.</div>
        {% endfor %}
    </div>

    <div class="athlete-section">
        <div class="content-wrapper">
            <div class="athlete-title">Athlete Picks</div>
            <div class="athlete-images-container">
                <div class="athlete-image-wrapper">
                    <img src="/static/ath.avif" alt="Athlete 1" class="athlete-image">
                </div>
                <div class="athlete-image-wrapper">
                    <img src="/static/ath2.avif" alt="Athlete 2" class="athlete-image">
                </div>
            </div>
        </div>
    </div>

    <div class="featured-heading-section">
        <div class="content-wrapper">
            <p class="featured-main-title">New Season Arrivals</p>
            <p class="featured-subtitle">Discover latest styles and innovations</p>
            <button class="featured-cta-button">Shop Now</button>
        </div>
    </div>

    <div class="discover-section">
        <div class="content-wrapper">
            <div class="discover-title">Featured</div>
            <div class="discover-grid">
                <div class="discover-item">
                    <img src="/static/f1.png" alt="Discover 1" class="discover-image">
                </div>
                <div class="discover-item">
                    <img src="/static/f2.png" alt="Discover 2" class="discover-image">
                </div>
                <div class="discover-item">
                    <img src="/static/f3.png" alt="Discover 3" class="discover-image">
                </div>
                <div class="discover-item">
                    <img src="/static/f4.png" alt="Discover 4" class="discover-image">
                </div>
            </div>
        </div>
    </div>

    <div class="features-section">
        <div class="content-wrapper">
            <div class="features-title">What's Hot</div>
            <div class="featured-images-container">
                <div class="featured-image-wrapper">
                    <img src="/static/hot.avif" alt="Featured 1" class="featured-image">
                    <button class="shop-tab-button" onclick="window.location.href='/men'">Shop</button>
                </div>
                <div class="featured-image-wrapper">
                    <img src="/static/hot1.avif" alt="Featured 2" class="featured-image">
                    <button class="shop-tab-button" onclick="window.location.href='/women'">Shop</button>
                </div>
                <div class="featured-image-wrapper">
                    <img src="/static/hot2.avif" alt="Featured 3" class="featured-image">
                    <button class="shop-tab-button" onclick="window.location.href='/msports'">Shop</button>
                </div>
                <div class="featured-image-wrapper">
                    <img src="/static/hot3.avif" alt="Featured 4" class="featured-image">
                    <button class="shop-tab-button" onclick="window.location.href='/wsports'">Shop</button>
                </div>
            </div>
        </div>
    </div>
    
    <div class="gear-section">
        <div class="content-wrapper">
            <div class="gear-title">KNWLS</div>
            <div class="gear-image-container">
                <img src="/static/youcan.jpg" alt="Gear Feature" class="gear-image">
            </div>
        </div>
    </div>
    
<div class="sports-section">
    <div class="content-wrapper">
        <div class="sports-title">Live For Sports</div>
        <div class="sports-slider-container">
            <button class="slider-btn left" onclick="slideLeft()">‹</button>
            <button class="slider-btn right" onclick="slideRight()">›</button>
            <div class="sports-slider" id="sportsSlider">
                <div class="sports-item" data-sport="Running" data-image="/static/running.avif">
                    <img src="/static/running.avif" alt="Sport 1" class="sports-image">
                    <div class="sports-text">Running</div>
                </div>
                <div class="sports-item" data-sport="Basketball" data-image="/static/basketball.avif">
                    <img src="/static/basketball.avif" alt="Sport 2" class="sports-image">
                    <div class="sports-text">Basketball</div>
                </div>
                <div class="sports-item" data-sport="Football" data-image="/static/football.avif">
                    <img src="/static/football.avif" alt="Sport 3" class="sports-image">
                    <div class="sports-text">Football</div>
                </div>
                <div class="sports-item" data-sport="Golf" data-image="/static/golg.avif">
                    <img src="/static/golg.avif" alt="Sport 4" class="sports-image">
                    <div class="sports-text">Golf</div>
                </div>
                <div class="sports-item" data-sport="Skating" data-image="/static/skate.avif">
                    <img src="/static/skate.avif" alt="Sport 5" class="sports-image">
                    <div class="sports-text">Skating</div>
                </div>
                <div class="sports-item" data-sport="Tennis" data-image="/static/tennis.avif">
                    <img src="/static/tennis.avif" alt="Sport 6" class="sports-image">
                    <div class="sports-text">Tennis</div>
                </div>
            </div>
        </div>
        
        <div class="select-icons-title">Select By Icons</div>
        <div class="icons-slider-container">
            <button class="icons-slider-btn left" onclick="slideIconsLeft()">‹</button>
            <button class="icons-slider-btn right" onclick="slideIconsRight()">›</button>
<div class="icons-slider" id="iconsSlider">
                {% for j in range(10) %}
                <a href="#airmax" class="icon-item" data-icon="Air Max" data-image="/static/airmax.png">
                    <img src="/static/airmax.png" alt="Air Max" class="icon-image">
                </a>
                <a href="#airforce" class="icon-item" data-icon="Air Force" data-image="/static/airforce.png">
                    <img src="/static/airforce.png" alt="Air Force" class="icon-image">
                </a>
                <a href="#blazer" class="icon-item" data-icon="Blazer" data-image="/static/blazer.png">
                    <img src="/static/blazer.png" alt="Blazer" class="icon-image">
                </a>
                <a href="#dunk" class="icon-item" data-icon="Dunk" data-image="/static/dunk.png">
                    <img src="/static/dunk.png" alt="Dunk" class="icon-image">
                </a>
                <a href="#cortez" class="icon-item" data-icon="Cortez" data-image="/static/cortez.png">
                    <img src="/static/cortez.png" alt="Cortez" class="icon-image">
                </a>
                <a href="#killshot" class="icon-item" data-icon="Killshot" data-image="/static/killshot.png">
                    <img src="/static/killshot.png" alt="Killshot" class="icon-image">
                </a>
                <a href="#jordans" class="icon-item" data-icon="Jordans" data-image="/static/jordan.png">
                    <img src="/static/jordan.png" alt="Jordans" class="icon-image">
                </a>
                <a href="#metcon" class="icon-item" data-icon="Metcon" data-image="/static/metcon.png">
                    <img src="/static/metcon.png" alt="Metcon" class="icon-image">
                </a>
                <a href="P6000" class="icon-item" data-icon="P6000" data-image="/static/P6000.png">
                    <img src="/static/p.png" alt="P6000" class="icon-image">
                </a>
                {% endfor %}
            </div>
        </div>
    </div>
</div>
            
    <div class="nba-section">
        <div class="content-wrapper">
            <div class="nba-section-title">Shop Nike X NBA</div>
            <div class="nba-slider-container">
                <div class="nba-slider" id="nbaSlider">
                <div class="nba-item">
                        <img src="/static/nba1.avif" alt="NBA 1" class="nba-image">
                        <div class="nba-item-title">Milwaukee Bucks Icon Edition</div>
                        <div class="nba-description">Men's Nike Dri-FIT NBA Swingman Jersey</div>
                        <div class="nba-price">MRP : ₹ 5995.00</div>
                    </div>
                    <div class="nba-item">
                        <img src="/static/nba2.avif" alt="NBA 2" class="nba-image">
                        <div class="nba-item-title">Denver Nuggets Icon Edition</div>
                        <div class="nba-description">Men's Nike Dri-FIT NBA Swingman Jersey</div>
                        <div class="nba-price">MRP : ₹ 5995.00</div>
                    </div>
                    <div class="nba-item">
                        <img src="/static/nba3.avif" alt="NBA 3" class="nba-image">
                        <div class="nba-item-title">Team 13</div>
                        <div class="nba-description">Nike WNBA T-shirt</div>
                        <div class="nba-price">MRP : ₹ 1795.00</div>
                    </div>
                    <div class="nba-item">
                        <img src="/static/nba4.avif" alt="NBA 4" class="nba-image">
                        <div class="nba-item-title">Los Angeles Lakers Icon Edition</div>
                        <div class="nba-description">Men's Nike Dri-FIT NBA Swingman Jersey</div>
                        <div class="nba-price">MRP : ₹ 5995.00</div>
                    </div>
                    <div class="nba-item">
                        <img src="/static/nba5.avif" alt="NBA 5" class="nba-image">
                        <div class="nba-item-title">Sacramento Kings Icon Edition</div>
                        <div class="nba-description">Nike Dri-FIT NBA Swingman Jersey</div>
                        <div class="nba-price">MRP : ₹ 5995.00</div>
                    </div>
                    <div class="nba-item">
                        <img src="/static/nba6.avif" alt="NBA 6" class="nba-image">
                        <div class="nba-item-title">San Antonio Spurs Icon Edition</div>
                        <div class="nba-description">Men's Nike Dri-FIT NBA Swingman Jersey</div>
                        <div class="nba-price">MRP : ₹ 5995.00</div>
                    </div>
                    <div class="nba-item">
                        <img src="/static/nba7.avif" alt="NBA 7" class="nba-image">
                        <div class="nba-item-title">Team 13</div>
                        <div class="nba-description">Women's Nike WNBA Boxy Crew-Neck T-Shirt</div>
                        <div class="nba-price">₹ 2087.00</div>
                    </div>
                    <div class="nba-item">
                        <img src="/static/nba8.avif" alt="NBA 8" class="nba-image">
                        <div class="nba-item-title">Stephen Curry Golden State Warriors Select Series</div>
                        <div class="nba-description">Men's Nike NBA T-Shirt</div>
                        <div class="nba-price">₹ 2087.00</div>
                    </div>
                    <div class="nba-item">
                        <img src="/static/nba10.avif" alt="NBA 10" class="nba-image">
                        <div class="nba-item-title">Boston Celtics</div>
                        <div class="nba-description">Men's Nike NBA T-Shirt</div>
                        <div class="nba-price">MRP : ₹ 1795.00</div>
                    </div>
                    <div class="nba-item">
                        <img src="/static/nba12.avif" alt="NBA 12" class="nba-image">
                        <div class="nba-item-title">Los Angeles Lakers</div>
                        <div class="nba-description">Men's Nike NBA T-Shirt</div>
                        <div class="nba-price">MRP : ₹ 1795.00</div>
                    </div>
                    <div class="nba-item">
                        <img src="/static/nba13.avif" alt="NBA 13" class="nba-image">
                        <div class="nba-item-title">New York Knicks Statement Edition</div>
                        <div class="nba-description">Men's Nike Dri-FIT NBA Swingman Jersey</div>
                        <div class="nba-price">MRP : ₹ 5995.00</div>
                    </div>
                    <div class="nba-item">
                        <img src="/static/nba14.avif" alt="NBA 15" class="nba-image">
                        <div class="nba-item-title">Chicago Bulls Courtside Windrunner</div>
                        <div class="nba-description">Men's Nike NBA Anorak Jacket</div>
                        <div class="nba-price">₹ 5217.00</div>
                    </div>
                    <div class="nba-item">
                        <img src="/static/nba15.avif" alt="NBA 15" class="nba-image">
                        <div class="nba-item-title">Chicago Bulls Courtside Windrunner</div>
                        <div class="nba-description">Men's Nike NBA Anorak Jacket</div>
                        <div class="nba-price">₹ 5517.00</div>
                    </div>
                </div>
            </div>
            <div class="nba-slider-controls">
                <button class="nba-slider-btn left" onclick="slideNbaLeft()">‹</button>
                <button class="nba-slider-btn right" onclick="slideNbaRight()">›</button>
                </button>
            </div>
        </div>
    </div>
    
    <footer class="footer-section">
        <div class="footer-content">
            <div class="footer-column">
                <div class="footer-column-title">Resources</div>
                <a href="/find-store" class="footer-link">Find A Store</a>
                <a href="/become-member" class="footer-link">Become A Member</a>
                <a href="/shoe-finder" class="footer-link">Running Shoe Finder</a>
                <a href="/product-advice" class="footer-link">Product Advice</a>
                <a href="/coaching" class="footer-link">Nike Coaching</a>
                <a href="/feedback" class="footer-link">Send Us Feedback</a>
            </div>
            
            <div class="footer-column">
                <div class="footer-column-title">Help</div>
                <a href="/help" class="footer-link">Get Help</a>
                <a href="/order-status" class="footer-link">Order Status</a>
                <a href="/delivery" class="footer-link">Delivery</a>
                <a href="/returns" class="footer-link">Returns</a>
                <a href="/payment-options" class="footer-link">Payment Options</a>
                <a href="/contact-nike" class="footer-link">Contact Us On nikebydeepika.com Inquiries</a>
                <a href="/contact-other" class="footer-link">Contact Us On All Other Inquiries</a>
            </div>
            
            <div class="footer-column">
                <div class="footer-column-title">Company</div>
                <a href="/about" class="footer-link">About Nike</a>
                <a href="/news" class="footer-link">News</a>
                <a href="/careers" class="footer-link">Careers</a>
                <a href="/investors" class="footer-link">Investors</a>
                <a href="/sustainability" class="footer-link">Sustainability</a>
                <a href="/impact" class="footer-link">Impact</a>
                <a href="/report" class="footer-link">Report a Concern</a>
            </div>
            
            <div class="footer-column footer-location-column">
                <div class="footer-location">
                    <svg class="location-icon" fill="currentColor" viewBox="0 0 24 24">
                        <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/>
                    </svg>
                    <span>India</span>
                </div>
            </div>
        </div>
        
        <div class="footer-bottom">
            <div class="footer-bottom-left">
                <span>© 2025 Nikebydeepika Inc. All rights reserved</span>
                <a href="/guides" class="footer-bottom-link">Guides</a>
                <a href="/terms-of-sale" class="footer-bottom-link">Terms of Sale</a>
                <a href="/terms-of-use" class="footer-bottom-link">Terms of Use</a>
                <a href="/privacy-policy" class="footer-bottom-link">Nikebydeepika Privacy Policy</a>
            </div>
            <div class="footer-bottom-right">
                <a href="/privacy-settings" class="footer-bottom-link">Privaslidescy Settings</a>
            </div>
        </div>
    </footer>
    <div class="sports-popup" id="sportsPopup"></div>
    <div class="icons-popup" id="iconsPopup"></div>
    
    <script>
        //Slideshow//
        let currentIndex = 0;
        const slides = document.querySelectorAll('.slide');
        const totalSlides = slides.length;
        let slideTimeout;
        let isPaused = false;

        function showSlide(index, direction = 'next') {
            try {
                // Clear existing timer
                clearTimeout(slideTimeout);
                
                // Stop all videos
                slides.forEach(slide => {
                    if (slide.tagName === 'VIDEO') {
                        slide.pause();
                        slide.currentTime = 0;
                    }
                });
                
                // Get previous slide index
                const prevIndex = currentIndex;
                
                // Handle index boundaries - loop infinitely
                if (index >= totalSlides) {
                    currentIndex = 0;
                } else if (index < 0) {
                    currentIndex = totalSlides - 1;
                } else {
                    currentIndex = index;
                }
                
                // Reset all slides - remove animations and reset z-index
                slides.forEach((slide, idx) => {
                    slide.classList.remove('active', 'slide-out');
                    slide.style.zIndex = '0';
                    slide.style.opacity = '0';
                    slide.style.transform = 'none';
                    slide.style.pointerEvents = 'none';
                });
                
                // Apply slide-out animation to previous slide if moving forward
                if (direction === 'next' && prevIndex !== currentIndex) {
                    const prevSlide = slides[prevIndex];
                    prevSlide.classList.add('slide-out');
                    prevSlide.style.zIndex = '1';
                }
                
                // Set current slide as active
                const currentSlide = slides[currentIndex];
                currentSlide.classList.add('active');
                currentSlide.style.zIndex = '2';
                currentSlide.style.opacity = '1';
                currentSlide.style.pointerEvents = 'auto';
                
                // Update dots
                updateDots();
                
                // Handle video slides
                if (currentSlide.tagName === 'VIDEO') {
                    const video = currentSlide;
                    
                    // Reset video
                    video.currentTime = 0;
                    video.load();
                    
                    // Try to play video
                    const playPromise = video.play();
                    
                    if (playPromise !== undefined) {
                        playPromise.then(() => {
                            // Video playing successfully
                            const duration = video.duration && !isNaN(video.duration) ? Math.floor(video.duration * 1000) : 5000;
                            
                            slideTimeout = setTimeout(() => {
                                if (!isPaused) {
                                    nextSlideAuto();
                                }
                            }, duration);
                        }).catch(err => {
                            console.error('Video play failed:', err);
                            // If video fails, move to next slide after 5 seconds
                            slideTimeout = setTimeout(() => {
                                if (!isPaused) {
                                    nextSlideAuto();
                                }
                            }, 5000);
                        });
                    } else {
                        // Fallback if play() doesn't return a promise
                        slideTimeout = setTimeout(() => {
                            if (!isPaused) {
                                nextSlideAuto();
                            }
                        }, 5000);
                    }
                }
                // Handle image slides
                else {
                    const imageDuration = 4000;
                    slideTimeout = setTimeout(() => {
                        if (!isPaused) {
                            nextSlideAuto();
                        }
                    }, imageDuration);
                }
            } catch (error) {
                console.error('Slideshow error:', error);
                // If anything fails, try to continue to next slide
                slideTimeout = setTimeout(() => {
                    if (!isPaused) {
                        nextSlideAuto();
                    }
                }, 5000);
            }
        }

        function nextSlideAuto() {
            if (!isPaused) {
                currentIndex++;
                showSlide(currentIndex, 'next');
            }
        }

        function updateDots() {
            const dots = document.querySelectorAll('.slide-dot');
            const totalDots = 3; // Only show 3 dots
            const slideGroup = Math.floor(currentIndex / totalDots);
            const dotIndex = currentIndex % totalDots;
            
            dots.forEach((dot, index) => {
                dot.classList.remove('active');
                // Only show 3 dots at a time
                if (index >= slideGroup * totalDots && index < (slideGroup + 1) * totalDots) {
                    dot.style.display = 'block';
                } else {
                    dot.style.display = 'none';
                }
            });
            
            // Highlight active dot within visible group
            const visibleDots = Array.from(dots).filter(dot => dot.style.display !== 'none');
            if (visibleDots[dotIndex]) {
                visibleDots[dotIndex].classList.add('active');
            }
        }

        function goToSlide(index) {
            clearTimeout(slideTimeout);
            
            // Reset pause state
            isPaused = false;
            const pauseBtn = document.getElementById('pauseBtn');
            if (pauseBtn) {
                const iconContainer = pauseBtn.querySelector('.pause-icon, .play-icon');
                iconContainer.className = 'pause-icon';
                iconContainer.innerHTML = '<div class="pause-bar"></div><div class="pause-bar"></div>';
            }
            
            // Reset all slides
            slides.forEach(slide => {
                slide.classList.remove('active', 'slide-out');
                slide.style.zIndex = '0';
                slide.style.opacity = '0';
                slide.style.transform = 'none';
            });
            
            // Set target slide
            currentIndex = index;
            const currentSlide = slides[currentIndex];
            currentSlide.classList.remove('slide-out');
            currentSlide.style.zIndex = '2';
            currentSlide.style.opacity = '1';
            currentSlide.style.transform = 'translateX(0)';
            currentSlide.style.pointerEvents = 'auto';
            
            updateDots();
            
            // Auto-advance after dot click
            const imageDuration = 5000;
            slideTimeout = setTimeout(() => {
                if (!isPaused) {
                    nextSlideAuto();
                }
            }, imageDuration);
        }

        function togglePause() {
            isPaused = !isPaused;
            const pauseBtn = document.getElementById('pauseBtn');
            const iconContainer = pauseBtn.querySelector('.pause-icon, .play-icon');
            const currentSlide = slides[currentIndex];
            
            if (isPaused) {
                iconContainer.className = 'play-icon';
                iconContainer.innerHTML = '';
                
                if (currentSlide.tagName === 'VIDEO') {
                    currentSlide.pause();
                }
                
                clearTimeout(slideTimeout);
            } else {
                iconContainer.className = 'pause-icon';
                iconContainer.innerHTML = '<div class="pause-bar"></div><div class="pause-bar"></div>';
                
                if (currentSlide.tagName === 'VIDEO') {
                    const video = currentSlide;
                    video.play().catch(err => console.error('Resume video failed:', err));
                    
                    const remainingTime = (video.duration - video.currentTime) * 1000;
                    
                    slideTimeout = setTimeout(() => {
                        if (!isPaused) {
                            nextSlideAuto();
                        }
                    }, remainingTime);
                } else {
                    const imageDuration = 3000;
                    slideTimeout = setTimeout(() => {
                        if (!isPaused) {
                            nextSlideAuto();
                        }
                    }, imageDuration);
                }
            }
        }

        function prevSlide() {
            clearTimeout(slideTimeout);
            
            isPaused = false;
            const pauseBtn = document.getElementById('pauseBtn');
            if (pauseBtn) {
                const iconContainer = pauseBtn.querySelector('.pause-icon, .play-icon');
                iconContainer.className = 'pause-icon';
                iconContainer.innerHTML = '<div class="pause-bar"></div><div class="pause-bar"></div>';
            }
            
            // Reset all slides
            slides.forEach(slide => {
                slide.classList.remove('active', 'slide-out');
                slide.style.zIndex = '0';
                slide.style.opacity = '0';
                slide.style.transform = 'none';
            });
            
            currentIndex--;
            if (currentIndex < 0) {
                currentIndex = totalSlides - 1;
            }
            
            const currentSlide = slides[currentIndex];
            currentSlide.style.zIndex = '2';
            currentSlide.style.opacity = '1';
            currentSlide.style.transform = 'translateX(0)';
            currentSlide.style.pointerEvents = 'auto';
            
            updateDots();
            
            const imageDuration = 5000;
            slideTimeout = setTimeout(() => {
                if (!isPaused) {
                    nextSlideAuto();
                }
            }, imageDuration);
        }

        function nextSlide() {
            clearTimeout(slideTimeout);
            
            isPaused = false;
            const pauseBtn = document.getElementById('pauseBtn');
            if (pauseBtn) {
                const iconContainer = pauseBtn.querySelector('.pause-icon, .play-icon');
                iconContainer.className = 'pause-icon';
                iconContainer.innerHTML = '<div class="pause-bar"></div><div class="pause-bar"></div>';
            }
            
            currentIndex++;
            showSlide(currentIndex, 'next');
        }

        // Start slideshow on page load
        window.addEventListener('load', () => {
            // Initialize slideshow
            showSlide(0, 'next');
            
            // Generate dots dynamically for 30 slides
            const slideIndicators = document.getElementById('slideIndicators');
            if (slideIndicators) {
                for (let i = 0; i < 30; i++) {
                    const dot = document.createElement('div');
                    dot.className = 'slide-dot';
                    // Hide all dots except first 3 initially
                    if (i >= 3) {
                        dot.style.display = 'none';
                    }
                    if (i === 0) {
                        dot.classList.add('active');
                    }
                    dot.onclick = () => goToSlide(i);
                    slideIndicators.appendChild(dot);
                }
            }
        });

        //Sports Slider//
        function slideLeft() {
            const slider = document.getElementById('sportsSlider');
            if (slider) {
                const itemWidth = document.querySelector('.sports-item').offsetWidth + 8;
                slider.scrollLeft -= itemWidth;
                updateSliderButtons();
            }
        }

        function slideRight() {
            const slider = document.getElementById('sportsSlider');
            if (slider) {
                const itemWidth = document.querySelector('.sports-item').offsetWidth + 8;
                slider.scrollLeft += itemWidth;
                updateSliderButtons();
            }
        }

        function slideRight() {
            const slider = document.getElementById('sportsSlider');
            if (slider) {
                const itemWidth = document.querySelector('.sports-item').offsetWidth + 8;
                slider.scrollLeft += itemWidth * 3;
                updateSliderButtons();
            }
        }

        function updateSliderButtons() {
            const slider = document.getElementById('sportsSlider');
            const leftBtn = document.querySelector('.slider-btn.left');
            const rightBtn = document.querySelector('.slider-btn.right');
            
            if (slider && leftBtn && rightBtn) {
                if (slider.scrollLeft <= 0) {
                    leftBtn.classList.add('hidden');
                } else {
                    leftBtn.classList.remove('hidden');
                }
                
                if (slider.scrollLeft >= slider.scrollWidth - slider.clientWidth - 10) {
                    rightBtn.classList.add('hidden');
                } else {
                    rightBtn.classList.remove('hidden');
                }
            }
        }

        const sportsSlider = document.getElementById('sportsSlider');
        if (sportsSlider) {
            sportsSlider.addEventListener('scroll', updateSliderButtons);
        }

        //Icons Slider//
        function slideIconsLeft() {
            const slider = document.getElementById('iconsSlider');
            if (slider) {
                const itemWidth = document.querySelector('.icon-item').offsetWidth + 15;
                slider.scrollLeft -= itemWidth;
                updateIconsSliderButtons();
            }
        }

        function slideIconsRight() {
            const slider = document.getElementById('iconsSlider');
            if (slider) {
                const itemWidth = document.querySelector('.icon-item').offsetWidth + 15;
                slider.scrollLeft += itemWidth;
                updateIconsSliderButtons();
            }
        }

        function updateIconsSliderButtons() {
            const slider = document.getElementById('iconsSlider');
            const leftBtn = document.querySelectorAll('.icons-slider-btn.left')[0];
            const rightBtn = document.querySelectorAll('.icons-slider-btn.right')[0];
            
            if (slider && leftBtn && rightBtn) {
                if (slider.scrollLeft <= 0) {
                    leftBtn.classList.add('hidden');
                } else {
                    leftBtn.classList.remove('hidden');
                }
                
                if (slider.scrollLeft >= slider.scrollWidth - slider.clientWidth - 10) {
                    rightBtn.classList.add('hidden');
                } else {
                    rightBtn.classList.remove('hidden');
                }
            }
        }

        const iconsSlider = document.getElementById('iconsSlider');
        if (iconsSlider) {
            iconsSlider.addEventListener('scroll', updateIconsSliderButtons);
            
            // Center to middle position on load
            window.addEventListener('load', () => {
                const totalItems = iconsSlider.querySelectorAll('.icon-item').length;
                const itemWidth = iconsSlider.querySelector('.icon-item').offsetWidth + 15;
                const middlePosition = Math.floor(totalItems / 2);
                const scrollPosition = middlePosition * itemWidth - (iconsSlider.clientWidth / 2) + (itemWidth / 2);
                iconsSlider.scrollLeft = scrollPosition;
                updateIconsSliderButtons();
            });
        }

        //NBA Slider//
        function slideNbaLeft() {
            const slider = document.getElementById('nbaSlider');
            if (slider) {
                const itemWidth = document.querySelector('.nba-item').offsetWidth + 15;
                slider.scrollLeft -= itemWidth;
                updateNbaSliderButtons();
            }
        }

        function slideNbaRight() {
            const slider = document.getElementById('nbaSlider');
            if (slider) {
                const itemWidth = document.querySelector('.nba-item').offsetWidth + 15;
                slider.scrollLeft += itemWidth;
                updateNbaSliderButtons();
            }
        }

        function updateNbaSliderButtons() {
            const slider = document.getElementById('nbaSlider');
            const leftBtn = document.querySelectorAll('.nba-slider-btn.left')[0];
            const rightBtn = document.querySelectorAll('.nba-slider-btn.right')[0];
            
            if (slider && leftBtn && rightBtn) {
                if (slider.scrollLeft <= 0) {
                    leftBtn.classList.add('hidden');
                } else {
                    leftBtn.classList.remove('hidden');
                }
                
                if (slider.scrollLeft >= slider.scrollWidth - slider.clientWidth - 10) {
                    rightBtn.classList.add('hidden');
                } else {
                    rightBtn.classList.remove('hidden');
                }
            }
        }

        const nbaSlider = document.getElementById('nbaSlider');
        if (nbaSlider) {
            nbaSlider.addEventListener('scroll', updateNbaSliderButtons);
        }

        // Initialize all slider buttons on load
        window.addEventListener('load', () => {
            updateSliderButtons();
            updateIconsSliderButtons();
            updateNbaSliderButtons();
        });

        //Sports Items Hover Popup//
        document.querySelectorAll('.sports-item').forEach(item => {
            item.addEventListener('mouseenter', function(e) {
                const popup = document.getElementById('sportsPopup');
                const sportName = this.getAttribute('data-sport');
                const imageUrl = this.getAttribute('data-image');
                
                if (popup) {
                    popup.innerHTML = `
                        <img src="${imageUrl}" alt="${sportName}" class="sports-popup-image">
                        <div class="sports-popup-text">${sportName}</div>
                    `;
                    
                    popup.classList.add('active');
                    popup.style.left = e.pageX + 10 + 'px';
                    popup.style.top = e.pageY + 10 + 'px';
                }
            });
            
            item.addEventListener('mousemove', function(e) {
                const popup = document.getElementById('sportsPopup');
                if (popup) {
                    popup.style.left = e.pageX + 10 + 'px';
                    popup.style.top = e.pageY + 10 + 'px';
                }
            });
            
            item.addEventListener('mouseleave', function() {
                const popup = document.getElementById('sportsPopup');
                if (popup) {
                    popup.classList.remove('active');
                }
            });
        });

        //Icons Items Hover Popup//
        document.querySelectorAll('.icon-item').forEach(item => {
            item.addEventListener('mouseenter', function(e) {
                const popup = document.getElementById('iconsPopup');
                const iconName = this.getAttribute('data-icon');
                const imageUrl = this.getAttribute('data-image');
                
                if (popup) {
                    popup.innerHTML = `
                        <img src="${imageUrl}" alt="${iconName}" class="icons-popup-image">
                        <div class="icons-popup-text">${iconName}</div>
                    `;
                    
                    popup.classList.add('active');
                    popup.style.left = e.pageX + 10 + 'px';
                    popup.style.top = e.pageY + 10 + 'px';
                }
            });
            
            item.addEventListener('mousemove', function(e) {
                const popup = document.getElementById('iconsPopup');
                if (popup) {
                    popup.style.left = e.pageX + 10 + 'px';
                    popup.style.top = e.pageY + 10 + 'px';
                }
            });
            
            item.addEventListener('mouseleave', function() {
                const popup = document.getElementById('iconsPopup');
                if (popup) {
                    popup.classList.remove('active');
                }
            });
});

        // Text Slideshow
        let textCurrentIndex = 0;
        const textSlides = document.querySelectorAll('.text-slide');
        const textTotalSlides = textSlides.length;
        let textSlideTimeout;

        function showTextSlide(index) {
            const prevIndex = textCurrentIndex;
            
            if (index >= textTotalSlides) {
                textCurrentIndex = 0;
            } else if (index < 0) {
                textCurrentIndex = textTotalSlides - 1;
            } else {
                textCurrentIndex = index;
            }
            
            textSlides.forEach((slide, idx) => {
                slide.classList.remove('text-active', 'text-slide-out');
                slide.style.zIndex = '0';
                slide.style.opacity = '0';
            });
            
            if (prevIndex !== textCurrentIndex) {
                const prevSlide = textSlides[prevIndex];
                prevSlide.classList.add('text-slide-out');
                prevSlide.style.zIndex = '1';
            }
            
            const currentSlide = textSlides[textCurrentIndex];
            currentSlide.classList.add('text-active');
            currentSlide.style.zIndex = '2';
            currentSlide.style.opacity = '1';
            
            textSlideTimeout = setTimeout(() => {
                textCurrentIndex++;
                showTextSlide(textCurrentIndex);
            }, 5000);
        }

        window.addEventListener('load', () => {
            showTextSlide(0);
        });
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/new-featured')
def new_featured():
    return "<h1>New & Featured Section</h1><p>Coming Soon...</p>"

@app.route('/men')
def men():
    return "<h1>Men's Section</h1><p>Coming Soon...</p>"

@app.route('/women')
def women():
    return "<h1>Women's Section</h1><p>Coming Soon...</p>"

@app.route('/kids')
def kids():
    return "<h1>Kids' Section</h1><p>Coming Soon...</p>"

@app.route('/sale')
def sale():
    return "<h1>Sale Section</h1><p>Coming Soon...</p>"

@app.route('/snkrs')
def snkrs():
    return "<h1>SNKRS Section</h1><p>Coming Soon...</p>"

@app.route('/find-stores')
def find_stores():
    return "<h1>Find Stores</h1><p>Store locator coming soon...</p>"

@app.route('/help')
def help_page():
    return "<h1>Help Center</h1><p>How can we help you?</p>"

@app.route('/join')
def join():
    return "<h1>Join Us</h1><p>Become a Nike Member</p>"

@app.route('/signin')
def signin():
    return "<h1>Sign In</h1><p>Sign in to your Nike account</p>"

@app.route('/favorites')
def favorites():
    return "<h1>Your Favorites</h1><p>No favorites yet</p>"

@app.route('/basket')
def basket():
    return "<h1>Shopping Basket</h1><p>Your basket is empty</p>"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)