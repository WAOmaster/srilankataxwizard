#!/usr/bin/env python3
"""
Test: Form Validation Testing
Tests all form validations in the wizard
"""

from playwright.sync_api import sync_playwright
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from selectors import Selectors, TestHelpers

def test_required_fields():
    """Test that required fields show error messages"""
    print("🧪 Testing Required Field Validation...")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            page.goto('http://localhost:3000')
            TestHelpers.wait_for_navigation(page)
            TestHelpers.clear_local_storage(page)
            page.reload()
            TestHelpers.wait_for_navigation(page)
            
            # Try to click Next without filling anything
            page.locator(Selectors.NEXT_BUTTON).first.click()
            page.wait_for_timeout(500)
            
            # Should still be on Step 1 due to validation
            current_step = TestHelpers.get_current_step(page)
            assert current_step == 1, "Should not advance with empty required fields"
            print("✅ Prevented advancement with empty required fields")
            
            # Check for error messages
            errors = page.locator(Selectors.ERROR_MESSAGE).all()
            assert len(errors) > 0, "Expected error messages to be displayed"
            print(f"✅ Error messages displayed: {len(errors)} found")
            
            TestHelpers.take_screenshot(page, 'tests/screenshots/validation_required.png')
            
        except AssertionError as e:
            print(f"❌ Test failed: {e}")
            TestHelpers.take_screenshot(page, 'tests/screenshots/error_validation.png')
            browser.close()
            sys.exit(1)
        
        browser.close()


def test_tin_validation():
    """Test TIN field validation (must be 9 digits)"""
    print("\n🧪 Testing TIN Validation...")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            page.goto('http://localhost:3000')
            TestHelpers.wait_for_navigation(page)
            TestHelpers.clear_local_storage(page)
            page.reload()
            TestHelpers.wait_for_navigation(page)
            
            # Fill form with invalid TIN (too short)
            page.locator(Selectors.INPUT_NAME).fill("Test User")
            page.locator(Selectors.INPUT_TIN).fill("12345")  # Only 5 digits
            page.locator(Selectors.INPUT_EMAIL).fill("test@example.com")
            page.locator(Selectors.INPUT_INCOME).fill("2000000")
            
            # Try to advance
            page.locator(Selectors.NEXT_BUTTON).first.click()
            page.wait_for_timeout(500)
            
            # Should still be on Step 1
            current_step = TestHelpers.get_current_step(page)
            assert current_step == 1, "Should not advance with invalid TIN"
            print("✅ Prevented advancement with short TIN")
            
            # Fix TIN with valid 9 digits
            page.locator(Selectors.INPUT_TIN).fill("123456789")
            
            # Now should advance
            page.locator(Selectors.NEXT_BUTTON).first.click()
            page.wait_for_timeout(500)
            
            current_step = TestHelpers.get_current_step(page)
            assert current_step == 2, "Should advance with valid TIN"
            print("✅ Advanced with valid 9-digit TIN")
            
        except AssertionError as e:
            print(f"❌ Test failed: {e}")
            browser.close()
            sys.exit(1)
        
        browser.close()


def test_email_validation():
    """Test email field validation"""
    print("\n🧪 Testing Email Validation...")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            page.goto('http://localhost:3000')
            TestHelpers.wait_for_navigation(page)
            TestHelpers.clear_local_storage(page)
            page.reload()
            TestHelpers.wait_for_navigation(page)
            
            # Fill form with invalid email
            page.locator(Selectors.INPUT_NAME).fill("Test User")
            page.locator(Selectors.INPUT_TIN).fill("123456789")
            page.locator(Selectors.INPUT_EMAIL).fill("notanemail")  # Invalid format
            page.locator(Selectors.INPUT_INCOME).fill("2000000")
            
            # Try to advance
            page.locator(Selectors.NEXT_BUTTON).first.click()
            page.wait_for_timeout(500)
            
            # Should still be on Step 1
            current_step = TestHelpers.get_current_step(page)
            assert current_step == 1, "Should not advance with invalid email"
            print("✅ Prevented advancement with invalid email")
            
            # Fix email
            page.locator(Selectors.INPUT_EMAIL).fill("test@example.com")
            
            # Now should advance
            page.locator(Selectors.NEXT_BUTTON).first.click()
            page.wait_for_timeout(500)
            
            current_step = TestHelpers.get_current_step(page)
            assert current_step == 2, "Should advance with valid email"
            print("✅ Advanced with valid email")
            
        except AssertionError as e:
            print(f"❌ Test failed: {e}")
            browser.close()
            sys.exit(1)
        
        browser.close()


def test_income_validation():
    """Test income field validation (must be positive)"""
    print("\n🧪 Testing Income Validation...")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            page.goto('http://localhost:3000')
            TestHelpers.wait_for_navigation(page)
            TestHelpers.clear_local_storage(page)
            page.reload()
            TestHelpers.wait_for_navigation(page)
            
            # Fill form with zero income
            page.locator(Selectors.INPUT_NAME).fill("Test User")
            page.locator(Selectors.INPUT_TIN).fill("123456789")
            page.locator(Selectors.INPUT_EMAIL).fill("test@example.com")
            page.locator(Selectors.INPUT_INCOME).fill("0")
            
            # Try to advance
            page.locator(Selectors.NEXT_BUTTON).first.click()
            page.wait_for_timeout(500)
            
            # Should still be on Step 1
            current_step = TestHelpers.get_current_step(page)
            assert current_step == 1, "Should not advance with zero income"
            print("✅ Prevented advancement with zero income")
            
            # Fix with valid income
            page.locator(Selectors.INPUT_INCOME).fill("2000000")
            
            # Now should advance
            page.locator(Selectors.NEXT_BUTTON).first.click()
            page.wait_for_timeout(500)
            
            current_step = TestHelpers.get_current_step(page)
            assert current_step == 2, "Should advance with valid income"
            print("✅ Advanced with valid income")
            
        except AssertionError as e:
            print(f"❌ Test failed: {e}")
            browser.close()
            sys.exit(1)
        
        browser.close()


if __name__ == '__main__':
    print("=" * 60)
    print("FORM VALIDATION TESTS")
    print("=" * 60)
    
    test_required_fields()
    test_tin_validation()
    test_income_validation()
    
    print("\n" + "=" * 60)
    print("✅ ALL VALIDATION TESTS PASSED")
    print("=" * 60)
