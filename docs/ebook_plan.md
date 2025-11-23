# Implementation Plan: GreenKode HTML Ebook

## Goal
Create a visually stunning, 8-page HTML ebook for GreenKode that can be viewed in a browser and downloaded/printed as a PDF.

## Content Structure (8 Pages)
1.  **Cover Page**: Title, Subtitle, Author, "World of 8 Billion" Badge, Hero SVG.
2.  **The Invisible Cost**: Problem statement, "Did you know?" stats, visual representation of energy waste.
3.  **Introducing GreenKode**: Solution overview, Static vs. Dynamic engines, features.
4.  **Under the Hood**: Technical Architecture (SVG Diagram showing CLI -> Sensors flow).
5.  **The Experiment**: Methodology (Dirty vs. Green algorithms), code snippets.
6.  **Results & Data**: Bar charts comparing execution time and emissions (80% reduction).
7.  **Global Impact**: "What if?" scenario, scaling the impact to 1 million developers.
8.  **Conclusion**: Final thoughts, Call to Action, References.

## Design System
*   **Theme**: "Cyber-Nature" - Dark background (`#0f172a`), Neon Green accents (`#22c55e`), White text.
*   **Typography**: `Inter` or `Roboto` (Google Fonts).
*   **Layout**: Flexbox/Grid, A4 aspect ratio containers.
*   **Visuals**:
    *   Inline SVGs for icons and diagrams.
    *   CSS-based bar charts for data.
    *   `@media print` rules to enforce page breaks (`break-after: page`).

## Technical Stack
*   **File**: `docs/greenkode_ebook.html` (Single file).
*   **Libraries**:
    *   Google Fonts (CDN).
    *   FontAwesome (CDN) for icons.
    *   (Optional) Chart.js for the results page, or custom CSS charts for better print stability. *Decision: Custom CSS charts for perfect print rendering.*
*   **PDF Generation**: A "Download PDF" button that triggers `window.print()`.

## Verification
*   Open `docs/greenkode_ebook.html` in browser.
*   Verify visual layout of all 8 pages.
*   Test "Download PDF" (Print Preview) to ensure pages break correctly.
