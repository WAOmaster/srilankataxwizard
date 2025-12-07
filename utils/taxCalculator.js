/**
 * Sri Lanka Personal Income Tax Calculator (2024/2025)
 * Tax-free threshold: Rs. 1,200,000 per annum (Rs. 100,000 per month)
 * Tax slabs: Rs. 500,000 each
 * Rates: 6%, 12%, 18%, 24%, 30%, 36%
 */

export const TAX_BRACKETS = [
    { limit: 500000, rate: 0.06 },
    { limit: 500000, rate: 0.12 },
    { limit: 500000, rate: 0.18 },
    { limit: 500000, rate: 0.24 },
    { limit: 500000, rate: 0.30 },
    { limit: Infinity, rate: 0.36 },
];

export const TAX_FREE_THRESHOLD = 1200000; // Rs. 1.2M per year

export function calculateTax(annualIncome) {
    if (!annualIncome || isNaN(annualIncome)) return 0;

    let taxableIncome = Math.max(0, annualIncome - TAX_FREE_THRESHOLD);
    let totalTax = 0;
    let remainingIncome = taxableIncome;

    for (const bracket of TAX_BRACKETS) {
        if (remainingIncome <= 0) break;

        const taxableAmount = Math.min(remainingIncome, bracket.limit);
        totalTax += taxableAmount * bracket.rate;
        remainingIncome -= taxableAmount;
    }

    return {
        grossIncome: annualIncome,
        taxableIncome,
        totalTax,
        monthlyTax: totalTax / 12,
        effectiveRate: (totalTax / annualIncome) * 100
    };
}

export function formatCurrency(amount) {
    return new Intl.NumberFormat('en-LK', {
        style: 'currency',
        currency: 'LKR',
        minimumFractionDigits: 2
    }).format(amount);
}
