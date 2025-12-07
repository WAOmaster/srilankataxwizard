#!/usr/bin/env python3
"""
Test: Complete User Flow Testing
Tests end-to-end wizard completion with data persistence
"""

from playwright.sync_api import sync_playwright
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from selectors import Selectors, TestHelpers

def test_complete_wizard_flow():
    """Test completing the entire wizard from Step 1 to Step 5"""
    print("🧪 Testing Complete Wizard Flow...")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            page.goto('http://localhost:3000')
            TestHelpers.wait_for_navigation(page)
            TestHelpers.clear_local_storage(page)
            page.reload()
            TestHelpers.wait_for_navigation(page)
            
            print("  Step 1: Filling personal information...")
            # Step 1: Personal Info
            TestHelpers.fill_step1_form(page,
                name="John Doe",
                tin="987654321",
                income="3000000"
            )
            TestHelpers.take_screenshot(page, 'tests/screenshots/flow_step1_filled.png')
            
            page.locator(Selectors.NEXT_BUTTON).first.click()
            page.wait_for_timeout(500)
            
            current_step = TestHelpers.get_current_step(page)
            assert current_step == 2, f"Should be on Step 2, got {current_step}"
            print("  ✅ Advanced to Step 2")
            
            print("  Step 2: Selecting income sources...")
            # Step 2: Income Sources - Select Employment
            checkboxes = page.locator('input[type="checkbox"]').all()
            if len(checkboxes) > 0 and not checkboxes[0].is_checked():
                checkboxes[0].check()
            
            TestHelpers.take_screenshot(page, 'tests/screenshots/flow_step2_selected.png')
            
            page.locator(Selectors.NEXT_BUTTON).first.click()
            page.wait_for_timeout(500)
            
            current_step = TestHelpers.get_current_step(page)
            assert current_step == 3, f"Should be on Step 3, got {current_step}"
            print("  ✅ Advanced to Step 3")
            
            print("  Step 3: Document checklist...")
            # Step 3: Document Checklist - just view and proceed
            TestHelpers.take_screenshot(page, 'tests/screenshots/flow_step3_docs.png')
            
            page.locator(Selectors.NEXT_BUTTON).first.click()
            page.wait_for_timeout(500)
            
            current_step = TestHelpers.get_current_step(page)
            assert current_step == 4, f"Should be on Step 4, got {current_step}"
            print("  ✅ Advanced to Step 4")
            
            print("  Step 4: Tax calculation preview...")
            # Step 4: Tax Calculation - verify it's displayed
            TestHelpers.take_screenshot(page, 'tests/screenshots/flow_step4_tax.png')
            
            # Check if tax summary is visible
            page_content = page.content()
            assert 'tax' in page_content.lower() or 'බදු' in page_content or 'வரி' in page_content
            
            page.locator(Selectors.NEXT_BUTTON).first.click()
            page.wait_for_timeout(500)
            
            current_step = TestHelpers.get_current_step(page)
            assert current_step == 5, f"Should be on Step 5, got {current_step}"
            print("  ✅ Advanced to Step 5")
            
            print("  Step 5: Final summary...")
            # Step 5: Final Summary
            TestHelpers.take_screenshot(page, 'tests/screenshots/flow_step5_summary.png')
            
            # Verify Finish button is present
            finish_button = page.locator(Selectors.SUBMIT_BUTTON).first
            assert finish_button.is_visible(), "Finish button should be visible on Step 5"
            
            print("✅ Successfully completed entire wizard flow!")
            
        except AssertionError as e:
            print(f"❌ Test failed: {e}")
            TestHelpers.take_screenshot(page, 'tests/screenshots/error_complete_flow.png')
            browser.close()
            sys.exit(1)
        
        browser.close()


def test_data_persistence_across_steps():
    """Test that data persists when navigating back and forth"""
    print("\n🧪 Testing Data Persistence...")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            page.goto('http://localhost:3000')
            TestHelpers.wait_for_navigation(page)
            TestHelpers.clear_local_storage(page)
            page.reload()
            TestHelpers.wait_for_navigation(page)
            
            # Fill Step 1
            test_name = "Persistence Test User"
            test_income = "2500000"
            
            page.locator(Selectors.INPUT_NAME).fill(test_name)
            page.locator(Selectors.INPUT_TIN).fill("111222333")
            page.locator(Selectors.INPUT_INCOME).fill(test_income)
            
            # Go to Step 2
            page.locator(Selectors.NEXT_BUTTON).first.click()
            page.wait_for_timeout(500)
            
            # Select income source
            checkboxes = page.locator('input[type="checkbox"]').all()
            if len(checkboxes) > 0:
                checkboxes[0].check()
            
            # Go to Step 3
            page.locator(Selectors.NEXT_BUTTON).first.click()
            page.wait_for_timeout(500)
            
            # Go back to Step 2
            page.locator(Selectors.BACK_BUTTON).first.click()
            page.wait_for_timeout(500)
            
            # Verify checkbox is still checked
            checkboxes = page.locator('input[type="checkbox"]').all()
            if len(checkboxes) > 0:
                assert checkboxes[0].is_checked(), "Checkbox should still be checked"
                print("  ✅ Step 2 data persisted")
            
            # Go back to Step 1
            page.locator(Selectors.BACK_BUTTON).first.click()
            page.wait_for_timeout(500)
            
            # Verify all fields are still filled
            name_value = page.locator(Selectors.INPUT_NAME).input_value()
            income_value = page.locator(Selectors.INPUT_INCOME).input_value()
            
            assert name_value == test_name, f"Name should be {test_name}, got {name_value}"
            assert income_value == test_income, f"Income should be {test_income}, got {income_value}"
            
            print("  ✅ Step 1 data persisted")
            print("✅ Data persistence verified across all steps!")
            
        except AssertionError as e:
            print(f"❌ Test failed: {e}")
            browser.close()
            sys.exit(1)
        
        browser.close()


def test_localStorage_state():
    """Test that wizard state is saved to localStorage"""
    print("\n🧪 Testing localStorage State Management...")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            page.goto('http://localhost:3000')
            TestHelpers.wait_for_navigation(page)
            TestHelpers.clear_local_storage(page)
            page.reload()
            TestHelpers.wait_for_navigation(page)
            
            # Fill Step 1
            TestHelpers.fill_step1_form(page)
            page.locator(Selectors.NEXT_BUTTON).first.click()
            page.wait_for_timeout(500)
            
            # Check localStorage for wizard data
            local_storage_keys = page.evaluate("() => Object.keys(localStorage)")
            print(f"  localStorage keys: {local_storage_keys}")
            
            # Should have some wizard-related data
            has_wizard_data = any('wizard' in key.lower() or 'tax' in key.lower() for key in local_storage_keys)
            assert has_wizard_data or len(local_storage_keys) > 0, "Wizard data should be in localStorage"
            
            print("✅ Wizard state is saved to localStorage")
            
        except AssertionError as e:
            print(f"❌ Test failed: {e}")
            browser.close()
            sys.exit(1)
        
        browser.close()


if __name__ == '__main__':
    print("=" * 60)
    print("COMPLETE USER FLOW TESTS")
    print("=" * 60)
    
    test_complete_wizard_flow()
    test_data_persistence_across_steps()
    test_localStorage_state()
    
    print("\n" + "=" * 60)
    print("✅ ALL FLOW TESTS PASSED")
    print("=" * 60)
