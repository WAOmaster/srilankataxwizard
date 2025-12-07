import { Inter } from "next/font/google";
import "./globals.css";
import { ThemeProvider } from "@/context/ThemeContext";
import { WizardProvider } from "@/context/WizardContext";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "Sri Lanka Tax Wizard",
  description: "Step-by-step guide for Sri Lanka Personal Income Tax filing",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className={inter.className}>
        <ThemeProvider>
          <WizardProvider>
            <main className="min-h-screen flex flex-col">
              {children}
            </main>
          </WizardProvider>
        </ThemeProvider>
      </body>
    </html>
  );
}
