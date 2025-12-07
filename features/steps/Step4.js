"use client";

import React, { useEffect, useState } from 'react';
import { useWizard } from '@/context/WizardContext';
import { Card } from '@/components/ui/Card';
import { Navigation } from '@/components/wizard/Navigation';
import { t } from '@/data/translations';
import { calculateTax, formatCurrency } from '@/utils/taxCalculator';
import { Calculator, AlertCircle } from 'lucide-react';

export function Step4() {
    const { wizardData, nextStep, prevStep, language } = useWizard();
    const [calculation, setCalculation] = useState(null);

    useEffect(() => {
        const income = parseFloat(wizardData.income) || 0;
        const result = calculateTax(income);
        setCalculation(result);
    }, [wizardData.income]);

    if (!calculation) return null;

    return (
        <div className="animate-in fade-in slide-in-from-bottom-4 duration-500">
            <div className="text-center mb-8">
                <h1 className="text-3xl font-bold text-primary mb-2">
                    {t('tax_summary', language)}
                </h1>
                <p className="text-gray-600 dark:text-gray-400">
                    Based on the income you provided.
                </p>
            </div>

            <Card className="mb-6 border-primary/20 shadow-lg">
                <div className="flex items-center gap-3 mb-6 pb-4 border-b border-gray-100 dark:border-gray-800">
                    <div className="p-2 bg-primary/10 rounded-full text-primary">
                        <Calculator size={24} />
                    </div>
                    <div>
                        <h2 className="text-lg font-semibold text-primary">Estimated Liability</h2>
                        <p className="text-xs text-gray-500">Year of Assessment 2024/2025</p>
                    </div>
                </div>

                <div className="space-y-4">
                    <div className="flex justify-between items-center">
                        <span className="text-gray-600 dark:text-gray-400">Total Annual Income</span>
                        <span className="font-medium text-lg">{formatCurrency(calculation.grossIncome)}</span>
                    </div>

                    <div className="flex justify-between items-center text-sm">
                        <span className="text-gray-500">Tax-Free Allowance</span>
                        <span className="text-green-600">- {formatCurrency(1200000)}</span>
                    </div>

                    <div className="flex justify-between items-center pt-2 border-t border-dashed border-gray-200 dark:border-gray-700">
                        <span className="font-medium">Taxable Income</span>
                        <span className="font-medium">{formatCurrency(calculation.taxableIncome)}</span>
                    </div>

                    <div className="bg-gray-50 dark:bg-gray-800 p-4 rounded-lg mt-4">
                        <div className="flex justify-between items-center mb-1">
                            <span className="font-bold text-gray-700 dark:text-gray-300">{t('tax_liability', language)}</span>
                            <span className="font-bold text-xl text-primary">{formatCurrency(calculation.totalTax)}</span>
                        </div>
                        <div className="flex justify-between items-center text-xs text-gray-500">
                            <span>Monthly Tax</span>
                            <span>{formatCurrency(calculation.monthlyTax)} / month</span>
                        </div>
                    </div>
                </div>
            </Card>

            <div className="bg-yellow-50 dark:bg-yellow-900/20 border border-yellow-200 dark:border-yellow-800 p-4 rounded-lg flex gap-3 items-start mb-8">
                <AlertCircle className="text-yellow-600 dark:text-yellow-500 shrink-0 mt-0.5" size={18} />
                <p className="text-sm text-yellow-800 dark:text-yellow-200">
                    <strong>Disclaimer:</strong> This is an estimate only. Actual tax liability may vary based on specific deductions, exemptions, and final APIT tables. Please consult a tax professional or the IRD for official assessments.
                </p>
            </div>

            <Navigation onNext={nextStep} onBack={prevStep} isLastStep={false} />
        </div>
    );
}
