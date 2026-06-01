# Research Technical Context

When drafting the Technical Context and Constraints section, follow these guidelines:

## 1. Architecture Review
Scenario: You are migrating or building a new feature on existing systems.
Action: Consult with Engineering Leads to understand the current architecture (e.g., monolith vs. microservices). Document exactly what needs to change to support the new feature.

## 2. Dependency Mapping
Scenario: The feature relies on external APIs or other teams.
Action: Explicitly list all third-party services, internal APIs, and cross-team dependencies. Note any rate limits or integration risks.

## 3. Security & Compliance
Scenario: The feature handles PII or payments data.
Action: Verify compliance requirements (e.g., GDPR, CCPA, PCI-DSS). Document data handling constraints, logging limitations, and required access controls.
