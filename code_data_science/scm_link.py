def _base_scm_link(scm_dictionary, origin: str, organization: str, repository: str) -> str:
    if origin in scm_dictionary and scm_dictionary[origin] == 'BitbucketConfiguration':
        return f"{origin}/projects/{organization}/repos/{repository}"
    else:
        return f"{origin}/{organization}/{repository}"


def line_number(scm_dictionary, origin: str, organization: str, repository: str,
                committish: str, source_path: str, line) -> str:
    """
    Generates a link to a repository's landing page specific to the SCM system it originated from
    """
    scheme = "https://"
    pathname = _base_scm_link(scm_dictionary, origin, organization, repository)
    search_params = ""
    url_hash = ""

    if origin in scm_dictionary and committish:
        if scm_dictionary[origin] == "GithubConfiguration":
            pathname = '/'.join(
                filter(lambda x: bool(x), [pathname, 'blob' if source_path else 'tree', committish, source_path]))
            if line:
                url_hash = f"L{line}"
        elif scm_dictionary[origin] == "BitbucketConfiguration":
            pathname = '/'.join(filter(lambda x: bool(x), [pathname, 'browse', source_path]))
            search_params = f"?at={committish}"
            if line:
                url_hash = line
        elif scm_dictionary[origin] == "BitbucketCloudConfiguration":
            pathname = '/'.join(filter(lambda x: bool(x), [pathname, 'src', committish, source_path]))
            if line:
                url_hash = f"lines-{line}"
        elif scm_dictionary[origin] == "GitLabConfiguration":
            pathname = '/'.join(filter(lambda x: bool(x), [pathname, '-', 'blob', committish, source_path]))
            if line:
                url_hash = f"L{line}"

    return f"{scheme}{pathname}{search_params}{'#' if url_hash else ''}{url_hash}"
