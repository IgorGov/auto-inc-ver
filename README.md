# Auto Increment Version

<p align="center">
    <a href="https://github.com/IgorGov/auto-inc-ver/blob/main/LICENSE">
        <img alt="GitHub License" src="https://img.shields.io/github/license/IgorGov/auto-inc-ver?logo=GitHub&style=flat-square">
    </a>
    <a href="https://github.com/IgorGov/auto-inc-ver/releases/latest">
        <img alt="GitHub Latest Release" src="https://img.shields.io/github/v/release/IgorGov/auto-inc-ver?logo=GitHub&style=flat-square">
    </a>
    <a href="https://github.com/IgorGov/auto-inc-ver">
        <img alt="GitHub stars" src="https://img.shields.io/github/stars/IgorGov/auto-inc-ver?logo=GitHub&style=flat-square">
    </a>
    <a href="https://hub.docker.com/r/igorgov/auto-inc-ver">
      <img alt="pulls" src="https://img.shields.io/docker/pulls/igorgov/auto-inc-ver?logo=docker&color=%23099cec">
    </a>
    <a href="https://hub.docker.com/r/igorgov/auto-inc-ver">
      <img alt="size" src="https://img.shields.io/docker/image-size/igorgov/auto-inc-ver/latest?logo=docker&color=%23099cec">
    </a>
    <a href="https://hub.docker.com/r/igorgov/auto-inc-ver">
      <img alt="Doker stars" src="https://img.shields.io/docker/stars/igorgov/auto-inc-ver.svg?logo=docker&color=%23099cec">
    </a>
</p>

This action will automatically determine the version for next release by using repository tags. For develop releases: \<major\>.\<patch\>-dev\<increment\> (e.g 2.0-dev0, 2.0-dev1), for official releases: \<major\>.\<patch\> (1.0, 2.0, 2.1).

## Action Inputs

* **github_token**: Token to get tags from the repo. Pass in using 'secrets.GITHUB_TOKEN'.
* **mode**: Mode for next version calculation. Default: 'dev'. Available options:
  * ***dev***: increment the 'dev' version (ignoring commit message) e.g. 1.0-dev1, 1.0-dev2.
  * ***official*** search the commit message for hashtags: #major - for major version (e.g 2.0), #patch - for patch version (e.g 1.1), if no hashtag found fails.
* **suffix**: suffix for un official releases. default: 'dev'.

## Action Outputs

* **version**: The next release version

## Example

1. Pushing commit to develop branch -> 1.0-dev0 -> 1.0-dev1 -> 1.0-dev2 ...
2. Releasing an official release -> commit with '#major' in commit message -> 1.0
3. Continue development (working on the next release) -> 2.0-dev0 -> 2.0-dev1 -> 2.0-dev2 ...
4. Hot-fix needed (official release) -> commit with '#patch' in commit message -> 1.1
5. Continue pushing to develop branch -> 2.0-dev0 -> 2.0-dev1 -> 2.0-dev2 ...

## Usage

```yaml
- name: Auto Increment Version
    uses: docker://igorgov/auto-inc-ver:v1.0.0
    id: versioning
    with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        mode: official

- name: Print next release version
    shell: bash
    run: |
        echo "${{ steps.versioning.outputs.version }}"       
```
