#!/usr/bin/env python3
"""
Test: Multi-Language Support Testing
Tests language toggle and translation display
"""

from playwright.sync_api import sync_playwright
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from selectors import Selectors, TestHelpers

def test_language_toggle():
    """Test cycling through all three languages"""
    print("🧪 Testing Language Toggle...")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            page.goto('http://localhost:3000')
            TestHelpers.wait_for_navigation(page)
            TestHelpers.clear_local_storage(page)
            page.reload()
            TestHelpers.wait_for_navigation(page)
            
            # Initial language should be English
            lang_button = page.locator(Selectors.LANGUAGE_TOGGLE).first
            initial_lang = lang_button.text_content()
            assert 'EN' in initial_lang, f"Expected EN, got {initial_lang}"
            print(f"✅ Initial language: {initial_lang}")
            
            TestHelpers.take_screenshot(page, 'tests/screenshots/lang_english.png')
            
            # Click to switch to Sinhala
            lang_button.click()
            page.wait_for_timeout(300)
            
            lang_text = page.locator(Selectors.LANGUAGE_TOGGLE).first.text_content()
            assert 'SI' in lang_text, f"Expected SI, got {lang_text}"
            print(f"✅ Switched to Sinhala: {lang_text}")
            
            TestHelpers.take_screenshot(page, 'tests/screenshots/lang_sinhala.png')
            
            # Click to switch to Tamil
            page.locator(Selectors.LANGUAGE_TOGGLE).first.click()
            page.wait_for_timeout(300)
            
            lang_text = page.locator(Selectors.LANGUAGE_TOGGLE).first.text_content()
            assert 'TA' in lang_text, f"Expected TA, got {lang_text}"
            print(f"✅ Switched to Tamil: {lang_text}")
            
            TestHelpers.take_screenshot(page, 'tests/screenshots/lang_tamil.png')
            
            # Click to cycle back to English
            page.locator(Selectors.LANGUAGE_TOGGLE).first.click()
            page.wait_for_timeout(300)
            
            lang_text = page.locator(Selectors.LANGUAGE_TOGGLE).first.text_content()
            assert 'EN' in lang_text, f"Expected EN, got {lang_text}"
            print("✅ Cycled back to English")
            
        except AssertionError as e:
            print(f"❌ Test failed: {e}")
            TestHelpers.take_screenshot(page, 'tests/screenshots/error_language.png')
            browser.close()
            sys.exit(1)
        
        browser.close()


def test_translation_display():
    """Test that content changes in different languages"""
    print("\n🧪 Testing Translation Display...")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            page.goto('http://localhost:3000')
            TestHelpers.wait_for_navigation(page)
            TestHelpers.clear_local_storage(page)
            page.reload()
            TestHelpers.wait_for_navigation(page)
            
            # Get content in English
            page_content_en = page.content()
            assert 'Full Name' in page_content_en or 'Name' in page_content_en, "English content not found"
            print("✅ English content detected")
            
            # Switch to Sinhala
            page.locator(Selectors.LANGUAGE_TOGGLE).first.click()
            page.wait_for_timeout(500)
            
            # Get content in Sinhala
            page_content_si = page.content()
            # Sinhala should have different content
            assert page_content_si != page_content_en, "Content should change in Sinhala"
            print("✅ Sinhala content is different from English")
            
            # Switch to Tamil
            page.locator(Selectors.LANGUAGE_TOGGLE).first.click()
            page.wait_for_timeout(500)
            
            # Get content in Tamil
            page_content_ta = page.content()
            # Tamil should be different from both
            assert page_content_ta != page_content_en, "Content should change in Tamil"
            assert page_content_ta != page_content_si, "Tamil should differ from Sinhala"
            print("✅ Tamil content is different from English and Sinhala")
            
        except AssertionError as e:
            print(f"❌ Test failed: {e}")
            browser.close()
            sys.exit(1)
        
        browser.close()


def test_language_persistence():
    """Test that language choice persists across navigation"""
    print("\n🧪 Testing Language Persistence...")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            page.goto('http://localhost:3000')
            TestHelpers.wait_for_navigation(page)
            TestHelpers.clear_local_storage(page)
            page.reload()
            TestHelpers.wait_for_navigation(page)
            
            # Switch to Sinhala
            page.locator(Selectors.LANGUAGE_TOGGLE).first.click()
            page.wait_for_timeout(300)
            
            lang_text = page.locator(Selectors.LANGUAGE_TOGGLE).first.text_content()
            assert 'SI' in lang_text, "Should be in Sinhala"
            
            # Fill form and navigate to Step 2
            TestHelpers.fill_step1_form(page)
            page.locator(Selectors.NEXT_BUTTON).first.click()
            page.wait_for_timeout(500)
            
            # Check language is still Sinhala
            lang_text = page.locator(Selectors.LANGUAGE_TOGGLE).first.text_content()
            assert 'SI' in lang_text, "Language should persist to Step 2"
            print("✅ Language persisted to Step 2")
            
            # Navigate back to Step 1
            page.locator(Selectors.BACK_BUTTON).first.click()
            page.wait_for_timeout(500)
            
            # Check language is still Sinhala
            lang_text = page.locator(Selectors.LANGUAGE_TOGGLE).first.text_content()
            assert 'SI' in lang_text, "Language should persist when going back"
            print("✅ Language persisted when navigating back")
            
        except AssertionError as e:
            print(f"❌ Test failed: {e}")
            browser.close()
            sys.exit(1)
        
        browser.close()


if __name__ == '__main__':
    print("=" * 60)
    print("MULTI-LANGUAGE TESTS")
    print("=" * 60)
    
    test_language_toggle()
    test_translation_display()
    test_language_persistence()
    
    print("\n" + "=" * 60)
    print("✅ ALL LANGUAGE TESTS PASSED")
    print("=" * 60)
