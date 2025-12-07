"use client";

import { createContext, useContext, useState, useEffect } from 'react';

const WizardContext = createContext();

const STORAGE_KEY = 'tax-wizard-data';

const initialData = {
    name: '',
    tin: '',
    income: '',
    sources: [],
    // Add more fields as needed
};

export function WizardProvider({ children }) {
    const [currentStep, setCurrentStep] = useState(1);
    const [wizardData, setWizardData] = useState(initialData);
    const [language, setLanguage] = useState('en');

    // Load from localStorage on mount
    useEffect(() => {
        const saved = localStorage.getItem(STORAGE_KEY);
        if (saved) {
            try {
                const parsed = JSON.parse(saved);
                if (parsed.wizardData) setWizardData(parsed.wizardData);
                if (parsed.currentStep) setCurrentStep(parsed.currentStep);
                if (parsed.language) setLanguage(parsed.language);
            } catch (e) {
                console.error("Failed to load wizard data", e);
            }
        }
    }, []);

    // Save to localStorage on change
    useEffect(() => {
        const stateToSave = {
            wizardData,
            currentStep,
            language,
            lastSaved: new Date().toISOString()
        };
        localStorage.setItem(STORAGE_KEY, JSON.stringify(stateToSave));
    }, [wizardData, currentStep, language]);

    const updateData = (newData) => {
        setWizardData((prev) => ({ ...prev, ...newData }));
    };

    const nextStep = () => setCurrentStep((prev) => prev + 1);
    const prevStep = () => setCurrentStep((prev) => Math.max(1, prev - 1));
    const goToStep = (step) => setCurrentStep(step);

    const changeLanguage = (lang) => {
        setLanguage(lang);
        // In a real app, this might also trigger a translation reload or context update
    };

    return (
        <WizardContext.Provider value={{
            currentStep,
            wizardData,
            updateData,
            nextStep,
            prevStep,
            goToStep,
            language,
            changeLanguage
        }}>
            {children}
        </WizardContext.Provider>
    );
}

export function useWizard() {
    return useContext(WizardContext);
}
