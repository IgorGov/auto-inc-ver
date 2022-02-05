import re


class ReleaseTypes:
    MAJOR = "major"
    PATCH = "patch"
    INCREMENT = "increment"


class Version:
    def __init__(self, suffix: str, major: int, patch: int, increment: int = None) -> None:
        self.major = major
        self.patch = patch
        self.increment = increment
        self.suffix = suffix
    
    @staticmethod
    def parse(str_ver: str, suffix: str) -> None:
        reg_search = re.search("^(\d+)\.(\d+)\.(\d+)$", str_ver, re.IGNORECASE)
        if reg_search:
            major = int(reg_search.group(2))
            patch = int(reg_search.group(3))
            return Version(suffix, major, patch)
        reg_search = re.search(f'^(\d+)\.(\d+)$', str_ver, re.IGNORECASE)
        if reg_search:
            major = int(reg_search.group(1))
            patch = int(reg_search.group(2))
            return Version(suffix, major, patch)
        reg_search = re.search(f'^(\d+)\.(\d+)\-{suffix}(\d+)$', str_ver, re.IGNORECASE)
        if reg_search:
            major = int(reg_search.group(1))
            patch = int(reg_search.group(2))
            increment = int(reg_search.group(3))
            return Version(suffix, major, patch, increment)
        return None

    def get_next_major(self):
        return Version(self.suffix, self.major + 1, 0)
    
    def get_next_patch(self):
        return Version(self.suffix, self.major, self.patch + 1)
    
    def get_next_increment(self):
        if self.is_dev():
            return Version(self.suffix, self.major, self.patch, self.increment + 1)
        else:
            return Version(self.suffix, self.major + 1, 0, 0)

    def is_dev(self):
        return self.increment is not None

    def __str__(self) -> str:
     return f'{self.major}.{self.patch}' + (f'-{self.suffix}{self.increment}' if self.is_dev() else '')
    
    def __eq__(self, other) -> bool:
        return ((self.major, self.patch, self.increment) ==
                (other.major, other.patch, other.increment))
    
    def __lt__(self, other) -> bool:
        if self.is_dev() and other.is_dev():
            return (self.major, self.patch, self.increment) < (other.major, other.patch, other.increment)
        elif self.is_dev() and not other.is_dev():
            return (self.major, self.patch) <= (other.major, other.patch)
        else:
            return (self.major, self.patch) < (other.major, other.patch)
    

def get_most_recent_release(versions: list[Version]) -> Version:
    versions.sort()
    return versions[-1]

def get_most_recent_official_release(versions: list[Version]) -> Version:
    major_versions = [v for v in versions if not v.is_dev()]
    major_versions.sort()
    return major_versions[-1]

def get_next(version: Version, release_type: str) -> Version:
    if release_type == ReleaseTypes.MAJOR:
        return version.get_next_major()
    elif release_type == ReleaseTypes.INCREMENT:
        return version.get_next_increment()
    elif release_type == ReleaseTypes.PATCH:
        return version.get_next_patch()
    else:
        raise ValueError(f'Invalid release type: {release_type}, should be: {ReleaseTypes.MAJOR} or {ReleaseTypes.INCREMENT}')

def get_next_version(suffix: str, tags: list[str], release_type: str) -> Version:
    if not tags:
        return Version(suffix, 0, 0, 0) if release_type == ReleaseTypes.INCREMENT else Version(suffix, 0, 0)
    versions = [Version.parse(tag, suffix) for tag in tags if Version.parse(tag, suffix)]
    if not versions:
        return Version(suffix, 0, 0, 0) if release_type == ReleaseTypes.INCREMENT else Version(suffix, 0, 0)
    if release_type == ReleaseTypes.INCREMENT:
        last_version = get_most_recent_release(versions)
    else:   
        last_version = get_most_recent_official_release(versions)
    print(f'most recent release version {last_version}')
    next_version = get_next(last_version, release_type)
    return next_version
