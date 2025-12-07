"use client";

import React from 'react';
import { useWizard } from '@/context/WizardContext';
import { useTheme } from '@/context/ThemeContext';
import { StepIndicator } from '@/components/wizard/StepIndicator';
import { Step1 } from '@/features/steps/Step1';
import { Step2 } from '@/features/steps/Step2';
import { Step3 } from '@/features/steps/Step3';
import { Step4 } from '@/features/steps/Step4';
import { Step5 } from '@/features/steps/Step5';
import { Button } from '@/components/ui/Button';
import { Moon, Sun, Globe } from 'lucide-react';

export default function Home() {
  const { currentStep, language, changeLanguage } = useWizard();
  const { theme, toggleTheme } = useTheme();

  const renderStep = () => {
    switch (currentStep) {
      case 1:
        return <Step1 />;
      case 2:
        return <Step2 />;
      case 3:
        return <Step3 />;
      case 4:
        return <Step4 />;
      case 5:
        return <Step5 />;
      default:
        return <Step1 />;
    }
  };

  const toggleLanguage = () => {
    const langs = ['en', 'si', 'ta'];
    const currentIndex = langs.indexOf(language);
    const nextIndex = (currentIndex + 1) % langs.length;
    changeLanguage(langs[nextIndex]);
  };

  return (
    <div className="min-h-screen bg-background text-text-primary transition-colors duration-300">
      <header className="border-b border-border bg-surface sticky top-0 z-10">
        <div className="container h-16 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <span className="text-2xl">🇱🇰</span>
            <span className="font-bold text-lg hidden sm:inline-block">
              Tax Wizard
            </span>
          </div>

          <div className="flex items-center gap-2">
            <Button
              variant="ghost"
              size="sm"
              onClick={toggleLanguage}
              className="font-medium"
              icon={<Globe size={18} />}
            >
              {language.toUpperCase()}
            </Button>

            <Button
              variant="ghost"
              size="sm"
              onClick={toggleTheme}
              icon={theme === 'dark' ? <Sun size={18} /> : <Moon size={18} />}
            />
          </div>
        </div>
      </header>

      <main className="container py-8 max-w-2xl flex-1">
        <StepIndicator totalSteps={5} />
        {renderStep()}
      </main>

      <footer className="border-t border-border py-6 mt-auto bg-surface">
        <div className="container text-center text-sm text-text-secondary">
          <p>© 2025 Sri Lanka Tax Wizard. Not affiliated with IRD.</p>
        </div>
      </footer>
    </div>
  );
}
