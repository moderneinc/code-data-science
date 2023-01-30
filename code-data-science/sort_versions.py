import functools
import re


def sort_versions(versions, metadata_pattern=None):
    """
        Sort the versions in order from oldest to newest. Not every version must strictly adhere to Semver.
        :param versions: a list of versions to sort
        :param metadata_pattern: optionally, a metadata pattern like '-jre' in Google Guava versions
        :rtype array:
        >>> sort_versions(['1.1.1.1', '1.1.1.2'])
        ['1.1.1.1', '1.1.1.2']
        >>> sort_versions(['1.1.1.1', '1'])
        ['1', '1.1.1.1']
        >>> sort_versions(['2.1.1', '1.1.1'])
        ['1.1.1', '2.1.1']
        """

    def metadata_compare(v1, v2):
        return compare_versions(v1, v2, metadata_pattern)
    return sorted(versions, key=functools.cmp_to_key(metadata_compare))


def compare_versions(v1, v2, metadata_pattern=None):
    nv1 = v1
    nv2 = v2

    vp1 = __count_version_parts(nv1)
    vp2 = __count_version_parts(nv2)
    len_diff = abs(vp1 - vp2)
    if v1 > v2:
        for i in range(1, len_diff):
            nv2 += ".0"
    elif v2 > v1:
        for i in range(1, len_diff):
            nv1 += ".0"

    releasePattern = re.compile(r"(\d+)(?:\.(\d+))?(?:\.(\d+))?(?:\.(\d+))?(?:\.(\d+))?([-+].*)?")
    v1Gav = releasePattern.match(nv1)
    v2Gav = releasePattern.match(nv2)

    normalized1 = nv1 if metadata_pattern is None else nv1.replace(metadata_pattern, "")
    normalized2 = nv2 if metadata_pattern is None else nv2.replace(metadata_pattern, "")

    for i in range(1, max(vp1, vp2)):
        v1Part = v1Gav.group(i)
        v2Part = v2Gav.group(i)
        if v1Part is None:
            return normalized1.compareTo(normalized2) if v2Part is None else -1
        elif v2Part is None:
            return 1
        diff = int(v1Part) - int(v2Part)
        if diff != 0:
            return diff

    if normalized1 == normalized2:
        return 0
    elif normalized1 > normalized2:
        return 1
    else:
        return -1


def __normalize_version(v) -> str:
    """
    Remove RELEASE and FINAL suffixes and make sure there are at least three parts to the version.
    :param v:
    :return: str:
    >>> __normalize_version("1.5.1.2.RELEASE")
    '1.5.1.2'
    >>> __normalize_version("1.5.1.RELEASE")
    '1.5.1'
    >>> __normalize_version("1.5.1.FINAL")
    '1.5.1'
    >>> __normalize_version("1.5.1.Final")
    '1.5.1'
    >>> __normalize_version("29.0")
    '29.0.0'
    >>> __normalize_version("29.0-jre")
    '29.0.0-jre'
    >>> __normalize_version("29-jre")
    '29.0.0-jre'
    """
    if v.endswith(".RELEASE"):
        return v[0:len(v) - len(".RELEASE")]
    if v.endswith(".FINAL") or v.endswith(".Final"):
        return v[0:len(v) - len(".FINAL")]

    version_parts = __count_version_parts(v)
    if version_parts <= 2:
        version_and_metadata = re.split("(?=[-+])", v)
        while version_parts <= 2:
            version_and_metadata[0] += ".0"
            version_parts += 1
        return version_and_metadata[0] + (version_and_metadata[1] if len(version_and_metadata) > 1 else "")

    return v


def __count_version_parts(v) -> int:
    count = 0
    for part in re.split(r"[.\-$]", v):
        if len(part) == 0 or not (part[0].isdigit()):
            break
        count += 1
    return count
