from type_alias import Synonyms


def merge_synonyms(existing_synonyms: list[Synonyms], new_synonyms: Synonyms) -> list[Synonyms]:
    """
    Merge new synonyms with existing sets of synonyms.

    This function takes a list of tuples, `existing_synonyms`, where each tuple represents
    a set of synonyms. It merges the new set of synonyms, `new_synonyms`, with the existing
    sets if there are any overlapping synonyms, and returns a new list of merged sets.

    Parameters:
        existing_synonyms (List[Synonyms]): A list of tuples, where each tuple contains strings representing
            synonyms.
        new_synonyms (Synonyms): A tuple of strings representing a new set of synonyms to be merged.

    Returns:
        List[Synonyms]: A new list of tuples representing merged sets of synonyms.

    Example:
        > existing_synonyms = [('apple', 'fruit'), ('big', 'large')]
        > new_synonyms = ('banana', 'fruit')
        > merge_synonyms(existing_synonyms, new_synonyms)
        [('apple', 'fruit', 'banana'), ('big', 'large')]
    """
    found = False

    for i, entry in enumerate(existing_synonyms):
        if any(syn in entry for syn in new_synonyms):
            existing_synonyms[i] = tuple(sorted(set(entry).union(new_synonyms)))
            found = True
            break

    if not found:
        existing_synonyms.append(new_synonyms)

    return existing_synonyms


def merge_synonyms_list(data: list[Synonyms]) -> list[Synonyms]:
    """
    Merge sets of synonyms in a list.

    This function takes a list of tuples, where each tuple represents a set of synonyms.
    It merges sets with any overlapping synonyms and returns a new list of merged sets.

    Parameters:
        data (List[Synonyms]): A list of tuples, where each tuple contains strings representing synonyms.

    Returns:
        List[Synonyms]: A new list of tuples representing merged sets of synonyms.

    Example:
        > data = [('apple', 'fruit'), ('orange', 'fruit', 'citrus'), ('banana', 'fruit')]
        > merge_synonyms_list(data)
        [('apple', 'banana', 'citrus', 'fruit', 'orange')]
    """
    merged_tuples: list[set[str]] = []

    for current_tuple in data:
        merged = False
        current_set = set(current_tuple)

        for existing_tuple in merged_tuples:
            if any(val in existing_tuple for val in current_set):
                existing_tuple.update(current_set)
                merged = True
                break

        if not merged:
            merged_tuples.append(current_set)

    return [tuple(sorted(merged_tuple)) for merged_tuple in merged_tuples]
