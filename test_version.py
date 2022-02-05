from version import get_next_version

def test_get_next_version_major():
    release_type  = "major"
    prefix = "dev"
    for tags in ([], None):
        version = get_next_version(prefix, tags, release_type)
        assert str(version) == '0.0'
    
    tags = ['1.0', '2.0-dev0', '2.0-dev1', '2.0']
    version = get_next_version(prefix, tags, release_type)
    assert str(version) == '3.0'

    # much less sense but should be tested
    tags = ['1.0', '1.1']
    version = get_next_version(prefix, tags, release_type)
    assert str(version) == '2.0'

    tags = ['1.0', '2.0-dev0', '2.0-dev1', '1.1', '2.0-dev2', '1.2',]
    version = get_next_version(prefix, tags, release_type)
    assert str(version) == '2.0'

    tags = ['0.23.0', '0.24.1', '0.23.1', '0.24.0', '0.23.2']
    version = get_next_version(prefix, tags, release_type)
    assert str(version) == '25.0'


def test_get_next_version_patch():
    release_type  = "patch"
    prefix = "dev"
    for tags in ([], None):
        version = get_next_version(prefix, tags, release_type)
        assert str(version) == '0.0'
    
    tags = ['1.0', '2.0-dev0', '2.0-dev1', '2.0']
    version = get_next_version(prefix, tags, release_type)
    assert str(version) == '2.1'

    # much less sense but should be tested
    tags = ['1.0', '1.1']
    version = get_next_version(prefix, tags, release_type)
    assert str(version) == '1.2'

    tags = ['1.0', '2.0-dev0', '2.0-dev1', '1.1', '2.0-dev2', '1.2',]
    version = get_next_version(prefix, tags, release_type)
    assert str(version) == '1.3'

    tags = ['0.23.0', '0.24.1', '0.23.1', '0.24.0', '0.23.2']
    version = get_next_version(prefix, tags, release_type)
    assert str(version) == '24.2'

def test_get_next_version_increment():
    release_type  = "increment"
    prefix = "dev"
    for tags in ([], None):
        version = get_next_version(prefix, tags, release_type)
        assert str(version) == '0.0-dev0'
    
    tags = ['1.0', '2.0-dev0', '2.0-dev1', '2.0']
    version = get_next_version(prefix, tags, release_type)
    assert str(version) == '3.0-dev0'

    # much less sense but should be tested
    tags = ['1.0', '1.1']
    version = get_next_version(prefix, tags, release_type)
    assert str(version) == '2.0-dev0'

    tags = ['1.0', '2.0-dev0', '2.0-dev1', '1.1', '2.0-dev2', '1.2',]
    version = get_next_version(prefix, tags, release_type)
    assert str(version) == '2.0-dev3'

    tags = ['0.23.0', '0.24.1', '0.23.1', '0.24.0', '0.23.2']
    version = get_next_version(prefix, tags, release_type)
    assert str(version) == '25.0-dev0'

def test_get_next_version_special_cases():
    prefix = "dev"
    tags = ['2.0-dev0', '1.1', 'stable', '2.0-dev2', '0.2.2.3', '2.0-dev1',  '1.2', '1.0',]

    assert str(get_next_version(prefix, tags, "increment")) == '2.0-dev3'

    assert str(get_next_version(prefix, tags, "patch")) == '1.3'
    
    assert str(get_next_version(prefix, tags, "major")) == '2.0'

    tags = ['stable']
    assert str(get_next_version(prefix, tags, "major")) == '0.0'
