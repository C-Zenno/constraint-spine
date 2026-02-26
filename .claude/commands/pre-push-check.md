# /pre-push-check — Constraint-Spine Push Gate

Repo-local governance gate. Run before every push to master.

## When to use

Before any `git push` to `master` on this repo.

## Tag requirement

This repo enforces `require-head-tag.yml` — every commit on master
must carry a tag matching:

```
public-spine-vX.Y.Z
```

Pattern: `^public-spine-v[0-9]+(\.[0-9]+){1,2}$`

## Procedure

1. **Check current tag state:**

```bash
git describe --tags --exact-match HEAD 2>/dev/null
```

If this returns a tag → HEAD is already tagged. Verify the tag matches
`public-spine-vX.Y.Z`. If yes, push is safe.

2. **If HEAD is untagged:**

Find the latest tag:

```bash
git tag --sort=-version:refname | head -1
```

Increment the minor version by 1. Example:
- `public-spine-v0.15` → `public-spine-v0.16`

Create the tag, then push both commit and tag explicitly:

```bash
git tag public-spine-v<NEXT>
git push origin master
git push origin public-spine-v<NEXT>
```

Do NOT use `--follow-tags` — it only pushes annotated tags.
Lightweight tags (created by `git tag` without `-a`) require explicit push.

3. **After push — verify CI:**

```bash
gh run list --limit 1
```

Expect: `completed success`. If failed, check `gh run view <id> --log`.

## What NOT to do

- Do not push to master without a tag on HEAD
- Do not skip the CI verification step
- Do not use tags that don't match the pattern
- Do not amend tagged commits (create a new commit + new tag instead)

## Branch rules

- All pushes go to `master`
- No PR required (single-maintainer repo)
- Tag must exist before or at push time
