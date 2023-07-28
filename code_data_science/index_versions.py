from code_data_science.sort_versions import sort_versions


def index_versions(versions: [str], metadata_pattern=None):
    sorted_versions = sort_versions(set(versions), metadata_pattern)
    return {v: sorted_versions.index(v) for v in sorted_versions}
