# Translation Guide - Sri Lanka Tax Wizard

## 1. Strategy: "Natural Language"
The goal is to make the application accessible and easy to understand for the average Sri Lankan taxpayer. We prioritize **clarity and common usage** over strict academic correctness.

### 1.1 The "Natural Language" Rule
-   **Native Terms:** Use Sinhala/Tamil words when they are commonly used and understood in daily conversation (e.g., "Name", "Address", "Income").
-   **English Fallback:** If a technical tax term or digital concept is obscure in the native language, or if the English term is more widely recognized (even by non-fluent speakers), **use the English term**.
    -   *Example:* Use "Email" instead of "විද්‍යුත් තැපෑල" (Vidyuth Thapala).
    -   *Example:* Use "Online" instead of "අන්තර්ජාලය ඔස්සේ" (Antharjalaya Osse) if it fits better.
    -   *Example:* "TIN Number" can be kept as "TIN අංකය" rather than a complex translation of "Taxpayer Identification Number".
-   **Transliteration:** In some cases, writing the English word in native script (Transliteration) is acceptable if it's the colloquial norm.

## 2. Languages
1.  **English (en):** Primary / Default.
2.  **Sinhala (si):** Native.
3.  **Tamil (ta):** Native.

## 3. Implementation
-   Translations are stored in a JavaScript object/JSON structure (`data/translations.js`).
-   Keys should be descriptive (e.g., `step1_title`, `btn_next`).
-   The app detects the user's preference and persists it in `localStorage`.

## 4. Initial Dictionary (Draft)

| Key | English | Sinhala (Natural) | Tamil (Natural) |
| :--- | :--- | :--- | :--- |
| `app_title` | Sri Lanka Tax Wizard | Sri Lanka Tax Wizard | Sri Lanka Tax Wizard |
| `btn_next` | Next Step | ඊළඟ පියවර (Next) | அடுத்த படி (Next) |
| `btn_back` | Back | ආපසු (Back) | பின் (Back) |
| `btn_submit` | Finish | අවසන් කරන්න | முடி (Finish) |
| `lbl_name` | Full Name | සම්පූර්ණ නම | முழுப் பெயர் |
| `lbl_tin` | TIN Number | TIN අංකය | TIN எண் |
| `lbl_income` | Annual Income | වාර්ෂික ආදායම | வருடாந்திர வருமானம் |
| `lbl_email` | Email Address | Email ලිපිනය | Email முகவரி |
| `step1_title` | Welcome | ආයුබෝවන් | வணக்கம் |
| `step_employment`| Employment | රැකියා | வேலைவாய்ப்பு |
| `step_business` | Business | ව්‍යාපාර | வியாபாரம் |
| `err_required` | This field is required | මෙම කොටස අනිවාර්යයි | இது தேவை |

> **Note:** This dictionary will be expanded as we build the UI. The focus is on keeping it simple and conversational.
