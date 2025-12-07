"use client";

import React, { useState, useEffect } from 'react';
import { useWizard } from '@/context/WizardContext';
import { Card } from '@/components/ui/Card';
import { Navigation } from '@/components/wizard/Navigation';
import { t } from '@/data/translations';
import { Briefcase, Building, TrendingUp, Home as HomeIcon, Globe } from 'lucide-react';

export function Step2() {
    const { wizardData, updateData, nextStep, prevStep, language } = useWizard();
    const [selectedSources, setSelectedSources] = useState(wizardData.sources || []);

    useEffect(() => {
        setSelectedSources(wizardData.sources || []);
    }, [wizardData]);

    const toggleSource = (sourceId) => {
        setSelectedSources(prev => {
            if (prev.includes(sourceId)) {
                return prev.filter(id => id !== sourceId);
            } else {
                return [...prev, sourceId];
            }
        });
    };

    const handleNext = () => {
        updateData({ sources: selectedSources });
        nextStep();
    };

    const sources = [
        { id: 'employment', icon: <Briefcase />, label: t('step_employment', language) },
        { id: 'business', icon: <Building />, label: t('step_business', language) },
        { id: 'investment', icon: <TrendingUp />, label: 'Investment' }, // Add translation later
        { id: 'rental', icon: <HomeIcon />, label: 'Rental' }, // Add translation later
        { id: 'other', icon: <Globe />, label: 'Other' } // Add translation later
    ];

    return (
        <div className="animate-in fade-in slide-in-from-bottom-4 duration-500">
            <div className="text-center mb-8">
                <h1 className="text-3xl font-bold text-primary mb-2">
                    Income Sources
                </h1>
                <p className="text-gray-600 dark:text-gray-400">
                    Select all sources of income you received during the tax year.
                </p>
            </div>

            <Card>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-6">
                    {sources.map((source) => (
                        <div
                            key={source.id}
                            onClick={() => toggleSource(source.id)}
                            className={`
                cursor-pointer p-4 rounded-lg border-2 transition-all duration-200 flex items-center gap-3
                ${selectedSources.includes(source.id)
                                    ? 'border-primary bg-primary/5 dark:bg-primary/10'
                                    : 'border-gray-200 dark:border-gray-700 hover:border-primary/50'}
              `}
                        >
                            <div className={`
                p-2 rounded-full 
                ${selectedSources.includes(source.id) ? 'bg-primary text-white' : 'bg-gray-100 dark:bg-gray-800 text-gray-500'}
              `}>
                                {source.icon}
                            </div>
                            <span className="font-medium">{source.label}</span>
                        </div>
                    ))}
                </div>

                <Navigation onNext={handleNext} onBack={prevStep} isLastStep={false} />
            </Card>
        </div>
    );
}
