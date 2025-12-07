"use client";

import React from 'react';
import { useWizard } from '@/context/WizardContext';
import { Card } from '@/components/ui/Card';
import { Navigation } from '@/components/wizard/Navigation';
import { Button } from '@/components/ui/Button';
import { ExternalLink, CheckCircle, Phone, Mail } from 'lucide-react';

export function Step5() {
    const { prevStep } = useWizard();

    const handleFinish = () => {
        // In a real app, this might clear local storage or redirect
        alert("Congratulations! You are ready to file.");
    };

    return (
        <div className="animate-in fade-in slide-in-from-bottom-4 duration-500">
            <div className="text-center mb-8">
                <div className="inline-flex items-center justify-center w-16 h-16 bg-green-100 dark:bg-green-900/30 rounded-full text-green-600 dark:text-green-400 mb-4">
                    <CheckCircle size={32} />
                </div>
                <h1 className="text-3xl font-bold text-primary mb-2">
                    Ready to File!
                </h1>
                <p className="text-gray-600 dark:text-gray-400">
                    You have all the information needed to submit your return.
                </p>
            </div>

            <Card className="mb-6">
                <h2 className="text-xl font-semibold mb-4">Next Steps</h2>
                <div className="space-y-6">
                    <div className="flex gap-4">
                        <div className="flex-shrink-0 w-8 h-8 bg-primary text-white rounded-full flex items-center justify-center font-bold">1</div>
                        <div>
                            <h3 className="font-medium mb-1">Log in to IRD e-Services</h3>
                            <p className="text-sm text-gray-600 dark:text-gray-400 mb-2">
                                Visit the official Inland Revenue Department portal.
                            </p>
                            <a
                                href="https://eservices.ird.gov.lk"
                                target="_blank"
                                rel="noopener noreferrer"
                                className="inline-flex items-center text-primary hover:underline text-sm font-medium"
                            >
                                Go to IRD Portal <ExternalLink size={14} className="ml-1" />
                            </a>
                        </div>
                    </div>

                    <div className="flex gap-4">
                        <div className="flex-shrink-0 w-8 h-8 bg-primary text-white rounded-full flex items-center justify-center font-bold">2</div>
                        <div>
                            <h3 className="font-medium mb-1">Select "Return of Income"</h3>
                            <p className="text-sm text-gray-600 dark:text-gray-400">
                                Choose the assessment year <strong>2024/2025</strong>.
                            </p>
                        </div>
                    </div>

                    <div className="flex gap-4">
                        <div className="flex-shrink-0 w-8 h-8 bg-primary text-white rounded-full flex items-center justify-center font-bold">3</div>
                        <div>
                            <h3 className="font-medium mb-1">Enter Your Figures</h3>
                            <p className="text-sm text-gray-600 dark:text-gray-400">
                                Use the summary from the previous step to fill in your income details.
                            </p>
                        </div>
                    </div>
                </div>
            </Card>

            <Card className="bg-gray-50 dark:bg-gray-800 border-none">
                <h3 className="font-semibold mb-3">Need Help?</h3>
                <div className="flex flex-col sm:flex-row gap-4 text-sm">
                    <div className="flex items-center gap-2 text-gray-600 dark:text-gray-400">
                        <Phone size={16} />
                        <span>IRD Call Center: <strong>1944</strong></span>
                    </div>
                    <div className="flex items-center gap-2 text-gray-600 dark:text-gray-400">
                        <Mail size={16} />
                        <span>Email: <strong>callcentre@ird.gov.lk</strong></span>
                    </div>
                </div>
            </Card>

            <Navigation onNext={handleFinish} onBack={prevStep} isLastStep={true} />
        </div>
    );
}
