"use client";

import React from 'react';
import { useWizard } from '@/context/WizardContext';
import { useTheme } from '@/context/ThemeContext';
import { t } from '@/data/translations';

export function StepIndicator({ totalSteps = 5 }) {
    const { currentStep, language } = useWizard();
    const { theme } = useTheme();

    const progress = ((currentStep - 1) / (totalSteps - 1)) * 100;

    return (
        <div className="mb-8">
            <div className="flex justify-between items-center mb-2">
                <span className="text-sm font-medium text-gray-500 dark:text-gray-400">
                    {t('step_indicator', language)
                        .replace('{current}', currentStep)
                        .replace('{total}', totalSteps)}
                </span>
                <span className="text-sm font-medium text-primary">
                    {Math.round(progress)}%
                </span>
            </div>
            <div className="w-full bg-gray-200 rounded-full h-2.5 dark:bg-gray-700">
                <div
                    className="bg-primary h-2.5 rounded-full transition-all duration-500 ease-out"
                    style={{ width: `${progress}%` }}
                ></div>
            </div>
        </div>
    );
}
