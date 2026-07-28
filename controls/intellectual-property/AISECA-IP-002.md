---
id: AISECA-IP-002
title: "Copyright infringement"
domain: "Intellectual Property"
severity: Medium
nist_ai_rmf: ["MAP-2", "MAN-4"]
mitre_atlas: "No Direct Mapping"
stakeholders: ["Leadership"]
references:
  - https://hls.harvard.edu/today/does-chatgpt-violate-new-york-times-copyrights/
---

# AISECA-IP-002 — Copyright infringement

**Risk.** AI generates, reproduces, or uses content in ways that violate intellectual property rights.

**Scenario.** Real world example: The New York Times filed a lawsuit against OpenAI and backer Microsoft, arguing that its content was used to build generative AI models without permission or proper financial restitution.  OpenAI outputs had produced verbatim or near-verbatim reproduction of its articles in AI outputs proving that its copyrighted work was in the training set

## Tier 1 — Define & Constrain

Define acceptable output constraints by formally documenting which content types, reproduction thresholds, and use cases the AI system is permitted to generate, drawing clear boundaries around verbatim reproduction, substantial similarity, and derivative works across text, code, images, and other modalities. Constrain the system by filtering training data to exclude or license clearly protected material, restricting the model's ability to reproduce extended passages or highly specific creative content, and requiring legal review of any use case where generated outputs could plausibly substitute for or reproduce copyrighted works.

## Tier 2 — Enforce & Monitor

Enforce detection and takedown by deploying output scanning tools that identify verbatim or near-verbatim reproduction of protected content before responses are served, implementing similarity detection against known copyrighted works, and establishing a rapid takedown process for cases where infringing outputs are identified in production. Monitor by logging outputs flagged for potential infringement, tracking patterns in the types of content or prompts that trigger reproduction risks, and maintaining a feedback mechanism for rights holders and users to report suspected infringing outputs for review.

## Tier 3 — Validate & Adapt

Continuously adapt to legal changes by tracking evolving copyright case law, regulatory guidance, and jurisdiction-specific AI legislation including developments around training data rights, fair use boundaries, and AI-generated work ownership and updating output constraints and acceptable use policies accordingly. Validate by conducting regular audits of model outputs for reproduction risk across a representative sample of use cases, red-teaming the system with prompts designed to elicit protected content, and ensuring that legal, compliance, and technical controls remain aligned as both the model and the legal landscape evolve.

## Tooling landscape

**Categories.** SCA / License Compliance; AI Governance; Disinformation Security (attribution)

**License compliance & attribution**

- FOSSology (Linux Foundation; Siemens-originated) (license scanning for training corpora & code) — https://github.com/fossology/fossology
- IBM Adversarial Robustness Toolbox (ART) (membership-inference testing to assess memorization) — https://github.com/Trusted-AI/adversarial-robustness-toolbox
- c2patool / C2PA (Adobe-led, with Microsoft/Google/Intel) (attribution credentials on generated content) — https://github.com/contentauth/c2patool
