# Cascadia Office of Technology — Authentication and Password Policy

Document ID: COT-SEC-001
Effective Date: January 1, 2026
Owner: Office of the Chief Information Security Officer

## Purpose
This policy establishes requirements for authentication to State of Cascadia information systems.

## Password Requirements
- Minimum password length is 14 characters for all user accounts.
- Passwords must include at least one uppercase letter, one lowercase letter, and one number.
- Passwords for privileged (administrator) accounts must be rotated every 90 days.
- Standard user account passwords are not subject to forced periodic rotation unless a compromise is suspected.
- Reuse of the previous 10 passwords is prohibited.

## Multi-Factor Authentication
- Multi-factor authentication (MFA) is required for all remote access and for all privileged accounts.
- Approved second factors are the state authenticator app and FIDO2 hardware keys. SMS-based codes are not permitted.

## Account Lockout
- Accounts are locked after 5 consecutive failed sign-in attempts.
- Locked accounts remain locked for 15 minutes or until reset by the service desk.

## Privileged Access
- All privileged accounts must be enrolled in Privileged Identity Management (PIM) and activated just-in-time.
- Standing administrative access is prohibited.
