# Design System - Sri Lanka Tax Wizard

## 1. Design Philosophy
-   **Clean & Professional:** Trustworthy aesthetic suitable for financial tasks.
-   **Accessible:** High contrast, clear typography, WCAG AA compliant.
-   **Culturally Relevant:** Color palette inspired by Sri Lankan identity but modernized for a digital interface.
-   **Responsive:** Mobile-first approach.

## 2. Color Palette

### 2.1 Primary Colors
-   **Teal (Primary):** `#1F8B8C` (Trust, Calm, Growth)
    -   *Light:* `#32B8C6`
    -   *Dark:* `#166667`
-   **Maroon (Secondary):** `#C60C30` (Sri Lankan Flag Red - used sparingly for accents/CTAs)
-   **Gold (Accent):** `#FFC000` (Highlight, Warning)

### 2.2 Functional Colors
-   **Success:** `#51CF66` (Green)
-   **Error:** `#FF6B6B` (Red)
-   **Warning:** `#FCC419` (Yellow)
-   **Info:** `#339AF0` (Blue)

### 2.3 Neutrals (Light Mode)
-   **Background:** `#F8F9FA` (Off-white)
-   **Surface:** `#FFFFFF` (White)
-   **Text Primary:** `#212529` (Almost Black)
-   **Text Secondary:** `#868E96` (Gray)
-   **Border:** `#DEE2E6`

### 2.4 Neutrals (Dark Mode)
-   **Background:** `#121212` (Dark Gray)
-   **Surface:** `#1E1E1E` (Card Background)
-   **Text Primary:** `#F8F9FA` (Off-white)
-   **Text Secondary:** `#ADB5BD` (Light Gray)
-   **Border:** `#2C2C2C`

## 3. Typography
-   **Font Family:** `Inter`, sans-serif (Google Fonts) - Clean, modern, highly readable.
-   **Fallback:** `system-ui`, `-apple-system`, `BlinkMacSystemFont`, `Segoe UI`, `Roboto`, `Helvetica Neue`, `Arial`, sans-serif.

### 3.1 Scale
-   **H1 (Page Title):** 2.5rem (40px) / 700 Bold
-   **H2 (Section Title):** 2rem (32px) / 600 SemiBold
-   **H3 (Card Title):** 1.5rem (24px) / 600 SemiBold
-   **Body:** 1rem (16px) / 400 Regular
-   **Small:** 0.875rem (14px) / 400 Regular

## 4. Components

### 4.1 Buttons
-   **Primary:** Teal background, White text, Rounded corners (8px).
-   **Secondary:** Transparent background, Teal border, Teal text.
-   **Ghost:** Transparent background, Gray text (for "Back" or "Cancel").

### 4.2 Inputs
-   **Style:** Outlined, 1px border (`#DEE2E6`), 8px radius.
-   **Focus:** 2px ring (`#1F8B8C` with opacity).
-   **Error:** Red border, error message below.

### 4.3 Cards
-   **Style:** White background (Light) / Dark Gray (Dark), Shadow (`0 4px 6px -1px rgba(0, 0, 0, 0.1)`), 12px radius.

### 4.4 Progress Bar
-   **Container:** Gray background (`#E9ECEF`), 4px height.
-   **Fill:** Primary Teal (`#1F8B8C`), animated transition.
