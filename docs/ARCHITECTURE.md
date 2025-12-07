# System Architecture - Sri Lanka Tax Wizard

## 1. Overview
The **Sri Lanka Tax Wizard** is a client-side, single-page application (SPA) built with **Next.js**. It is designed to guide users through the tax filing process with a step-by-step wizard interface. The application is stateless on the server side, relying on `localStorage` for client-side persistence and **Vercel** for static hosting and global distribution.

## 2. Technology Stack
- **Framework:** Next.js 14+ (App Router)
- **Language:** JavaScript (ES6+)
- **Styling:** CSS Modules / Global CSS (Custom properties for theming)
- **State Management:** React Context API + `localStorage`
- **Hosting:** Vercel (Static Export / Edge Network)
- **Analytics:** Vercel Analytics

## 3. Architecture Patterns
We follow a **Component-Based Architecture** with a clear separation of concerns:

### 3.1 Layered Structure
1.  **Presentation Layer (UI):**
    -   `app/`: Next.js App Router pages.
    -   `components/`: Reusable UI components (Buttons, Inputs, Cards).
    -   `features/`: Feature-specific components (Wizard steps).
2.  **State Layer (Logic):**
    -   `context/`: React Context providers (`WizardContext`, `ThemeContext`).
    -   Manages global state (current step, user data, theme, language).
3.  **Utility Layer (Helpers):**
    -   `utils/`: Helper functions (Tax calculations, Validation, Storage wrappers).
    -   `data/`: Static data (Translations, Tax brackets).

### 3.2 Data Flow
-   **Unidirectional Data Flow:** Data flows down from Context to Components.
-   **Events:** Components trigger actions in Context to update state.
-   **Persistence:** State changes are subscribed to and synced with `localStorage` for auto-save.

## 4. Directory Structure
```
srilankataxwizard/
├── app/
│   ├── layout.js      # Root layout (Providers wrap here)
│   ├── page.js        # Home / Wizard entry
│   └── globals.css    # Global styles & Theme variables
├── components/
│   ├── ui/            # Generic UI (Button, Card, Input)
│   └── wizard/        # Wizard-specific (StepIndicator, Navigation)
├── features/
│   ├── steps/         # Individual Step Components (Step1, Step2...)
│   └── summary/       # Final Summary Component
├── context/
│   ├── WizardContext.js # Main application state
│   └── ThemeContext.js  # Theme state
├── utils/
│   ├── storage.js     # localStorage wrapper
│   ├── taxCalculator.js # Tax logic
│   └── validation.js  # Form validation
├── data/
│   └── translations.js # Multi-language dictionary
└── public/            # Static assets
```

## 5. Scalability & Performance
-   **Static Optimization:** The app is statically generated where possible for maximum performance.
-   **Code Splitting:** Next.js automatically splits code by route/component.
-   **Lazy Loading:** Heavy components (if any) can be lazy-loaded.
-   **Edge Caching:** Vercel handles caching at the edge.

## 6. Security
-   **Client-Side Only:** No sensitive data is sent to a backend server. All data resides in the user's browser (`localStorage`).
-   **Sanitization:** Inputs are validated and sanitized before processing (though primarily for UX, as there's no DB injection risk).
-   **HTTPS:** Enforced by Vercel.
