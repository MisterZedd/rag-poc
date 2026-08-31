# Cascadia Office of Technology — Data Classification Policy

Document ID: COT-GOV-002
Effective Date: January 1, 2026
Owner: Office of the Chief Data Officer

## Classification Tiers
The State of Cascadia classifies all data into four tiers:

1. **Public** — Information approved for public release. No handling restrictions.
2. **Internal** — Information intended for state employees. Not for public release, but low sensitivity.
3. **Restricted** — Sensitive information whose disclosure could cause harm. Includes personnel records and non-public financial data.
4. **Confidential** — Highly sensitive information whose disclosure could cause serious harm. Includes criminal justice information, health records, and tax records.

## Handling Requirements
- Restricted and Confidential data must be encrypted at rest and in transit.
- Confidential data must not leave the state's Azure tenant under any circumstances.
- Confidential data must not be entered into any external or public AI tool.
- Data owners are responsible for assigning a classification to each dataset before it is stored or processed.

## Default Classification
- Any data that has not been explicitly classified is treated as Restricted until a data owner assigns a tier.
