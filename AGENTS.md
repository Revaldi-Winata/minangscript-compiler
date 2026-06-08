# Agent Instructions

## Package Manager
Use **python** (standard library only unless specified).

## Commit Attribution
AI commits MUST include:
```
Co-Authored-By: (the agent model's name and attribution byline)
```

## File-Scoped Commands
| Task | Command |
|------|---------|
| Execute Script | `python <file>.py` |

## MinangScript Compiler Conventions
- **Pipeline & Phases**: Must strictly follow the 7 sequential phases documented in `docs/compiler_phases.md`.
- **Phase Documentation**: Agent MUST document the results and status of each phase into `docs/documentations-compiler/` as individual markdown files (e.g. `fase_2_lexer.md`) ONLY AFTER the phase is completed, tested, and verified to be safe, stable, and running smoothly.
- **Validation Constraint**: Runtime MUST output both **Parse Tree** and **AST** simultaneously to prove AST validity (as per Phase 4).
- **Architecture Strictness**: Parser implementation (Phase 3) MUST ONLY output raw Concrete Syntax Tree (CST) nodes containing all tokens exactly. AST simplification MUST be strictly reserved for Phase 4.
- **Syntax Implementation**:
  - Use `{}` for blocks (ignore Python indentation logic).
  - Implicit variable declaration (e.g., `x = 5`).
- **Language Specs**: Refer to `docs/project_setup.md` for exact Minang translations of 35 keywords and 68 built-in functions.
