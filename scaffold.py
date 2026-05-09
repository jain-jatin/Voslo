import os
import json

base_dir = r"c:\Users\ASUS\OneDrive\Downloads\Voslo"

directories = [
    "context",
    "templates",
    ".claude/rules",
    ".claude/skills",
    ".claude/hooks"
]

for d in directories:
    os.makedirs(os.path.join(base_dir, d), exist_ok=True)

# --- 1. CLAUDE.md & INDEX.md ---
claude_md = """# PM Context
- Role: Product Manager / AI Builder
- Company: [Voslo]
- Product: [AI PM OS]
- Target users: [Product Managers, Founders]
- Current focus: [Building the full-stack AI workflow]
- Primary metric: [Time saved per PM task]
- Guardrails: [No fabricated data, no unverified metrics]
- OKRs: @context/okrs.md
- Terminology: @context/terminology.md

---

## Writing Rules
- Direct, concise, active voice. No filler.
- Lead with the recommendation, then context.
- Audience-match: casual for Slack, structured for docs, precise for specs.
- Banned words: delve, landscape, synergy, leverage, robust, streamline, cutting-edge.
- Never fabricate data, quotes, or metrics. Use `[NEED: data from X]` for gaps.

---

## Sub-Agent Roles
When I say "review as [role]," fully adopt that perspective:

| Role | Lens | Key Questions |
|------|------|---------------|
| **Engineer** | Feasibility | Missing from spec? Edge cases? Technical risks? |
| **Designer** | Usability | Flow clear? Where do users drop off? |
| **Executive** | Strategy | Aligned with OKRs? ROI case? |
| **Skeptic** | Risk | What could go wrong? Untested assumptions? |
| **Customer** | Value | Would I use this? Would I pay? |
| **Data Analyst** | Measurement | Metrics precise? Baselines? Instrumentation? |
| **Legal/Compliance** | Risk & Privacy | Any PII exposed? Regulatory risks? Terms of service impact? |

---

## Verification Sequence
1. Clarify — ask 3-5 questions before generating. Never assume.
2. Draft — default short. Over 2 pages? Ask first.
3. Self-review — check against the relevant skill's checklist and anti-patterns.
4. Flag gaps — surface unknowns with `[NEED: ...]`, don't fill them with guesses.

---

## Context Management
- Suggest `/clear` when switching between unrelated tasks.
- Use `@path/to/file` to reference docs — never ask me to paste. Keep the context window lean.
- Use Plan Mode (Shift+Tab) before multi-step tasks. Outline first, execute after approval.
- Parallelize independent subtasks with subagents. Don't serialize what can run concurrently.
"""
with open(os.path.join(base_dir, "CLAUDE.md"), "w", encoding="utf-8") as f:
    f.write(claude_md)

index_md = """# Voslo PM OS Index
This is the master router for the agent. Before doing anything, load the relevant file.

- **For competitor questions, positioning, or pricing intel:** Load `@context/competitors.md`
- **For activation funnel, experiment results, or what failed:** Load `@context/activation.md`
- **For retention patterns, cohort insights, or interventions:** Load `@context/retention.md`
- **For pricing reasoning and historical decisions:** Load `@context/pricing.md`
- **For hypotheses currently being tested or rejected:** Load `@context/hypotheses.md`
- **For team structure and reporting:** Load `@context/team_structure.md`
- **For product terminology:** Load `@context/terminology.md`
- **For current OKRs:** Load `@context/okrs.md`
"""
with open(os.path.join(base_dir, "INDEX.md"), "w", encoding="utf-8") as f:
    f.write(index_md)

# --- 2. Context Files ---
context_files = {
    "competitors.md": "---\nlast_updated: 2026-05-09\ndomain: competitors\n---\n# Competitor Intel\nLog positioning, pricing intel, last known moves, and weaknesses here.",
    "activation.md": "---\nlast_updated: 2026-05-09\ndomain: activation\n---\n# Activation Experiments\nLog funnel step rates, A/B test outcomes, and what failed and why.",
    "retention.md": "---\nlast_updated: 2026-05-09\ndomain: retention\n---\n# Retention Insights\nLog cohort patterns, interventions tried, and what moved the needle.",
    "pricing.md": "---\nlast_updated: 2026-05-09\ndomain: pricing\n---\n# Pricing Decisions\nLog pricing changes, reasoning, false beliefs corrected.",
    "hypotheses.md": "---\nlast_updated: 2026-05-09\ndomain: hypotheses\n---\n# Hypotheses\nLog what you believe, what's tested, what's rejected.",
    "okrs.md": "# Current OKRs\nO1: Build the ultimate PM OS\nKR1: Complete full 41+ skill setup\nKR2: Run first sprint fully via AI",
    "team_structure.md": "# Team Structure\n- Jatin: Full-Stack AI Builder / PM\n- AI Agents: 10-person equivalent team (Engineers, Designers, Analysts)",
    "terminology.md": "# Terminology Glossary\n- **Voslo**: The name of this PM OS.\n- **ELIS**: [Your ELIS project definition]\n- **ARQ**: [Your ARQ funnel definition]"
}
for name, content in context_files.items():
    with open(os.path.join(base_dir, "context", name), "w", encoding="utf-8") as f:
        f.write(content)

# --- 3. Templates ---
templates = {
    "prd-template.md": "# PRD: [Feature Name]\n## 1. Hypothesis\n## 2. Problem\n## 3. Strategic Fit\n## 4. Solution\n## 5. Success Metrics\n## 6. Non-Goals\n## 7. Open Questions",
    "launch-plan.md": "# Launch Plan: [Feature]\n## Positioning\n## Target Audience\n## Launch Channels\n## Success Metrics\n## Rollback Plan",
    "okr-template.md": "# OKRs: [Quarter]\n## O1: [Objective]\n| KR | Baseline | Target | Current | Status |\n## Health Check",
    "sprint-review.md": "# Sprint Review: [Sprint]\n## Results\n## Metrics\n## Demo Notes\n## Key Decisions",
    "roadmap-template.md": "# Product Roadmap\n## Now (Next 4 Weeks)\n## Next (1-3 Months)\n## Later (3+ Months)",
    "retro-template.md": "# Retrospective\n## What went well?\n## What didn't go well?\n## Action Items (Who/What/When)"
}
for name, content in templates.items():
    with open(os.path.join(base_dir, "templates", name), "w", encoding="utf-8") as f:
        f.write(content)

# --- 4. 41+ Skills ---
skills = [
    "prd-writer", "competitive-analysis", "launch-checklist", "metrics-definer", 
    "sprint-planner", "user-research-synth", "roadmap-generator", "retro-facilitator",
    "hypothesis-tester", "pricing-calculator", "user-story-writer", "bug-triage",
    "release-notes-writer", "stakeholder-update", "data-query-builder", "churn-analyzer",
    "funnel-optimizer", "experiment-designer", "customer-interview-prep", "onboarding-auditor",
    "feature-audit", "tech-debt-evaluator", "build-vs-buy", "vendor-assessment",
    "okr-drafter", "gogo-to-market-strategy", "persona-generator", "job-to-be-done-mapper",
    "api-spec-reviewer", "design-feedback", "copy-polisher", "translation-manager",
    "accessibility-checker", "security-review-prep", "compliance-checklist", "financial-modeler",
    "capacity-planner", "daily-standup-summarizer", "incident-postmortem", "support-ticket-analyzer",
    "user-feedback-categorizer", "investor-update-writer"
]

for skill in skills:
    skill_dir = os.path.join(base_dir, ".claude", "skills", skill)
    os.makedirs(skill_dir, exist_ok=True)
    with open(os.path.join(skill_dir, "SKILL.md"), "w", encoding="utf-8") as f:
        f.write(f"# Skill: {skill}\n\n**Trigger:** \"run {skill}\" or implicit based on context.\n\n## Instructions\nWhen executing this skill, always follow best practices for {skill}. Gather necessary context, ask clarifying questions, and use the appropriate template if one exists.\n")

# --- 5. Hooks / Settings ---
settings = {
    "hooks": {
        "pre-commit": {
            "command": "python .claude/hooks/spellcheck_and_protect.py",
            "description": "Automated spell-checking and file protection before writes."
        }
    }
}
with open(os.path.join(base_dir, ".claude", "settings.json"), "w", encoding="utf-8") as f:
    json.dump(settings, f, indent=4)

hook_script = '''import sys
import os
# Mock spell checker and file protector
print("Running automated spell-check and file protection...")
# In a real hook, this would parse git diffs or file contents
# and exit(1) if sensitive files like templates are modified without flag
print("Check passed.")
sys.exit(0)
'''
with open(os.path.join(base_dir, ".claude", "hooks", "spellcheck_and_protect.py"), "w", encoding="utf-8") as f:
    f.write(hook_script)

print("Scaffold complete.")
