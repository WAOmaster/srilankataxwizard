/**
 * Form Validation Utility for Sri Lanka Tax Wizard
 * Provides reusable validation functions with translations support
 */

/**
 * Validates that a field is not empty
 * @param {string} value - The value to check
 * @returns {boolean} True if valid
 */
export function isRequired(value) {
    if (typeof value === 'string') {
        return value.trim().length > 0;
    }
    return value !== null && value !== undefined;
}

/**
 * Validates TIN format (Sri Lanka TIN: 9 digits)
 * @param {string} tin - The TIN to validate
 * @returns {boolean} True if valid TIN format
 */
export function isValidTIN(tin) {
    if (!tin) return true; // TIN is optional
    const cleaned = tin.replace(/\D/g, '');
    return cleaned.length === 9;
}

/**
 * Validates email format
 * @param {string} email - The email to validate
 * @returns {boolean} True if valid email format
 */
export function isValidEmail(email) {
    if (!email) return true; // Email is optional
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

/**
 * Validates income is a positive number
 * @param {string|number} income - The income to validate
 * @returns {boolean} True if valid
 */
export function isValidIncome(income) {
    if (!income) return false;
    const num = parseFloat(income);
    return !isNaN(num) && num >= 0;
}

/**
 * Formats number as currency (LKR)
 * @param {string|number} value - The value to format
 * @returns {string} Formatted currency string
 */
export function formatCurrencyInput(value) {
    if (!value) return '';
    const num = parseFloat(value.toString().replace(/,/g, ''));
    if (isNaN(num)) return value;
    return num.toLocaleString('en-LK');
}

/**
 * Validates and formats TIN input
 * @param {string} value - The TIN input
 * @returns {string} Formatted TIN (digits only, max 9)
 */
export function formatTINInput(value) {
    if (!value) return '';
    return value.replace(/\D/g, '').slice(0, 9);
}

/**
 * Run validation rules and return errors object
 * @param {Object} data - Form data to validate
 * @param {Object} rules - Validation rules { fieldName: [validators] }
 * @param {string} language - Current language for error messages
 * @returns {Object} Errors object { fieldName: errorMessage }
 */
export function validateForm(data, rules, t, language) {
    const errors = {};

    for (const [field, validators] of Object.entries(rules)) {
        for (const validator of validators) {
            const result = validator(data[field], data);
            if (result !== true) {
                errors[field] = typeof result === 'string' ? result : t('err_required', language);
                break; // Stop at first error for this field
            }
        }
    }

    return errors;
}

/**
 * Common validation rules factory
 */
export const validators = {
    required: (t, language) => (value) =>
        isRequired(value) || t('err_required', language),

    tin: (t, language) => (value) =>
        isValidTIN(value) || t('err_invalid_tin', language),

    email: (t, language) => (value) =>
        isValidEmail(value) || t('err_invalid_email', language),

    income: (t, language) => (value) =>
        isValidIncome(value) || t('err_invalid_income', language),

    minValue: (min, t, language) => (value) => {
        const num = parseFloat(value);
        return (!isNaN(num) && num >= min) || t('err_min_value', language).replace('{min}', min);
    }
};
