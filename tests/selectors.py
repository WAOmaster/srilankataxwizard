"""
Centralized selectors and helper functions for Sri Lanka Tax Wizard tests
"""

class Selectors:
    """CSS selectors for common elements"""
    
    # Header elements
    HEADER = "header"
    APP_TITLE = "header span.font-bold"
    LANGUAGE_TOGGLE = "header button:has(svg)"  # Globe icon button
    THEME_TOGGLE = "header button:nth-of-type(2)"  # Second button in header
    
    # Step indicator
    STEP_INDICATOR = "span.text-sm.font-medium.text-gray-500, span.text-sm.font-medium"
    
    # Navigation buttons
    NEXT_BUTTON = "button:has-text('Next Step'), button:has-text('ඊළඟ පියවර'), button:has-text('அடுத்த படி')"
    BACK_BUTTON = "button:has-text('Back'), button:has-text('ආපසු'), button:has-text('பின்')"
    SUBMIT_BUTTON = "button:has-text('Finish'), button:has-text('අවසන් කරන්න'), button:has-text('முடி')"
    
    # Step 1 form fields (using actual IDs from the app)
    INPUT_NAME = "input#name"
    INPUT_TIN = "input#tin"
    INPUT_INCOME = "input#income"
    
    # Error messages
    ERROR_MESSAGE = "p[class*='text-red'], span[class*='text-red']"
    
    # Step 2 checkboxes
    INCOME_SOURCE_EMPLOYMENT = "input[type='checkbox']"
    INCOME_SOURCE_BUSINESS = "input[type='checkbox']:near(:text('Business'))"
    
    # Footer
    FOOTER = "footer"


class TestHelpers:
    """Helper functions for common test operations"""
    
    @staticmethod
    def wait_for_navigation(page):
        """Wait for page to be fully loaded"""
        page.wait_for_load_state('networkidle')
        page.wait_for_timeout(500)  # Additional stabilization time
    
    @staticmethod
    def take_screenshot(page, path):
        """Take a full-page screenshot"""
        page.screenshot(path=path, full_page=True)
    
    @staticmethod
    def get_current_step(page):
        """Extract current step number from step indicator"""
        try:
            # Get all spans that match the step indicator pattern
            indicators = page.locator(Selectors.STEP_INDICATOR).all()
            for indicator in indicators:
                text = indicator.text_content()
                if 'Step' in text or 'පියවර' in text or 'படி' in text:
                    # Extract first number from "Step X of Y" format
                    import re
                    match = re.search(r'\d+', text)
                    if match:
                        return int(match.group())
            return None
        except Exception as e:
            print(f"Error getting current step: {e}")
            return None
    
    @staticmethod
    def fill_step1_form(page, name="Test User", tin="123456789", income="2000000"):
        """Fill Step 1 form with provided data"""
        page.locator(Selectors.INPUT_NAME).fill(name)
        if tin:
            page.locator(Selectors.INPUT_TIN).fill(tin)
        page.locator(Selectors.INPUT_INCOME).fill(income)
    
    @staticmethod
    def clear_local_storage(page):
        """Clear localStorage to reset app state"""
        page.evaluate("() => localStorage.clear()")
    
    @staticmethod
    def get_local_storage_item(page, key):
        """Get item from localStorage"""
        return page.evaluate(f"() => localStorage.getItem('{key}')")
    
    @staticmethod
    def get_theme(page):
        """Get current theme from document class"""
        return page.evaluate("() => document.documentElement.classList.contains('dark') ? 'dark' : 'light'")
