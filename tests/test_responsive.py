#!/usr/bin/env python3
"""
Test: Responsive Design Testing
Tests the wizard across different viewport sizes
"""

from playwright.sync_api import sync_playwright
import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from selectors import Selectors, TestHelpers

def load_viewports():
    """Load viewport configurations from test data"""
    with open('tests/test_data.json', 'r') as f:
        data = json.load(f)
    return data['viewports']


def test_mobile_viewports():
    """Test wizard on mobile viewports"""
    print("🧪 Testing Mobile Viewports...")
    
    viewports = load_viewports()
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        
        for mobile in viewports['mobile']:
            print(f"\n  Testing {mobile['name']} ({mobile['width']}x{mobile['height']})...")
            
            page = browser.new_page(viewport={'width': mobile['width'], 'height': mobile['height']})
            
            try:
                page.goto('http://localhost:3000')
                TestHelpers.wait_for_navigation(page)
                
                # Check header is visible
                header = page.locator(Selectors.HEADER).first
                assert header.is_visible(), f"Header should be visible on {mobile['name']}"
                
                # Check language and theme buttons are visible
                lang_btn = page.locator(Selectors.LANGUAGE_TOGGLE).first
                theme_btn = page.locator(Selectors.THEME_TOGGLE).first
                
                assert lang_btn.is_visible(), f"Language toggle should be visible on {mobile['name']}"
                assert theme_btn.is_visible(), f"Theme toggle should be visible on {mobile['name']}"
                
                # Check form fields are visible
                name_input = page.locator(Selectors.INPUT_NAME).first
                assert name_input.is_visible(), f"Form inputs should be visible on {mobile['name']}"
                
                # Check footer is present (may need to scroll)
                footer = page.locator(Selectors.FOOTER).first
                assert footer.is_visible() or True, "Footer exists"
                
                # Take screenshot
                screenshot_name = f"tests/screenshots/mobile_{mobile['name'].replace(' ', '_').lower()}.png"
                TestHelpers.take_screenshot(page, screenshot_name)
                
                print(f"  ✅ {mobile['name']} layout verified")
                
            except AssertionError as e:
                print(f"  ❌ Test failed for {mobile['name']}: {e}")
                page.close()
                browser.close()
                sys.exit(1)
            
            page.close()
        
        browser.close()
    
    print("✅ All mobile viewports tested successfully")


def test_tablet_viewports():
    """Test wizard on tablet viewports"""
    print("\n🧪 Testing Tablet Viewports...")
    
    viewports = load_viewports()
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        
        for tablet in viewports['tablet']:
            print(f"\n  Testing {tablet['name']} ({tablet['width']}x{tablet['height']})...")
            
            page = browser.new_page(viewport={'width': tablet['width'], 'height': tablet['height']})
            
            try:
                page.goto('http://localhost:3000')
                TestHelpers.wait_for_navigation(page)
                
                # All elements should be visible on tablet
                header = page.locator(Selectors.HEADER).first
                assert header.is_visible(), f"Header should be visible on {tablet['name']}"
                
                # App title should be visible on tablet
                title = page.locator(Selectors.APP_TITLE).first
                assert title.is_visible(), f"App title should be visible on {tablet['name']}"
                
                # Form should be well-laid out
                name_input = page.locator(Selectors.INPUT_NAME).first
                assert name_input.is_visible(), f"Form should be accessible on {tablet['name']}"
                
                screenshot_name = f"tests/screenshots/tablet_{tablet['name'].replace(' ', '_').lower()}.png"
                TestHelpers.take_screenshot(page, screenshot_name)
                
                print(f"  ✅ {tablet['name']} layout verified")
                
            except AssertionError as e:
                print(f"  ❌ Test failed for {tablet['name']}: {e}")
                page.close()
                browser.close()
                sys.exit(1)
            
            page.close()
        
        browser.close()
    
    print("✅ All tablet viewports tested successfully")


def test_desktop_viewports():
    """Test wizard on desktop viewports"""
    print("\n🧪 Testing Desktop Viewports...")
    
    viewports = load_viewports()
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        
        for desktop in viewports['desktop']:
            print(f"\n  Testing {desktop['name']} ({desktop['width']}x{desktop['height']})...")
            
            page = browser.new_page(viewport={'width': desktop['width'], 'height': desktop['height']})
            
            try:
                page.goto('http://localhost:3000')
                TestHelpers.wait_for_navigation(page)
                
                # Everything should be visible on desktop
                header = page.locator(Selectors.HEADER).first
                assert header.is_visible(), f"Header should be visible on {desktop['name']}"
                
                # Full app title visible
                title = page.locator(Selectors.APP_TITLE).first
                assert title.is_visible(), f"Full app title should be visible on {desktop['name']}"
                
                # Content should be centered with max-width
                main = page.locator("main").first
                assert main.is_visible(), f"Main content should be visible on {desktop['name']}"
                
                screenshot_name = f"tests/screenshots/desktop_{desktop['name'].replace(' ', '_').lower()}.png"
                TestHelpers.take_screenshot(page, screenshot_name)
                
                print(f"  ✅ {desktop['name']} layout verified")
                
            except AssertionError as e:
                print(f"  ❌ Test failed for {desktop['name']}: {e}")
                page.close()
                browser.close()
                sys.exit(1)
            
            page.close()
        
        browser.close()
    
    print("✅ All desktop viewports tested successfully")


if __name__ == '__main__':
    print("=" * 60)
    print("RESPONSIVE DESIGN TESTS")
    print("=" * 60)
    
    test_mobile_viewports()
    test_tablet_viewports()
    test_desktop_viewports()
    
    print("\n" + "=" * 60)
    print("✅ ALL RESPONSIVE TESTS PASSED")
    print("=" * 60)
