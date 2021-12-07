# Release strategy
This repository uses [GitLab Flow](https://docs.gitlab.com/ee/topics/gitlab_flow.html) strategy.

This repository has three permanent branches: 'main', and 'prod'.
### Main
This branch has the code that will be released on successful build (likely stable).
#### Rules
- No code will be directly written to this branch.
- A release is triggered when code is merged to this branch.
- Versioning is automatically generated when merging, this is created by detecting the branch prefix:
    - 'major/' prefix for major release (e.g. N.x.x)
    - 'minor/' prefix for minor release (e.g. x.N.x)
    - no prefix for patch release (e.g. x.x.N)
- On successful release, this branch is merged to 'prod'.

### Prod
This is the latest production code (stable).
#### Rules
- No code will be directly written to this branch.
- Merge 'main' branch is merged into this branch on successful release
- Only 'main' branch can merge into this branch.
