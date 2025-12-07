#!/usr/bin/env python3
"""
Test: Wizard Functional Testing
Tests core wizard navigation and functionality
"""

from playwright.sync_api import sync_playwright
import sys
import os

# Add tests directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from selectors import Selectors, TestHelpers

def test_wizard_navigation():
    """Test forward and backward navigation through wizard steps"""
    print("🧪 Testing Wizard Navigation...")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            # Navigate to the app
            page.goto('http://localhost:3000')
            TestHelpers.wait_for_navigation(page)
            
            # Clear any existing state
            TestHelpers.clear_local_storage(page)
            page.reload()
            TestHelpers.wait_for_navigation(page)
            
            # Take initial screenshot
            TestHelpers.take_screenshot(page, 'tests/screenshots/01_initial_load.png')
            
            # Verify we're on Step 1
            current_step = TestHelpers.get_current_step(page)
            assert current_step == 1, f"Expected Step 1, got {current_step}"
            print("✅ Initial load on Step 1")
            
            # Fill Step 1 form
            TestHelpers.fill_step1_form(page, 
                name="Test User",
                tin="123456789",
                income="2000000"
            )
            
            # Click Next to go to Step 2
            page.locator(Selectors.NEXT_BUTTON).first.click()
            page.wait_for_timeout(500)
            
            current_step = TestHelpers.get_current_step(page)
            assert current_step == 2, f"Expected Step 2, got {current_step}"
            print("✅ Advanced to Step 2")
            
            TestHelpers.take_screenshot(page, 'tests/screenshots/02_step2.png')
            
            # Select an income source
            employment_checkbox = page.locator('input[type="checkbox"]').first
            if not employment_checkbox.is_checked():
                employment_checkbox.check()
            
            # Click Next to go to Step 3
            page.locator(Selectors.NEXT_BUTTON).first.click()
            page.wait_for_timeout(500)
            
            current_step = TestHelpers.get_current_step(page)
            assert current_step == 3, f"Expected Step 3, got {current_step}"
            print("✅ Advanced to Step 3")
            
            TestHelpers.take_screenshot(page, 'tests/screenshots/03_step3.png')
            
            # Test backward navigation
            page.locator(Selectors.BACK_BUTTON).first.click()
            page.wait_for_timeout(500)
            
            current_step = TestHelpers.get_current_step(page)
            assert current_step == 2, f"Expected Step 2 after back, got {current_step}"
            print("✅ Back button works - returned to Step 2")
            
            # Go back to Step 1
            page.locator(Selectors.BACK_BUTTON).first.click()
            page.wait_for_timeout(500)
            
            current_step = TestHelpers.get_current_step(page)
            assert current_step == 1, f"Expected Step 1 after back, got {current_step}"
            
            # Verify data persistence - check if name is still filled
            name_value = page.locator(Selectors.INPUT_NAME).input_value()
            assert name_value == "Test User", f"Name not persisted: {name_value}"
            print("✅ Data persisted after backward navigation")
            
            print("✅ All wizard navigation tests passed!")
            
        except AssertionError as e:
            print(f"❌ Test failed: {e}")
            TestHelpers.take_screenshot(page, 'tests/screenshots/error_wizard_nav.png')
            browser.close()
            sys.exit(1)
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            TestHelpers.take_screenshot(page, 'tests/screenshots/error_wizard_nav.png')
            browser.close()
            sys.exit(1)
        
        browser.close()


def test_step_indicator():
    """Test that step indicator updates correctly"""
    print("\n🧪 Testing Step Indicator...")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            page.goto('http://localhost:3000')
            TestHelpers.wait_for_navigation(page)
            TestHelpers.clear_local_storage(page)
            page.reload()
            TestHelpers.wait_for_navigation(page)
            
            # Check step indicator exists
            step_indicator = page.locator(Selectors.STEP_INDICATOR).first
            assert step_indicator.is_visible(), "Step indicator not visible"
            print("✅ Step indicator is visible")
            
            # Check it shows correct format
            indicator_text = step_indicator.text_content()
            assert '1' in indicator_text and '5' in indicator_text, f"Unexpected format: {indicator_text}"
            print(f"✅ Step indicator shows: {indicator_text}")
            
            print("✅ Step indicator tests passed!")
            
        except AssertionError as e:
            print(f"❌ Test failed: {e}")
            browser.close()
            sys.exit(1)
        
        browser.close()


if __name__ == '__main__':
    print("=" * 60)
    print("WIZARD FUNCTIONAL TESTS")
    print("=" * 60)
    
    test_wizard_navigation()
    test_step_indicator()
    
    print("\n" + "=" * 60)
    print("✅ ALL TESTS PASSED")
    print("=" * 60)
