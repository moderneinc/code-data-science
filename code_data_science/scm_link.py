def _base_scm_link(scm_dictionary, origin, organization, repository) -> str:
    if origin in scm_dictionary and scm_dictionary[origin] == 'BitbucketConfiguration':
        return f"{origin}/projects/{organization}/repos/{repository}"
    else:
        return f"{origin}/{organization}/{repository}"
    

def scm_link(scm_dictionary, origin, organization, repository, committish, sourcePath, line):
    """
    Generates a link to a repository's landing page specific to the SCM system it originated from
    """
    scheme = "https://"
    pathname = _base_scm_link(scm_dictionary, origin, organization, repository)
    searchParams = ""
    hash = ""

    if origin in scm_dictionary and committish:
        if scm_dictionary[origin] == "GithubConfiguration":
            pathname = '/'.join(filter(lambda x: bool(x), [pathname, 'blob' if sourcePath else 'tree', committish, sourcePath]))
            if line:
                hash = f"L{line}"
        elif scm_dictionary[origin] == "BitbucketConfiguration":
            pathname = '/'.join(filter(lambda x: bool(x), [pathname, 'browse', sourcePath]))
            searchParams = f"?at={committish}"
            if line:
                hash = line
        elif scm_dictionary[origin] == "BitbucketCloudConfiguration":
            pathname = '/'.join(filter(lambda x: bool(x), [pathname, 'src', committish, sourcePath]))
            if line:
                hash = f"lines-{line}"
        elif scm_dictionary[origin] == "GitLabConfiguration":
            pathname = '/'.join(filter(lambda x: bool(x), [pathname, '-', 'blob', committish, sourcePath]))
            if line:
                hash = f"L{line}"
    
    return f"{scheme}{pathname}{searchParams}{'#' if hash else ''}{hash}"