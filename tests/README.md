# Sri Lanka Tax Wizard - Test Suite

This directory contains automated tests for the Sri Lanka Tax Wizard application using Playwright.

## Prerequisites

- Python 3.11+
- Playwright installed: `pip install playwright`
- Playwright browsers installed: `playwright install chromium`
- Development server running on `http://localhost:3000`

## Test Structure

```
tests/
├── selectors.py              # Shared selectors and helper functions
├── test_data.json           # Test data fixtures
├── test_wizard_functional.py # Wizard navigation tests
├── test_validation.py        # Form validation tests
├── test_multilingual.py      # Multi-language support tests
├── test_theme_toggle.py      # Theme toggling tests
├── test_responsive.py        # Responsive design tests
├── test_complete_flow.py     # End-to-end flow tests
└── screenshots/              # Test screenshots (generated)
```

## Running Tests

### Run All Tests

```bash
# From the project root directory
cd f:\Dev\AIt\srilankataxwizard

# Ensure dev server is running
npm run dev

# In a new terminal, run all tests
python tests/test_wizard_functional.py
python tests/test_validation.py
python tests/test_multilingual.py
python tests/test_theme_toggle.py
python tests/test_responsive.py
python tests/test_complete_flow.py
```

### Run Individual Test Suites

```bash
# Test wizard navigation
python tests/test_wizard_functional.py

# Test form validation
python tests/test_validation.py

# Test multi-language support
python tests/test_multilingual.py

# Test theme toggle
python tests/test_theme_toggle.py

# Test responsive design
python tests/test_responsive.py

# Test complete user flow
python tests/test_complete_flow.py
```

## Test Coverage

### 1. Functional Tests (`test_wizard_functional.py`)
- ✅ Forward navigation through all steps
- ✅ Backward navigation with data retention
- ✅ Step indicator updates
- ✅ Form field presence

### 2. Validation Tests (`test_validation.py`)
- ✅ Required field validation
- ✅ TIN format validation (9 digits)
- ✅ Email format validation
- ✅ Income validation (positive numbers)
- ✅ Error message display

### 3. Multi-Language Tests (`test_multilingual.py`)
- ✅ Language toggle (EN → SI → TA → EN)
- ✅ Translation display on all steps
- ✅ Validation errors in all languages
- ✅ Language persistence across navigation

### 4. Theme Tests (`test_theme_toggle.py`)
- ✅ Light/Dark theme toggle
- ✅ Theme persistence in localStorage
- ✅ Visual verification of theme changes
- ✅ CSS custom property application

### 5. Responsive Tests (`test_responsive.py`)
- ✅ Mobile viewports (iPhone SE, iPhone 11 Pro Max)
- ✅ Tablet viewports (iPad, iPad Pro)
- ✅ Desktop viewports (HD, Full HD)
- ✅ Element visibility across breakpoints

### 6. Complete Flow Tests (`test_complete_flow.py`)
- ✅ Complete wizard Steps 1-5
- ✅ Data persistence across steps
- ✅ localStorage state management
- ✅ Summary display accuracy

## Screenshots

All tests generate screenshots in the `tests/screenshots/` directory for visual verification:

- Initial page load
- Each wizard step
- Language variations
- Theme variations
- Different viewport sizes
- Error states

## Known Limitations

1. **Tax Calculation Accuracy**: Tax calculations should be manually verified against Sri Lanka IRD 2024/2025 tax brackets for accuracy.

2. **Browser Support**: Tests run on Chromium only. For production, consider testing on Firefox and Safari.

3. **Accessibility**: Automated accessibility testing is limited. Manual screen reader testing is recommended.

4. **Performance**: Page load performance metrics are captured but not compared against thresholds.

## Troubleshooting

### Server Not Running
```
Error: net::ERR_CONNECTION_REFUSED at http://localhost:3000
```
**Solution**: Ensure `npm run dev` is running before executing tests.

### Playwright Not Installed
```
ModuleNotFoundError: No module named 'playwright'
```
**Solution**: Run `pip install playwright` and `playwright install chromium`

### Failing Selectors
If tests fail with selector errors, the UI may have changed. Update selectors in `selectors.py`.

## Manual Testing Checklist

After automated tests pass, perform these manual verifications:

- [ ] Visual polish in both light and dark modes
- [ ] Smooth animations and transitions
- [ ] Mobile touch interactions
- [ ] Tax calculation accuracy for sample scenarios
- [ ] Cross-browser compatibility (Chrome, Firefox, Edge)
- [ ] No console errors or warnings

## Contributing

When adding new tests:
1. Add selectors to `selectors.py` if needed
2. Use `TestHelpers` for common operations
3. Include descriptive print statements
4. Take screenshots for visual states
5. Update this README with test coverage

## Support

For issues or questions about the test suite, refer to:
- Project documentation in `docs/`
- Implementation plan in `.gemini/antigravity/brain/*/implementation_plan.md`
