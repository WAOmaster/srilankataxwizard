"use client";

import React from 'react';
import { useWizard } from '@/context/WizardContext';
import { Card } from '@/components/ui/Card';
import { Navigation } from '@/components/wizard/Navigation';
import { t } from '@/data/translations';
import { FileText, Mail, CheckCircle } from 'lucide-react';

export function Step3() {
    const { wizardData, nextStep, prevStep, language } = useWizard();
    const sources = wizardData.sources || [];

    const getDocuments = () => {
        const docs = [];

        // Always required
        docs.push({
            id: 'tin',
            title: 'TIN Certificate',
            desc: 'Your Taxpayer Identification Number certificate from IRD.'
        });

        if (sources.includes('employment')) {
            docs.push({
                id: 't10',
                title: 'T-10 Certificate',
                desc: 'Request this from your employer. It details your total remuneration and any tax deducted (APIT).',
                action: 'email_employer'
            });
        }

        if (sources.includes('investment') || sources.includes('business')) {
            docs.push({
                id: 'wht',
                title: 'WHT Certificates',
                desc: 'Withholding Tax certificates from banks or financial institutions for interest income.',
                action: 'email_bank'
            });
        }

        return docs;
    };

    const documents = getDocuments();

    return (
        <div className="animate-in fade-in slide-in-from-bottom-4 duration-500">
            <div className="text-center mb-8">
                <h1 className="text-3xl font-bold text-primary mb-2">
                    Document Collection
                </h1>
                <p className="text-gray-600 dark:text-gray-400">
                    Based on your profile, you need the following documents.
                </p>
            </div>

            <div className="space-y-4">
                {documents.map((doc) => (
                    <Card key={doc.id} className="flex gap-4 items-start">
                        <div className="p-2 bg-primary/10 rounded-lg text-primary mt-1">
                            <FileText size={24} />
                        </div>
                        <div className="flex-1">
                            <h3 className="font-semibold text-lg">{doc.title}</h3>
                            <p className="text-gray-600 dark:text-gray-400 text-sm mb-3">
                                {doc.desc}
                            </p>

                            {doc.action === 'email_employer' && (
                                <div className="bg-gray-50 dark:bg-gray-800 p-3 rounded text-sm border border-gray-200 dark:border-gray-700">
                                    <div className="flex items-center gap-2 font-medium mb-1 text-primary">
                                        <Mail size={14} />
                                        <span>Email Template for HR</span>
                                    </div>
                                    <p className="italic text-gray-500 mb-2">"Dear HR, Please provide my T-10 certificate for the tax year 2024/2025..."</p>
                                    <button className="text-xs bg-white dark:bg-gray-700 border border-gray-300 dark:border-gray-600 px-2 py-1 rounded hover:bg-gray-100 dark:hover:bg-gray-600 transition-colors">
                                        Copy to Clipboard
                                    </button>
                                </div>
                            )}
                        </div>
                        <div className="text-green-500">
                            <CheckCircle size={20} className="opacity-20" />
                        </div>
                    </Card>
                ))}
            </div>

            <div className="mt-8">
                <Navigation onNext={nextStep} onBack={prevStep} isLastStep={false} />
            </div>
        </div>
    );
}
