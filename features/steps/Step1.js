"use client";

import React, { useState, useEffect } from 'react';
import { useWizard } from '@/context/WizardContext';
import { Input } from '@/components/ui/Input';
import { Card } from '@/components/ui/Card';
import { Navigation } from '@/components/wizard/Navigation';
import { t } from '@/data/translations';

export function Step1() {
    const { wizardData, updateData, nextStep, language } = useWizard();
    const [errors, setErrors] = useState({});
    const [formData, setFormData] = useState({
        name: wizardData.name || '',
        tin: wizardData.tin || '',
        income: wizardData.income || ''
    });

    useEffect(() => {
        setFormData({
            name: wizardData.name || '',
            tin: wizardData.tin || '',
            income: wizardData.income || ''
        });
    }, [wizardData]);

    const handleChange = (e) => {
        const { id, value } = e.target;
        setFormData(prev => ({ ...prev, [id]: value }));
        if (errors[id]) {
            setErrors(prev => ({ ...prev, [id]: null }));
        }
    };

    const validate = () => {
        const newErrors = {};
        if (!formData.name.trim()) newErrors.name = t('err_required', language);
        if (!formData.income.trim()) newErrors.income = t('err_required', language);
        // TIN is optional for estimation but good to have

        setErrors(newErrors);
        return Object.keys(newErrors).length === 0;
    };

    const handleNext = () => {
        if (validate()) {
            updateData(formData);
            nextStep();
        }
    };

    return (
        <div className="animate-in fade-in slide-in-from-bottom-4 duration-500">
            <div className="text-center mb-8">
                <h1 className="text-3xl font-bold text-primary mb-2">
                    {t('step1_title', language)}
                </h1>
                <p className="text-gray-600 dark:text-gray-400">
                    {t('step1_desc', language)}
                </p>
            </div>

            <Card>
                <div className="space-y-4">
                    <Input
                        id="name"
                        label={t('lbl_name', language)}
                        value={formData.name}
                        onChange={handleChange}
                        error={errors.name}
                        placeholder="e.g. A.B. Perera"
                    />

                    <Input
                        id="tin"
                        label={t('lbl_tin', language)}
                        value={formData.tin}
                        onChange={handleChange}
                        placeholder="e.g. 123456789"
                    />

                    <Input
                        id="income"
                        label={t('lbl_income', language)}
                        type="number"
                        value={formData.income}
                        onChange={handleChange}
                        error={errors.income}
                        placeholder="e.g. 2500000"
                    />
                </div>

                <Navigation onNext={handleNext} isLastStep={false} />
            </Card>
        </div>
    );
}
