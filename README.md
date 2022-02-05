# Auto Increment Version

<p align="center">
    <a href="https://github.com/IgorGov/auto-inc-ver/blob/main/LICENSE">
        <img alt="GitHub License" src="https://img.shields.io/github/license/IgorGov/auto-inc-ver?logo=GitHub&style=flat-square">
    </a>
    <a href="https://github.com/IgorGov/auto-inc-ver/releases/latest">
        <img alt="GitHub Latest Release" src="https://img.shields.io/github/v/release/IgorGov/auto-inc-ver?logo=GitHub&style=flat-square">
    </a>
    <a href="https://hub.docker.com/r/igorgov/auto-inc-ver">
      <img alt="Docker pulls" src="https://img.shields.io/docker/pulls/igorgov/auto-inc-ver?color=%23099cec">
    </a>
    <a href="https://hub.docker.com/r/igorgov/auto-inc-ver">
      <img alt="Image size" src="https://img.shields.io/docker/image-size/igorgov/auto-inc-ver/latest">
    </a>
    <a href="https://hub.docker.com/r/igorgov/auto-inc-ver">
      <img alt="Image size" src="https://img.shields.io/docker/stars/igorgov/auto-inc-ver.svg">
    </a>
</p>

This action will automaticly determine the version for next release. Working with \<major\>.\<patch\>-dev\<increment\> version pattern

Official releases will look like: 1.0, 2.0, 2.1 <br />
Development releases will look like: 2.0-dev0, 2.0-dev1 <br />

## Action Inputes

* **github_token**: Token to get tags from the repo. Pass in using `secrets.GITHUB_TOKEN`.
* **mode**: Mode for next version calculation. Default: 'dev'. Available options:
  * ***dev***: will increment the 'dev' version (ignoring commit message) e.g. 1.0-dev1, 1.0-dev2
  * ***official*** try to find in commit message hastags: #major - for major version (e.g 2.0), #patch - for patch version (e.g 1.1), if no hashtag found fails.
* **suffix**: suffix for un official releases. default: 'dev'.

## Action Outputs

* **version**: The next release version

## Example

1. Pushing commites to develop branch -> 1.0-dev0 -> 1.0-dev1 -> 1.0-dev2 ...
2. Releasing an official release -> commit with '#major' in commit message -> 1.0
3. Continue developement (working on the next release) -> 2.0-dev0 -> 2.0-dev1 -> 2.0-dev2 ...
4. Hotfix needed (official release) -> commit with '#patch' in commit message -> 1.1
5. Continue pusing to develop branch -> 2.0-dev0 -> 2.0-dev1 -> 2.0-dev2 ...

## Official version usage

```yaml
- name: Auto Increment Version
    uses: docker://igorgov/auto-inc-ver:latest
    id: versioning
    with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        mode: official

- name: Print next release version
    shell: bash
    run: |
        echo "${{ steps.versioning.outputs.version }}"       
```

## Development version usage

```yaml
- name: Auto Increment Version
    uses: docker://igorgov/auto-inc-ver:latest
    id: versioning
    with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        mode: dev  

- name: Print next release version
    shell: bash
    run: |
        echo "${{ steps.versioning.outputs.version }}"
```
