# Next Actions

Concrete, startable actions only.

## Now
- Run one first-time-user dry run using only `README.md` + `AGENTS.md`; append `updates/2026-04-08-first-run-dry-run.md` with friction points in sections: `Observed`, `Blocked`, `Suggested safe-update`.
- Run `python3 scripts/validate_repo.py` after the dry run and record pass/fail output verbatim in the same update log.
- Add one `sources.md` secondary-source entry linking the dry-run update file and labeling which claims are still inferred.

## Soon
- Execute one handoff simulation across two different models and append `updates/2026-04-08-handoff-sim.md` with restart time, misses, and first-correct-action latency.
- Based on simulation evidence, append one decision entry in `decisions.md` if a handoff formatting rule should become mandatory.
- Tighten one adapter file only where evidence shows repeat failure, then append a dated update log explaining why the edit was safe.

## Later
- Decide and document validator ownership + cadence in `decisions.md` after at least two weeks of update-log evidence.
- Evaluate heading-structure enforcement in `scripts/validate_repo.py` and log rationale before enabling any new hard-fail checks.
