"use client";

import React from 'react';
import { Button } from '@/components/ui/Button';
import { useWizard } from '@/context/WizardContext';
import { t } from '@/data/translations';
import { ArrowLeft, ArrowRight, Check } from 'lucide-react';

export function Navigation({
    onNext,
    onBack,
    isNextDisabled = false,
    isLastStep = false,
    isLoading = false
}) {
    const { language, prevStep } = useWizard();

    const handleBack = () => {
        if (onBack) {
            onBack();
        } else {
            prevStep();
        }
    };

    return (
        <div className="flex justify-between mt-8 pt-4 border-t border-gray-200 dark:border-gray-700">
            <Button
                variant="ghost"
                onClick={handleBack}
                icon={<ArrowLeft size={16} />}
            >
                {t('btn_back', language)}
            </Button>

            <Button
                variant="primary"
                onClick={onNext}
                disabled={isNextDisabled}
                isLoading={isLoading}
                icon={!isLoading && (isLastStep ? <Check size={16} /> : <ArrowRight size={16} />)}
            >
                {isLastStep ? t('btn_submit', language) : t('btn_next', language)}
            </Button>
        </div>
    );
}
