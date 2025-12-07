#!/usr/bin/env python3
"""
Test: Theme Toggle Testing
Tests light/dark mode toggle and persistence
"""

from playwright.sync_api import sync_playwright
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from selectors import Selectors, TestHelpers

def test_theme_toggle():
    """Test switching between light and dark themes"""
    print("🧪 Testing Theme Toggle...")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            page.goto('http://localhost:3000')
            TestHelpers.wait_for_navigation(page)
            TestHelpers.clear_local_storage(page)
            page.reload()
            TestHelpers.wait_for_navigation(page)
            
            # Get initial theme
            initial_theme = TestHelpers.get_theme(page)
            print(f"✅ Initial theme: {initial_theme}")
            
            TestHelpers.take_screenshot(page, f'tests/screenshots/theme_{initial_theme}_initial.png')
            
            # Click theme toggle
            theme_button = page.locator(Selectors.THEME_TOGGLE).first
            theme_button.click()
            page.wait_for_timeout(500)  # Wait for transition
            
            # Get new theme
            new_theme = TestHelpers.get_theme(page)
            assert new_theme != initial_theme, f"Theme should have changed from {initial_theme}"
            print(f"✅ Theme toggled to: {new_theme}")
            
            TestHelpers.take_screenshot(page, f'tests/screenshots/theme_{new_theme}_toggled.png')
            
            # Toggle back
            theme_button.click()
            page.wait_for_timeout(500)
            
            final_theme = TestHelpers.get_theme(page)
            assert final_theme == initial_theme, f"Should return to {initial_theme}"
            print(f"✅ Toggled back to: {final_theme}")
            
        except AssertionError as e:
            print(f"❌ Test failed: {e}")
            TestHelpers.take_screenshot(page, 'tests/screenshots/error_theme.png')
            browser.close()
            sys.exit(1)
        
        browser.close()


def test_theme_persistence():
    """Test that theme choice persists in localStorage"""
    print("\n🧪 Testing Theme Persistence...")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            page.goto('http://localhost:3000')
            TestHelpers.wait_for_navigation(page)
            TestHelpers.clear_local_storage(page)
            page.reload()
            TestHelpers.wait_for_navigation(page)
            
            # Get initial theme
            initial_theme = TestHelpers.get_theme(page)
            
            # Toggle theme
            page.locator(Selectors.THEME_TOGGLE).first.click()
            page.wait_for_timeout(500)
            
            toggled_theme = TestHelpers.get_theme(page)
            
            # Check localStorage
            stored_theme = TestHelpers.get_local_storage_item(page, 'theme')
            assert stored_theme is not None, "Theme should be stored in localStorage"
            print(f"✅ Theme stored in localStorage: {stored_theme}")
            
            # Reload page
            page.reload()
            TestHelpers.wait_for_navigation(page)
            
            # Check theme persisted
            reloaded_theme = TestHelpers.get_theme(page)
            assert reloaded_theme == toggled_theme, f"Theme should persist after reload"
            print(f"✅ Theme persisted after page reload: {reloaded_theme}")
            
        except AssertionError as e:
            print(f"❌ Test failed: {e}")
            browser.close()
            sys.exit(1)
        
        browser.close()


def test_theme_visual_changes():
    """Test that theme toggle causes visual changes"""
    print("\n🧪 Testing Theme Visual Changes...")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            page.goto('http://localhost:3000')
            TestHelpers.wait_for_navigation(page)
            TestHelpers.clear_local_storage(page)
            page.reload()
            TestHelpers.wait_for_navigation(page)
            
            # Get background color in initial theme
            initial_bg = page.evaluate("() => getComputedStyle(document.body).backgroundColor")
            print(f"Initial background: {initial_bg}")
            
            # Toggle theme
            page.locator(Selectors.THEME_TOGGLE).first.click()
            page.wait_for_timeout(500)
            
            # Get background color after toggle
            toggled_bg = page.evaluate("() => getComputedStyle(document.body).backgroundColor")
            print(f"Toggled background: {toggled_bg}")
            
            # Colors should be different
            assert initial_bg != toggled_bg, "Background color should change with theme"
            print("✅ Visual changes detected (background color changed)")
            
        except AssertionError as e:
            print(f"❌ Test failed: {e}")
            browser.close()
            sys.exit(1)
        
        browser.close()


if __name__ == '__main__':
    print("=" * 60)
    print("THEME TOGGLE TESTS")
    print("=" * 60)
    
    test_theme_toggle()
    test_theme_persistence()
    test_theme_visual_changes()
    
    print("\n" + "=" * 60)
    print("✅ ALL THEME TESTS PASSED")
    print("=" * 60)
