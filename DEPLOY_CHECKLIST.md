# Pre-Deploy Checklist — constraint-spine

Run before any public push.

## SEO sanity (avoid soft-404 + canonical drift)

- [ ] `404.html` exists at the repo root.
- [ ] **After deploy**, curl a path that doesn't exist:
      `curl -sS -o /dev/null -w "%{http_code}\n" https://constraintphysics.org/this-page-does-not-exist-xyz`
      Must return **404** (NOT 200).
- [ ] If `_redirects` exists, it must NOT start with `<!DOCTYPE` or `<html`. If it does, it was overwritten by a sync.
- [ ] **After deploy**, curl every URL in `sitemap.xml`. All must return 200 directly.

## Tag/release discipline (constraint-spine specific)

- [ ] Every push to `master` requires a tag matching `^public-spine-v[0-9]+(\.[0-9]+){1,2}$` (CI workflow at `.github/workflows/require-head-tag.yml` enforces this).
- [ ] If updating tag pins in URLs (e.g., on cc-website), point to the latest spine tag.

## Canonical posture

- [ ] `<link rel="canonical">` on `index.html` is `https://constraintphysics.org/`.
- [ ] If sitemap lists `/axioms.html`, verify the page actually exists or remove it (current sitemap-vs-repo drift flagged in 2026-04-30 audit).

## Known historical bugs

| Date | Bug | Fix |
|---|---|---|
| 2026-05-05 | No `404.html` at root — CF Pages was serving `index.html` for unknown paths with HTTP 200 (soft-404). | Added `404.html`. |
| 2026-04-30 | Sitemap listed `/axioms.html` but local repo had only `index.html`; live URL 308'd. | Flagged for surface owner; not yet resolved. |
